"""Genera la plantilla de página web del Tema 3.6 (publicar imágenes en la web).

  web/descargas/plantilla-web-proyecto.zip
      plantilla-web-proyecto/
          index.html        la página: cabecera con logo, imagen principal, galería y créditos
          estilo.css        estilos (no hace falta tocarlos)
          favicon.ico       icono provisional (se sustituye por el del alumno)
          img/              imágenes provisionales en SVG con el tamaño de cada hueco
          LEEME.txt         qué archivo va en cada sitio

Los huecos dicen qué imagen va en cada uno y de qué tamaño. El alumno cambia el
atributo src (y alt, width y height) por los de sus archivos exportados en el 3.5.

Uso: python scripts/generar_plantilla_web.py
"""
import io
import zipfile
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / 'web' / 'descargas' / 'plantilla-web-proyecto.zip'
CARPETA = 'plantilla-web-proyecto/'

INDEX = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>NOMBRE DEL PROYECTO · Kit de prensa</title>
  <!-- 1. El icono de la pestaña: cambia favicon.ico por el tuyo (mismo nombre) -->
  <link rel="icon" href="favicon.ico">
  <link rel="stylesheet" href="estilo.css">
</head>
<body>

  <header class="cabecera">
    <!-- 2. Tu logotipo en PNG con transparencia.
         src: la ruta del archivo · alt: qué es · width y height: sus píxeles -->
    <img class="logo" src="img/logo.svg" alt="Logotipo de NOMBRE DEL PROYECTO" width="120" height="120">
    <div>
      <h1>NOMBRE DEL PROYECTO</h1>
      <p>Una frase que diga qué sois: un grupo de música, un estudio de videojuegos…</p>
    </div>
  </header>

  <main>
    <!-- 3. La imagen principal: tu portada en WebP de 1200 × 1200 -->
    <img class="principal" src="img/portada.svg" alt="Describe la portada en una frase" width="1200" height="1200">

    <h2>Galería</h2>
    <div class="galeria">
      <!-- 4. Tres fotos o piezas tuyas, en WebP o JPG, de 1200 px de ancho como mucho.
           loading="lazy": el navegador no las descarga hasta que te acercas a ellas -->
      <img src="img/foto-1.svg" alt="Describe la foto 1" width="1200" height="800" loading="lazy">
      <img src="img/foto-2.svg" alt="Describe la foto 2" width="1200" height="800" loading="lazy">
      <img src="img/miniatura.svg" alt="Describe la miniatura" width="1280" height="720" loading="lazy">
    </div>
  </main>

  <footer class="creditos">
    <!-- 5. Quién ha hecho cada imagen y con qué licencia -->
    <p>Imágenes: TU NOMBRE, 2026. Licencia <a href="https://creativecommons.org/licenses/by/4.0/deed.es">CC BY 4.0</a>.</p>
  </footer>

</body>
</html>
'''

ESTILO = '''* { box-sizing: border-box; }
body { margin: 0; font-family: Arial, Helvetica, sans-serif; background: #1e1a24; color: #f6efe6; line-height: 1.5; }
.cabecera { display: flex; gap: 1rem; align-items: center; padding: 1rem 1.5rem; background: #2b2533; }
.cabecera h1 { margin: 0; font-size: 1.8rem; }
.cabecera p { margin: 0.2rem 0 0; opacity: 0.85; }
.logo { width: 96px; height: auto; }
main { max-width: 960px; margin: 0 auto; padding: 1.5rem; }
img { max-width: 100%; height: auto; display: block; }
.principal { width: 100%; max-width: 640px; margin: 0 auto; border-radius: 6px; }
.galeria { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; }
.galeria img { width: 100%; border-radius: 6px; }
.creditos { text-align: center; padding: 1.5rem; font-size: 0.9rem; opacity: 0.8; }
.creditos a { color: #f28c9e; }
'''

LEEME = '''Plantilla de página web · Tema 3.6 · 0223 Aplicaciones ofimáticas
===================================================================

1. Copia en la carpeta img/ tus imágenes exportadas en el bloque 3.5.
2. Abre index.html con el Bloc de notas (clic derecho > Abrir con).
3. En cada <img> cambia:
     src     el nombre de tu archivo, por ejemplo img/picotas_portada_1200x1200.webp
     alt     una frase que describa la imagen (la leen los lectores de pantalla
             y aparece si la imagen no carga)
     width   y height: los píxeles de tu imagen
4. Cambia NOMBRE DEL PROYECTO, la frase de la cabecera y los créditos.
5. Sustituye favicon.ico por el tuyo (con el mismo nombre).
6. Guarda y abre index.html con doble clic: se ve en el navegador.
7. Pulsa F12 > Red y recarga (F5) para ver cuánto pesa cada imagen.

Las imágenes provisionales (.svg) dicen qué va en cada hueco: cuando pongas
las tuyas, puedes borrarlas.
'''


def svg(ancho, alto, texto, sub):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}">
  <rect width="{ancho}" height="{alto}" fill="#3a3344"/>
  <rect x="8" y="8" width="{ancho - 16}" height="{alto - 16}" fill="none" stroke="#f28c9e" stroke-width="6" stroke-dasharray="24 16"/>
  <text x="50%" y="46%" text-anchor="middle" font-family="Arial, sans-serif" font-size="{max(14, ancho // 14)}" font-weight="700" fill="#f6efe6">{texto}</text>
  <text x="50%" y="60%" text-anchor="middle" font-family="Arial, sans-serif" font-size="{max(10, ancho // 24)}" fill="#cfc6d6">{sub}</text>
</svg>
'''


def favicon():
    im = Image.new('RGBA', (48, 48), (0, 0, 0, 0))
    from PIL import ImageDraw
    d = ImageDraw.Draw(im)
    d.ellipse((6, 18, 26, 38), fill='#b3123a')
    d.ellipse((22, 16, 44, 38), fill='#b3123a')
    b = io.BytesIO()
    im.save(b, 'ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    return b.getvalue()


def main():
    huecos = {
        'img/logo.svg': svg(120, 120, 'LOGO', 'PNG'),
        'img/portada.svg': svg(1200, 1200, 'Tu portada', 'WebP · 1200 × 1200'),
        'img/foto-1.svg': svg(1200, 800, 'Foto 1', 'WebP o JPG · 1200 × 800'),
        'img/foto-2.svg': svg(1200, 800, 'Foto 2', 'WebP o JPG · 1200 × 800'),
        'img/miniatura.svg': svg(1280, 720, 'Tu miniatura', 'JPG · 1280 × 720'),
    }
    with zipfile.ZipFile(DESTINO, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr(CARPETA + 'index.html', INDEX)
        z.writestr(CARPETA + 'estilo.css', ESTILO)
        z.writestr(CARPETA + 'LEEME.txt', LEEME.replace('\n', '\r\n'))
        z.writestr(CARPETA + 'favicon.ico', favicon())
        for ruta, contenido in huecos.items():
            z.writestr(CARPETA + ruta, contenido)
    print('Plantilla generada:', DESTINO, f'({DESTINO.stat().st_size / 1024:.1f} KB)')


if __name__ == '__main__':
    main()
