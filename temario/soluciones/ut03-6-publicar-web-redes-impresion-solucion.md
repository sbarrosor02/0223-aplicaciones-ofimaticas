# Solucionario · UT3.6 Publicar en web, redes e impresión

No se publica en la web del alumnado. Pesos medidos con Pillow sobre el material
del 3.5 (`exportar-foto.jpg`, `exportar-logo-transparente.png`); en GIMP pueden
variar ±20 %.

## P3.6.1 · Una página web con tus imágenes

| Comprobación | Esperado |
|---|---|
| Abre con doble clic | Se ven el logotipo, la portada, las dos fotos/miniatura y el icono en la pestaña |
| `alt` | Una frase por imagen que describe lo que se ve; ningún `alt=""`, «imagen» ni nombre de archivo |
| `width` / `height` | Los píxeles reales del archivo (p. ej. 1200 / 1200 en la portada WebP) |
| Peso total (F12 > Red) | ≈ 250–350 KB con el material del 3.5 (portada WebP ≈ 60 KB, fotos ≈ 50 KB, miniatura JPG ≈ 90 KB). Más de 1 MB = alguna imagen sin escalar |
| Modo móvil | La galería pasa a una columna; no hay desplazamiento horizontal |
| Créditos | Título, autor, licencia (con enlace) y fuente de la foto CC; resto de imágenes atribuidas al alumno |
| Captura de la licencia | La ficha de Openverse o Wikimedia Commons con la licencia visible, y coincide con la citada |

Errores típicos: rutas con mayúsculas o espacios distintos del archivo real
(la imagen no carga), dejar los SVG provisionales, `width`/`height` copiados
de la plantilla aunque la imagen sea otra (se deforma), foto con licencia NC
o ND usada recortada y con texto.

## P3.6.2 · Una foto, tres redes

| Pieza | Píxeles | Zona segura (guías) | Peso JPG 85 |
|---|---|---|---|
| Publicación Instagram | 1080 × 1350 | La imagen entera (en el perfil se ve 3:4: recorta 45 px arriba y abajo) | ≈ 200 KB |
| Historia | 1080 × 1920 | Horizontales en 250 y 1670 | ≈ 300 KB |
| Banner YouTube | 2560 × 1440 | Verticales en 507 y 2053, horizontales en 508 y 931 | ≈ 500 KB |

Penalizar: proporciones distintas (la red recorta), texto fuera de la zona
segura (en la historia, pegado arriba o abajo; en el banner, fuera de la franja
central), logotipo con fondo blanco (exportó el logotipo en JPG o aplanó con
fondo antes de colocarlo).

## P3.6.3 · Flyer A5 para la imprenta

| Comprobación | Esperado |
|---|---|
| Lienzo | 1819 × 2551 px, 300 ppp (154 × 216 mm) |
| Guías de corte | Verticales 35 y 1784; horizontales 35 y 2516 |
| Guías de zona segura | Verticales 94 y 1725; horizontales 94 y 2457 |
| Fondo | Llega a los cuatro bordes del archivo (sin filo blanco al cortar) |
| Textos | Todos dentro de la zona segura; los cuatro textos pedidos sin faltas |
| PDF | Propiedades del documento en el navegador: 154 × 216 mm (6,06 × 8,5 in) |
| Metadatos | Autor y copyright en el editor de metadatos; XMP marcado al exportar |
| Versión para redes | 1080 × 1515 px (o recortada a 1080 × 1350), ≈ 140 KB en JPG 85, menos de 500 KB |

Fallo más común: lienzo de 1748 × 2480 (A5 sin sangrado) o texto pegado al
borde. Otro frecuente: crear el lienzo en mm a 72 ppp (420 × 595 px) y
cambiar luego a 300 ppp sin remuestrear: los píxeles no cambian.

## Autocomprobación (apartado 7)

| Pregunta | Correcta |
|---|---|
| 1 | c |
| 2 | a |
| 3 | d |
| 4 | b |
| 5 | a |
| 6 | c |
| 7 | b |
| 8 | d |

## Bloque 3.6 de los ejercicios (formativo)

- Cartel A3 con sangrado: 3579 × 5031 px a 300 ppp; guías de corte en 35 / 3544
  y 35 / 4996; zona segura en 94 / 3485 y 94 / 4937. PDF de 303 × 426 mm.
- Versión del cartel para redes: 1080 × 1350.
- Banner: 2560 × 1440 (YouTube) o 1500 × 500 (X); historia 1080 × 1920.
- Tabla de licencias: una fila por imagen o tipografía ajena; ninguna NC en
  piezas comerciales ni ND modificada. Licencia propia en los créditos de la web.
