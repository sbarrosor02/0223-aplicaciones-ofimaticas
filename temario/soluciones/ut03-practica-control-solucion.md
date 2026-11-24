# Solucionario · Práctica guiada de GIMP (p37) y punto de control del Tema 3 (p38)

No se publica en la web del alumnado. Los valores salen de cómo se estropeó el
material en `scripts/generar_material_gimp.py`.

## p37 · Práctica guiada (valores esperados)

| Paso | Valor de referencia | Margen aceptable |
|---|---|---|
| 2 · Medir | 3,0° | 2,5–3,5° |
| 3 · Recorte 3:2 | ≈ 2200 × 1467 px | 2150–2250 de ancho, sin transparencias |
| 4 · Niveles (Valor) | 5 · 1,50 · 145 | negro 0–12, gamma 1,3–1,7, blanco 135–155 |
| 5 · Por canal (si no usan el cuentagotas) | R 5–145, G 4–122, B 3–87 (gamma 1,5) | — |
| 6 · Limpieza | letrero + cable + 10 motas | ninguna visible al 100 % |
| 8 · Lienzo | 1819 × 2551, 300 ppp, 154 × 216 mm | exacto |
| 9 · Foto | 1819 × ≈ 1213, en (0, 0), máscara con degradado | — |
| 10 · Guitarra | ≈ 584 × 1000 tras escalar | sin halo de pared |
| 11 · Textura | 3401 × 2551, X −791, Multiplicar 60 % | 50–70 % |
| 14 · PDF | 154 × 216 mm | exacto |
| 15 · Redes | 1080 × 1350, < 500 KB | exacto |

Errores típicos: degradado pintado en la capa y no en la máscara; selección
difusa que deja la sombra de la pared pegada a la guitarra; textura en Normal;
recorte de redes sin sangrado pero cortando la franja de datos (si colocaron la
franja más abajo que en la guía).

## p38 · Punto de control (guía de corrección)

### Parte A · `a01.jpg` / `a01.xcf`

| Comprobación | Cómo se mira | Referencia |
|---|---|---|
| Recta | Borde de la mesa horizontal | Giro de ≈ 2° (el material está a −2°) |
| 16:9 y tamaño | Propiedades de la imagen | 1920 × 1080 exacto |
| Luz | Histograma en GIMP | Antes: valores entre ≈ 46 y 220; después, de 0 a 255 sin pico en los bordes |
| Dominante | Cuentagotas sobre un panel de la pared | R ≈ G ≈ B (diferencia < 10). Valores de entrada por canal: R 46–161, G 53–185, B 63–220 |
| Limpieza | Al 100 % | Sin lata roja ni las 12 motas de los paneles; sin repeticiones visibles |
| Exif | Propiedades del archivo / laboratorio, apartado 5 | Sin datos Exif |
| XCF | Diálogo Capas | Original oculto debajo |

### Parte B · `a02.xcf` / `a02.pdf`

| Comprobación | Referencia |
|---|---|
| Lienzo | 2551 × 3579 px, 300 ppp (216 × 303 mm) |
| Guías | Verticales 35, 94, 2457, 2516; horizontales 35, 94, 3485, 3544 |
| Capas | fondo, foto (con máscara), luces (Pantalla), auriculares, logo y 4 textos, todas con nombre |
| Recorte | Sin filo gris claro alrededor de los auriculares al 100 %; ancho ≥ 1200 px; sombra arrojada |
| Logotipo | Capa de 600 × 600 abierta desde el SVG (bordes nítidos al 100 %). Si está pixelado, se abrió pequeño y se amplió: 0 en ese punto |
| Textos | Literales: «JERTE GAMING CUP», «Torneo de videojuegos del IES Valle del Jerte», «Viernes 19 de febrero · 16:30 · Salón de actos», «Inscripciones en la biblioteca hasta el 12 de febrero». Título ≥ 150 px. Máximo dos familias tipográficas |
| Zona segura | Ninguna capa de texto ni el logo cruza x < 94, x > 2457, y < 94, y > 3485 (se ve con las guías o con el borde amarillo de cada capa) |
| Metadatos | Imagen > Metadatos > Ver metadatos: autor y copyright |
| PDF | Una página de 216 × 303 mm |

### Parte C · `a03.jpg` / `a03.xcf`

| Comprobación | Referencia |
|---|---|
| Tamaño | 1280 × 720 exacto |
| Esquina | Nada importante en el rectángulo inferior derecho (≈ 1150–1280 × 650–720) |
| Legibilidad | «LA FINAL» se lee con la imagen reducida a 320 × 180 |
| Peso | < 2 MB (con JPG 85 sale entre 150 y 400 KB) |

### Casos dudosos

- Composición distinta del ejemplo: correcto si cumple el pliego.
- Luces en Normal con opacidad baja: 0 en «Pantalla» aunque se vea parecido.
- Textos rasterizados (se pintó encima): pierden el punto de «textos editables».
- Foto escalada sin recortar a 16:9 (deformada): 0 en «recta y 16:9».
