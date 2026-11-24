"""Imágenes de «cómo debe quedar» de la práctica guiada de GIMP (p37) y del punto
de control del Tema 3 (p38).

Imitan lo que el alumno hace en GIMP partiendo del mismo material inventado
(scripts/generar_material_gimp.py): cada paso de la guiada parte del anterior.

Salida en web/assets/img/entregas/:
  p37-01-material.jpg ... p37-14-redes.jpg   un paso de la guiada por imagen
  p38-ejemplo-*.jpg y p38-bien-mal-*.jpg     ejemplos del punto de control

Uso: python scripts/generar_resultados_gimp.py  (también lo llama
generar_resultados_esperados.py)
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / 'web' / 'assets' / 'img' / 'entregas'
sys.path.insert(0, str(RAIZ / 'scripts'))
import generar_material_capas as capas   # noqa: E402
import generar_material_gimp as mat      # noqa: E402

NEGRITA = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
NORMAL = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONDO_LIENZO = (30, 26, 36)
CREMA, ROSA = (246, 239, 230), (242, 140, 158)
GUIA = (40, 120, 255)          # GIMP dibuja las guías azules y discontinuas
GRIS_PANEL = (214, 222, 230)

# A5 con sangrado a 300 ppp
A5 = (1819, 2551)
A5_CORTE, A5_SEGURA = 35, 94
# A4 con sangrado a 300 ppp
A4 = (2551, 3579)


def f(tam, negrita=True):
    return ImageFont.truetype(NEGRITA if negrita else NORMAL, tam)


def guardar(im, nombre, ancho=None, calidad=84):
    if ancho and im.width > ancho:
        im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
    im.convert('RGB').save(SALIDA / nombre, quality=calidad, optimize=True)
    return im.size


def ajedrez(w, h, lado=24):
    yy, xx = np.mgrid[0:h, 0:w]
    a = np.where(((xx // lado) + (yy // lado)) % 2 == 0, 204, 153).astype(np.uint8)
    return Image.fromarray(a).convert('RGB')


def discontinua(d, p0, p1, color, ancho=4, trazo=22):
    (x0, y0), (x1, y1) = p0, p1
    largo = max(abs(x1 - x0), abs(y1 - y0))
    for t in range(0, int(largo), trazo * 2):
        a, b = t / largo, min(t + trazo, largo) / largo
        d.line((x0 + (x1 - x0) * a, y0 + (y1 - y0) * a, x0 + (x1 - x0) * b, y0 + (y1 - y0) * b), fill=color, width=ancho)


def guias(im, lineas_v, lineas_h, color=GUIA, ancho=5):
    d = ImageDraw.Draw(im)
    for x in lineas_v:
        discontinua(d, (x, 0), (x, im.height), color, ancho)
    for y in lineas_h:
        discontinua(d, (0, y), (im.width, y), color, ancho)
    return im


def panel(vistas, alto=460, sep=18, titulo_alto=40):
    """Junta varias imágenes (im, rótulo) en fila, a la misma altura."""
    escaladas = [(im.convert('RGB').resize((round(im.width * alto / im.height), alto), Image.LANCZOS), r) for im, r in vistas]
    ancho = sum(v.width for v, _ in escaladas) + sep * (len(escaladas) - 1)
    lienzo = Image.new('RGB', (ancho, alto + titulo_alto), GRIS_PANEL)
    d = ImageDraw.Draw(lienzo)
    x = 0
    for v, r in escaladas:
        tam = 21
        while tam > 13 and d.textlength(r, font=f(tam)) > v.width - 8:
            tam -= 1
        d.text((x + 4, 9 + (21 - tam) // 2), r, font=f(tam), fill=(20, 24, 30))
        lienzo.paste(v, (x, titulo_alto))
        x += v.width + sep
    return lienzo


def histograma(a, ancho=512, alto=150, canal=None):
    """Histograma como lo dibuja GIMP (Valor = máximo de R, G, B)."""
    v = a.max(axis=2) if canal is None else a[..., canal]
    h, _ = np.histogram((np.clip(v, 0, 1) * 255).astype(int), bins=256, range=(0, 256))
    h = h / h[1:255].max()
    im = Image.new('RGB', (ancho, alto), (250, 250, 250))
    d = ImageDraw.Draw(im)
    for i, val in enumerate(h):
        x = i * ancho / 256
        d.rectangle((x, alto - min(1, val) * (alto - 6), x + ancho / 256, alto), fill=(60, 60, 60))
    d.rectangle((0, 0, ancho - 1, alto - 1), outline=(150, 150, 150))
    return im


def con_histograma(im_arr, rotulo):
    im = mat.a_img(im_arr)
    im = im.resize((900, round(900 * im.height / im.width)), Image.LANCZOS)
    hi = histograma(im_arr, 900, 170)
    t = Image.new('RGB', (900, im.height + 190), GRIS_PANEL)
    t.paste(im, (0, 0)); t.paste(hi, (0, im.height + 20))
    return t, rotulo


def niveles(a, negro, gamma, blanco):
    """Colores > Niveles de GIMP (valores de entrada en 0-255)."""
    return np.clip((a - negro / 255) / ((blanco - negro) / 255), 0, 1) ** (1 / gamma)


def recorte_central(a, ancho, alto):
    h, w = a.shape[:2]
    x, y = (w - ancho) // 2, (h - alto) // 2
    return a[y:y + alto, x:x + ancho]


def texto(d, xy, txt, tam, color, negrita=True, anchor='ma', sombra=False):
    fu = f(tam, negrita)
    if sombra:
        d.text((xy[0] + tam // 14, xy[1] + tam // 14), txt, font=fu, fill=(0, 0, 0), anchor=anchor)
    d.text(xy, txt, font=fu, fill=color, anchor=anchor)


def sombra_arrojada(base, capa, pos, desp=(14, 18), radio=16, opacidad=150):
    m = Image.new('L', base.size, 0)
    m.paste(capa.getchannel('A').point(lambda v: opacidad if v > 0 else 0), (pos[0] + desp[0], pos[1] + desp[1]))
    m = m.filter(ImageFilter.GaussianBlur(radio))
    return Image.composite(Image.new('RGB', base.size, (0, 0, 0)), base, m)


def multiplicar(base, textura, opacidad):
    b = np.asarray(base, np.float32) / 255
    t = np.asarray(textura.convert('RGB'), np.float32) / 255
    return mat.a_img(b * (1 - opacidad) + b * t * opacidad)


def pantalla(base, luces, opacidad=1.0):
    b = np.asarray(base, np.float32) / 255
    l = np.asarray(luces.convert('RGB'), np.float32) / 255
    return mat.a_img(b * (1 - opacidad) + (1 - (1 - b) * (1 - l)) * opacidad)


def cubrir(im, w, h):
    """Escala una capa para que cubra w × h (cadena cerrada) y la centra."""
    esc = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * esc), round(im.height * esc)), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


# ==================================================================== guiada
def guiada():
    limpio_letrero = mat.escenario_limpio(con_letrero=True)
    limpio = mat.escenario_limpio()
    defecto = mat.oscurecer(limpio_letrero) * mat.GUIADA_DOMINANTE
    con_motas = mat.motas(defecto, 31, mat.GUIADA_MOTAS, 10)
    material = mat.escenario_estropeado()
    CW, CH = 2200, 1467                          # recorte 3:2 tras enderezar

    # 1 · el material
    guardar(panel([(mat.a_img(material), 'guiada-escenario.jpg · 2400 × 1600')], 520), 'p37-01-material.jpg')

    # 2 · enderezar con Medir
    torcida = mat.a_img(material)
    d = ImageDraw.Draw(torcida)
    # el canto del escenario en la foto torcida: y = 1180 girado 3° (aprox., sobre la foto ya girada)
    ang = np.radians(mat.GUIADA_ANGULO)
    cx, cy = 1200, 800
    def rot(x, y):
        x, y = (x - cx) * 1.0, (y - cy)
        xr = cx + (x * np.cos(ang) + y * np.sin(ang)) * 1.075
        yr = cy + (-x * np.sin(ang) + y * np.cos(ang)) * 1.11
        return xr, yr
    p0, p1 = rot(250, 1181), rot(2150, 1181)
    d.line((p0, p1), fill=(255, 230, 0), width=7)
    for p in (p0, p1):
        d.ellipse((p[0] - 16, p[1] - 16, p[0] + 16, p[1] + 16), outline=(255, 230, 0), width=6)
    d.rectangle((60, 1450, 760, 1560), fill=(20, 20, 20))
    d.text((80, 1468), 'Ángulo: 3,00°', font=f(56), fill=(255, 230, 0))
    derecha = Image.new('RGBA', (W := 2400, Hh := 1600))
    girada = mat.a_img(material).convert('RGBA').rotate(-mat.GUIADA_ANGULO, Image.BICUBIC)
    fondo = ajedrez(W, Hh, 40).convert('RGBA')
    fondo.alpha_composite(girada)
    guardar(panel([(torcida, 'Medir: del canto izquierdo al derecho'), (fondo, 'Enderezar: esquinas vacías (transparentes)')], 380), 'p37-02-enderezar.jpg')

    # 3 · recortar 3:2 con regla de los tercios
    rec = fondo.convert('RGB')
    d = ImageDraw.Draw(rec)
    x0, y0 = (2400 - CW) // 2, (1600 - CH) // 2
    sombra = Image.new('L', rec.size, 120)
    ImageDraw.Draw(sombra).rectangle((x0, y0, x0 + CW, y0 + CH), fill=0)
    rec = Image.composite(Image.new('RGB', rec.size, (0, 0, 0)), rec, sombra)
    d = ImageDraw.Draw(rec)
    d.rectangle((x0, y0, x0 + CW, y0 + CH), outline=(255, 255, 255), width=5)
    for k in (1, 2):
        d.line((x0 + CW * k / 3, y0, x0 + CW * k / 3, y0 + CH), fill=(255, 255, 255), width=2)
        d.line((x0, y0 + CH * k / 3, x0 + CW, y0 + CH * k / 3), fill=(255, 255, 255), width=2)
    paso3 = recorte_central(con_motas, CW, CH)
    guardar(panel([(rec, 'Recortar · Relación de aspecto 3:2'), (mat.a_img(paso3), 'Resultado: 2200 × 1467 px')], 380), 'p37-03-recortar.jpg')

    # 4 · niveles (canal Valor): 5 · 1,50 · 145
    paso4 = niveles(paso3, 5, 1.5, 145)
    guardar(panel([con_histograma(paso3, 'Antes: todo a la izquierda'), con_histograma(paso4, 'Niveles 5 · 1,50 · 145')], 520), 'p37-04-niveles.jpg')

    # 5 · color: cuentagotas gris en la rejilla del amplificador
    paso5 = recorte_central(mat.motas(limpio_letrero, 31, mat.GUIADA_MOTAS, 10), CW, CH)
    marca = mat.a_img(paso4)
    d = ImageDraw.Draw(marca)
    ax, ay = 480 + 130 - x0, 1040 - y0
    d.ellipse((ax - 34, ay - 34, ax + 34, ay + 34), outline=(0, 255, 255), width=8)
    d.line((ax + 26, ay - 26, ax + 120, ay - 120), fill=(0, 255, 255), width=8)
    guardar(panel([(marca, 'Cuentagotas gris en la rejilla'), (mat.a_img(paso5), 'Sin dominante: la rejilla es gris')], 380), 'p37-05-color.jpg')

    # 6 · limpiar: letrero con Clonar, motas con Saneado (detalle al 100 %)
    paso6 = recorte_central(limpio, CW, CH)
    zona = (0, 60, 1300, 760)
    antes = mat.a_img(paso5).crop(zona)
    despues = mat.a_img(paso6).crop(zona)
    guardar(panel([(antes, 'Antes (al 100 %)'), (despues, 'Clonar el letrero · Saneado en las motas')], 380), 'p37-06-limpiar.jpg')

    # 7 · la foto terminada
    foto = mat.a_img(paso6)
    guardar(panel([(mat.a_img(material), 'Material'), (foto, 'guiada-foto.jpg · 2200 × 1467')], 380), 'p37-07-foto.jpg')

    # ------------------------------------------------- parte B: el cartel A5
    W5, H5 = A5
    lienzo = Image.new('RGB', A5, FONDO_LIENZO)
    v = [A5_CORTE, A5_SEGURA, W5 - A5_SEGURA, W5 - A5_CORTE]
    h = [A5_CORTE, A5_SEGURA, H5 - A5_SEGURA, H5 - A5_CORTE]
    con_guias = guias(lienzo.copy(), v, h)
    d = ImageDraw.Draw(con_guias)
    d.text((W5 // 2, H5 // 2 - 120), '1819 × 2551 px', font=f(110), fill=CREMA, anchor='mm')
    d.text((W5 // 2, H5 // 2 + 40), '300 ppp · relleno #1e1a24', font=f(64, False), fill=(200, 195, 210), anchor='mm')
    d.text((W5 // 2, H5 // 2 + 160), 'guías en 35 y 94 px de cada borde', font=f(56, False), fill=(200, 195, 210), anchor='mm')
    guardar(panel([(con_guias, 'Imagen nueva A5 con sangrado y ocho guías')], 640), 'p37-08-lienzo.jpg')

    # 9 · la foto como capa, con máscara en degradado
    fw, fh = W5, round(CH * W5 / CW)            # 1819 × 1213
    foto_c = foto.resize((fw, fh), Image.LANCZOS)
    mascara = Image.new('L', (fw, fh), 255)
    md = ImageDraw.Draw(mascara)
    for y in range(750, fh):
        md.line((0, y, fw, y), fill=round(255 * (1 - (y - 750) / (fh - 750))))
    paso9 = lienzo.copy()
    paso9.paste(foto_c, (0, 0), mascara)
    mini = Image.new('RGB', (fw, fh + 0), (0, 0, 0)); mini.paste(mascara.convert('RGB'))
    guardar(panel([(paso9, 'La foto se funde con el fondo'), (mini, 'Su máscara: blanco arriba, degradado a negro')], 520), 'p37-09-foto-mascara.jpg')

    # 10 · la guitarra recortada
    gcapa = capas.capa_guitarra()
    gcapa = gcapa.crop(gcapa.getchannel('A').getbbox())          # lo que se pega: 687 × 1177
    gesc = gcapa.resize((round(gcapa.width * 1000 / gcapa.height), 1000), Image.LANCZOS)   # altura 1000
    gpos = (1040, 900)
    paso10 = sombra_arrojada(paso9, gesc, gpos)
    paso10.paste(gesc, gpos, gesc)
    suelta = ajedrez(gcapa.width, gcapa.height, 30).convert('RGBA'); suelta.alpha_composite(gcapa)
    guardar(panel([(suelta, 'Pegada como capa nueva'), (paso10, 'Altura 1000 px y sombra')], 520), 'p37-10-guitarra.jpg')

    # 11 · textura en Multiplicar al 60 %
    tex = cubrir(capas.textura(), W5, H5)
    paso11 = multiplicar(paso10, tex, 0.6)
    guardar(panel([(paso10, 'Sin textura'), (paso11, 'Textura en Multiplicar, opacidad 60 %')], 520), 'p37-11-textura.jpg')

    # 12 · textos, franja y logotipo
    paso12 = paso11.copy()
    franja = Image.new('L', A5, 0)
    ImageDraw.Draw(franja).rectangle((0, 2110, W5, 2330), fill=128)
    paso12 = Image.composite(Image.new('RGB', A5, (0, 0, 0)), paso12, franja)
    d = ImageDraw.Draw(paso12)
    texto(d, (W5 // 2, 1290), 'LOS PICOTAS', 170, CREMA, sombra=True)
    texto(d, (W5 // 2, 1470), 'ELÉCTRICAS', 170, CREMA, sombra=True)
    texto(d, (W5 // 2, 1700), 'Concierto acústico', 84, ROSA, negrita=False, sombra=True)
    texto(d, (W5 // 2, 2150), 'Sábado 12 de diciembre · 21:00', 54, CREMA)
    texto(d, (W5 // 2, 2235), 'Plaza Mayor de Cabezuela del Valle · Entrada libre', 44, CREMA, negrita=False)
    logo = mat.logo_claro(280)
    paso12.paste(logo, (W5 - A5_SEGURA - 40 - 280, 230), logo)
    guardar(panel([(paso12, 'Textos, franja al 50 % y logotipo')], 640), 'p37-12-textos.jpg')

    # 13 · terminado: con guías y cortado
    con = guias(paso12.copy(), v, h)
    cortado = paso12.crop((A5_CORTE, A5_CORTE, W5 - A5_CORTE, H5 - A5_CORTE))
    guardar(panel([(con, 'El archivo, con las guías'), (cortado, 'Impreso y cortado: A5')], 560), 'p37-13-cartel.jpg')

    # 14 · versión para redes 1080 × 1350
    rx, ry, rw, rh = 35, 182, 1749, 2186
    marco = paso12.copy()
    sombra = Image.new('L', A5, 140)
    ImageDraw.Draw(sombra).rectangle((rx, ry, rx + rw, ry + rh), fill=0)
    marco = Image.composite(Image.new('RGB', A5, (0, 0, 0)), marco, sombra)
    ImageDraw.Draw(marco).rectangle((rx, ry, rx + rw, ry + rh), outline=(255, 255, 255), width=8)
    redes = paso12.crop((rx, ry, rx + rw, ry + rh)).resize((1080, 1350), Image.LANCZOS)
    guardar(panel([(marco, 'Recortar 4:5 · 35, 182 · 1749 × 2186'), (redes, 'guiada-redes.jpg · 1080 × 1350')], 560), 'p37-14-redes.jpg')
    return paso12


# ==================================================================== punto de control
def control():
    limpia = mat.sala_limpia()
    material = mat.sala_estropeada()
    # Foto retocada a 16:9 y 1920 × 1080
    foto = mat.a_img(recorte_central(limpia, 2208, 1242)).resize((1920, 1080), Image.LANCZOS)
    guardar(panel([(mat.a_img(material), 'pc-sala.jpg: torcida, lavada, azulada, con motas y una lata'),
                   (foto, 'Retocada: 1920 × 1080')], 360), 'p38-ejemplo-foto.jpg')

    # Auriculares recortados
    aur = mat.auriculares_capa()
    aur = aur.crop(aur.getchannel('A').getbbox())

    # Cartel A4 de ejemplo
    W4, H4 = A4
    cartel = Image.new('RGB', A4, (14, 16, 24))
    fw, fh = W4, round(1080 * W4 / 1920)
    fc = foto.resize((fw, fh), Image.LANCZOS)
    m = Image.new('L', (fw, fh), 255)
    md = ImageDraw.Draw(m)
    for y in range(fh // 2, fh):
        md.line((0, y, fw, y), fill=round(255 * (1 - (y - fh // 2) / (fh - fh // 2))))
    cartel.paste(fc, (0, 0), m)
    cartel = pantalla(cartel, cubrir(mat.luces(), W4, H4), 0.8)
    ae = aur.resize((1500, round(aur.height * 1500 / aur.width)), Image.LANCZOS)
    apos = ((W4 - 1500) // 2, 1150)
    cartel = sombra_arrojada(cartel, ae, apos, (20, 30), 24, 170)
    cartel.paste(ae, apos, ae)
    d = ImageDraw.Draw(cartel)
    texto(d, (W4 // 2, 2480), 'JERTE GAMING CUP', 190, (255, 255, 255), sombra=True)
    texto(d, (W4 // 2, 2760), 'Torneo de videojuegos del IES Valle del Jerte', 78, (0, 220, 255), negrita=False, sombra=True)
    texto(d, (W4 // 2, 3050), 'Viernes 19 de febrero · 16:30 · Salón de actos', 74, (255, 255, 255))
    texto(d, (W4 // 2, 3170), 'Inscripciones en la biblioteca hasta el 12 de febrero', 62, (210, 210, 220), negrita=False)
    logo = mat.logo_pc_png(600)
    cartel.paste(logo, ((W4 - 600) // 2, 280), logo)
    vg = [35, 94, W4 - 94, W4 - 35]
    hg = [35, 94, H4 - 94, H4 - 35]
    guardar(panel([(guias(cartel.copy(), vg, hg), 'Cartel A4: 2551 × 3579 px con las guías'),
                   (cartel.crop((35, 35, W4 - 35, H4 - 35)), 'Impreso y cortado')], 600), 'p38-ejemplo-cartel.jpg')

    # Miniatura 1280 × 720
    mini = foto.resize((1280, 720), Image.LANCZOS)
    mini = pantalla(mini, cubrir(mat.luces(), 1280, 720), 0.6)
    am = aur.resize((520, round(aur.height * 520 / aur.width)), Image.LANCZOS)
    mini = sombra_arrojada(mini, am, (700, 120), (10, 14), 12, 170)
    mini.paste(am, (700, 120), am)
    d = ImageDraw.Draw(mini)
    texto(d, (70, 140), 'LA', 120, (255, 255, 255), anchor='la', sombra=True)
    texto(d, (70, 270), 'FINAL', 170, (255, 40, 200), anchor='la', sombra=True)
    lm = mat.logo_pc_png(170)
    mini.paste(lm, (70, 480), lm)
    zona = mini.copy()
    dz = ImageDraw.Draw(zona)
    dz.rounded_rectangle((1150, 660, 1262, 702), radius=6, fill=(0, 0, 0))
    dz.text((1206, 681), '12:45', font=f(26), fill=(255, 255, 255), anchor='mm')
    guardar(panel([(mini, 'Miniatura: 1280 × 720'), (zona, 'Así se ve en YouTube: la esquina la tapa la duración')], 330), 'p38-ejemplo-miniatura.jpg')

    # Bien y mal
    # Recorte con halo frente a limpio
    fondo_auri = mat.auriculares()
    fondo_oscuro = Image.new('RGB', (700, 520), (92, 60, 150))
    caja = (120, 600, 820, 1120)                     # el casco izquierdo
    rec = fondo_auri.crop(caja)
    alfa = mat.auriculares_capa().getchannel('A').crop(caja)
    halo = alfa.filter(ImageFilter.MaxFilter(13))
    mal = fondo_oscuro.copy(); mal.paste(rec, (0, 0), halo)
    bien = fondo_oscuro.copy(); bien.paste(rec, (0, 0), alfa.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2)))
    guardar(panel([(mal, 'Mal: queda un borde del fondo'), (bien, 'Bien: Encoger 1 px y Difuminar 2 px')], 330), 'p38-bien-mal-recorte.jpg')
    # SVG importado a su tamaño frente a PNG pequeño ampliado
    nitido = mat.logo_pc_png(600).crop((100, 340, 500, 500))
    borroso = mat.logo_pc_png(100).resize((600, 600), Image.NEAREST).crop((100, 340, 500, 500))
    def sobre_negro(im):
        b = Image.new('RGB', im.size, (14, 16, 24)); b.paste(im, (0, 0), im); return b
    guardar(panel([(sobre_negro(borroso), 'Mal: abierto pequeño y ampliado'), (sobre_negro(nitido), 'Bien: SVG importado a 600 × 600')], 260), 'p38-bien-mal-logo.jpg')
    # Texto fuera de la zona segura
    malc = cartel.copy()
    d = ImageDraw.Draw(malc)
    d.rectangle((0, 3270, W4, H4), fill=(14, 16, 24))
    texto(d, (W4 // 2, 3470), 'Viernes 19 de febrero · 16:30', 90, (255, 255, 255))
    guias(malc, vg, hg)
    zona_mal = malc.crop((0, 2900, W4, H4))
    zona_bien = guias(cartel.copy(), vg, hg).crop((0, 2900, W4, H4))
    guardar(panel([(zona_mal, 'Mal: el texto pisa el corte'), (zona_bien, 'Bien: dentro de la zona segura')], 240), 'p38-bien-mal-zona.jpg')


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    guiada()
    control()
    for p in sorted(SALIDA.glob('p3[78]-*.jpg')):
        print(f'{p.name:32s} {p.stat().st_size / 1024:6.0f} KB  {Image.open(p).size}')


if __name__ == '__main__':
    main()
