"""Genera las imágenes «Cómo debe quedar» de los recuadros Entrega del Tema 3.

Parte del mismo material inventado que se da al alumnado (los generadores
de fotos de retoque, del documento fotografiado y de las capas), así que el
resultado esperado coincide con lo que sale si se hace bien la práctica:

  p31-vectorial-mapa.png     el mismo logotipo ampliado al 800 %: vectorial y mapa de bits
  p33-foto1.jpg              foto 1 antes y después de enderezar y aplicar niveles
  p33-foto2.jpg              foto 2 antes y después de quitar la dominante
  p33-foto3.jpg              foto 3 antes y después de sanear y clonar
  p33-documento.jpg          foto 4 antes y después de corregir la perspectiva
  p34-recorte.jpg            guitarra recortada sobre la textura con sombra nueva
  p34-fusion.jpg             paisaje con la textura en Multiplicar y un degradado en Pantalla
  p34-fundido.jpg            paisaje que se convierte en la composición de la guitarra con una máscara
  p34-miniatura.jpg          miniatura de 1280 × 720 con título y línea secundaria

Uso: python scripts/generar_resultados_esperados.py
Salida: web/assets/img/entregas/
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / 'scripts'))
import generar_fotos_retoque as retoque          # noqa: E402
import generar_documento_fotografiado as docfoto  # noqa: E402
import generar_material_capas as capas           # noqa: E402

SALIDA = RAIZ / 'web' / 'assets' / 'img' / 'entregas'
NEGRITA = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
NORMAL = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
ANCHO = 900  # ancho de las parejas antes/después


def a_imagen(a):
    return Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))


def rotulo(im, texto):
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(NEGRITA, 22)
    w = d.textlength(texto, font=f)
    y = im.height - 46
    d.rounded_rectangle((10, y, 30 + w, y + 36), radius=6, fill=(20, 24, 30))
    d.text((20, y + 4), texto, font=f, fill=(255, 255, 255))
    return im


def pareja(antes, despues, nombre):
    """Antes y después lado a lado, con la misma altura."""
    alto = 300
    a = antes.resize((round(antes.width * alto / antes.height), alto), Image.LANCZOS)
    b = despues.resize((round(despues.width * alto / despues.height), alto), Image.LANCZOS)
    lienzo = Image.new('RGB', (a.width + b.width + 12, alto), (255, 255, 255))
    lienzo.paste(rotulo(a, 'Antes'), (0, 0))
    lienzo.paste(rotulo(b, 'Después'), (a.width + 12, 0))
    if lienzo.width > ANCHO * 1.4:
        lienzo = lienzo.resize((round(ANCHO * 1.4), round(alto * ANCHO * 1.4 / lienzo.width)), Image.LANCZOS)
    lienzo.save(SALIDA / nombre, quality=82)


def vectorial_mapa():
    """P3.1.4: el mismo dibujo, nítido (vectorial) y pixelado (mapa de bits pequeño ampliado)."""
    def logo(lado):
        im = Image.new('RGB', (lado, lado), (255, 255, 255))
        d = ImageDraw.Draw(im)
        k = lado / 40
        d.ellipse((4 * k, 4 * k, 36 * k, 36 * k), fill=(31, 92, 143))
        d.polygon([(14 * k, 12 * k), (30 * k, 20 * k), (14 * k, 28 * k)], fill=(255, 255, 255))
        return im
    nitido = logo(320)
    pixelado = logo(40).resize((320, 320), Image.NEAREST)
    lienzo = Image.new('RGB', (652, 320), (255, 255, 255))
    lienzo.paste(rotulo(nitido, 'SVG al 800 %'), (0, 0))
    lienzo.paste(rotulo(pixelado, 'PNG al 800 %'), (332, 0))
    lienzo.save(SALIDA / 'p31-vectorial-mapa.png')


def sombra_nueva(fondo, objeto, desplazamiento, radio, fuerza):
    alfa = objeto.getchannel('A')
    sombra = Image.new('L', fondo.size, 0)
    sombra.paste(alfa.point(lambda v: fuerza if v > 0 else 0), desplazamiento)
    sombra = sombra.filter(ImageFilter.GaussianBlur(radio))
    return Image.composite(Image.new('RGB', fondo.size, (40, 30, 20)), fondo, sombra)


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)

    # Tema 3.1
    vectorial_mapa()

    # Tema 3.3: el «después» es el paisaje del que salen las fotos estropeadas
    base = retoque.paisaje()
    original = a_imagen(base)
    w, h = original.size
    k = 0.918  # lo que queda tras enderezar 3,5° y recortar sin esquinas vacías
    recorte = original.crop((round(w * (1 - k) / 2), round(h * (1 - k) / 2),
                             round(w * (1 + k) / 2), round(h * (1 + k) / 2)))
    pareja(a_imagen(retoque.torcida_oscura(base)), recorte, 'p33-foto1.jpg')
    pareja(a_imagen(retoque.lavada_amarilla(base)), original, 'p33-foto2.jpg')
    pareja(a_imagen(retoque.manchas_cable(base)), original, 'p33-foto3.jpg')
    hoja = docfoto.hoja(*docfoto.HOJAS[0], 1)
    foto4 = Image.open(RAIZ / 'web' / 'descargas' / 'documento-fotografiado-1.jpg')
    pareja(foto4, hoja, 'p33-documento.jpg')

    # Tema 3.4 (a 1000 px de ancho: la mitad del material)
    textura = capas.textura()
    guitarra = capas.capa_guitarra()
    fondo = sombra_nueva(textura, guitarra, (-40, 30), 22, 120)  # luz desde la derecha
    fondo.paste(guitarra, (0, 0), guitarra)
    fondo.resize((1000, 750), Image.LANCZOS).save(SALIDA / 'p34-recorte.jpg', quality=82)

    paisaje = original.resize(textura.size, Image.LANCZOS)
    multiplicar = np.asarray(paisaje, float) * np.asarray(textura, float) / 255
    y = np.linspace(0, 1, textura.height)[:, None, None]
    degradado = np.broadcast_to(np.array([255, 140, 60]) * (1 - y), multiplicar.shape)
    pantalla = 255 - (255 - multiplicar) * (255 - degradado) / 255
    fusion = Image.fromarray(np.clip(multiplicar * 0.6 + pantalla * 0.4, 0, 255).astype(np.uint8))
    fusion.resize((1000, 750), Image.LANCZOS).save(SALIDA / 'p34-fusion.jpg', quality=82)

    # La capa de arriba (la composición de la P3.4.1) con una máscara en degradado
    x = np.linspace(0, 1, textura.width)[None, :]
    rampa = np.broadcast_to(np.clip((x - 0.3) / 0.4, 0, 1), (textura.height, textura.width))
    mascara = Image.fromarray((rampa * 255).astype(np.uint8))
    fundido = Image.composite(fondo, paisaje, mascara)
    fundido.resize((1000, 750), Image.LANCZOS).save(SALIDA / 'p34-fundido.jpg', quality=82)

    mini = fundido.resize((1280, 960), Image.LANCZOS).crop((0, 120, 1280, 840))
    d = ImageDraw.Draw(mini)
    d.rectangle((0, 470, 1280, 720), fill=(15, 18, 24))
    titulo, sub = ImageFont.truetype(NEGRITA, 104), ImageFont.truetype(NORMAL, 44)
    d.text((60, 490), 'MI PRIMER TEMA', font=titulo, fill=(255, 214, 90))
    d.text((64, 628), 'Grabado en el local de ensayo', font=sub, fill=(240, 240, 240))
    mini.save(SALIDA / 'p34-miniatura.jpg', quality=85)

    print('Imágenes generadas en', SALIDA)


if __name__ == '__main__':
    main()
