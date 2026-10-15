---
modulo: "0223"
ut: "2-reto"
titulo: "Solucionario · Reto en equipo: el documento saboteado"
documento: "web/descargas/reto-documento-saboteado.docx"
generador: "scripts/generar_saboteado.js"
actualizado: 2026-10-15
---

# Solucionario · El documento saboteado

Uso exclusivo del profesor. No se enlaza desde la web. Si se modifica
`scripts/generar_saboteado.js`, revisar esta lista.

El documento no tiene **ningún** párrafo con estilo: todo es *Normal* con
formato directo. Por eso las trampas 1 y 2 están encadenadas: sin títulos reales
no hay índice ni panel de navegación.

Tema del documento: bases de un torneo de EA Sports FC (PEGI 3) en los recreos,
escritas por «el capitán eliminado». Los datos del torneo son inventados.

## Los 15 sabotajes

| N.º | Dónde | Trampa | Cómo se descubre | Arreglo correcto | Subtema |
|---|---|---|---|---|---|
| 1 | Los cuatro apartados y el 3.1 | Títulos falsos: *Normal* con negrita, 16 pt (13 pt el 3.1), azul y Calibri Light, imitando Título 1 y Título 2 | Panel de navegación vacío; el panel Estilos marca *Normal* | Aplicar **Título 1** a los apartados y **Título 2** al 3.1 | 2.2 |
| 2 | Portada | Índice escrito a mano con tabulación de relleno de puntos. Páginas inventadas, un título que no coincide («Cómo apuntarse» frente a «Inscripción y material») y falta el 3.1 | Al hacer clic no se sombrea en gris (no es un campo); no coincide con el texto | Borrarlo e insertar **Referencias › Tabla de contenido** (exige la 1) | 2.4 |
| 3 | Normas | Numeración escrita a mano; salta del 2 al 4 | ¶: el número es texto, se puede seleccionar | Quitar los números y aplicar **Numeración** automática | 2.2 |
| 4 | Inscripción, «La organización pone» | Viñetas falsas: guion y dos espacios | ¶ muestra el guion y los puntos de espacio | Quitar los guiones y aplicar **Viñetas** | 2.2 |
| 5 | Calendario | Tabla simulada con espacios; ya está desalineada en pantalla | ¶ muestra filas de puntos entre columnas | **Insertar › Tabla** 3 × 6 (ronda, día, partidos) (o reemplazar espacios por tabulaciones y *Convertir texto en tabla*) | 2.3 |
| 6 | Final de la portada | 24 párrafos vacíos para empujar «1. Normas del torneo» a la página siguiente | ¶ muestra la columna de marcas vacías | Borrarlos e insertar **salto de página** (<kbd>Ctrl</kbd>+<kbd>Intro</kbd>) o activar *Salto de página anterior* | 2.2 |
| 7 | Pie de página | «Página 1» escrito a mano: sale igual en las tres páginas | Mirar el pie de la página 2 o 3 | **Insertar › Número de página › Posición actual** (campo) | 2.2 |
| 8 | Dos párrafos de «Normas» | Sangría de primera línea hecha con ocho espacios | ¶ muestra los puntos al inicio | Quitar espacios y poner **sangría especial › Primera línea** en *Párrafo* | 2.2 |
| 9 | Primer párrafo de «Inscripción» | Saltos de línea manuales (<kbd>Mayús</kbd>+<kbd>Intro</kbd>) que cortan el párrafo | ¶ muestra la flecha ↵ | Buscar `^l` y reemplazar por un espacio | 2.0 / 2.1 |
| 10 | «mundo␣␣pueda», «cumpla␣␣quedará», «pierde␣␣el» | Dobles espacios | ¶ | **Buscar y reemplazar** dos espacios por uno | 2.1 |
| 11 | Bajo el calendario | Título de tabla escrito a mano y referencia rota: el texto dice «Tabla 2» y solo hay una | El título no se actualiza; no aparece en *Tabla de ilustraciones* | **Referencias › Insertar título** y **Referencia cruzada** al título | 2.4 |
| 12 | Párrafo «Recuerda que los mandos son de todos…» | Formato pegado de la web: Times New Roman 12,5 pt con sombreado gris | Se ve distinto; *Mostrar formato* (<kbd>Mayús</kbd>+<kbd>F1</kbd>) | **Borrar todo el formato** y dejarlo en *Normal* | 2.0 / 2.2 |
| 13 | «modo Saque inicial¹» y la línea final «¹ Partido rápido…» | Nota al pie falsa: superíndice a mano y la «nota» está al final del documento, no al pie de la página | La nota no está donde el número; no se puede hacer doble clic para saltar | Borrar ambos y **Referencias › Insertar nota al pie** | 2.4 |
| 14 | Apartado «Contactos» | Comentario olvidado del capitán («Eliminado en cuartos por un penalti que no era…») | **Revisar › Mostrar comentarios**; Inspeccionar documento | Eliminar el comentario | 2.6 |
| 15 | Tras «¡Suerte, y que gane el mejor!» | Texto oculto: «Nota privada: los mandos 3 y 5 tienen el joystick derecho tocado; dárselos siempre a los rivales» | ¶ lo muestra con subrayado punteado; Inspeccionar documento | **Borrarlo** (ocultarlo no es eliminarlo) | 2.6 |

**El extra (+3).** Propiedades del documento: *Autor* y *Modificado por* «El
capitán eliminado» y comentarios «Versión definitiva. Al que la toque, tarjeta roja.». Se
ve en **Archivo › Información**. Arreglo: *Inspeccionar documento › Propiedades
del documento e información personal › Quitar todo*, o editar las propiedades.

### La trampa dentro de la trampa

Si un equipo usa *Reemplazar todo* de dos espacios a uno (10) **antes** de
convertir el calendario en tabla (5), el calendario queda descolocado y las
viñetas falsas pierden un espacio. Es buen momento para preguntar: «¿qué habría
pasado si el calendario hubiera sido una tabla desde el principio?».

### Arreglos que no puntúan

- Escribir «Página 2» y «Página 3» en el pie: pie único para todo el documento,
  y si funcionara sería la misma trampa.
- Cambiar los números del índice a mano.
- Escribir un 3 en la lista para tapar el salto.
- Poner el texto oculto en blanco o en tamaño 1.
- Volver a dar formato a mano a los títulos «para que se vean igual».

## Prueba de estrés (minuto 35–45)

Dictar una a una, 1 minuto cada una. **+2** por prueba superada. No se
publican antes en la página porque revelan las trampas.

| P | Qué se dicta | Se supera si… | Deja al descubierto |
|---|---|---|---|
| 1 | Abrid el panel de navegación | Aparecen los cuatro apartados y el 3.1 | 1 |
| 2 | Modificad el estilo Título 1: color rojo | Los cuatro apartados cambian a la vez | 1 |
| 3 | Añadid al final «5. Premios» como Título 1 y actualizad toda la tabla de contenido | El apartado 5 aparece en el índice con su página | 2 |
| 4 | Insertad una norma nueva entre la 2 y la siguiente: «Cada pareja elige un solo equipo para todo el torneo» | La lista se renumera sola sin saltos | 3 |
| 5 | Escribid tres líneas cualesquiera debajo del índice | «1. Normas del torneo» sigue empezando arriba de una página nueva | 6 |
| 6 | Id al pie de la página 3 | Pone el número de página correcto | 7 |
| 7 | <kbd>Ctrl</kbd>+<kbd>E</kbd> y cambiad la fuente a Arial 12 | El calendario sigue en columnas y las viñetas alineadas | 4, 5 |
| 8 | Archivo › Información › Inspeccionar documento | No encuentra comentarios, texto oculto ni información personal | 14, 15, extra |

**Si sobra tiempo:** Guardar como PDF con *Crear marcadores usando Títulos*.
Se supera si el PDF muestra los marcadores de los apartados (enlace con 2.5).

## Puntuación máxima

15 sabotajes × 2 + 8 pruebas × 2 + extra 3 = **49 puntos**.
