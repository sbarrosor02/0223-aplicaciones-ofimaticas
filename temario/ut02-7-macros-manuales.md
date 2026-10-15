---
modulo: "0223"
ut: "2.7"
titulo: "Macros y elaboración de manuales"
ra: "RA2"
ce: ["e", "f"]
horas: 8
evaluacion: 1
estado: publicado
actualizado: 2026-10-15
---

# UT2.7 — Macros y elaboración de manuales

## Posición en el currículo

Cierra el Tema 2 y cubre los dos criterios que quedaban del RA2 (Decreto
272/2009):

| CE | Enunciado |
|----|-----------|
| e | Se han creado y utilizado macros en la realización de documentos. |
| f | Se han elaborado manuales específicos. |

En la programación, la UT2 recoge «Diseño y creación de macros» y «Elaboración
de distintos tipos de documentos (manuales, partes de incidencia, etc.)». Los
dos criterios pesan lo mismo que el resto en pruebas, casos prácticos y trabajo
diario (1/6 cada uno).

## Idea vertebradora

Las dos mitades se plantean como **una sola**: las macros no se enseñan como
programación, sino como la **caja de herramientas del que escribe manuales**.
Un manual repite las mismas piezas decenas de veces (avisos, capturas con su
título, pasos numerados), y ahí es donde grabar una macro tiene sentido. El
alumnado termina el subtema con una plantilla `.dotm` de manual que tiene
estilos (2.2), estructura (2.4) y sus propias macros (2.7).

Regla que se repite en clase: **si haces lo mismo más de tres veces, grábalo**.

## Guion de la página web

1. Qué es una macro y cuándo merece la pena (y cuándo no).
2. Antes de grabar: dónde se guarda (Normal.dotm, documento, plantilla) y qué
   formatos admiten macros (`.docm`, `.dotm`; el `.docx` las pierde).
3. Grabar una macro paso a paso: nombre válido, botón o teclado, la limitación
   del ratón y el ejemplo guiado **Aviso**.
4. Ejecutar y gestionar: `Alt+F8`, botón en la barra de acceso rápido, atajo de
   teclado sin pisar los de Word.
5. Mirar y retocar el código: `Alt+F11`, qué es cada línea, cambiar un texto o
   un color. **Sin programar desde cero.**
6. Seguridad: recordatorio del 2.6, la barra amarilla y el bloqueo de macros en
   archivos descargados de Internet. Equivalencia en LibreOffice.
7. Qué es un manual específico, tipos y partes.
8. Cómo se redacta un paso (con ejemplos «mal / bien»).
9. Del borrador a la entrega: el recorrido completo, que reutiliza todos los
   subtemas anteriores.
10. Prácticas, cuestionario y lista de cierre del Tema 2.

## Decisiones de contenido

- **Grabar, no programar.** El CE pide crear y utilizar macros; con la
  grabadora se crean. El editor VBA se abre para **leer** y hacer retoques
  mínimos, porque desmitifica qué es una macro y explica por qué puede ser
  peligrosa. Programar en VBA queda fuera del nivel de 1.º de grado medio.
- **Macros que aplican estilos, no formato directo.** Es la continuación del
  reto del documento saboteado: una macro que pone negrita y 16 pt a mano
  fabrica documentos saboteados más rápido. La macro buena aplica *Título 3*.
- **No se usa el Organizador para copiar macros.** Su comportamiento cambia
  entre versiones de Word. Se enseña a grabar directamente en la plantilla
  abierta o a arrastrar el módulo en el editor VBA, que funciona siempre.
- **Archivos bloqueados de Internet.** Desde 2022 Word bloquea las macros de
  archivos descargados (marca de la web) con una barra roja de *Riesgo de
  seguridad*. Se explica porque es lo que verán en cualquier empresa y porque
  conecta con la seguridad del 2.6. Se insiste en que la solución
  (*Propiedades > Desbloquear*) solo se aplica a archivos de origen conocido.

## Errores típicos previstos

| Síntoma | Causa real |
|---|---|
| «Mi macro ha desaparecido» | Se grabó en el documento y se guardó como `.docx` |
| La macro no hace nada en otro documento | Se grabó en el documento, no en Normal.dotm o en la plantilla |
| No puedo seleccionar texto mientras grabo | Es normal: durante la grabación el ratón solo pulsa botones. Se selecciona con el teclado |
| La macro escribe en un sitio raro | Se grabó con clics de posición que dependen del documento; grabar desde una posición neutra |
| `Ctrl+G` ya no guarda | Se le asignó la macro a un atajo de Word. Revisar «Asignado actualmente a» |
| Barra roja «Riesgo de seguridad» | Archivo con marca de la web; no se habilita con un botón |
| Error de compilación al ejecutar | Se tocó el código y se borró una comilla o el `End Sub` |
| Al cambiar el estilo, lo que insertó la macro no cambia | La macro se grabó con formato directo |

## Prácticas (CE e y f)

- **P2.7.1** Macro *Aviso* en Normal.dotm con botón en la barra de acceso
  rápido.
- **P2.7.2** Macro *FormatoCaptura* con atajo de teclado libre.
- **P2.7.3** Retocar el código de *Aviso* en el editor VBA y guardar un
  documento de prueba como `.docm`.
- **P2.7.4** Plantilla `manual.dotm`: estilos de manual + las dos macros dentro.
- **P2.7.5** Manual breve (2 procedimientos, 4-6 páginas) hecho con la
  plantilla, con revisión cruzada en control de cambios y entregado en PDF con
  marcadores.

El **proyecto final (PC3)** integra el tema completo y se publica con
enunciado y rúbrica propios en la página de prácticas de control.

## Nota de montaje

- La práctica 2.1.1 exportó la personalización de la cinta (`.exportedUI`).
  En la P2.7.1 se vuelve a exportar con el botón de la macro añadido, como se
  anunciaba en `ut02-1-entorno-edicion-personalizacion.md`.
- Los equipos del aula tienen que permitir la ficha Programador y la
  grabación de macros. Comprobarlo **antes** de la primera sesión: algunas
  políticas de grupo deshabilitan VBA.

## Enlaces con el resto del tema

- **2.1**: barra de acceso rápido y métodos abreviados de teclado.
- **2.2**: las macros aplican estilos; el manual se apoya en ellos.
- **2.3**: capturas de pantalla, la herramienta que más se usa en un manual.
- **2.4**: plantilla, tabla de contenido, títulos y referencias cruzadas.
- **2.5**: exportación a PDF con marcadores.
- **2.6**: seguridad de macros, revisión con control de cambios e
  Inspeccionar documento antes de entregar.
