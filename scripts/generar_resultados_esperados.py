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
  p35-importar.png           el logotipo abierto desde el SVG frente al PNG pequeño ampliado
  p35-transparencia.png      el logotipo exportado en PNG (transparente) y en JPG (fondo blanco)
  p36-redes.jpg              la misma foto para un post 4:5, una historia y un banner de YouTube, con las zonas seguras
  p36-cartel.jpg             el flyer A5 con sangrado: corte, zona segura y fondo hasta el borde
  p36-web.jpg                la plantilla web rellena, vista en el ordenador y en el móvil (si está Playwright)

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
import generar_material_exportar as exportar     # noqa: E402

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

    # Tema 3.5: SVG frente a PNG pequeño, los dos a 2000 px; se muestra ampliada la misma zona
    nitido = exportar.logo_png(2000, transparente=False).convert('RGB')
    borroso = exportar.logo_png(120, transparente=False).convert('RGB').resize((2000, 2000), Image.BICUBIC)
    zona = (380, 1000, 1380, 1600)
    pareja_import = Image.new('RGB', (1012, 600), (255, 255, 255))
    pareja_import.paste(rotulo(nitido.crop(zona).resize((500, 300)), 'Desde el SVG'), (0, 0))
    pareja_import.paste(rotulo(borroso.crop(zona).resize((500, 300)), 'PNG de 120 px ampliado'), (512, 0))
    pareja_import = pareja_import.crop((0, 0, 1012, 300))
    pareja_import.save(SALIDA / 'p35-importar.png', optimize=True)

    # Transparencia: el PNG deja ver el fondo de cuadros; el JPG lo rellena de blanco
    logo = exportar.logo_png(400)
    cuadros = Image.new('RGB', (400, 400), (255, 255, 255))
    dc = ImageDraw.Draw(cuadros)
    for i in range(0, 400, 20):
        for j in range(0, 400, 20):
            if (i // 20 + j // 20) % 2:
                dc.rectangle((i, j, i + 19, j + 19), fill=(205, 205, 205))
    con_png = cuadros.copy(); con_png.paste(logo, (0, 0), logo)
    con_jpg = cuadros.copy(); blanco = Image.new('RGB', (400, 400), (255, 255, 255)); blanco.paste(logo, (0, 0), logo)
    con_jpg.paste(blanco.crop((0, 0, 400, 400)), (0, 0))
    t = Image.new('RGB', (848, 470), (214, 222, 230))   # gris alrededor: así se ve el blanco del JPG
    dt = ImageDraw.Draw(t)
    f = ImageFont.truetype(NEGRITA, 24)
    for x, im, txt in ((16, con_png, 'PNG: transparente'), (432, con_jpg, 'JPG: fondo blanco')):
        dt.text((x, 14), txt, font=f, fill=(20, 24, 30))
        t.paste(im, (x, 54))
    t.save(SALIDA / 'p35-transparencia.png', optimize=True)

    publicar()
    print('Imágenes generadas en', SALIDA)


# ------------------------------------------------------------------- Tema 3.6
def recorte(im, w, h, cx=0.5, cy=0.5):
    """Recorta la proporción w:h de im (centrado en cx, cy) y la escala a w × h."""
    ar = w / h
    if im.width / im.height > ar:
        cw, ch = round(im.height * ar), im.height
    else:
        cw, ch = im.width, round(im.width / ar)
    x = round((im.width - cw) * cx); y = round((im.height - ch) * cy)
    return im.crop((x, y, x + cw, y + ch)).resize((w, h), Image.LANCZOS)


def texto_centrado(d, cx, y, txt, tam, color=(255, 255, 255), negrita=True, sombra=True):
    f = ImageFont.truetype(NEGRITA if negrita else NORMAL, tam)
    if sombra:
        d.text((cx + max(2, tam // 18), y + max(2, tam // 18)), txt, font=f, fill=(0, 0, 0), anchor='ma')
    d.text((cx, y), txt, font=f, fill=color, anchor='ma')


def discontinua(d, caja, color, ancho, trazo=24):
    x0, y0, x1, y1 = caja
    for x in range(int(x0), int(x1), trazo * 2):
        d.line((x, y0, min(x + trazo, x1), y0), fill=color, width=ancho)
        d.line((x, y1, min(x + trazo, x1), y1), fill=color, width=ancho)
    for y in range(int(y0), int(y1), trazo * 2):
        d.line((x0, y, x0, min(y + trazo, y1)), fill=color, width=ancho)
        d.line((x1, y, x1, min(y + trazo, y1)), fill=color, width=ancho)


def pieza_post(foto, logo):
    im = recorte(foto, 1080, 1350, 0.5, 0.6)
    d = ImageDraw.Draw(im)
    im.paste(logo.resize((260, 260), Image.LANCZOS), (410, 70), logo.resize((260, 260), Image.LANCZOS))
    texto_centrado(d, 540, 1020, 'CEREZO ROCK', 96)
    texto_centrado(d, 540, 1140, 'Sábado 17 de abril', 52, negrita=False)
    return im, (0, 0, 1080, 1350)


def pieza_historia(foto, logo):
    im = recorte(foto, 1080, 1920, 0.35, 0.5)
    d = ImageDraw.Draw(im)
    im.paste(logo.resize((300, 300), Image.LANCZOS), (390, 330), logo.resize((300, 300), Image.LANCZOS))
    texto_centrado(d, 540, 700, 'CEREZO ROCK', 100)
    texto_centrado(d, 540, 1450, 'Entrada libre', 64, negrita=False)
    return im, (0, 250, 1080, 1670)


def pieza_banner(foto, logo):
    im = recorte(foto, 2560, 1440, 0.5, 0.5)
    d = ImageDraw.Draw(im)
    lg = logo.resize((300, 300), Image.LANCZOS)
    im.paste(lg, (530, 570), lg)
    d2 = ImageDraw.Draw(im)
    f = ImageFont.truetype(NEGRITA, 120)
    d2.text((864, 610), 'CEREZO ROCK', font=f, fill=(0, 0, 0)); d2.text((858, 604), 'CEREZO ROCK', font=f, fill=(255, 255, 255))
    f2 = ImageFont.truetype(NORMAL, 56)
    d2.text((864, 760), 'Festival del valle · 2027', font=f2, fill=(255, 255, 255))
    return im, ((2560 - 1546) // 2, (1440 - 423) // 2, (2560 + 1546) // 2, (1440 + 423) // 2)


def flyer_a5(foto, logo, guias=True):
    """Flyer A5 con 3 mm de sangrado a 300 ppp: 1819 × 2551 px."""
    W, H, S, Z = 1819, 2551, 35, 94   # sangrado 3 mm = 35 px; zona segura 8 mm del borde = 94 px
    im = Image.new('RGB', (W, H), (30, 26, 36))
    arriba = recorte(foto, W, 1500, 0.5, 0.55)
    degr = Image.linear_gradient('L').resize((W, 1500))   # negro arriba, blanco abajo
    im.paste(arriba, (0, 0), Image.eval(degr, lambda v: 255 - max(0, v - 120) * 255 // 135))
    d = ImageDraw.Draw(im)
    lg = logo.resize((420, 420), Image.LANCZOS)
    im.paste(lg, ((W - 420) // 2, 1120), lg)
    texto_centrado(d, W // 2, 1580, 'CEREZO ROCK', 190, sombra=False, color=(246, 239, 230))
    texto_centrado(d, W // 2, 1800, 'FESTIVAL DEL VALLE · 2027', 70, negrita=False, sombra=False, color=(242, 140, 158))
    for i, g in enumerate(['Los Picotas Eléctricas', 'Garganta Profunda', 'Niebla en Tornavacas']):
        texto_centrado(d, W // 2, 1930 + i * 95, g, 66, negrita=False, sombra=False, color=(246, 239, 230))
    texto_centrado(d, W // 2, H - Z - 70, 'Sábado 17 de abril · Cabezuela del Valle · Entrada libre', 46, negrita=False, sombra=False, color=(205, 198, 214))
    if guias:
        d.rectangle((S, S, W - S - 1, H - S - 1), outline=(229, 57, 53), width=6)
        discontinua(d, (Z, Z, W - Z, H - Z), (255, 212, 0), 6)
    return im


def captura_plantilla(foto, logo, destino):
    """Rellena la plantilla web con el material del 3.5 y la fotografía en 1280 y 390 px."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print('  (sin Playwright: no se genera p36-web.jpg)')
        return
    import tempfile, zipfile
    zipf = RAIZ / 'web' / 'descargas' / 'plantilla-web-proyecto.zip'
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        zipfile.ZipFile(zipf).extractall(tmp)
        base = tmp / 'plantilla-web-proyecto'
        logo.resize((240, 240), Image.LANCZOS).save(base / 'img' / 'cerezo_logo.png')
        portada = recorte(foto, 1200, 1200)
        dp = ImageDraw.Draw(portada)
        lg = logo.resize((360, 360), Image.LANCZOS); portada.paste(lg, (420, 330), lg)
        texto_centrado(dp, 600, 760, 'CEREZO ROCK', 110)
        portada.save(base / 'img' / 'cerezo_portada_1200x1200.webp', quality=80)
        recorte(foto, 1200, 800, 0.2, 0.5).save(base / 'img' / 'cerezo_foto1_1200x800.webp', quality=80)
        recorte(foto, 1200, 800, 0.9, 0.7).save(base / 'img' / 'cerezo_foto2_1200x800.webp', quality=80)
        mini = recorte(foto, 1280, 720); texto_centrado(ImageDraw.Draw(mini), 640, 280, 'CEREZO ROCK', 130)
        mini.save(base / 'img' / 'cerezo_miniatura_1280x720.jpg', quality=80)
        html = (base / 'index.html').read_text(encoding='utf-8')
        for a, b in (('img/logo.svg', 'img/cerezo_logo.png'), ('img/portada.svg', 'img/cerezo_portada_1200x1200.webp'),
                     ('img/foto-1.svg', 'img/cerezo_foto1_1200x800.webp'), ('img/foto-2.svg', 'img/cerezo_foto2_1200x800.webp'),
                     ('img/miniatura.svg', 'img/cerezo_miniatura_1280x720.jpg'),
                     ('NOMBRE DEL PROYECTO', 'Cerezo Rock'), ('Una frase que diga qué sois: un grupo de música, un estudio de videojuegos…', 'Festival de rock del valle del Jerte'),
                     ('TU NOMBRE', 'Ana Pérez')):
            html = html.replace(a, b)
        (base / 'index.html').write_text(html, encoding='utf-8')
        tomas = []
        with sync_playwright() as pw:
            nav = pw.chromium.launch()
            for ancho, alto in ((1280, 800), (390, 800)):
                pg = nav.new_page(viewport={'width': ancho, 'height': alto})
                pg.goto((base / 'index.html').as_uri()); pg.wait_for_timeout(300)
                ruta = tmp / f'toma{ancho}.png'; pg.screenshot(path=str(ruta)); tomas.append(Image.open(ruta).convert('RGB'))
            nav.close()
    alto = 520
    a = tomas[0].resize((round(1280 * alto / 800), alto), Image.LANCZOS)
    b = tomas[1].resize((round(390 * alto / 800), alto), Image.LANCZOS)
    lienzo = Image.new('RGB', (a.width + b.width + 16, alto + 50), (214, 222, 230))
    lienzo.paste(rotulo(a, 'Ordenador · 1280 px'), (0, 50)); lienzo.paste(rotulo(b, 'Móvil · 390 px'), (a.width + 16, 50))
    dl = ImageDraw.Draw(lienzo)
    dl.text((10, 12), 'La misma página, dos pantallas', font=ImageFont.truetype(NEGRITA, 24), fill=(20, 24, 30))
    lienzo.save(destino, quality=85)


def publicar():
    foto = Image.open(RAIZ / 'web' / 'descargas' / 'exportar-foto.jpg').convert('RGB')
    logo = exportar.logo_png(600)
    # Las tres piezas para redes, con la zona segura marcada
    piezas = [pieza_post(foto, logo), pieza_historia(foto, logo), pieza_banner(foto, logo)]
    nombres = ['Post 4:5 · 1080 × 1350', 'Historia · 1080 × 1920', 'Banner YouTube · 2560 × 1440']
    alto = 520
    vistas = []
    for (im, zona), nombre in zip(piezas, nombres):
        d = ImageDraw.Draw(im)
        if zona != (0, 0, im.width, im.height):
            discontinua(d, zona, (255, 212, 0), max(6, im.width // 300), trazo=max(24, im.width // 60))
        v = im.resize((round(im.width * alto / im.height), alto), Image.LANCZOS)
        vistas.append((v, nombre))
    ancho = sum(v.width for v, _ in vistas) + 16 * (len(vistas) - 1)
    lienzo = Image.new('RGB', (ancho, alto + 44), (214, 222, 230))
    x = 0
    f = ImageFont.truetype(NEGRITA, 20)
    dl = ImageDraw.Draw(lienzo)
    for v, nombre in vistas:
        dl.text((x + 4, 10), nombre, font=f, fill=(20, 24, 30))
        lienzo.paste(v, (x, 44)); x += v.width + 16
    lienzo.save(SALIDA / 'p36-redes.jpg', quality=85)
    # El flyer A5 con sangrado (con las guías dibujadas) y cómo queda cortado
    con = flyer_a5(foto, logo).resize((455, 638), Image.LANCZOS)
    cortado = flyer_a5(foto, logo, guias=False).crop((35, 35, 1819 - 35, 2551 - 35)).resize((437, 620), Image.LANCZOS)
    t = Image.new('RGB', (455 + 437 + 40, 638 + 50), (214, 222, 230))
    dt = ImageDraw.Draw(t)
    dt.text((4, 12), 'Archivo: 154 × 216 mm', font=f, fill=(20, 24, 30))
    dt.text((455 + 40, 12), 'Impreso y cortado: A5', font=f, fill=(20, 24, 30))
    t.paste(con, (0, 50)); t.paste(cortado, (455 + 40, 59))
    t.save(SALIDA / 'p36-cartel.jpg', quality=85)
    captura_plantilla(foto, logo, SALIDA / 'p36-web.jpg')


if __name__ == '__main__':
    main()
