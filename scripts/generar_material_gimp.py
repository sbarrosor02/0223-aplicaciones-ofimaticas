"""Genera el material de la práctica guiada de GIMP y del punto de control del Tema 3.

Todo inventado y dibujado aquí mismo, sin imágenes de terceros.

Práctica guiada (cartel del concierto acústico de Los Picotas Eléctricas):
  guiada-escenario.jpg   foto de un escenario: torcida 3°, oscura, con dominante
                         naranja, motas de polvo y un letrero de SALIDA que sobra
  guiada-guitarra.jpg    la guitarra del 3.4, para recortarla
  guiada-textura.jpg     la textura de papel del 3.4, para el modo Multiplicar
  guiada-logo.png        el logotipo del festival en claro, con transparencia
  -> web/descargas/gimp-guiada-material.zip

Punto de control (Jerte Gaming Cup, torneo de videojuegos):
  pc-sala.jpg            foto de la sala del torneo: torcida 2°, lavada, con
                         dominante azul, motas y una lata en la mesa
  pc-auriculares.jpg     unos auriculares sobre fondo liso, para recortarlos
  pc-luces.jpg           luces desenfocadas sobre negro, para el modo Pantalla
  pc-logo.svg            logotipo vectorial del torneo
  -> web/descargas/gimp-control-material.zip

Las funciones *_limpia() devuelven la escena sin defectos: las usa
generar_resultados_esperados.py para dibujar cómo debe quedar cada paso.

Uso: python scripts/generar_material_gimp.py
"""
import io
import math
import sys
import zipfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / 'web' / 'descargas'
sys.path.insert(0, str(RAIZ / 'scripts'))
import generar_fotos_retoque as retoque          # noqa: E402
import generar_material_capas as capas           # noqa: E402
import generar_material_exportar as exportar     # noqa: E402

W, H = 2400, 1600
NEGRITA = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

# Defectos (los valores los usan también la página y el solucionario)
GUIADA_ANGULO = 3.0                       # grados
GUIADA_DOMINANTE = np.array([1.00, 0.84, 0.60])
PC_ANGULO = -2.0
GUIADA_MOTAS = [(60, 300, 300, 800), (1000, 180, 1400, 700), (520, 250, 760, 650)]   # pared gris y conos de luz
PC_DOMINANTE = np.array([0.82, 0.94, 1.12])


def a_img(a):
    return Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))


def a_arr(im):
    return np.asarray(im.convert('RGB'), np.float32) / 255


def girar(a, grados):
    """Gira la foto como si se hubiera hecho torcida y recorta para que no se vean esquinas."""
    im = a_img(a).rotate(grados, Image.BICUBIC)
    mx, my = int(W * 0.035), int(H * 0.05)
    return a_arr(im.crop((mx, my, W - mx, H - my)).resize((W, H), Image.BICUBIC))


def motas(a, semilla, zonas, n=12):
    """Motas de polvo del sensor. zonas = lista de (x0, y0, x1, y1) donde caen."""
    if isinstance(zonas[0], (int, float)):
        zonas = [zonas]
    im = a_img(a)
    capa = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(capa)
    r = np.random.default_rng(semilla)
    for i in range(n):
        zona = zonas[i % len(zonas)]
        x, y, rad = r.uniform(zona[0], zona[2]), r.uniform(zona[1], zona[3]), r.uniform(12, 22)
        d.ellipse((x - rad, y - rad, x + rad, y + rad), fill=int(r.uniform(80, 130)))
    capa = capa.filter(ImageFilter.GaussianBlur(5))
    return a_arr(Image.composite(Image.new('RGB', (W, H), (25, 25, 30)), im, capa))


def conos(img, x_arriba, x_abajo, ancho_ab, color, fuerza, semilla):
    """Suma un cono de luz de foco (de arriba hacia el suelo)."""
    m = Image.new('L', (W, H), 0)
    ImageDraw.Draw(m).polygon([(x_arriba - 25, -10), (x_arriba + 25, -10),
                               (x_abajo + ancho_ab, 1250), (x_abajo - ancho_ab, 1250)], fill=255)
    m = np.asarray(m.filter(ImageFilter.GaussianBlur(60)), np.float32) / 255
    humo = 0.6 + 0.6 * retoque.ruido2d(W, H, 90, semilla)
    return img + m[..., None] * humo[..., None] * np.array(color) * fuerza


# ------------------------------------------------------------------ escenario
def escenario_limpio(con_letrero=False):
    y = np.linspace(0, 1, H)[:, None]
    xs = np.arange(W)[None, :]
    # Telón de fondo: terciopelo granate oscuro con pliegues
    pliegue = 0.75 + 0.25 * np.sin(xs / 38.0 + 2 * retoque.ruido1d(W, 4, 3)[None, :]) ** 2
    img = np.broadcast_to((np.array([0.30, 0.07, 0.11]) * (0.55 + 0.45 * pliegue[..., None])), (H, W, 3)).copy()
    img *= (0.55 + 0.45 * y)[..., None]
    # Pared lateral gris neutro con el letrero (izquierda) y franja de techo negra
    img[:, :330] = np.array([0.36, 0.36, 0.36]) * (0.8 + 0.2 * retoque.ruido2d(W, H, 30, 4)[:, :330, None])
    img[:140] = 0.04
    # Suelo del escenario: tarima de madera, el borde (y = 1180) es horizontal
    filas = np.arange(H)[:, None]
    suelo = filas >= 1180
    tablas = 0.85 + 0.15 * np.sin((filas - 1180) / 9.0 + 3 * retoque.ruido2d(W, H, 50, 5)) ** 2
    madera = np.array([0.42, 0.28, 0.17]) * tablas[..., None] * (0.8 + 0.3 * retoque.ruido2d(W, H, 4, 6)[..., None])
    img = np.where(suelo[..., None], madera, img)
    img[1176:1186] = np.array([0.80, 0.80, 0.78])     # canto del escenario (blanco)
    # Focos
    for xa, xb, ab, col, f, s in [(500, 700, 330, (1.0, 0.75, 0.35), 0.55, 21), (1200, 1200, 380, (1.0, 0.92, 0.75), 0.65, 22),
                                  (1900, 1680, 330, (0.55, 0.35, 1.0), 0.45, 23)]:
        img = conos(img, xa, xb, ab, col, f, s)
    im = a_img(img)
    d = ImageDraw.Draw(im)
    # Amplificadores grises (la rejilla es gris neutro: sirve para el cuentagotas)
    for x0 in (420, 1760):
        d.rounded_rectangle((x0, 880, x0 + 260, 1180), radius=12, fill=(34, 34, 36))
        d.rectangle((x0 + 18, 920, x0 + 242, 1160), fill=(128, 128, 128))
        for k in range(0, 224, 8):
            d.line((x0 + 18 + k, 920, x0 + 18 + k, 1160), fill=(112, 112, 112), width=2)
        d.rectangle((x0 + 18, 892, x0 + 242, 910), fill=(70, 70, 72))
    # Batería (silueta en el centro)
    cx = 1200
    d.ellipse((cx - 150, 980, cx + 150, 1180), fill=(26, 22, 24), outline=(200, 200, 205), width=6)   # bombo
    d.ellipse((cx - 95, 1015, cx + 95, 1145), fill=(170, 40, 50))
    for dx, yy, r in ((-260, 960, 85), (250, 980, 95), (-170, 900, 60), (160, 890, 62)):
        d.ellipse((cx + dx - r, yy - r * 0.45, cx + dx + r, yy + r * 0.45), fill=(38, 34, 36), outline=(200, 200, 205), width=4)
    for dx, yy in ((-330, 760), (360, 740)):
        d.line((cx + dx, yy, cx + dx * 0.9, 1180), fill=(185, 185, 190), width=6)
        d.ellipse((cx + dx - 130, yy - 14, cx + dx + 130, yy + 14), fill=(200, 165, 60))                  # platos
    # Micrófonos y taburete
    for xm in (760, 1600):
        d.line((xm, 760, xm, 1180), fill=(30, 30, 32), width=8)
        d.line((xm - 70, 1180, xm + 70, 1180), fill=(30, 30, 32), width=8)
        d.ellipse((xm - 16, 735, xm + 16, 775), fill=(60, 60, 64))
    d.rectangle((880, 1000, 1000, 1012), fill=(25, 25, 28))
    d.line((900, 1012, 880, 1180), fill=(25, 25, 28), width=7)
    d.line((980, 1012, 1000, 1180), fill=(25, 25, 28), width=7)
    if con_letrero:   # el letrero de SALIDA que hay que quitar con Clonar
        d.rectangle((90, 380, 290, 470), fill=(18, 150, 70))
        d.rectangle((90, 380, 290, 470), outline=(230, 255, 235), width=5)
        d.text((190, 425), 'SALIDA', font=ImageFont.truetype(NEGRITA, 40), fill=(240, 255, 240), anchor='mm')
        d.line((190, 140, 190, 380), fill=(30, 30, 30), width=4)
    im = im.filter(ImageFilter.GaussianBlur(1.0))
    a = a_arr(im)
    a += np.random.default_rng(2027).normal(0, 0.015, a.shape).astype(np.float32)
    return np.clip(a, 0, 1)


def oscurecer(a):
    return 0.02 + 0.55 * np.clip(a, 0, 1) ** 1.5      # Niveles de entrada ≈ 5 · 1,50 · 145


def escenario_estropeado():
    a = escenario_limpio(con_letrero=True)
    a = oscurecer(a) * GUIADA_DOMINANTE
    a = motas(a, 31, GUIADA_MOTAS, 10)
    return girar(a, GUIADA_ANGULO)


def logo_claro(lado=800):
    """El logotipo del festival con las letras en crema, para fondos oscuros."""
    im = exportar.logo_png(lado)
    a = np.asarray(im).copy()
    oscuro = (a[..., 0] < 70) & (a[..., 1] < 70) & (a[..., 2] < 70) & (a[..., 3] > 0)
    a[oscuro, :3] = (246, 239, 230)
    return Image.fromarray(a)


# ------------------------------------------------------------------ sala del torneo
def sala_limpia(con_lata=False):
    y = np.linspace(0, 1, H)[:, None]
    img = np.broadcast_to(np.array([0.16, 0.16, 0.17]) * (1.1 - 0.4 * y)[..., None], (H, W, 3)).copy()
    img *= (0.9 + 0.2 * retoque.ruido2d(W, H, 40, 41))[..., None]
    im = a_img(img)
    d = ImageDraw.Draw(im)
    # Paneles acústicos grises (gris neutro para el cuentagotas)
    for i in range(6):
        for j in range(2):
            x0, y0 = 120 + i * 370, 120 + j * 250
            d.rectangle((x0, y0, x0 + 330, y0 + 210), fill=(118, 118, 118))
            for k in range(0, 210, 14):
                d.line((x0, y0 + k, x0 + 330, y0 + k), fill=(104, 104, 104), width=3)
    # Tira de LED
    led = Image.new('RGB', (W, H), 0)
    dl = ImageDraw.Draw(led)
    dl.line((0, 640, W, 640), fill=(255, 40, 200), width=14)
    led = led.filter(ImageFilter.GaussianBlur(18))
    im = Image.fromarray(np.clip(np.asarray(im, np.int16) + np.asarray(led, np.int16), 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(im)
    d.line((0, 640, W, 640), fill=(255, 150, 235), width=6)
    # Monitores con un juego en pantalla
    for x0, col in ((260, (40, 160, 255)), (980, (255, 120, 40)), (1700, (70, 220, 120))):
        d.rounded_rectangle((x0, 700, x0 + 520, 1010), radius=10, fill=(14, 14, 16))
        pant = Image.new('RGB', (480, 270), col)
        dp = ImageDraw.Draw(pant)
        for k in range(8):
            dp.rectangle((30 + k * 55, 200 - (k * 37) % 120, 70 + k * 55, 270), fill=tuple(int(c * 0.45) for c in col))
        dp.ellipse((200, 60, 260, 120), fill=(255, 255, 255))
        im.paste(pant, (x0 + 20, 720))
        d.rectangle((x0 + 235, 1010, x0 + 285, 1090), fill=(20, 20, 22))
    # Mesa: el borde (y = 1090) es horizontal
    d.rectangle((0, 1090, W, H), fill=(52, 54, 60))
    d.rectangle((0, 1090, W, 1104), fill=(150, 152, 158))
    for x0 in (330, 1050, 1770):    # teclados
        d.rounded_rectangle((x0, 1180, x0 + 380, 1260), radius=8, fill=(24, 24, 26))
        for k in range(14):
            d.rectangle((x0 + 12 + k * 26, 1192, x0 + 32 + k * 26, 1212), fill=(80, 200, 255))
        d.ellipse((x0 + 450, 1190, x0 + 510, 1265), fill=(24, 24, 26))
    if con_lata:      # la lata que hay que quitar con Clonar
        d.rounded_rectangle((870, 980, 950, 1150), radius=12, fill=(200, 25, 30))
        d.rectangle((870, 1010, 950, 1030), fill=(240, 240, 240))
        d.ellipse((870, 968, 950, 992), fill=(190, 190, 195))
    im = im.filter(ImageFilter.GaussianBlur(1.0))
    a = a_arr(im)
    a += np.random.default_rng(3031).normal(0, 0.015, a.shape).astype(np.float32)
    return np.clip(a, 0, 1)


def lavar(a):
    return 0.22 + 0.55 * np.clip(a, 0, 1)            # Niveles de entrada ≈ 56 · 1,00 · 196


def sala_estropeada():
    a = sala_limpia(con_lata=True)
    a = np.clip(lavar(a) * PC_DOMINANTE, 0, 1)
    a = motas(a, 77, (150, 120, 2300, 600))
    return girar(a, PC_ANGULO)


def auriculares_capa(lado=1500):
    """Los auriculares solos, con transparencia (W × H de capas: 2000 × 1500)."""
    CW, CH = capas.W, capas.H
    capa = Image.new('RGBA', (CW, CH), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    cx, cy = 1000, 760
    d.arc((cx - 470, cy - 560, cx + 470, cy + 380), 190, 350, fill=(30, 30, 34, 255), width=70)     # diadema
    d.arc((cx - 430, cy - 520, cx + 430, cy + 340), 200, 340, fill=(70, 72, 80, 255), width=14)
    for lado_x in (-1, 1):
        x = cx + lado_x * 440
        d.rounded_rectangle((x - 150, cy - 40, x + 150, cy + 380), radius=120, fill=(26, 26, 30, 255))   # cascos
        d.rounded_rectangle((x - 110, cy, x + 110, cy + 340), radius=100, fill=(46, 48, 54, 255))
        d.ellipse((x - 60, cy + 110, x + 60, cy + 230), fill=(0, 220, 255, 255))                        # luz
        d.ellipse((x - 35, cy + 135, x + 35, cy + 205), fill=(180, 250, 255, 255))
        d.rectangle((x - 30, cy - 130, x + 30, cy - 30), fill=(60, 62, 70, 255))                        # brazo
    d.line((cx - 440, cy + 330, cx - 640, cy + 560), fill=(30, 30, 34, 255), width=18)                   # micro
    d.ellipse((cx - 680, cy + 530, cx - 610, cy + 600), fill=(20, 20, 24, 255))
    return capa


def auriculares():
    base = capas.fondo((236, 236, 238), (205, 206, 210), 9)
    cap = auriculares_capa()
    base = capas.con_sombra(base, cap.getchannel('A'), (25, 45), 30, 120)
    base.paste(cap, (0, 0), cap)
    return base.filter(ImageFilter.GaussianBlur(0.6))


def luces(ancho=2000, alto=1500):
    im = Image.new('RGB', (ancho, alto), 0)
    r = np.random.default_rng(55)
    capa = Image.new('RGB', (ancho, alto), 0)
    d = ImageDraw.Draw(capa)
    cols = [(255, 40, 200), (40, 200, 255), (130, 80, 255), (255, 170, 40)]
    for _ in range(45):
        x, y, rad = r.uniform(0, ancho), r.uniform(0, alto), r.uniform(25, 110)
        c = cols[int(r.integers(0, 4))]
        f = r.uniform(0.35, 0.9)
        d.ellipse((x - rad, y - rad, x + rad, y + rad), fill=tuple(int(v * f) for v in c))
    im = capa.filter(ImageFilter.GaussianBlur(16))
    return im


def logo_pc_svg():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<!-- Logotipo inventado del torneo Jerte Gaming Cup (punto de control del Tema 3) -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <path d="M100 12 L172 40 L164 116 C158 150 132 174 100 188 C68 174 42 150 36 116 L28 40 Z" fill="#14161f" stroke="#00dcff" stroke-width="7" stroke-linejoin="round"/>
  <path d="M60 78 h80 a24 24 0 0 1 0 48 h-10 l-10 -12 h-40 l-10 12 h-10 a24 24 0 0 1 0 -48 Z" fill="#ff28c8"/>
  <rect x="64" y="96" width="22" height="7" rx="2" fill="#14161f"/>
  <rect x="71.5" y="88.5" width="7" height="22" rx="2" fill="#14161f"/>
  <circle cx="124" cy="94" r="5" fill="#14161f"/><circle cx="136" cy="104" r="5" fill="#14161f"/>
  <text x="100" y="62" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-weight="700" font-size="21" fill="#ffffff">JERTE</text>
  <text x="100" y="148" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-weight="700" font-size="12" fill="#00dcff">GAMING CUP</text>
</svg>
'''


def logo_pc_png(lado):
    """El SVG convertido a PNG con rsvg-convert (para las imágenes de ejemplo)."""
    import subprocess, tempfile
    with tempfile.TemporaryDirectory() as t:
        s = Path(t) / 'l.svg'; s.write_text(logo_pc_svg(), encoding='utf-8')
        p = Path(t) / 'l.png'
        subprocess.run(['rsvg-convert', '-w', str(lado), '-h', str(lado), '-o', str(p), str(s)], check=True)
        return Image.open(p).convert('RGBA').copy()


def jpg(im, calidad=88):
    b = io.BytesIO(); im.convert('RGB').save(b, 'JPEG', quality=calidad); return b.getvalue()


def png(im):
    b = io.BytesIO(); im.save(b, 'PNG', optimize=True); return b.getvalue()


LEEME_GUIADA = '''Material de la práctica guiada de GIMP · Tema 3 · 0223 Aplicaciones ofimáticas
==============================================================================

guiada-escenario.jpg  la foto del escenario que vas a retocar (parte A)
guiada-guitarra.jpg   la guitarra que vas a recortar (parte B)
guiada-textura.jpg    textura de papel para el modo Multiplicar (parte B)
guiada-logo.png       el logotipo del festival, con transparencia (parte B)

Todo es material inventado para practicar. Copia la carpeta entera en
Tema3_Proyecto/guiada y trabaja siempre sobre copias.
'''

LEEME_PC = '''Material del punto de control · Tema 3 · 0223 Aplicaciones ofimáticas
=====================================================================

pc-sala.jpg         la foto de la sala del torneo, para retocar
pc-auriculares.jpg  los auriculares, para recortarlos
pc-luces.jpg        luces desenfocadas sobre negro, para el modo Pantalla
pc-logo.svg         el logotipo del torneo, en vectorial

Todo es material inventado. Copia la carpeta entera en Tema3_Proyecto/control.
'''


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(SALIDA / 'gimp-guiada-material.zip', 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('gimp-guiada/guiada-escenario.jpg', jpg(a_img(escenario_estropeado())))
        z.writestr('gimp-guiada/guiada-guitarra.jpg', jpg(capas.guitarra()))
        z.writestr('gimp-guiada/guiada-textura.jpg', jpg(capas.textura(), 85))
        z.writestr('gimp-guiada/guiada-logo.png', png(logo_claro(800)))
        z.writestr('gimp-guiada/LEEME.txt', LEEME_GUIADA.replace('\n', '\r\n'))
    with zipfile.ZipFile(SALIDA / 'gimp-control-material.zip', 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('gimp-control/pc-sala.jpg', jpg(a_img(sala_estropeada())))
        z.writestr('gimp-control/pc-auriculares.jpg', jpg(auriculares()))
        z.writestr('gimp-control/pc-luces.jpg', jpg(luces(), 85))
        z.writestr('gimp-control/pc-logo.svg', logo_pc_svg())
        z.writestr('gimp-control/LEEME.txt', LEEME_PC.replace('\n', '\r\n'))
    for n in ('gimp-guiada-material.zip', 'gimp-control-material.zip'):
        print(f'{n:30s} {(SALIDA / n).stat().st_size / 1024 / 1024:6.2f} MB')


if __name__ == '__main__':
    main()
