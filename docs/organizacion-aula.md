# Navegación del aula · revisión del 23/09/2026

## Diagnóstico

La lectura era clara y los materiales estaban separados por temas, pero acceder
a una práctica requería recorrer varios índices. Las páginas extensas tenían
pocos atajos; Ofimática no tenía la barra de apartados que ya existía en Montaje.
Los archivos descargables estaban repartidos entre enunciados. Las portadas
priorizaban códigos y metadatos frente a las tareas del alumnado.

Se conserva la secuencia didáctica, los enunciados, las rúbricas, los
cuestionarios, los dibujos y las URLs existentes. No se resuelven en esta
intervención los circuitos pendientes ni se redactan nuevos contenidos.

## Organización implementada

- Inicio: estudiar, practicar y preparar una entrega, más el recorrido por temas.
- Materiales: catálogo con filtros por tipo y búsqueda por títulos y apartados,
  incluidos encabezados de nivel 3. No es una búsqueda de texto completo.
- Prácticas: reúne tanto páginas propias como actividades incluidas en los apuntes.
- Descargas: archivos existentes con enlace al enunciado de procedencia.
- Lecciones: índice lateral en escritorio y desplegable en móvil.
- RA y criterios: desplegable consultable, abierto al imprimir.
- Montaje conserva su barra de apartados; Ofimática incorpora una equivalente.
- Se mantienen accesibles los materiales sin JavaScript; solo los filtros y
  el botón de impresión lo necesitan.

## Diseño

Misma estructura en ambos módulos, con acento verde en Montaje y azul en
Ofimática. Fondo claro, tipografía local Segoe UI/Calibri, columna de lectura
limitada y sin fuentes ni dependencias externas. Foco visible, enlace para
saltar al contenido, tablas con desplazamiento horizontal y estilos de impresión.
La búsqueda no envía datos a ningún servicio.

## Mantenimiento

Desde este repositorio, ejecutar:

```powershell
python scripts/actualizar_aula.py
```

Python 3, solo biblioteca estándar. El script lee `web/datos/temas.json` y las
páginas reales de `web/temas/`. Regenera `web/index.html`, `web/recursos.html`
y los índices de las lecciones. Las portadas generadas se modifican en el script;
el contenido de las lecciones se edita en sus HTML habituales.
Los títulos nuevos reciben identificadores; los existentes se conservan para
no romper enlaces. Al renombrar o eliminar apartados, revisar sus enlaces.

`assets/aula.css` y `assets/aula.js` son compartidos por los dos repositorios.
Se carga la capa nueva después del CSS original y de los estilos específicos
para conservar las figuras y componentes existentes. No hay proceso de build
en GitHub Pages; el generador se ejecuta antes del commit.

## Copia de seguridad y validación

Copia completa anterior al cambio, incluido `.git`, en:
`../copias-seguridad/20260923-131511/0223-aplicaciones-ofimaticas/`.
No forma parte de la web publicada. Para recuperar, copiar primero esa carpeta
a una ubicación nueva y comprobar su contenido antes de sustituir el repositorio.

Validación conjunta: 20 páginas en Chrome a 1440 y 390 px; enlaces locales y
anclas, identificadores únicos, ausencia de desbordamientos de página,
filtros, búsqueda sin resultados, limpieza, catálogo sin JavaScript,
respuesta del cuestionario de 2.2 y buscador del mapa de Word.
Capturas y resultados en `../revision-aulas/`.

La comprobación visual de navegación no constituye una revisión de exactitud
de todos los contenidos didácticos. Los circuitos y los textos se conservan.



## Revisión del 23/10/2026 · a qué tema pertenece cada material

Mismo cambio que en 0221 (PR #7 de ese repositorio), adaptado a los subtemas de este
módulo. Todo lo genera `scripts/actualizar_aula.py`:

- **Migas de pan** en todas las páginas de `temas/`: «Inicio › Tema 2 · Procesadores de
  texto… › 2.3 Tablas, imágenes y elementos gráficos». El apartado sale del enlace
  actual de la barra `.subnav` o, en subtemas y subpáginas, del `<h1>`
  («Tema 2.3 — Tablas…» → «2.3 Tablas…»).
- **Índice lateral** con la tarjeta del tema y «Todo el material del tema N»
  (`recursos.html?tema=N`).
- **Catálogo** con la etiqueta «Tema N» y su título en cada material, ordenado por tema y
  con **filtro por tema** combinable con el de tipo y la búsqueda. «Cómo se califica el
  módulo» lleva la etiqueta «Todo el módulo».
- Las páginas sin prefijo `utNN` se asignan a su tema en `TEMA_DE_PAGINA`
  (`laboratorio-imagen.html` → 3, `mapa-cinta.html` → 2). Al crear otra página así,
  añadirla allí.
- Las etiquetas de criterio (`<span class="ce">`) no aparecen en índices ni catálogo.

`assets/aula.js` vuelve a ser idéntico al de 0221. A `assets/aula.css` se le añade al
final el bloque «Tema de cada página…» del de 0221; el resto del archivo de 0223 no
cambia.


## Regla del 29/10/2026 · recuadro «Entrega» en boletines y prácticas

Todo boletín de ejercicios y toda práctica termina **cada bloque** con un recuadro
para el alumnado que dice qué se entrega y cómo debe quedar. Se aplica a las páginas
nuevas y a las existentes cuando se revisen.

```html
<section class="entrega" aria-labelledby="entrega-2-3">
  <h3 id="entrega-2-3">Qué entregas del bloque 2.3</h3>
  <p class="entrega-sub">Una línea con lo que se entrega.</p>
  <ul class="entrega-archivos"><li>cv_v3.docx</li></ul>
  <h4>Comprueba antes de entregar</h4>
  <ul class="entrega-lista"><li>…</li></ul>
  <h4>Cómo debe quedar</h4>
  <div class="entrega-ejemplos">
    <figure class="bien">…maqueta…<figcaption>…</figcaption></figure>
    <figure class="mal">…<figcaption>…</figcaption></figure>
  </div>
  <p class="entrega-ojo"><strong>Fallo más común:</strong> …</p>
</section>
```

- Va **dentro** del `<section>` del bloque, justo antes de su cierre, con un `id`
  `entrega-N-M` propio (el generador solo numera los `<h2>`).
- **Archivos**: nombres exactos, con la carpeta si importa. Si un archivo no queda
  en la carpeta de trabajo (por ejemplo, las plantillas de Word), se dice dónde está
  y que hay que copiarlo.
- **Comprueba antes de entregar**: comprobaciones que el alumno pueda hacer solo, en
  segunda persona, con la ruta de menú cuando haga falta.
- **Cómo debe quedar**: maquetas en HTML/CSS o SVG (`.hoja`, `.panel-word`,
  `.codigo-vba`, `.capas-gimp`, `.paleta`, `.arbol`), o capturas reales. `bien` y
  `mal` añaden la etiqueta ✓/✗; `entrega-ancho` ocupa toda la fila.
- **Se muestra el resultado completo**, incluidos valores calculados, recuentos y
  respuestas modelo. Los solucionarios detallados para el profesor (valores medidos,
  pruebas de estrés, criterios de corrección) siguen en `temario/soluciones/`.
- Los estilos están al final de `assets/aula.css`, en el bloque «Recuadro Entrega».
  Es compartido: cualquier cambio se replica en el otro repositorio.

### Nombres de los archivos de entrega

El recuadro da el **nombre exacto** de cada archivo según las normas de entrega del
módulo (`<usuario>` es el usuario del alumno):

| Qué se entrega | Nombre |
|---|---|
| Práctica en PDF | `<usuario>_pNN.pdf` (tema y número de práctica: `sbarrosor02_p01.pdf`) |
| Práctica en ZIP | `<usuario>_pNN.zip`, con `<usuario>_pNN.pdf` en la raíz si se pide memoria |
| Bloque de un boletín | `<usuario>_E<tema><bloque>.zip` (`sbarrosor02_E23.zip`), con la memoria `<usuario>_E23.pdf` en la raíz |
| Ejercicio de los apuntes | `<usuario>_ENN.pdf` |
| Archivo de una actividad dentro del ZIP | `<usuario>_aNN.<ext>`; NN es el número del ejercicio o actividad dentro del bloque o práctica |
| Varios archivos de una actividad con la misma extensión | `<usuario>_a01_1.jpg`, `<usuario>_a01_2.jpg`… |
| Entrega en grupo | `<usuario1>_<usuario2>_pNN.<ext>`; todos los integrantes la suben |

- Si un archivo recoge varios ejercicios, lleva el número del último ejercicio
  obligatorio que lo modifica.
- En una entrega individual de una actividad por parejas (como el bloque 2.6 de 0223),
  cada alumno sube su ZIP con su usuario.
- La memoria cumple las normas de presentación: portada, índice con hiperenlaces,
  páginas numeradas, enunciado en negrita y respuesta en normal, `Figura N: …`,
  comandos en texto monoespaciado, trabajo a mano fotografiado, sin faltas y capturas
  de pantalla completa con fecha y nombre del archivo.
- El recuadro incluye una tabla «En tu carpeta → Nombre dentro del ZIP» y la lista de
  capturas que no pueden faltar en la memoria. Los boletines llevan además, antes del
  primer bloque, un apartado «Cómo se entrega cada bloque» con estas normas.

### Numeración de las prácticas de 0223

| Tema | Práctica | Código |
|---|---|---|
| 1 | P1.1 a P1.6 | `p11` a `p16` |
| 2 | PC1 · PC2 · Carta del restaurante · PC3 · Taller T1–T5 · Práctica colaborativa | `p21` · `p22` · `p23` · `p24` · `p25` (T1–T5 son `a01`–`a05`) · `p26` (grupo) |
| 3 | Prácticas de cada subtema (P3.1.x … P3.6.x) · Práctica guiada de GIMP · Punto de control | `p31` a `p36`; cada P3.x.y es la actividad `a0y` · `p37` · `p38` (sin memoria: los XCF son la evidencia) |

Las prácticas ya entregadas el 29/10/2026 (Tema 1, PC1, carta y taller) conservan los
nombres con los que se entregaron; el código queda reservado. Las prácticas con
memoria (las del Tema 3) llevan `<usuario>_pNN.pdf` en la raíz del ZIP; PC2 y PC3 no
llevan memoria porque el propio documento es la evidencia.

### Imágenes del resultado esperado

Las imágenes de `web/assets/img/entregas/` se generan con
`python scripts/generar_resultados_esperados.py` a partir del mismo material
inventado que se da al alumnado (fotos de retoque, documento fotografiado y capas).
Si se regenera ese material, hay que volver a ejecutar este script.

## Revisión del 24/11/2026 · una página por tema y cinco secciones (como 0221)

Motivo: igual que en 0221, la portada y las páginas de tema acumulaban accesos
(«Estudiar / Practicar / Entregar», listas de subtemas, recursos de consulta) y la
barra del tema era distinta en cada tema. Se aplica la organización de 0221 del
18/11/2026.

- **Portada del módulo:** solo las tarjetas de los temas, con accesos a sus secciones
  y a la teoría en PDF, y debajo el enlace a la calificación.
- **Barra superior:** «Temas» y «Buscar material», como en 0221.
- **Página del tema (`utNN.html`):** secciones con color e icono propios: Teoría
  (azul), Ejercicios (verde), Prácticas (naranja), Preparar el examen (morado) y En
  clase (rojo). Debajo, plegados, «Cómo se califica este tema» y «Qué se evalúa y cómo
  se organiza el tema» (RA, criterios y, en el tema 3, los programas).
- **Teoría:** los subtemas (Tema 2.0 a 2.7, 3.1 a 3.6). El mapa de la cinta va en la
  Teoría del tema 2 como «Consulta» y no entra en el PDF.
- **Ejercicios:** cada bloque es su página (`ut02-bloque-0.html` a `ut02-bloque-7.html`,
  `ut03-bloque-1.html` a `ut03-bloque-6.html`). `utNN-ejercicios.html` queda como
  índice con «Cómo se entrega cada bloque» y redirige los enlaces antiguos con ancla
  (`ut02-ejercicios.html#apartado-bloque-2-3-…` → `ut02-bloque-3.html#…`), así que los
  enlaces de Moodle siguen funcionando. El laboratorio de imagen va en Ejercicios del
  tema 3, en el grupo «Herramientas interactivas» (`"grupo": "interactivo"`).
- **Tema 1:** la teoría pasa a `ut01-teoria.html` y `ut01.html` es la portada; los
  enlaces antiguos `ut01.html#apartado-…` se redirigen a la teoría.
- **Prácticas:** PC1–PC3, caso práctico y taller (tema 2); prácticas de cada subtema
  (enlace a su apartado), práctica guiada de GIMP y punto de control (tema 3).
- **Preparar el examen (`utNN-examen.html`):** el examen de repaso con su autocorrector
  y las autocomprobaciones de cada subtema.
- **En clase:** el reto del documento saboteado y la práctica colaborativa (tema 2).
- **Anterior / siguiente:** al pie de cada página, en el orden de las secciones.
- **Teoría en PDF:** `python scripts/generar_pdf_teoria.py [N]` (necesita `playwright`
  y `pypdf`). Reduce las fotos a 1200 px en JPG para que pese poco. Hay que
  regenerarlo cuando cambia la teoría: `actualizar_aula.py` avisa («AVISO: la teoría
  del tema N ha cambiado…») comparando con `web/descargas/teoria/huellas.json`.
- **Estilos:** `assets/organizacion.css`, igual que el de 0221 (si cambias uno, cambia
  el otro). No se han tocado `estilo.css`, `aula.css` ni `aula.js`.
- La migración se hizo una vez con `scripts/migrar_organizacion.py` (se conserva como
  registro; no hay que volver a ejecutarlo).

### Dónde va cada material nuevo

Añádelo en `temas.json` → tema → `secciones` → `teoria`, `ejercicios`, `practicas`,
`examen` o `enclase` (`etiqueta`, `titulo`, `url`, `texto`) y ejecuta
`python scripts/actualizar_aula.py`: crea la tarjeta, la barra del tema, el índice de
la sección, las migas y el «anterior / siguiente». Un bloque nuevo de ejercicios es
una página `utNN-bloque-K.html`.
