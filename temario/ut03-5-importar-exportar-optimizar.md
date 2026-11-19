---
modulo: "0223"
ut: "3.5"
titulo: "Importar, exportar y optimizar"
ra: "RA5"
ce: ["e"]
horas: 4
evaluacion: 1
estado: publicado
actualizado: 2026-11-19
---

# UT3.5 — Importar, exportar y optimizar

Página: `web/temas/ut03-5.html`. Herramienta: apartado 8 del laboratorio
(conversor y optimizador de varias imágenes: lado máximo, formato JPG/WebP/PNG,
calidad, fondo para la transparencia, tabla de pesos y descarga en ZIP, todo
en el navegador y sin metadatos).

## Material

Generado con `python scripts/generar_material_exportar.py` (inventado; el PDF
se escribe a mano para que sea vectorial de verdad):

| Archivo | Para |
|---|---|
| `importar-cartel.pdf` | Abrir un PDF A5 a 72 y 300 ppp (420 × 595 y 1748 × 2480 px) |
| `importar-logo.svg` | Abrir un vectorial al tamaño final |
| `importar-logo-pequeno.png` | El mismo logo a 120 px: ampliarlo pixela |
| `exportar-logo-transparente.png` | Transparencia en PNG/JPG, modo indexado e ICO |
| `exportar-foto.jpg` | Pesos por formato y por destino (paisaje del 3.3, 2400 × 1600) |

Imágenes del resultado esperado (`p35-importar.png`, `p35-transparencia.png`)
con `scripts/generar_resultados_esperados.py`; `p35-cartel.png` la crea el
script de material si está `pdftoppm`.

## Guion (4 sesiones de 1 h)

1. Guardar / Exportar como / Exportar a / Sobrescribir. Importar PDF, SVG, PSD,
   HEIC y portapapeles. P3.5.1 (partes 1 y 2).
2. Opciones de exportación: JPG (calidad, vista previa con peso, progresivo,
   submuestreo, metadatos), PNG (sin pérdida, indexado), WebP, GIF, ICO, PDF,
   TIFF. P3.5.2 y P3.5.3.
3. Optimizar: píxeles, formato, calidad, metadatos; tabla de destinos; nombres
   de archivo. Laboratorio, apartado 8. P3.5.4.
4. Imágenes en documentos: incrustar, vincular, comprimir en Word. P3.5.1
   (parte 3). Bloque 3.5 de los ejercicios (exportar el kit).

## Prácticas (CE e) · entrega `<usuario>_p35.zip`

- **P3.5.1** Importar PDF a 72/300 ppp; SVG frente a PNG pequeño a 2000 px;
  foto en Word sin comprimir y comprimida a 150 ppp.
- **P3.5.2** Foto a 1200 × 800 en JPG 90, JPG 60, PNG y WebP 80.
- **P3.5.3** Logotipo en JPG y PNG, PNG indexado a 64 colores y favicon ICO.
- **P3.5.4** Miniatura, foto web, post y copia para imprimir con pesos máximos
  y sin metadatos.

Valores de referencia y criterios: `temario/soluciones/ut03-5-importar-exportar-optimizar-solucion.md`.

## Avisos para el profesor

- Menús de GIMP 3 en español; pendiente de confirmar la versión del aula. En
  GIMP 2.10, algunas casillas del cuadro de exportar JPG cambian de nombre.
- HEIC: depende de que la instalación de GIMP tenga el soporte.
- Los pesos son medidos con Pillow (libjpeg, libwebp, zlib): en GIMP pueden
  variar un ±20 %. Se dan como «≈» en la página.
