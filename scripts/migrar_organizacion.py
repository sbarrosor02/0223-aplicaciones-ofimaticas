#!/usr/bin/env python3
"""Migración única del 24/11/2026 (reorganización del aula, como la de 0221 del 18/11/2026).
Ya ejecutada: se conserva como registro, no hay que volver a ejecutarla.

1. Parte ut02-ejercicios.html y ut03-ejercicios.html en una página por bloque
   (utNN-bloque-K.html) y deja utNN-ejercicios.html como índice con las normas de
   entrega y un hueco <!-- aula:indice --> que rellena actualizar_aula.py.
2. Tema 1: la teoría pasa de ut01.html a ut01-teoria.html; ut01.html queda como portada.
3. Reescribe en toda la web los enlaces a utNN-ejercicios.html#id y a ut01.html#id
   hacia la página donde ha quedado ese id.
4. Portadas de los temas 1, 2 y 3: secciones (<!-- aula:secciones -->) y un desplegable
   «Qué se evalúa y cómo se organiza el tema» con los criterios y el recorrido.
5. Crea utNN-examen.html (índice de «Preparar el examen») y escribe "secciones" en
   web/datos/temas.json.
"""
import json
import re
from pathlib import Path

WEB = Path(__file__).resolve().parents[1] / 'web'
TEMAS = WEB / 'temas'


def plain(s):
    return ' '.join(re.sub(r'<[^>]+>', ' ', s).split())


def partes(src):
    """(antes_de_main, cabecera_hasta_subnav, cuerpo, pie) de una página ya generada."""
    i = src.index('<main class="envoltura" id="contenido" tabindex="-1">')
    j = src.index('</nav>', src.index('<nav class="subnav"')) + len('</nav>')
    k = src.index('  <nav class="nav-temas">')
    return src[:i], src[i:j], src[j:k], src[k:]


mapa_ids = {}          # (tema, id) -> página donde está ahora
bloques_tema = {}

# ---------------------------------------------------------------- 1. bloques de ejercicios
DESCRIPCION = {
    '2.0': 'Escribir, moverte por el documento y guardarlo bien · repaso, va despacio',
    '2.1': 'Buscar y reemplazar, autocorrección y cinta personalizada · CE a',
    '2.2': 'El CV pasa a documento profesional con estilos, formato y página · base de b, e, f',
    '2.3': 'Tabla, foto, captura y diagrama en el CV · CE c',
    '2.4': 'El CV como plantilla y un documento largo con índice · CE b',
    '2.5': 'El CV en otros formatos y cartas combinadas a varias empresas · CE d',
    '2.6': 'Revisión con un compañero, comentarios y protección · transversal',
    '2.7': 'Una macro para la plantilla del CV y su manual · CE e, f',
    '3.1': 'Elegir el proyecto y decidir tamaño, resolución y formato de cada pieza · CE a, c',
    '3.2': 'Fotos propias, boceto escaneado y capturas, sin datos personales · CE b',
    '3.3': 'Enderezar, luz, color y limpieza del material · CE c, d',
    '3.4': 'Logotipo, portada y miniatura con capas, máscaras y texto · CE d',
    '3.5': 'Sacar de cada pieza los archivos de verdad, con su formato y peso · CE e',
    '3.6': 'La web del proyecto, el cartel A3 para imprenta, el banner y las licencias · CE f',
}

for n in (2, 3):
    origen = TEMAS / ('ut%02d-ejercicios.html' % n)
    src = origen.read_text(encoding='utf-8')
    antes, cabecera, cuerpo, pie = partes(src)
    trozos = re.split(r'(\n  <section>\n.*?\n  </section>)', cuerpo, flags=re.S)
    indice, bloques = '', []
    for t in trozos:
        h2 = re.search(r'<h2 id="([^"]+)">Bloque (\d+\.(\d+)) — (.*?)</h2>', t)
        if t.startswith('\n  <section>') and h2:
            numero, k, nombre = h2[2], h2[3], plain(h2[4])
            pagina = 'ut%02d-bloque-%s.html' % (n, k)
            for ident in re.findall(r'\bid="([^"]+)"', t):
                mapa_ids[(n, ident)] = pagina
            bloques.append((pagina, numero, nombre, t))
        else:
            indice += t
    for ident in re.findall(r'\bid="([^"]+)"', indice):
        mapa_ids.setdefault((n, ident), origen.name)
    bloques_tema[n] = bloques
    for pagina, numero, nombre, sec in bloques:
        cab = re.sub(r'<h1>.*?</h1>', '<h1>Bloque %s — %s</h1>' % (numero, nombre), cabecera, flags=re.S)
        cab = re.sub(r'(<p class="modulo">[^<]*?)(</p>)', r'\1 · Ejercicios\2', cab, count=1)
        aviso = ('\n\n  <p class="aula-mas">Antes de entregar, repasa '
                 '<a href="ut%02d-ejercicios.html#apartado-como-se-entrega-cada-bloque">cómo se entrega cada bloque</a>.</p>' % n)
        pag_antes = re.sub(r'<title>.*?</title>', '<title>Bloque %s · %s · Ejercicios · 0223 Aplicaciones ofimáticas</title>' % (numero, nombre), antes)
        (TEMAS / pagina).write_text(pag_antes + cab + aviso + sec + '\n\n' + pie, encoding='utf-8')
    indice = indice.rstrip() + '\n\n  <!-- aula:indice -->\n  <!-- /aula:indice -->\n\n'
    origen.write_text(antes + cabecera + indice + pie, encoding='utf-8')

# ---------------------------------------------------------------- 2. teoría del tema 1
p1 = TEMAS / 'ut01.html'
s1 = p1.read_text(encoding='utf-8')
teoria = s1.replace('<h1>Tema 1 — Instalación y actualización de aplicaciones ofimáticas</h1>',
                    '<h1>Teoría — Instalación y actualización de aplicaciones ofimáticas</h1>')
teoria = re.sub(r'<title>.*?</title>', '<title>Teoría · Tema 1 · Instalación y actualización de aplicaciones ofimáticas · 0223 Aplicaciones ofimáticas</title>', teoria)
teoria = re.sub(r'\n?<details class="ra-ce calif-tema">.*?</details>', '', teoria, flags=re.S)
teoria = re.sub(r'\n  <details class="ra-ce">.*?\n  </details>\n', '\n', teoria, flags=re.S)
ra_ce_ut01 = re.search(r'\n  <details class="ra-ce">(.*?)\n  </details>\n', s1, re.S)[1]
(TEMAS / 'ut01-teoria.html').write_text(teoria, encoding='utf-8')
for ident in re.findall(r'\bid="(apartado-[^"]+)"', teoria):
    mapa_ids[(1, ident)] = 'ut01-teoria.html'

# ---------------------------------------------------------------- 3. enlaces
def reescribir(texto, pagina_actual=None, tema_actual=None):
    def cambia(m):
        prefijo, n, ident = m[1], int(m[2]), m[3]
        dest = mapa_ids.get((n, ident))
        return 'href="' + prefijo + dest + '#' + ident + '"' if dest else m[0]
    texto = re.sub(r'href="((?:\.\./temas/|temas/)?)ut(0[23])-ejercicios\.html#([^"]+)"', cambia, texto)
    texto = re.sub(r'href="((?:\.\./temas/|temas/)?)ut(01)\.html#([^"]+)"', cambia, texto)
    if pagina_actual and tema_actual in (2, 3) and re.match(r'ut0[23]-(bloque-\d|ejercicios)\.html', pagina_actual):
        def interno(m):
            dest = mapa_ids.get((tema_actual, m[1]))
            if dest and dest != pagina_actual:
                return 'href="' + dest + '#' + m[1] + '"'
            return m[0]
        texto = re.sub(r'href="#([^"]+)"', interno, texto)
    return texto

for f in list(WEB.rglob('*.html')) + [WEB / 'datos/temas.json']:
    t = f.read_text(encoding='utf-8')
    m = re.match(r'ut(\d\d)-', f.name)
    nuevo = reescribir(t, f.name, int(m[1]) if m else None)
    if nuevo != t:
        f.write_text(nuevo, encoding='utf-8')

# ---------------------------------------------------------------- 4. portadas
def portada(n, intro, plan, extra_head=''):
    f = TEMAS / ('ut%02d.html' % n)
    s = f.read_text(encoding='utf-8')
    i = s.index('<nav class="subnav"') if '<nav class="subnav"' in s else s.index('<div class="aula-herramientas">')
    j = s.index('  <footer class="pie">')
    cuerpo = ('<nav class="subnav" aria-label="Apartados del tema %d"></nav>\n'
              '<div class="aula-herramientas"><button type="button" data-imprimir hidden>Imprimir / guardar PDF</button></div>\n\n' % n
              + intro + '\n\n  <!-- aula:secciones -->\n  <!-- /aula:secciones -->\n\n'
              '  <details class="ra-ce aula-plan"><summary>Qué se evalúa y cómo se organiza el tema</summary>\n'
              + plan + '\n  </details>\n\n' + extra_head)
    resto = s[j:]
    k, fin = resto.index('</main></div>'), resto.index('</body>')
    resto = resto[:k] + '</main></div>\n' + resto[fin:]   # sin los scripts de la teoría (autocomprobación)
    f.write_text(s[:i] + cuerpo + resto, encoding='utf-8')

# Tema 1: la portada nueva; los enlaces antiguos con ancla van a la teoría.
mapa_ut01 = {ident: 'ut01-teoria.html' for (n, ident), _ in mapa_ids.items() if n == 1}
portada(1, '''  <p>Antes de usar las aplicaciones ofimáticas hay que saber elegirlas, instalarlas,
  configurarlas y mantenerlas al día. Todo el tema se trabaja sobre máquina virtual.</p>
  <script>/* Enlaces antiguos (ut01.html#apartado) a la página de teoría */
  (function () { var m = ''' + json.dumps(mapa_ut01, ensure_ascii=False, sort_keys=True) + '''; var h = decodeURIComponent(location.hash.slice(1)); if (h && m[h]) location.replace(m[h] + "#" + h); })();</script>''',
        '  ' + ra_ce_ut01.strip())

s2 = (TEMAS / 'ut02.html').read_text(encoding='utf-8')
ra2 = re.search(r'\n  <details class="ra-ce">(.*?)\n  </details>\n', s2, re.S)[1].replace('<summary>Qué se evalúa · RA y criterios</summary>', '').strip()
portada(2, '''  <p>Es el tema más grande del módulo: se reparte en <strong>ocho subtemas</strong>
  (2.0 a 2.7) y lo recorres construyendo tu propio currículum vitae. Los estilos
  (2.2) se enseñan pronto porque son la base de las plantillas, del índice y de los
  manuales finales.</p>''', '    ' + ra2)

s3 = (TEMAS / 'ut03.html').read_text(encoding='utf-8')
ra3 = re.search(r'\n  <details class="ra-ce">(.*?)\n  </details>\n', s3, re.S)[1].replace('<summary>Qué se evalúa · RA y criterios</summary>', '').strip()
prog3 = re.search(r'(  <h2 id="apartado-programas">.*?</table></div>)', s3, re.S)[1]
portada(3, '''  <p>Vas a obtener, retocar, montar y publicar imágenes con <strong>GIMP 3</strong>.
  En los ejercicios eres el diseñador gráfico de un grupo de música o de un estudio
  de videojuegos inventado, y preparas todas sus piezas: logotipo, portada, miniatura,
  cartel, banner y web.</p>''', '    ' + ra3 + '\n' + prog3.replace('<h2 id="apartado-programas">', '<h3>').replace('</h2>', '</h3>'))

# ---------------------------------------------------------------- 5. «Preparar el examen» y secciones
PLANTILLA_EXAMEN = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Preparar el examen · Tema {n} · 0223 Aplicaciones ofimáticas</title>
<link rel="stylesheet" href="../assets/estilo.css">
</head>
<body>
<div class="envoltura">

  <header class="cab">
    <p class="modulo">0223 · Aplicaciones ofimáticas · Tema {n} · Preparar el examen</p>
    <h1>Preparar el examen — Tema {n}</h1>
    <p class="meta">1.º SMR · Curso 2026/2027 · 1.ª evaluación</p>
  </header>
<nav class="subnav" aria-label="Apartados del tema {n}"></nav>

  <p>{intro}</p>

  <!-- aula:indice -->
  <!-- /aula:indice -->

  <footer class="pie">
    <p>0223 Aplicaciones ofimáticas · Material de consulta del alumnado.
    Currículo: Decreto 272/2009 (Extremadura).</p>
  </footer>

</div>
</body>
</html>
'''
INTRO = {
    1: 'La autocomprobación de la teoría se corrige sola: repítela tantas veces como quieras. No cuenta para la nota.',
    2: 'El examen del tema es práctico, en Word. Aquí tienes un examen de repaso con el mismo formato, pistas y autocorrector, y las autocomprobaciones de cada subtema. Nada de esto cuenta para la nota.',
    3: 'Las autocomprobaciones de cada subtema se corrigen solas: repítelas tantas veces como quieras. No cuentan para la nota. Para practicar GIMP antes del punto de control, haz la práctica guiada.',
}
for n in (1, 2, 3):
    (TEMAS / ('ut%02d-examen.html' % n)).write_text(PLANTILLA_EXAMEN.format(n=n, intro=INTRO[n]), encoding='utf-8')


def item(etq, titulo, url, texto='', **extra):
    d = {'etiqueta': etq, 'titulo': titulo, 'url': url, 'texto': texto}
    d.update(extra)
    return d


def bloques(n):
    return [item('Bloque ' + num, nombre, pag, DESCRIPCION[num]) for pag, num, nombre, _ in bloques_tema[n]]


def comprueba(pagina):
    s = (TEMAS / pagina).read_text(encoding='utf-8')
    m = re.search(r'id="(apartado-\d+-comprueba[^"]*)"', s)
    return pagina + '#' + m[1]


SUB2 = [('2.0', 'Repaso: primer documento y edición básica', 'Repaso, no evalúa'),
        ('2.1', 'Entorno, edición avanzada y personalización de Word', 'CE a · 8 h'),
        ('2.2', 'Formato de documento y estilos', 'Base de b, e, f · 10 h'),
        ('2.3', 'Tablas, imágenes y elementos gráficos', 'CE c · 10 h'),
        ('2.4', 'Plantillas y documentos estructurados', 'CE b · 8 h'),
        ('2.5', 'Importación, exportación y combinación de correspondencia', 'CE d · 10 h'),
        ('2.6', 'Trabajo colaborativo y seguridad documental', 'Transversal, apoya f · 6 h'),
        ('2.7', 'Macros y elaboración de manuales', 'CE e, f · 8 h')]
SUB3 = [('3.1', 'La imagen digital', 'CE a, c · 4 h'),
        ('3.2', 'Obtener imágenes: escáner, cámara y capturas', 'CE b · 3 h'),
        ('3.3', 'Retoque básico en GIMP', 'CE c, d · 6 h'),
        ('3.4', 'Capas, selecciones y texto', 'CE d · 6 h'),
        ('3.5', 'Importar, exportar y optimizar', 'CE e · 4 h'),
        ('3.6', 'Publicar en web, redes e impresión', 'CE f · 3 h')]


def pag(num):
    a, b = num.split('.')
    return 'ut%02d-%s.html' % (int(a), b)


SECCIONES = {
    1: {'teoria': [item('Teoría', 'Instalación y actualización de aplicaciones ofimáticas', 'ut01-teoria.html',
                        'Tipos de suites, licencias, requisitos, instalación, configuración, actualización e incidencias')],
        'practicas': [item('Prácticas', 'Prácticas del tema 1 (P1.1 a P1.6)', 'ut01-teoria.html#apartado-9-practicas-del-tema',
                           'Sobre máquina virtual · entrega en Moodle')],
        'examen': [item('Autocomprobación', 'Comprueba lo que has entendido', comprueba('ut01-teoria.html'), 'Se corrige sola')]},
    2: {'teoria': [item('Tema ' + num, tit, pag(num), txt) for num, tit, txt in SUB2]
                  + [item('Consulta', 'Mapa de la cinta de Word', 'mapa-cinta.html', 'Las 8 pestañas, grupo a grupo, con buscador')],
        'ejercicios': bloques(2),
        'practicas': [item('PC1', 'Documento profesional integrador', 'ut02-practicas.html#apartado-pc1-documento-profesional-integrador', 'Punto de control · integra 2.0 a 2.3 · rúbrica de 10'),
                      item('PC2', 'Dossier corporativo y mailing comercial', 'ut02-practicas.html#apartado-pc2-dossier-corporativo-y-mailing-comercial', 'Punto de control · integra 2.0 a 2.5 · rúbrica de 10'),
                      item('PC3', 'Proyecto final: manual de usuario con macros', 'ut02-practicas.html#apartado-pc3-proyecto-final-manual-de-usuario-con-macros', 'Punto de control · todo el tema · rúbrica de 10'),
                      item('Caso práctico', 'La carta de un restaurante', 'ut02-practicas-carta.html', 'CE c · 4 sesiones · rúbrica de 10'),
                      item('Taller', 'Taller de maquetación (T1 a T5)', 'ut02-practicas-taller.html', 'Cinco prácticas cortas · trabajo diario')],
        'examen': [item('Examen de repaso', 'Examen de repaso con pistas', 'ut02-examen-repaso.html', 'Mismo formato que el examen, con pistas por bloque'),
                   item('Autocorrector', 'Autocorrector del examen de repaso', '../herramientas/ut02-autocorrector.html', 'Sube tus archivos y te dice qué está bien')]
                  + [item('Autocomprobación', 'Subtema ' + num, comprueba(pag(num)), tit) for num, tit, _ in SUB2[1:]],
        'enclase': [item('Reto en equipo', 'El documento saboteado', 'ut02-ejercicios-reto-saboteado.html', 'Equipos de 3 · 1 sesión · formativo'),
                    item('En equipo', 'Práctica colaborativa en Google Docs', 'ut02-6-practica-colaborativa.html', 'Equipos de 3 · 3 sesiones · formativa')]},
    3: {'teoria': [item('Tema ' + num, tit, pag(num), txt) for num, tit, txt in SUB3],
        'ejercicios': bloques(3) + [item('Laboratorio', 'Laboratorio de imagen', 'laboratorio-imagen.html',
                                         'Nueve herramientas para ver por dentro la resolución, el color, la compresión, las capas y los tamaños', grupo='interactivo')],
        'practicas': [item('P3.%s' % num[2], 'Prácticas del subtema %s' % num, pag(num) + '#' + re.search(r'id="(apartado-\d+-practicas-del-subtema)"', (TEMAS / pag(num)).read_text(encoding='utf-8'))[1], tit) for num, tit, _ in SUB3]
                     + [item('Guiada', 'Práctica guiada de GIMP: el cartel del concierto', 'ut03-gimp-guiada.html', 'Repaso de todo GIMP paso a paso · 3 h'),
                        item('Punto de control', 'Jerte Gaming Cup', 'ut03-practica-control.html', 'Evaluable, sin guía · rúbrica de 10 · 3 h')],
        'examen': [item('Autocomprobación', 'Subtema ' + num, comprueba(pag(num)), tit) for num, tit, _ in SUB3]},
}
p = WEB / 'datos/temas.json'
datos = json.loads(p.read_text(encoding='utf-8'))
for t in datos['temas']:
    if t['ut'] in SECCIONES:
        t['secciones'] = SECCIONES[t['ut']]
p.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('bloques:', {n: [b[0] for b in v] for n, v in bloques_tema.items()})
print('ids reubicados:', len(mapa_ids))
