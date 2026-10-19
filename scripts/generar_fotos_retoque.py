"""Genera las fotos «estropeadas» del Tema 3.3 (retoque básico en GIMP).

Parte de un paisaje inventado (un valle con cerezos en flor, generado aquí
mismo, sin fotos de terceros) y lo estropea de tres maneras distintas, una por
técnica de retoque:

  retoque-1-torcida-oscura.jpg  horizonte inclinado 3,5° y foto subexpuesta
  retoque-2-lavada-amarilla.jpg poco contraste y dominante amarilla
  retoque-3-manchas-cable.jpg   motas de polvo del sensor y un cable en el cielo

Uso: python scripts/generar_fotos_retoque.py [--original]
     --original guarda también el paisaje sin estropear (solo para el profesor,
     en temario/soluciones/, que no se publica en la web).
"""
import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / 'web' / 'descargas'
W, H = 2400, 1600
rng = np.random.default_rng(2026)


def ruido1d(n, octavas, semilla):
    r = np.random.default_rng(semilla)
    total = np.zeros(n)
    for o in range(octavas):
        puntos = 4 * 2 ** o + 1
        v = r.uniform(-1, 1, puntos)
        total += np.interp(np.linspace(0, puntos - 1, n), np.arange(puntos), v) / 2 ** o
    return total


def ruido2d(w, h, escala, semilla):
    r = np.random.default_rng(semilla)
    peq = r.uniform(0, 1, (max(2, h // escala), max(2, w // escala))).astype(np.float32)
    im = Image.fromarray((peq * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
    return np.asarray(im, np.float32) / 255


def paisaje():
    y = np.linspace(0, 1, H)[:, None]
    img = np.zeros((H, W, 3), np.float32)
    # Cielo: azul arriba, claro cerca del horizonte, con nubes suaves
    arriba, abajo = np.array([0.30, 0.50, 0.82]), np.array([0.80, 0.87, 0.95])
    t = np.clip(y / 0.55, 0, 1)
    img[:] = arriba * (1 - t[..., None]) + abajo * t[..., None]
    nubes = ruido2d(W, H, 160, 1) * 0.6 + ruido2d(W, H, 60, 2) * 0.4
    nubes = np.clip((nubes - 0.55) * 3, 0, 1) * np.clip(1 - y / 0.45, 0, 1)
    img = img * (1 - nubes[..., None] * 0.8) + nubes[..., None] * 0.8 * np.array([1, 1, 1])
    xs = np.arange(W)
    filas = np.arange(H)[:, None]
    # Sierras: la lejana azulada, las cercanas verdes
    sierras = [(0.40, 0.07, np.array([0.48, 0.56, 0.68]), 11),
               (0.50, 0.08, np.array([0.30, 0.42, 0.36]), 12),
               (0.62, 0.06, np.array([0.27, 0.45, 0.20]), 13)]
    for base, amp, color, s in sierras:
        perfil = (base - amp * ruido1d(W, 6, s)) * H
        mascara = filas >= perfil[None, :]
        textura = 0.92 + 0.16 * ruido2d(W, H, 40, s + 50)[..., None] + 0.05 * ruido2d(W, H, 5, s + 60)[..., None]
        sombra = 0.9 + 0.2 * (filas - perfil[None, :]).clip(0, 300)[..., None] / 300
        img = np.where(mascara[..., None], color * textura * sombra, img)
    # Embalse: la orilla del agua es una línea recta y horizontal (sirve para enderezar)
    agua = (filas >= int(0.665 * H)) & (filas < int(0.76 * H))
    reflejo = np.array([0.42, 0.56, 0.70]) * (0.9 + 0.12 * ruido2d(W, H, 3, 31)[..., None] * np.array([1, 1, 1]))
    ondas = 0.95 + 0.07 * np.sin(filas / 3.0 + ruido2d(W, H, 40, 32) * 6)[..., None]
    img = np.where(agua[..., None], reflejo * ondas, img)
    # Prado en bancales
    prado = filas >= (0.76 * H + 22 * np.sin(xs / 300.0) + 12)[None, :]
    verde = np.array([0.38, 0.58, 0.22]) * (0.8 + 0.4 * ruido2d(W, H, 6, 21)[..., None])
    img = np.where(prado[..., None], verde, img)
    im = Image.fromarray((np.clip(img, 0, 1) * 255).astype(np.uint8))
    d = ImageDraw.Draw(im)
    # Cerezos en flor: más pequeños cuanto más lejos
    r = np.random.default_rng(7)
    arboles = sorted([(r.uniform(0, W), r.uniform(0.80, 0.98) * H) for _ in range(40)], key=lambda a: a[1])
    for ax, ay in arboles:
        esc = 0.35 + 2.2 * (ay / H - 0.78)
        tronco = 70 * esc
        d.line((ax, ay, ax + 6 * esc, ay - tronco), fill=(78, 52, 36), width=max(2, int(12 * esc)))
        for _ in range(int(60 * esc + 18)):
            ang, dist = r.uniform(0, 2 * math.pi), r.uniform(0, 70 * esc) ** 1.0
            cx, cy = ax + math.cos(ang) * dist * 1.3, ay - tronco - 20 * esc + math.sin(ang) * dist * 0.8
            rad = r.uniform(10, 22) * esc
            luz = r.uniform(0.82, 1.0)
            rosa = (int(250 * luz), int(222 * luz), int(232 * luz))
            d.ellipse((cx - rad, cy - rad, cx + rad, cy + rad), fill=rosa)
    im = im.filter(ImageFilter.GaussianBlur(1.1))
    a = np.asarray(im, np.float32) / 255
    a += rng.normal(0, 0.018, a.shape).astype(np.float32)  # grano de foto
    return np.clip(a, 0, 1)


def guardar(a, nombre, carpeta=SALIDA):
    Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).save(carpeta / nombre, quality=88)


def torcida_oscura(a):
    im = Image.fromarray((a * 255).astype(np.uint8)).rotate(3.5, Image.BICUBIC)
    # Recorte central para que no se vean las esquinas vacías del giro
    mx, my = int(W * 0.035), int(H * 0.05)
    im = im.crop((mx, my, W - mx, H - my)).resize((W, H), Image.BICUBIC)
    b = np.asarray(im, np.float32) / 255
    return 0.02 + 0.50 * b ** 1.6  # subexpuesta: todo apiñado a la izquierda del histograma


def lavada_amarilla(a):
    b = 0.24 + 0.58 * a  # sin negros ni blancos
    return b * np.array([1.08, 1.02, 0.72])  # dominante amarilla


def manchas_cable(a):
    im = Image.fromarray((a * 255).astype(np.uint8))
    capa = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(capa)
    r = np.random.default_rng(99)
    for _ in range(14):  # motas de polvo del sensor: en el cielo, donde más se notan
        x, y, rad = r.uniform(80, W - 80), r.uniform(60, H * 0.36), r.uniform(9, 22)
        d.ellipse((x - rad, y - rad, x + rad, y + rad), fill=int(r.uniform(70, 120)))
    capa = capa.filter(ImageFilter.GaussianBlur(5))
    oscuro = Image.new('RGB', (W, H), (40, 45, 55))
    im = Image.composite(oscuro, im, capa)
    # Cable de la luz cruzando el cielo (catenaria)
    d2 = ImageDraw.Draw(im)
    puntos = [(x, 230 + 0.00009 * (x - 1300) ** 2) for x in range(-20, W + 20, 8)]
    d2.line(puntos, fill=(28, 28, 32), width=5)
    return np.asarray(im.filter(ImageFilter.GaussianBlur(0.5)), np.float32) / 255


if __name__ == '__main__':
    base = paisaje()
    guardar(torcida_oscura(base), 'retoque-1-torcida-oscura.jpg')
    guardar(lavada_amarilla(base), 'retoque-2-lavada-amarilla.jpg')
    guardar(manchas_cable(base), 'retoque-3-manchas-cable.jpg')
    if '--original' in sys.argv:
        guardar(base, 'ut03-3-paisaje-original.jpg', RAIZ / 'temario' / 'soluciones')
    print('Fotos de retoque generadas en', SALIDA)
