---
modulo: "0223"
ut: "3.6"
titulo: "Publicar en web, redes e impresión"
ra: "RA5"
ce: ["f"]
horas: 3
evaluacion: 1
estado: publicado
actualizado: 2026-11-19
---

# UT3.6 — Publicar en web, redes e impresión

Página: `web/temas/ut03-6.html`. Herramienta: apartado 9 del laboratorio
(calculadora de tamaños: Instagram, YouTube, X e impresión A5/A4/A3/10 × 15 a
300 ppp con 3 mm de sangrado; recorta la imagen del alumno a la proporción,
dibuja la zona segura, el corte y los elementos que tapan la imagen, avisa si
habría que ampliar y descarga el recorte en JPG).

## Material

- `web/descargas/plantilla-web-proyecto.zip`, generado con
  `python scripts/generar_plantilla_web.py`: `index.html` comentado paso a
  paso (logotipo, imagen principal, galería de tres, créditos con licencia),
  `estilo.css` adaptable al móvil, `favicon.ico` provisional, huecos SVG que
  dicen la imagen y el tamaño de cada sitio y `LEEME.txt`.
- Se reutiliza el material del 3.5: `exportar-foto.jpg` y
  `exportar-logo-transparente.png`.
- Resultados esperados (`p36-web.jpg`, `p36-redes.jpg`, `p36-cartel.jpg`) con
  `scripts/generar_resultados_esperados.py`; `p36-web.jpg` necesita Playwright
  (rellena la plantilla y la fotografía a 1280 y 390 px).

## Guion (3 sesiones de 1 h)

1. Qué pide cada medio (tabla web / redes / impresión). La web: `src`, `alt`,
   `width`, `height`, `loading="lazy"`, favicon; rellenar la plantilla, peso con
   F12 > Red, modo móvil. P3.6.1 (sin la parte de la licencia).
2. Redes: tamaños de noviembre de 2026, recortes del perfil, zona segura con
   guías en GIMP, recompresión, metadatos y texto alternativo. Laboratorio,
   apartado 9. P3.6.2.
3. Impresión: 300 ppp, RGB/CMYK y prueba de color, sangrado de 3 mm y zona
   segura de 5 mm, guías, exportar PDF; impresora de oficina. Derechos y
   licencias CC, dónde buscar, cómo citar, derecho a la propia imagen,
   metadatos de autor y marca de agua. P3.6.3 y licencia de la P3.6.1. Bloque
   3.6 de los ejercicios.

## Prácticas (CE f) · entrega `<usuario>_p36.zip`

- **P3.6.1** La plantilla web rellena con las exportaciones del 3.5 y una foto
  CC BY o CC0 citada; `alt`, `width`, `height`; peso < 1 MB; capturas en
  ordenador y móvil. Se entrega como carpeta `<usuario>_a01/` (excepción a la
  norma de nombres: dentro no se renombra nada).
- **P3.6.2** Publicación 1080 × 1350, historia 1080 × 1920 y banner de YouTube
  2560 × 1440 con el texto en la zona segura.
- **P3.6.3** Flyer A5 con sangrado (1819 × 2551 px a 300 ppp), guías, metadatos
  de autor, PDF y versión de 1080 px para redes.

Valores de referencia y criterios:
`temario/soluciones/ut03-6-publicar-web-redes-impresion-solucion.md`.

## Ejercicios guiados · bloque 3.6 (entrega `<usuario>_E36.zip`)

La web del proyecto con su kit, el cartel A3 con sangrado (3579 × 5031 px) y
su versión 1080 × 1350, el banner (YouTube o cabecera de X) y una historia, y
la tabla de licencias de la ficha con la licencia elegida para su trabajo.

## Avisos para el profesor

- Los tamaños de redes cambian: se dan como «recomendados en noviembre de
  2026» en la página y en el laboratorio. Revisarlos cada curso.
- Instagram muestra el perfil en 3:4 desde 2025; por eso se recomienda 4:5 o
  3:4 frente al cuadrado.
- Menús de GIMP 3 en español (guías, editor de metadatos, prueba de color);
  pendiente de confirmar la versión del aula. El editor de metadatos guarda el
  autor en XMP (y Exif); al exportar hay que dejar XMP marcado.
- Edad para el consentimiento de imagen: se simplifica a «menor de 14 años, el
  de su familia» (LOPDGDD, art. 7) para el contexto escolar.
- La carpeta de la web va dentro del ZIP sin renombrar sus archivos: si se
  renombran, la página deja de encontrar las imágenes.
