"""Genera el material del Tema 3.4 (capas, selecciones y texto).

Todo inventado y dibujado aquí mismo, sin fotos de terceros:

  capas-guitarra.jpg  una guitarra sobre una pared clara, con sombra (para recortarla)
  capas-mando.jpg     un mando de videoconsola sobre una mesa (para recortarlo)
  capas-textura.jpg   textura de papel viejo (para los modos de fusión)

Uso: python scripts/generar_material_capas.py
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / 'web' / 'descargas'
W, H = 2000, 1500


def ruido(w, h, escala, semilla):
    r = np.random.default_rng(semilla)
    peq = r.uniform(0, 255, (max(2, h // escala), max(2, w // escala))).astype(np.uint8)
    return Image.fromarray(peq).resize((w, h), Image.BICUBIC)


def fondo(color_a, color_b, semilla):
    y = np.linspace(0, 1, H)[:, None, None]
    a = np.array(color_a, float) * (1 - y) + np.array(color_b, float) * y
    a = np.broadcast_to(a, (H, W, 3)).copy()
    a += (np.asarray(ruido(W, H, 30, semilla), float)[..., None] - 128) * 0.06
    a += np.random.default_rng(semilla).normal(0, 3, a.shape)
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def con_sombra(base, mascara, desplazamiento=(30, 40), radio=28, fuerza=110):
    sombra = Image.new('L', (W, H), 0)
    sombra.paste(mascara.point(lambda v: fuerza if v > 0 else 0), desplazamiento)
    sombra = sombra.filter(ImageFilter.GaussianBlur(radio))
    return Image.composite(Image.new('RGB', (W, H), (30, 25, 20)), base, sombra)


def capa_guitarra():
    """La guitarra sola, girada y con transparencia (la usa también generar_resultados_esperados.py)."""
    # Silueta: dos círculos y la cintura, girada luego
    capa = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    m = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(m)
    cx, cy = 760, 760
    d.ellipse((cx - 330, cy - 120, cx + 330, cy + 440), fill=255)    # parte baja
    d.ellipse((cx - 250, cy - 420, cx + 250, cy + 40), fill=255)     # parte alta
    d.rectangle((cx - 230, cy - 200, cx + 230, cy + 120), fill=255)
    cuerpo = m.copy()
    d.rectangle((cx - 45, cy - 1050, cx + 45, cy - 300), fill=255)   # mástil
    d.polygon([(cx - 70, cy - 1300), (cx + 70, cy - 1300), (cx + 55, cy - 1040), (cx - 55, cy - 1040)], fill=255)  # pala
    # Color: «sunburst» del centro a los bordes
    yy, xx = np.mgrid[0:H, 0:W]
    dist = np.sqrt(((xx - cx) / 330) ** 2 + ((yy - cy - 60) / 420) ** 2)
    sol = np.clip(dist, 0, 1)[..., None]
    color = np.array([236, 170, 60]) * (1 - sol) + np.array([90, 30, 15]) * sol
    madera = (np.asarray(ruido(W, H, 4, 9), float)[..., None] - 128) * 0.08
    rgb = np.clip(color + madera * 255 / 128 * 0.4, 0, 255).astype(np.uint8)
    capa = Image.fromarray(rgb).convert('RGBA')
    capa.putalpha(cuerpo)
    dc = ImageDraw.Draw(capa)
    dc.ellipse((cx - 95, cy - 160, cx + 95, cy + 30), fill=(25, 18, 12, 255))           # boca
    dc.ellipse((cx - 115, cy - 180, cx + 115, cy + 50), outline=(240, 220, 170, 255), width=8)
    dc.rectangle((cx - 110, cy + 230, cx + 110, cy + 265), fill=(45, 28, 18, 255))      # puente
    mastil = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    dm = ImageDraw.Draw(mastil)
    dm.rectangle((cx - 45, cy - 1050, cx + 45, cy - 180), fill=(70, 42, 26, 255))
    dm.polygon([(cx - 70, cy - 1300), (cx + 70, cy - 1300), (cx + 55, cy - 1040), (cx - 55, cy - 1040)], fill=(52, 32, 20, 255))
    for i in range(1, 15):
        y = cy - 1040 + i * 55
        dm.line((cx - 45, y, cx + 45, y), fill=(200, 200, 205, 255), width=4)            # trastes
    for lado in (-1, 1):
        for k in range(3):
            dm.ellipse((cx + lado * 82 - 12, cy - 1270 + k * 75 - 12, cx + lado * 82 + 12, cy - 1270 + k * 75 + 12), fill=(210, 210, 215, 255))  # clavijas
    capa = Image.alpha_composite(capa, mastil)
    ds = ImageDraw.Draw(capa)
    for i in range(6):
        x = cx - 30 + i * 12
        ds.line((x, cy - 1040, x, cy + 248), fill=(225, 225, 230, 255), width=2)          # cuerdas
    m = capa.getchannel('A')
    return capa.rotate(-18, Image.BICUBIC, center=(cx, cy), translate=(160, 40))


def guitarra():
    base = fondo((232, 226, 214), (205, 198, 186), 3)
    gir = capa_guitarra()
    base = con_sombra(base, gir.getchannel('A'))
    base.paste(gir, (0, 0), gir)
    return base.filter(ImageFilter.GaussianBlur(0.6))


def mando():
    base = fondo((96, 120, 140), (60, 78, 96), 5)
    capa = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    m = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(m)
    cx, cy = 1000, 700
    d.rounded_rectangle((cx - 520, cy - 230, cx + 520, cy + 130), radius=170, fill=255)
    d.ellipse((cx - 640, cy - 120, cx - 260, cy + 430), fill=255)   # empuñaduras
    d.ellipse((cx + 260, cy - 120, cx + 640, cy + 430), fill=255)
    yy = np.linspace(0, 1, H)[:, None, None]
    grad = np.array([62, 64, 72]) * (1 - yy) + np.array([28, 29, 34]) * yy
    rgb = np.broadcast_to(grad, (H, W, 3)).astype(np.uint8)
    capa = Image.fromarray(rgb).convert('RGBA')
    capa.putalpha(m)
    dc = ImageDraw.Draw(capa)
    # Cruceta
    dc.rounded_rectangle((cx - 445, cy - 70, cx - 255, cy - 10), radius=10, fill=(18, 18, 22, 255))
    dc.rounded_rectangle((cx - 380, cy - 135, cx - 320, cy + 55), radius=10, fill=(18, 18, 22, 255))
    # Botones de colores
    for (dx, dy, col) in [(350, -100, (60, 200, 90)), (430, -40, (220, 60, 60)), (270, -40, (60, 120, 230)), (350, 20, (235, 200, 40))]:
        dc.ellipse((cx + dx - 34, cy + dy - 34, cx + dx + 34, cy + dy + 34), fill=col + (255,))
        dc.ellipse((cx + dx - 20, cy + dy - 26, cx + dx + 4, cy + dy - 10), fill=(255, 255, 255, 90))
    # Palancas
    for dx in (-170, 170):
        dc.ellipse((cx + dx - 85, cy + 60 - 85, cx + dx + 85, cy + 60 + 85), fill=(15, 15, 18, 255))
        dc.ellipse((cx + dx - 60, cy + 60 - 60, cx + dx + 60, cy + 60 + 60), fill=(48, 50, 56, 255))
    dc.ellipse((cx - 30, cy - 160, cx + 30, cy - 100), fill=(120, 220, 255, 255))  # botón central
    # Brillo superior
    brillo = Image.new('L', (W, H), 0)
    ImageDraw.Draw(brillo).rounded_rectangle((cx - 480, cy - 215, cx + 480, cy - 150), radius=40, fill=60)
    brillo = ImageChops.multiply(brillo.filter(ImageFilter.GaussianBlur(14)), m)
    capa = Image.composite(Image.new('RGBA', (W, H), (255, 255, 255, 255)), capa, brillo)
    capa.putalpha(m)
    base = con_sombra(base, m, (20, 45), 30, 140)
    base.paste(capa, (0, 0), capa)
    return base.filter(ImageFilter.GaussianBlur(0.6))


def textura():
    a = np.full((H, W, 3), (226, 212, 180), float)
    for esc, peso, s in [(200, 0.18, 1), (40, 0.10, 2), (6, 0.08, 3)]:
        a += (np.asarray(ruido(W, H, esc, s), float)[..., None] - 128) * peso
    manchas = np.asarray(ruido(W, H, 90, 7), float)
    a -= np.clip(manchas - 170, 0, 255)[..., None] * 0.8 * np.array([0.6, 0.8, 1.2])
    yy, xx = np.mgrid[0:H, 0:W]
    vi = ((xx / W - 0.5) ** 2 + (yy / H - 0.5) ** 2) ** 0.5
    a *= (1 - 0.45 * np.clip(vi - 0.3, 0, 1))[..., None]   # bordes más oscuros
    a += np.random.default_rng(4).normal(0, 4, a.shape)
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


if __name__ == '__main__':
    guitarra().save(SALIDA / 'capas-guitarra.jpg', quality=88)
    mando().save(SALIDA / 'capas-mando.jpg', quality=88)
    textura().save(SALIDA / 'capas-textura.jpg', quality=85)
    print('Material del 3.4 generado en', SALIDA)
