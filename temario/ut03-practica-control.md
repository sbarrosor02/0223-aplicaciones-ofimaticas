---
modulo: "0223"
tipo: "práctica de control"
codigo: "p38"
titulo: "Punto de control del Tema 3: Jerte Gaming Cup"
ra: "RA5"
ce: ["c", "d", "e", "f"]
integra: ["3.1", "3.3", "3.4", "3.5", "3.6"]
horas: 3
evaluable: true
estado: publicado
actualizado: 2026-11-24
---

# Punto de control del Tema 3 (p38)

Página: `web/temas/ut03-practica-control.html`. Se hace después de la práctica
guiada (p37): mismo recorrido, otro encargo y otro material, sin guía.

## Qué es (y qué no)

- **No** es la guiada con otros nombres: no dice qué herramienta usar ni dónde
  está cada opción.
- **Sí** es un pliego cerrado con valores exactos (tamaños, ppp, capas, textos,
  zona segura, formatos) para que la corrección sea objetiva, como en las PC del
  Tema 2.
- Los ejemplos de la página muestran un resultado que cumple; la composición es
  libre, los valores no.

## Material

`web/descargas/gimp-control-material.zip` (`scripts/generar_material_gimp.py`):

| Archivo | Qué es |
|---|---|
| `pc-sala.jpg` | Sala de un torneo inventada, 2400 × 1600: girada −2°, lavada (`0,22 + 0,55·x`), dominante azul (× 0,82 / 0,94 / 1,12), 12 motas en los paneles y una lata roja en la mesa |
| `pc-auriculares.jpg` | Auriculares sobre fondo gris claro con sombra, 2000 × 1500 |
| `pc-luces.jpg` | Luces desenfocadas sobre negro, 2000 × 1500 (para Pantalla) |
| `pc-logo.svg` | Logotipo vectorial del torneo |

## Encargo

- **A** · Foto retocada: recta, 16:9, 1920 × 1080, luz, sin dominante, sin lata ni
  motas, enfocada, JPG 85 sin Exif.
- **B** · Cartel A4 con sangrado: 2551 × 3579 px a 300 ppp, guías 35 y 94, capas
  fondo / foto con máscara en degradado / luces en Pantalla / auriculares
  recortados (≥ 1200 px de ancho, con sombra) / logo importado del SVG a 600 × 600
  / cuatro textos exactos (título ≥ 150 px, máximo dos tipografías), todo en la
  zona segura; metadatos de autor; PDF de una página.
- **C** · Miniatura 1280 × 720 con LA FINAL, auriculares y logotipo, sin nada en
  la esquina inferior derecha; JPG 85 < 2 MB.

## Rúbrica (10 puntos, por CE)

| CE | Puntos | Qué se comprueba |
|---|---|---|
| d | 5,0 | Foto: recta y 16:9 (0,5), luz (0,5), sin dominante (0,5), limpia (0,5). Composición: recorte sin halo con sombra (1,0), máscara en degradado (0,5), Pantalla (0,5), textos (0,5), capas con nombre y textos editables (0,5) |
| c | 1,5 | Cartel 2551 × 3579 a 300 ppp (0,5), foto 1920 × 1080 (0,5), miniatura 1280 × 720 (0,5) |
| e | 1,5 | Logotipo importado del SVG a 600 nítido (0,5), PDF de una página y JPG 85 sin Exif (0,5), entrega con nombres (0,5) |
| f | 2,0 | Sangrado y zona segura (1,0), miniatura legible y sin nada en la esquina (0,5), metadatos de autor (0,5) |

## Entrega `<usuario>_p38.zip`

Sin memoria: `a01.xcf` + `a01.jpg`, `a02.xcf` + `a02.pdf`, `a03.xcf` + `a03.jpg`.

Guía de corrección con los valores de referencia:
`temario/soluciones/ut03-practica-control-solucion.md`.

## Avisos para el profesor

- Con la guiada, el tema suma 32 sesiones (26 de subtemas + 3 + 3); la
  programación da 28 al Tema 3. Hay que absorber 4 sesiones o ajustar la
  programación.
- Falta decidir si durante el punto de control pueden consultar los apuntes y su
  práctica guiada; la página no dice nada.
- Los instrumentos de calificación del tema siguen pendientes: cuando se
  definan, el punto de control irá en «casos prácticos» de `temas.json`.
