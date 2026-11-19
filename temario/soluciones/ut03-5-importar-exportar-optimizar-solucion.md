# Solucionario · UT3.5 Importar, exportar y optimizar

No se publica en la web del alumnado. Pesos medidos con Pillow sobre el material
de `scripts/generar_material_exportar.py`; en GIMP pueden variar ±20 %.

## P3.5.1 · Importar

| Qué | Resultado |
|---|---|
| Cartel A5 (148 × 210 mm) a 72 ppp | 420 × 595 px |
| A 150 ppp | 874 × 1240 px |
| A 300 ppp | 1748 × 2480 px |
| Logo SVG abierto a 2000 × 2000 | Bordes nítidos |
| Logo PNG de 120 px escalado a 2000 | Bordes escalonados (Ninguna/Lineal) o borrosos (Cúbica/NoHalo) |

Explicación esperada: el SVG se dibuja a partir de formas y se convierte en
píxeles al abrirlo, al tamaño pedido; el PNG solo tiene 120 × 120 píxeles y al
ampliarlo GIMP se los inventa (interpolación).

Word: `exportar-foto.jpg` pesa 1,27 MB; con «No comprimir las imágenes del
archivo» el `.docx` queda algo por encima (≈ 1,3 MB). A 16 cm de ancho y
150 ppp la imagen pasa a unos 945 px: el `.docx` baja a ≈ 0,1–0,2 MB. Si
olvidan marcar «No comprimir», Word ya habrá reducido a 220 ppp al guardar y
la diferencia será menor (es una buena pregunta de clase).

## P3.5.2 · Foto a 1200 × 800

| Formato | Peso |
|---|---|
| JPG 90 | ≈ 157 KB |
| JPG 60 | ≈ 61 KB |
| PNG | ≈ 1,2 MB |
| WebP 80 | ≈ 50 KB |

A 2400 × 1600 (por si no escalan): JPG 90 ≈ 948 KB, JPG 80 ≈ 408 KB,
JPG 60 ≈ 207 KB, WebP 80 ≈ 260 KB, PNG ≈ 5,2 MB, TIFF LZW ≈ 8 MB.
La foto lleva grano a propósito: por eso PNG/TIFF pesan tanto.

Respuesta esperada: WebP 80 (o JPG 75–85). La JPG 60 muestra bloques y halos
en el cielo y el agua al 200 %. PNG no tiene sentido para una foto.

## P3.5.3 · Logotipo

| Salida | Peso | Observación |
|---|---|---|
| PNG RGBA 1000 × 1000 | ≈ 15 KB | Transparente |
| PNG indexado 64 colores | ≈ 7 KB | Transparente, bordes algo más duros |
| JPG 90 | ≈ 59 KB | Fondo blanco (color de fondo de GIMP), pesa MÁS que el PNG |
| WebP sin pérdida | ≈ 6 KB | (por si lo prueban) |
| ICO 16/32/48 | Pocos KB | Tres capas al abrirlo en GIMP |

Errores típicos: ICO con una sola capa; indexar el XCF original en vez de una
copia; JPG «transparente» (no existe).

## P3.5.4 · Destinos (calidad 80 salvo TIFF)

| Archivo | Píxeles | Peso | Límite |
|---|---|---|---|
| miniatura JPG | 1280 × 720 | ≈ 88 KB | < 200 KB |
| web WebP | 1200 × 800 | ≈ 50 KB | < 100 KB |
| post JPG | 1080 × 1080 | ≈ 114 KB | < 150 KB |
| imprimir TIFF LZW | 1772 × 1181 | ≈ 4,6 MB | — |

Comprobar: proporciones recortadas (16:9, 1:1, 3:2) antes de escalar, sin
deformar; sin Exif (visor del laboratorio, apartado 5); nombres sin espacios,
tildes ni eñes.
