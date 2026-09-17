---
modulo: "0223"
ut: "2.2"
titulo: "Formato de documento y estilos"
ra: "RA2"
ce: []
horas: 10
evaluacion: 1
base_de: ["RA2.b", "RA2.e", "RA2.f"]
---

# Tema 2.2 — Formato de documento y estilos

> Este subtema no certifica por sí solo un criterio de evaluación: es la **base
> técnica** de las plantillas (b), las macros (e) y los manuales (f). Está en
> `web/temas/ut02-2.html`. Fuente: apuntes UT2 (Natalia Marcos), bloques de
> Formato del documento (2.6), Estilos (2.7) y Diseño de página (2.8), adaptados
> de forma más concisa y guiada.

## Idea central

Aplicar un **estilo** no solo da formato: **etiqueta la función** del texto
(Título 1, Título 2, Normal…) y con ello define la **estructura** del documento.
Un **tema** cambia el aspecto de todo el documento con un clic… pero solo si los
estilos están bien aplicados. Por eso los estilos son la base de b, e y f.

## 1. Formato: de qué hablamos

Formato = aspecto, no contenido. Word distingue dos niveles clásicos:

- **Formato de carácter**: afecta a letras sueltas (fuente, tamaño, negrita…).
- **Formato de párrafo**: afecta al párrafo entero (alineación, sangría…).

Y por encima, el **formato de página/documento** (márgenes, encabezados, temas).
Al final llegan los **estilos**, que agrupan formato *y* dan estructura.

## 2. Formato de carácter (la fuente)

Pestaña **Inicio > grupo Fuente** (y en el minibar al seleccionar texto).

- **Tipografía** y **tamaño**. La unidad es el punto (72 pt = 1 pulgada =
  2,54 cm); habituales, 10 y 12.
- Efectos con atajo: **Negrita** `Ctrl+N`, **Cursiva** `Ctrl+K`, **Subrayado**
  `Ctrl+S`, tachado, **subíndice** `Ctrl+=`, **superíndice** `Ctrl++`. Subíndice
  y superíndice son los únicos que no se combinan entre sí.
- **Color de fuente** y **color de resaltado** (rotulador).
- **Cambiar mayúsculas/minúsculas**: tipo oración, minúsculas, MAYÚSCULAS, cada
  palabra… También con `Mayús+F3`, que alterna las tres formas.
- **WordArt** (Insertar > Texto): rótulos vistosos; a medio camino entre texto e
  imagen (el corrector no lo revisa).
- **Copiar formato** (la brocha, en Portapapeles): copia el formato de un texto a
  otro. Doble clic en la brocha = aplicarlo a varios sitios seguidos.

## 3. Formato de párrafo

Pestaña **Inicio > grupo Párrafo**.

- **Alineación**: izquierda, centrada, derecha, justificada.
- **Sangría**: desplaza el párrafo; 1,25 cm por clic (o el valor que quieras).
  También sangría de primera línea y sangría francesa.
- **Interlineado** y **espaciado** antes/después del párrafo.
- **Listas**: con **viñetas** (sin orden), **numeradas** (con orden) o
  **multinivel** (jerárquicas). Se inserta una viñeta por párrafo (por cada
  `Intro`); para dos líneas en la misma viñeta, `Mayús+Intro`.
- **Tabulaciones**: posiciones fijas a las que salta el cursor con `TAB`. Se
  colocan en la regla (activa la regla en Vista > Mostrar > Regla) eligiendo el
  tipo en el extremo izquierdo: izquierda, centrada, derecha, decimal, barra.
- **Conservar líneas juntas** (cuadro Párrafo > Líneas y saltos de página) evita
  que un párrafo se parta entre dos páginas.

## 4. Formato de página y de documento

- **Temas** (Diseño > Temas): cambian de golpe **colores, fuentes y efectos** de
  todo el documento. Se pueden combinar por separado con los botones Colores,
  Fuentes y Efectos.
- **Portada** (Insertar > Páginas > Portada): página inicial predefinida con
  campos para título, autor, fecha…
- **Fondo de página** (Diseño > Fondo de página): **marca de agua** (Borrador,
  Confidencial…), **color de página**, **bordes de página**.
- **Configurar página** (Disposición > Configurar página): **márgenes**,
  **orientación** (vertical/horizontal), **tamaño** de papel.
- **Encabezado y pie** (Insertar): texto que se repite en cada página; suele
  llevar el **número de página** (Insertar > Número de página; sección *Página X
  de Y*).
- **Saltos de sección** (Disposición > Saltos): permiten cambiar el formato
  (encabezado, numeración, orientación, columnas, márgenes) a partir de un punto.
  Para que un encabezado sea distinto hay que romper el vínculo con **Vincular al
  anterior**.

## 5. Estilos: el corazón del subtema

Un **estilo** es un paquete de formato (carácter + párrafo) que se aplica de una
vez y que **etiqueta la función** del texto. Dos funciones:

1. Dar formato rápido y **coherente**.
2. Definir la **estructura/jerarquía** del documento (Título 1 > Título 2 >
   Título 3…).

- **Aplicar**: selecciona y pulsa el estilo en Inicio > Estilos (o abre el panel
  con `Ctrl+Alt+Mayús+S`). **Quitar**: *Borrar formato*.
- **Crear/modificar/borrar**: lo más recomendable es partir de un estilo que ya
  tenga el nivel jerárquico que buscas (p. ej. crear tu estilo a partir de
  Título 1) para que herede ese nivel.
- **Truco potente**: aplicar una **lista multinivel al estilo Título 1** numera
  automáticamente todos los apartados y subapartados (Título 2, 3…).
- **Temas y conjuntos de estilos** (Diseño): cambian el aspecto de todos los
  estilos a la vez.
- **Preferencias** cuando se mezclan formatos, tres reglas:
  1. El formato aplicado **en último lugar** manda.
  2. El formato **manual** manda sobre el del estilo.
  3. El formato **de carácter** manda sobre el de párrafo.

## 6. Por qué los estilos son la base de b, e, f

- **Sin** estilos aplicados: los temas no cambian nada, no se puede generar
  índice/tabla de contenido automáticos, las plantillas no tienen estructura y un
  manual largo es imposible de mantener.
- **Con** estilos: un clic reestiliza todo, el índice se genera y **se actualiza
  solo**, y una plantilla reutiliza esa estructura. Esto conecta directamente con
  2.4 (plantillas e índices) y 2.7 (manuales, proyecto final).

## 7. Prácticas del subtema (P2.2.x)

1. **P2.2.1** · Formato de carácter y párrafo sobre un texto plano: fuente,
   tamaño, efectos con atajo, alineación, sangría, interlineado, una lista con
   viñetas y otra numerada, y una tabla de datos alineada con tabulaciones en la
   regla.
2. **P2.2.2** · Aplicar estilos (Título 1/2/3 y Normal) a un documento
   estructurado y luego cambiar su aspecto completo con **dos temas** distintos,
   comprobando que el cambio solo funciona porque los estilos están bien puestos.
3. **P2.2.3** · Crear un estilo propio partiendo de Título 1, aplicarle una
   **lista multinivel** para que numere solo, y usarlo en el documento.
4. **P2.2.4** · Configurar página (márgenes y orientación), añadir **portada**,
   **encabezado/pie** con número *Página X de Y* y **marca de agua** «BORRADOR».
5. **P2.2.5** · Con un **salto de sección**, conseguir que la portada no lleve
   número de página y que el resto empiece a numerar en 1.
6. **P2.2.6** · Unificar con **Copiar formato** (brocha) el formato de varios
   fragmentos desordenados de un mismo documento.

## Autocomprobación y checklist

La web incluye 8 preguntas de autocomprobación (no evaluables) y una checklist
«Antes de pasar al subtema 2.3».
