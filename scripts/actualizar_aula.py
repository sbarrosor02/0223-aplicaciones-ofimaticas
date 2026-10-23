from pathlib import Path
import re
import json
import html
import unicodedata

ROOT = Path(__file__).resolve().parents[2]
REPOS = [Path(__file__).resolve().parents[1].name]

def plain(value):
    return html.unescape(re.sub('<[^>]+>', '', value)).strip()

def escape(value):
    return html.escape(str(value), quote=True)

def slug(value):
    value = unicodedata.normalize('NFKD', plain(value)).encode('ascii', 'ignore').decode().lower()
    return re.sub('[^a-z0-9]+', '-', value).strip('-')

def sin_ce(value):
    """Quita las etiquetas de criterio (<span class="ce">CE e</span>) de un título."""
    return re.sub(r'<span class="ce[^"]*">.*?</span>', '', value, flags=re.S)

def headings(source):
    return [(match[0], plain(sin_ce(match[1]))) for match in re.findall(r'<h2\b[^>]*\bid="([^"]+)"[^>]*>(.*?)</h2>', source, re.S)]

def identify(source):
    used = set(re.findall(r'\bid="([^"]+)"', source))
    def add(match):
        if re.search(r'\bid=', match[1]):
            return match[0]
        target = 'apartado-' + slug(match[2])
        while target in used:
            target += '-mas'
        used.add(target)
        return '<h2' + match[1] + ' id="' + target + '">' + match[2] + '</h2>'
    return re.sub(r'<h2([^>]*)>(.*?)</h2>', add, source, flags=re.S)

def calificacion_tema(topic, data):
    """Recuadro «Cómo se califica este tema» de la portada de cada tema, desde temas.json."""
    cal = data.get('calificacion')
    inst = topic.get('instrumentos')
    if not cal or not inst or not topic.get('ra'):
        return ''
    ra = next((r for r in cal['ra'] if r['ra'] == topic['ra']), None)
    if not ra:
        return ''
    rep = cal['reparto_dual'] if ra.get('dual') else cal['reparto']
    def enlaces(items):
        partes = []
        for item in items:
            texto = escape(item['texto'])
            url = item.get('url')
            if url:
                url = url[len('temas/'):] if url.startswith('temas/') else '../' + url
                texto = '<a href="' + escape(url) + '">' + texto + '</a>'
            partes.append(texto)
        return '; '.join(partes)
    html_box = ('<details class="ra-ce calif-tema"><summary>Cómo se califica este tema · ' + escape(ra['ra']) + ' · '
                + str(ra['peso']) + ' % de la nota del módulo</summary>'
                + '<p>La nota del ' + escape(ra['ra']) + ' es de 0 a 10 y sale de estos instrumentos. Todos los '
                + 'criterios de evaluación del resultado pesan lo mismo.</p><ul>'
                + '<li><strong>Pruebas de evaluación · ' + str(rep['pruebas']) + ' %</strong> — ' + escape(inst['pruebas']) + '</li>'
                + '<li><strong>Casos prácticos · ' + str(rep['casos']) + ' %</strong> — ' + enlaces(inst['casos']) + '.</li>'
                + '<li><strong>Trabajo diario · ' + str(rep['diario']) + ' %</strong> — ' + enlaces(inst['diario']) + '.</li>')
    if 'feoe' in rep:
        html_box += '<li><strong>Formación en empresa · ' + str(rep['feoe']) + ' %</strong> — informe de la estancia.</li>'
    html_box += ('</ul><p><strong>Para aprobarlo:</strong> al menos un 5 en pruebas y un 5 en casos prácticos, '
                 'todas las prácticas entregadas y en plazo, y superadas al menos el 70 % de las tareas de '
                 'trabajo diario.</p>')
    if inst.get('no_cuenta'):
        html_box += '<p><strong>No cuentan para la nota:</strong> ' + escape(inst['no_cuenta']) + '</p>'
    html_box += '<p><a href="calificacion.html">Cómo se calcula la nota del módulo</a></p></details>'
    return html_box


# Páginas de un tema cuyo nombre no empieza por utNN.
TEMA_DE_PAGINA = {'laboratorio-imagen.html': 3, 'mapa-cinta.html': 2}

def tema_de(name):
    """Número de tema a partir del nombre del archivo (ut02-3.html → 2)."""
    if name in TEMA_DE_PAGINA:
        return TEMA_DE_PAGINA[name]
    match = re.match(r'ut(\d\d)', name)
    return int(match[1]) if match else None

def seccion_de(source, name):
    """Apartado del tema para las migas: el enlace actual de .subnav o, en subtemas y
    subpáginas, el título de la página («Tema 2.3 — Tablas…» → «2.3 Tablas…»)."""
    if re.fullmatch(r'ut\d\d\.html', name):
        return ''
    nav = re.search(r'<nav class="subnav".*?</nav>', source, re.S)
    if nav:
        actual = re.search(r'<a\b[^>]*aria-current="page"[^>]*>(.*?)</a>', nav[0], re.S)
        if actual:
            return plain(actual[1])
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', source, re.S)
    if not h1:
        return ''
    titulo = plain(h1[1])
    sub = re.match(r'Tema (\d+\.\d+)\s+—\s+(.*)', titulo)
    if sub:
        return sub[1] + ' ' + sub[2]
    return re.split(r'\s+[—·]\s+', titulo)[0]

def migas(source, tema):
    """Ruta «Inicio › Tema N › Apartado» al principio del contenido. Se regenera en cada ejecución."""
    source = re.sub(r'<nav class="aula-migas".*?</nav>', '', source, flags=re.S)
    if not tema:
        return source
    partes = ['<a href="../index.html">Inicio</a>']
    titulo = 'Tema %d · %s' % (tema['ut'], escape(tema['titulo']))
    if tema.get('seccion'):
        partes.append('<a href="ut%02d.html">%s</a>' % (tema['ut'], titulo))
        partes.append('<span aria-current="page">' + escape(tema['seccion']) + '</span>')
    else:
        partes.append('<span aria-current="page">' + titulo + '</span>')
    nav = '<nav class="aula-migas" aria-label="Estás en">' + '<span aria-hidden="true">›</span>'.join(partes) + '</nav>'
    return source.replace('<main class="envoltura" id="contenido" tabindex="-1">', '<main class="envoltura" id="contenido" tabindex="-1">' + nav, 1)


def shell(source, code, current, short_name, tema=None):
    prefix = '../' if current.startswith('temas/') else ''
    source = identify(source)
    entries = headings(source)
    toc = ''.join('<li><a href="#' + escape(target) + '">' + escape(label) + '</a></li>' for target, label in entries if 'criterio' not in label.lower() and 'resultado de aprendizaje' not in label.lower())
    if current == 'recursos.html' or current.endswith('mapa-cinta.html'):
        toc = '<li><a href="#contenido">Consultar el material</a></li>'
    bloque_tema = ''
    if tema:
        bloque_tema = ('<a class="indice-tema" href="ut%02d.html"><span>Tema %d</span>%s</a>' % (tema['ut'], tema['ut'], escape(tema['titulo'])) +
                       '<a class="indice-material" href="../recursos.html?tema=%d">Todo el material del tema %d</a>' % (tema['ut'], tema['ut']))
    sidebar = '<aside class="aula-indice"><a class="indice-inicio" href="' + prefix + 'index.html">Inicio del módulo</a>' + bloque_tema + '<details open><summary>En esta página</summary><ul>' + toc + '</ul></details></aside>'
    if 'class="aula-layout"' in source:
        source = re.sub(r'<aside class="aula-indice">.*?</aside>', lambda match: sidebar, source, count=1, flags=re.S)
        return migas(source, tema)
    source = source.replace('</head>', '<link rel="stylesheet" href="' + prefix + 'assets/aula.css">\n<script defer src="' + prefix + 'assets/aula.js"></script>\n</head>')
    top = '<a class="saltar" href="#contenido">Saltar al contenido</a><header class="aula-barra"><a class="aula-marca" href="' + prefix + 'index.html">' + code + ' / ' + short_name + '</a><nav aria-label="Navegación del módulo">'
    for label, target in [('Temas', 'index.html'), ('Apuntes', 'recursos.html?tipo=apuntes'), ('Ejercicios', 'recursos.html?tipo=ejercicios'), ('Prácticas', 'recursos.html?tipo=practicas'), ('Materiales', 'recursos.html')]:
        active = ' aria-current="page"' if current == target else ''
        top += '<a href="' + prefix + target + '"' + active + '>' + label + '</a>'
    top += '</nav></header>'
    source = source.replace('<body>', '<body data-modulo="' + code + '">\n' + top)
    source = source.replace('<div class="envoltura">', '<div class="aula-layout">' + sidebar + '<main class="envoltura" id="contenido" tabindex="-1">', 1)
    last = source.rfind('\n</div>')
    if last < 0:
        raise ValueError(current)
    source = source[:last] + '\n</main></div>' + source[last + len('\n</div>'):]
    source = re.sub(r'(<header class="cab">.*?</header>(?:\s*<nav class="subnav".*?</nav>)?)', r'\1\n<div class="aula-herramientas"><button type="button" data-imprimir hidden>Imprimir / guardar PDF</button></div>', source, count=1, flags=re.S)
    source = re.sub(r'<div class="ra-ce">(.*?)</div>', lambda match: '<details class="ra-ce"><summary>Qué se evalúa · RA y criterios</summary>' + match[1] + '</details>', source, flags=re.S)
    source = re.sub(r'(<table\b.*?</table>)', r'<div class="aula-tabla" role="region" aria-label="Tabla de datos; desplazamiento horizontal" tabindex="0">\1</div>', source, flags=re.S)
    return migas(source, tema)

def document(title, content):
    return '<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>' + escape(title) + '</title>\n<link rel="stylesheet" href="assets/estilo.css">\n</head>\n<body>\n<div class="envoltura">\n' + content + '\n<footer class="pie"><p>IES Valle del Jerte · CFGM Sistemas Microinformáticos y Redes · Curso 2026/2027</p></footer>\n</div>\n</body>\n</html>\n'

for repo in REPOS:
    web = ROOT / repo / 'web'
    data = json.loads((web / 'datos/temas.json').read_text(encoding='utf-8'))
    code = data['modulo']
    short_name = 'Montaje y mantenimiento' if code == '0221' else 'Aplicaciones ofimáticas'
    pages = {}
    titulos = {topic['ut']: topic['titulo'] for topic in data['temas']}
    for path in sorted((web / 'temas').glob('*.html')):
        source = path.read_text(encoding='utf-8')
        subnavs = {
            'ut02': [('Portada del tema', 'ut02.html'), ('Apuntes', 'ut02.html#apartado-subtemas'), ('Ejercicios guiados', 'ut02-ejercicios.html'), ('Reto en equipo', 'ut02-ejercicios-reto-saboteado.html'), ('Prácticas de control', 'ut02-practicas.html'), ('Examen de repaso', 'ut02-examen-repaso.html'), ('Mapa de Word', 'mapa-cinta.html')],
            'ut03': [('Portada del tema', 'ut03.html'), ('Apuntes', 'ut03.html#apartado-subtemas'), ('Ejercicios guiados', 'ut03-ejercicios.html'), ('Laboratorio de imagen', 'laboratorio-imagen.html')],
        }
        prefijo_tema = 'ut03' if path.name.startswith('laboratorio-imagen') else path.name[:4]
        if code == '0223' and prefijo_tema in subnavs and re.match(r'ut\d\d', prefijo_tema):
            source = re.sub(r'\n?<nav class="subnav"[^>]*>.*?</nav>', '', source, count=1, flags=re.S)
            nav = '<nav class="subnav" aria-label="Apartados del tema ' + str(int(prefijo_tema[2:])) + '">'
            for label, target in subnavs[prefijo_tema]:
                if not (web / 'temas' / target.split('#')[0]).exists():
                    continue
                active = ' aria-current="page"' if target == path.name else ''
                nav += '<a href="' + target + '"' + active + '>' + label + '</a>'
            nav += '</nav>'
            source = re.sub(r'(<header class="cab">.*?</header>)', lambda match: match[1] + '\n' + nav, source, count=1, flags=re.S)
        source = re.sub(r'\n?<details class="ra-ce calif-tema">.*?</details>', '', source, flags=re.S)
        topic = next((t for t in data['temas'] if path.name == 'ut%02d.html' % t['ut']), None)
        box = calificacion_tema(topic, data) if topic else ''
        numero = tema_de(path.name)
        tema = {'ut': numero, 'titulo': titulos[numero], 'seccion': seccion_de(source, path.name)} if numero in titulos else None
        source = shell(source, code, 'temas/' + path.name, short_name, tema)
        if box:
            source = re.sub(r'(<div class="aula-herramientas">.*?</div>)', lambda match: match[1] + '\n' + box, source, count=1, flags=re.S)
        path.write_text(source, encoding='utf-8')
        pages[path.name] = source
    cards = []
    downloads = {}
    orden_tipos = ['apuntes', 'ejercicios', 'practicas', 'consulta', 'descargas']
    def card(category, title, url, description, terms='', shortcuts='', ut=None):
        labels = {'apuntes': 'Apuntes', 'ejercicios': 'Ejercicios guiados / repaso', 'practicas': 'Prácticas evaluables', 'consulta': 'Consulta', 'descargas': 'Descarga'}
        etiqueta_tema = ''
        if ut is not None:
            etiqueta_tema = '<span class="aula-tema">Tema ' + str(ut) + '</span><span class="aula-tema-titulo">' + escape(titulos.get(ut, '')) + '</span>'
            terms = 'tema ' + str(ut) + ' ' + titulos.get(ut, '') + ' ' + terms
        else:
            etiqueta_tema = '<span class="aula-tema">Todo el módulo</span>'
        html_card = ('<li data-material="' + category + '" data-tema="' + ('' if ut is None else str(ut)) + '" data-busqueda="' + escape(terms) + '">' +
                     '<div class="aula-etiquetas">' + etiqueta_tema + '<span class="aula-tipo">' + labels[category] + '</span></div>' +
                     '<h2><a href="' + escape(url) + '">' + escape(title) + '</a></h2><p>' + escape(description) + '</p>' + shortcuts + '</li>')
        return ((ut if ut is not None else 99), orden_tipos.index(category), html_card)
    for name, source in pages.items():
        title = plain(re.search(r'<h1[^>]*>(.*?)</h1>', source, re.S)[1])
        section_list = headings(source)
        category = 'apuntes'
        if 'ejercicios' in name or 'examen-repaso' in name:
            category = 'ejercicios'
        elif 'practicas' in name:
            category = 'practicas'
        elif 'mapa-' in name or 'laboratorio-' in name or name in ('ut00.html', 'calificacion.html'):
            category = 'consulta'
        elif name in (('ut01.html',) if code == '0221' else ('ut02.html', 'ut03.html')):
            continue
        filtered = [(target, label) for target, label in section_list if not any(word in label.lower() for word in ['criterio', 'resultado de aprendizaje', 'pendiente', 'próximos', 'en esta página'])]
        shortcuts = '<div class="aula-atajos">' + ''.join('<a href="temas/' + name + '#' + target + '">' + escape(label) + '</a>' for target, label in (filtered if category == 'ejercicios' else filtered[:5])) + '</div>'
        description = 'Material de consulta para seguir las sesiones.'
        if category == 'ejercicios':
            description = 'Practica y comprueba lo aprendido. Actividades formativas; no cuentan para la nota.'
        if category == 'practicas':
            description = 'Consulta el enunciado, las condiciones de entrega y la rúbrica.'
        search_terms = ' '.join(plain(sin_ce(text)) for text in re.findall(r'<h[23][^>]*>(.*?)</h[23]>', source, re.S))
        cards.append(card(category, title, 'temas/' + name, description, search_terms, shortcuts, tema_de(name)))
        if category == 'apuntes':
            for target, label in section_list:
                if 'prácticas del' in label.lower():
                    cards.append(card('practicas', title + ' · Prácticas del apartado', 'temas/' + name + '#' + target, 'Actividades incluidas en los apuntes. Consulta allí sus requisitos y criterios.', '', '', tema_de(name)))
        for target, label in re.findall(r'<a\b[^>]*href="([^"]+\.(?:docx|dotx|xlsx|pptx|odt|pdf|zip|png|jpg))"[^>]*>(.*?)</a>', source, re.S):
            if target.startswith('../'):
                destination = target[3:]
                if (web / destination).is_file():
                    downloads[destination] = (plain(label) or Path(destination).name, name)
    for target, (label, origin) in downloads.items():
        cards.append(card('descargas', label, target, 'Archivo ' + Path(target).suffix[1:].upper() + ' · ' + Path(target).name, '', '<p><a href="temas/' + origin + '">Ver el enunciado que utiliza este archivo</a></p>', tema_de(origin)))
    cards = [html_card for _, _, html_card in sorted(cards, key=lambda c: (c[0], c[1]))]
    filters = ''.join('<button type="button" data-filtro="' + value + '" aria-pressed="' + ('true' if value == 'todos' else 'false') + '">' + label + '</button>' for value, label in [('todos','Todos'), ('apuntes','Apuntes'), ('ejercicios','Ejercicios'), ('practicas','Prácticas'), ('consulta','Consulta'), ('descargas','Descargas')])
    temas_catalogo = sorted({tema_de(name) for name in pages if tema_de(name) is not None and tema_de(name) in titulos})
    filtros_tema = ''.join('<button type="button" data-filtro-tema="' + value + '" aria-pressed="' + ('true' if value == 'todos' else 'false') + '"' + (' title="' + escape(titulos[int(value)]) + '"' if value != 'todos' else '') + '>' + label + '</button>' for value, label in [('todos', 'Todos los temas')] + [(str(n), 'Tema ' + str(n)) for n in temas_catalogo])
    catalogue = '<header class="cab"><p class="modulo">' + code + ' · ' + short_name + '</p><h1>Encuentra tu material</h1><p class="meta">Apuntes, ejercicios, prácticas y archivos de trabajo, en un solo lugar.</p></header><div class="aula-busqueda" hidden><label for="buscar-material">Buscar por título o apartado</label><input id="buscar-material" type="search" placeholder="Por ejemplo: estilos, tabla, circuito…"><p class="aula-filtros-titulo">Tema</p><div class="aula-filtros" aria-label="Filtrar por tema">' + filtros_tema + '</div><p class="aula-filtros-titulo">Tipo de material</p><div class="aula-filtros" aria-label="Filtrar por tipo">' + filters + '<button type="button" data-limpiar>Limpiar búsqueda</button></div><p id="estado-busqueda" role="status" aria-live="polite"></p></div><noscript><p>Todos los materiales están disponibles en la lista. Activa JavaScript para usar los filtros.</p></noscript><ul class="aula-catalogo">' + '\n'.join(cards) + '</ul>'
    (web / 'recursos.html').write_text(shell(document('Materiales · ' + short_name, catalogue), code, 'recursos.html', short_name), encoding='utf-8')
    home = '<header class="cab"><p class="modulo">IES Valle del Jerte · CFGM SMR · ' + code + '</p><h1>' + escape(data['titulo']) + '</h1><p class="meta">' + ('2.º curso · 6 h/semana' if code == '0221' else '1.º curso · 7 h/semana') + ' · Curso 2026/2027</p></header><p>Tu aula de consulta: estudia el tema, practica con los ejercicios y prepara las entregas que indique el profesor.</p><nav class="ruta-estudio" aria-label="Qué necesitas hacer">'
    for label, target, description in [('Estudiar', 'apuntes', 'Apuntes y explicaciones por tema'), ('Practicar', 'ejercicios', 'Ejercicios para aprender y repasar'), ('Preparar una entrega', 'practicas', 'Enunciados, requisitos y rúbricas')]:
        home += '<a href="recursos.html?tipo=' + target + '"><strong>' + label + '</strong><span>' + description + '</span></a>'
    home += '</nav><p><a href="recursos.html">Buscar un material o descargar un archivo</a></p><h2>Recorrido del módulo</h2><p>Sigue el orden de los temas y las indicaciones del profesor. Los próximos contenidos se añadirán aquí.</p><ul class="lista-temas">'
    for topic in data['temas']:
        available = (web / ('temas/ut%02d.html' % topic['ut'])).exists()
        if not available:
            continue
        label = 'Diagnóstico inicial · no cuenta para la nota' if topic['ut'] == 0 else str(topic['horas']) + ' h · ' + topic['ra']
        if topic.get('estado') == 'en progreso':
            available_blocks = [str(block['ut']) for block in topic.get('subtemas', []) if block.get('estado') == 'publicado']
            label += ' · En desarrollo'
            if available_blocks:
                label += ' · Disponibles: ' + ', '.join(available_blocks)
        home += '<li><a href="temas/ut%02d.html"><span class="ut">Tema %s</span>%s<br><span class="etq">%s</span></a></li>' % (topic['ut'], topic['ut'], escape(topic['titulo']), escape(label))
    home += '</ul><h2>Antes de entregar</h2><p>Los ejercicios sirven para entrenar. En las prácticas, lee el enunciado completo, revisa los archivos que se piden y comprueba la rúbrica antes de entregar por el medio indicado en clase.</p>'
    if (web / 'temas/calificacion.html').exists():
        home += '<div class="tarjeta"><strong>¿Cómo se calcula tu nota?</strong><p><a href="temas/calificacion.html">Consulta cómo se califica el módulo</a>: el peso de cada resultado de aprendizaje, qué cuenta en cada tema y qué hace falta para aprobar.</p></div>'
    if code == '0223':
        home += '<div class="tarjeta"><strong>¿No encuentras una opción de Word?</strong><p><a href="temas/mapa-cinta.html">Consulta el mapa de la cinta</a>: pestañas, grupos y atajos.</p></div>'
    else:
        home += '<div class="aviso"><strong>Antes de trabajar en el taller</strong><p>Revisa <a href="temas/ut01-prl.html">Seguridad y PRL</a> y sigue las instrucciones del profesor.</p></div>'
    (web / 'index.html').write_text(shell(document(short_name, home), code, 'index.html', short_name), encoding='utf-8')
    print(repo, len(pages), 'páginas de contenido; catálogo:', len(cards), 'materiales')
