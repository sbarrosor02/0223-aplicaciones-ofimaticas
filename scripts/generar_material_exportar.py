"""Genera el material del Tema 3.5 (importar, exportar y optimizar).

Todo inventado y dibujado aquí mismo, sin imágenes de terceros:

  importar-cartel.pdf            cartel A5 VECTORIAL de un festival inventado (PDF escrito a mano)
  importar-logo.svg              logotipo vectorial del festival
  importar-logo-pequeno.png      el mismo logotipo en mapa de bits de 120 × 120 px
  exportar-logo-transparente.png logotipo de 1000 × 1000 px con fondo transparente
  exportar-foto.jpg              el paisaje del 3.3 sin defectos, 2400 × 1600 px
  (y web/assets/img/entregas/p35-cartel.png, vista previa del cartel, si está pdftoppm)

Uso: python scripts/generar_material_exportar.py
Solo usa la biblioteca estándar, Pillow y NumPy (el PDF se escribe a mano para
que sea vectorial de verdad).
"""
import math
import shutil
import subprocess
import sys
import zlib
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / 'web' / 'descargas'
sys.path.insert(0, str(RAIZ / 'scripts'))
import generar_fotos_retoque as retoque  # noqa: E402

CEREZA = (0.70, 0.07, 0.23)
HOJA = (0.37, 0.62, 0.23)
NOCHE = (0.12, 0.10, 0.14)
CREMA = (0.96, 0.94, 0.90)
FUENTE_N = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


# ------------------------------------------------------------------- PDF vectorial
def _circulo(cx, cy, r):
    k = 0.5523 * r
    return (f'{cx + r:.2f} {cy:.2f} m '
            f'{cx + r:.2f} {cy + k:.2f} {cx + k:.2f} {cy + r:.2f} {cx:.2f} {cy + r:.2f} c '
            f'{cx - k:.2f} {cy + r:.2f} {cx - r:.2f} {cy + k:.2f} {cx - r:.2f} {cy:.2f} c '
            f'{cx - r:.2f} {cy - k:.2f} {cx - k:.2f} {cy - r:.2f} {cx:.2f} {cy - r:.2f} c '
            f'{cx + k:.2f} {cy - r:.2f} {cx + r:.2f} {cy - k:.2f} {cx + r:.2f} {cy:.2f} c f ')


def _color(rgb):
    return '%.3f %.3f %.3f rg ' % rgb


def _texto(x, y, tam, txt, fuente='F2', centrado=False, ancho=420):
    # Helvetica: ancho medio aproximado para centrar
    if centrado:
        x = (ancho - len(txt) * tam * (0.62 if fuente == 'F2' else 0.52)) / 2
    t = txt.encode('cp1252').replace(b'\\', b'\\\\').replace(b'(', b'\\(').replace(b')', b'\\)')
    return b'BT /' + fuente.encode() + b' %d Tf %.1f %.1f Td (' % (tam, x, y) + t + b') Tj ET '


def cartel_pdf(destino):
    w, h = 420, 595  # A5 en puntos
    c = [(_color(NOCHE) + f'0 0 {w} {h} re f ').encode()]
    # Cerezas grandes
    c.append((_color(HOJA) + '210 470 m 250 520 300 530 330 520 c 300 500 260 480 210 470 c f ').encode())
    c.append(b'0.62 0.45 0.28 RG 4 w 210 470 m 170 400 150 380 140 360 S 210 470 m 230 400 250 380 265 355 S ')
    c.append((_color(CEREZA) + _circulo(140, 330, 48) + _circulo(265, 325, 52)).encode())
    c.append((_color((0.95, 0.55, 0.62)) + _circulo(122, 350, 10) + _circulo(245, 348, 11)).encode())
    # Textos
    c.append(_color(CREMA).encode())
    c.append(_texto(0, 230, 34, 'CEREZO ROCK', centrado=True))
    c.append(_texto(0, 200, 14, 'FESTIVAL DEL VALLE · 2027', 'F1', centrado=True))
    c.append((_color(CEREZA) + '60 182 300 2 re f ').encode())
    c.append(_color(CREMA).encode())
    for i, linea in enumerate(['Los Picotas Eléctricas', 'Garganta Profunda', 'Niebla en Tornavacas', 'Píxel y los Mandos']):
        c.append(_texto(0, 150 - i * 22, 15, linea, 'F1', centrado=True))
    c.append(_color((0.80, 0.78, 0.74)).encode())
    c.append(_texto(0, 40, 11, 'Sábado 17 de abril · Cabezuela del Valle · Entrada libre', 'F1', centrado=True))
    contenido = b''.join(c)
    objetos = [
        b'<< /Type /Catalog /Pages 2 0 R >>',
        b'<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
        b'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 %d %d] /Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> /Contents 4 0 R >>' % (w, h),
        b'<< /Length %d /Filter /FlateDecode >>\nstream\n' % len(zlib.compress(contenido)) + zlib.compress(contenido) + b'\nendstream',
        b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>',
        b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>',
        b'<< /Title (Cartel del festival Cerezo Rock - material inventado) /Creator (generar_material_exportar.py) >>',
    ]
    pdf = bytearray(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')
    pos = []
    for i, o in enumerate(objetos, 1):
        pos.append(len(pdf))
        pdf += b'%d 0 obj\n' % i + o + b'\nendobj\n'
    xref = len(pdf)
    pdf += b'xref\n0 %d\n0000000000 65535 f \n' % (len(objetos) + 1)
    for p in pos:
        pdf += b'%010d 00000 n \n' % p
    pdf += b'trailer\n<< /Size %d /Root 1 0 R /Info 7 0 R >>\nstartxref\n%d\n%%%%EOF\n' % (len(objetos) + 1, xref)
    destino.write_bytes(bytes(pdf))


# ------------------------------------------------------------------- logotipo
def logo_svg(destino):
    destino.write_text('''<?xml version="1.0" encoding="UTF-8"?>
<!-- Logotipo inventado del festival Cerezo Rock (material del Tema 3.5) -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <path d="M100 40 C120 60 145 66 160 60 C146 50 124 42 100 40 Z" fill="#5e9e3a"/>
  <path d="M100 40 C84 80 72 96 66 112 M100 40 C110 80 122 96 132 110" stroke="#4d3320" stroke-width="5" fill="none" stroke-linecap="round"/>
  <circle cx="66" cy="132" r="28" fill="#b3123a"/>
  <circle cx="134" cy="130" r="30" fill="#b3123a"/>
  <circle cx="56" cy="122" r="6" fill="#f28c9e"/>
  <circle cx="124" cy="120" r="6" fill="#f28c9e"/>
  <text x="100" y="190" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-weight="700" font-size="22" fill="#1e1a24">CEREZO ROCK</text>
</svg>
''', encoding='utf-8')


def logo_png(lado, transparente=True):
    """Dibuja el mismo logotipo que el SVG en un mapa de bits de «lado» píxeles."""
    s = lado / 200
    im = Image.new('RGBA', (lado, lado), (0, 0, 0, 0) if transparente else (255, 255, 255, 255))
    d = ImageDraw.Draw(im)
    def bez(p0, p1, p2, p3, n=40):
        return [((1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t * t * p2[0] + t ** 3 * p3[0],
                 (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t * t * p2[1] + t ** 3 * p3[1]) for t in [i / n for i in range(n + 1)]]
    esc = lambda pts: [(x * s, y * s) for x, y in pts]
    d.polygon(esc(bez((100, 40), (120, 60), (145, 66), (160, 60)) + bez((160, 60), (146, 50), (124, 42), (100, 40))), fill='#5e9e3a')
    for pts in (bez((100, 40), (84, 80), (72, 96), (66, 112)), bez((100, 40), (110, 80), (122, 96), (132, 110))):
        d.line(esc(pts), fill='#4d3320', width=max(1, round(5 * s)), joint='curve')
    for cx, cy, r, col in ((66, 132, 28, '#b3123a'), (134, 130, 30, '#b3123a'), (56, 122, 6, '#f28c9e'), (124, 120, 6, '#f28c9e')):
        d.ellipse(((cx - r) * s, (cy - r) * s, (cx + r) * s, (cy + r) * s), fill=col)
    f = ImageFont.truetype(FUENTE_N, max(6, round(20 * s)))
    d.text((100 * s, 190 * s), 'CEREZO ROCK', font=f, fill='#1e1a24', anchor='ms')
    return im


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    cartel_pdf(SALIDA / 'importar-cartel.pdf')
    logo_svg(SALIDA / 'importar-logo.svg')
    logo_png(120, transparente=False).convert('RGB').save(SALIDA / 'importar-logo-pequeno.png', optimize=True)
    logo_png(1000).save(SALIDA / 'exportar-logo-transparente.png', optimize=True)
    a = retoque.paisaje()
    Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).save(SALIDA / 'exportar-foto.jpg', quality=95)
    # Vista previa del cartel para la página (si está pdftoppm, de poppler-utils)
    if shutil.which('pdftoppm'):
        previa = RAIZ / 'web' / 'assets' / 'img' / 'entregas' / 'p35-cartel'
        subprocess.run(['pdftoppm', '-r', '72', '-png', '-singlefile', str(SALIDA / 'importar-cartel.pdf'), str(previa)], check=True)
    for n in ('importar-cartel.pdf', 'importar-logo.svg', 'importar-logo-pequeno.png', 'exportar-logo-transparente.png', 'exportar-foto.jpg'):
        print(f'{n:32s} {(SALIDA / n).stat().st_size / 1024:8.1f} KB')


if __name__ == '__main__':
    main()
