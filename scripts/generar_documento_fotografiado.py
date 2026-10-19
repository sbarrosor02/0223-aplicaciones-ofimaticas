"""Genera dos fotos simuladas de un documento hecho con el móvil (Tema 3.2).

Sirven para la P3.2.1 a quien no tenga móvil o no quiera usarlo: la hoja sale
torcida, con sombra y sobre una mesa, como una foto real hecha con prisa.
El contenido es inventado (normas de un local de ensayo y bases de un torneo).

Uso: python scripts/generar_documento_fotografiado.py
Salida: web/descargas/documento-fotografiado-1.jpg y -2.jpg
"""
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / 'web' / 'descargas'
FUENTE = '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
FUENTE_N = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'

HOJAS = [
    ('Local de ensayo «La Garganta» · Normas de uso', [
        '1. El local se reserva por franjas de dos horas en el tablón de la entrada.',
        '2. Cada grupo deja la batería y los amplificadores como los encontró.',
        '3. El volumen máximo es de 95 decibelios a partir de las nueve de la noche.',
        '4. Está prohibido comer y beber junto a la mesa de mezclas.',
        '5. Los cables se recogen enrollados, nunca anudados.',
        '6. Si algo se rompe, se apunta en el cuaderno de incidencias el mismo día.',
        '7. La llave se devuelve en conserjería antes de las once.',
        '8. Quien incumpla tres veces las normas pierde la reserva un mes.',
    ]),
    ('Torneo de videojuegos del instituto · Bases', [
        '1. Pueden participar parejas de cualquier curso del centro.',
        '2. Las inscripciones se hacen en la biblioteca hasta el 6 de noviembre.',
        '3. Cada partida dura doce minutos y se juega al mejor de tres.',
        '4. Los mandos los pone la organización; no se admiten mandos propios.',
        '5. Los empates se resuelven con una prórroga de tres minutos.',
        '6. La final se retransmite en la pantalla grande del salón de actos.',
        '7. El premio es un lote de juegos de mesa para la clase ganadora.',
        '8. La organización puede cambiar el horario si hay algún problema.',
    ]),
]


def hoja(titulo, lineas, n):
    w, h = 1240, 1754  # A4 a 150 ppp
    im = Image.new('RGB', (w, h), (250, 249, 244))
    d = ImageDraw.Draw(im)
    ft, fl, fp = ImageFont.truetype(FUENTE_N, 40), ImageFont.truetype(FUENTE, 29), ImageFont.truetype(FUENTE, 22)
    d.text((110, 140), titulo, font=ft, fill=(25, 25, 25))
    d.line((110, 205, w - 110, 205), fill=(60, 60, 60), width=3)
    y = 270
    for linea in lineas:
        palabras, actual = linea.split(), ''
        for p in palabras:
            prueba = (actual + ' ' + p).strip()
            if d.textlength(prueba, font=fl) > w - 240:
                d.text((110, y), actual, font=fl, fill=(30, 30, 30))
                y += 46
                actual = p
            else:
                actual = prueba
        d.text((110, y), actual, font=fl, fill=(30, 30, 30))
        y += 72
    d.text((110, h - 130), f'Hoja {n} de 2 · Documento inventado para practicar', font=fp, fill=(90, 90, 90))
    return im


def mesa(w, h, semilla):
    rnd = random.Random(semilla)
    im = Image.new('RGB', (w, h), (122, 86, 58))
    d = ImageDraw.Draw(im)
    for y in range(0, h, 3):  # vetas de madera
        t = rnd.randint(-14, 14)
        d.line((0, y, w, y), fill=(122 + t, 86 + t, 58 + t // 2), width=3)
    return im.filter(ImageFilter.GaussianBlur(1.2))


def coeficientes(origen, destino):
    """Coeficientes de Image.transform(PERSPECTIVE) que llevan destino -> origen."""
    import numpy as np
    filas, b = [], []
    for (x, y), (u, v) in zip(destino, origen):
        filas.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); b.append(u)
        filas.append([0, 0, 0, x, y, 1, -v * x, -v * y]); b.append(v)
    return np.linalg.solve(np.array(filas, float), np.array(b, float)).tolist()


def foto(n, titulo, lineas):
    papel = hoja(titulo, lineas, n)
    W, H = 2000, 2600
    fondo = mesa(W, H, n)
    pw, ph = papel.size
    # Esquinas de la hoja en la foto: torcida y algo en perspectiva
    destino = [(330, 300), (1690, 360), (1790, 2330), (230, 2260)] if n == 1 else \
              [(290, 360), (1650, 290), (1760, 2250), (200, 2350)]
    origen = [(0, 0), (pw, 0), (pw, ph), (0, ph)]
    c = coeficientes(origen, destino)
    hoja_t = papel.transform((W, H), Image.PERSPECTIVE, c, Image.BICUBIC)
    mascara = Image.new('L', (pw, ph), 255).transform((W, H), Image.PERSPECTIVE, c, Image.BICUBIC)
    # Sombra de la hoja sobre la mesa
    sombra = Image.new('L', (W, H), 0)
    ImageDraw.Draw(sombra).polygon([(x + 25, y + 30) for x, y in destino], fill=150)
    sombra = sombra.filter(ImageFilter.GaussianBlur(25))
    fondo.paste((40, 28, 18), (0, 0), sombra)
    fondo.paste(hoja_t, (0, 0), mascara)
    # Luz irregular: más oscuro en una esquina (la sombra del móvil y la mano)
    luz = Image.new('L', (W, H), 0)
    ImageDraw.Draw(luz).ellipse((-700, 1500, 1300, 3600), fill=95)
    luz = luz.filter(ImageFilter.GaussianBlur(160))
    fondo.paste((0, 0, 0), (0, 0), luz)
    fondo = fondo.filter(ImageFilter.GaussianBlur(0.8))
    fondo.save(SALIDA / f'documento-fotografiado-{n}.jpg', quality=85)


if __name__ == '__main__':
    for i, (t, l) in enumerate(HOJAS, 1):
        foto(i, t, l)
    print('Generadas', [f'documento-fotografiado-{i}.jpg' for i in (1, 2)])
