---
modulo: "0223"
ut: "2-pc3"
titulo: "Práctica de Control 3: manual de usuario con macros (proyecto final)"
ra: ["RA2"]
ce: ["e", "f"]
integra: ["2.0", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7"]
evaluable: true
evaluacion: 1
sesiones: 6
entrega: "Moodle de Educarex, tarea PC3, un .zip"
actualizado: 2026-10-15
---

# PC3 · Manual de usuario con macros (proyecto final)

Tercer punto de control y cierre del Tema 2. Enunciado en
`web/temas/ut02-practicas.html#apartado-pc3-proyecto-final-manual-de-usuario-con-macros`.

## Qué acredita

| CE | Enunciado (Decreto 272/2009) | Apartados de la rúbrica |
|----|------------------------------|-------------------------|
| e | Se han creado y utilizado macros en la realización de documentos. | Macros (2,5) |
| f | Se han elaborado manuales específicos. | Todo lo demás (7,5) |

Para el cálculo por criterio, la nota del CE e es la del apartado *Macros*
sobre 2,5, y la del CE f, el resto sobre 7,5.

## Decisiones de diseño

- **Misma empresa que el PC2** (Soporte Integral Jerte): da continuidad y el
  encargo es verosímil. Pero el material es nuevo; no se parte de nada del PC2.
- **Sin material de partida.** A diferencia del PC1 y el PC2, aquí el
  contenido lo genera el alumnado haciendo los procedimientos en el
  ordenador. Por eso hay una lista cerrada de **ocho procedimientos** entre los
  que eligen tres: hay variedad (cuesta más copiar) pero todos se pueden hacer
  en el aula y corregir con criterio común.
- **Las macros van en la plantilla, no en Normal.dotm.** Es lo que se puede
  entregar y corregir, y en los equipos del aula Normal.dotm puede perderse al
  cambiar de usuario o de equipo. La barra de acceso rápido también se
  guarda *para la plantilla*, de modo que los botones viajan con el `.dotm`.
- **Macros que aplican estilos.** Coherente con el 2.7 y con el reto del
  documento saboteado: *InsertarAviso* aplica el estilo Aviso en lugar de
  sombrear a mano.
- **El comentario en VBA** es la evidencia mínima de que han abierto el
  editor; el anexo de macros convierte la propia documentación de las macros
  en un pequeño manual dentro del manual.
- **Revisión cruzada obligatoria con prueba del usuario**: recoge el 2.6 y es
  la mejor prueba de un manual (apuntes del 2.7, apartado 9). Se entrega la
  revisión **hecha**, no solo la recibida, para que se pueda evaluar a cada
  uno por su trabajo de revisor.

## Organización

| Sesión | Trabajo |
|---|---|
| 1 | Parte A: estilos, contenido fijo y las tres macros. Prueba en otro equipo |
| 2-3 | Parte B: introducción y los tres procedimientos, primero el texto haciendo las tareas |
| 4 | Capturas, avisos, referencias, solución de problemas, glosario y anexo. Versión 0.1 |
| 5 | Parte C: revisión cruzada (intercambio al principio de la sesión) |
| 6 | Resolver la revisión, versión 1.0, inspección, PDF y entrega |

Asignar las parejas de revisión **antes de la sesión 5** y tener previsto
qué hacer con quien falte: el profesor revisa su manual o se forma un trío
circular (A revisa a B, B a C, C a A).

Comprobar antes de la sesión 1 que en los equipos del aula se puede activar
la ficha Programador y grabar macros (alguna política de grupo deshabilita
VBA).

## Para corregir rápido

1. **Descomprimir y desbloquear.** El `.zip` descargado de Moodle lleva la
   marca de la web y Windows la pasa a los archivos extraídos: el `.dotm`
   abrirá con las macros bloqueadas. Desbloquear el `.zip` *antes* de
   extraerlo (`Propiedades > Desbloquear`) evita hacerlo archivo a archivo.
2. **Macros en la plantilla.** Abrir el `.dotm` con `Archivo > Abrir` y
   pulsar `Alt+F11`: en el explorador de proyectos, el proyecto de la
   plantilla debe tener un módulo con las tres macros. Si el módulo está
   vacío y las macros no aparecen, se grabaron en Normal.dotm: apartado de
   macros a 0 salvo la parte de botones.
3. **Que funcionen.** Crear un documento desde la plantilla y probar los
   tres botones. *InsertarAviso* debe dejar el párrafo en estilo Aviso (panel
   Estilos), no con formato directo.
4. **Botones para la plantilla.** Si los botones no aparecen al crear el
   documento desde la plantilla en el equipo del profesor, se guardaron *para
   todos los documentos*.
5. **Estilo Paso con numeración.** Clic en un paso: el panel Estilos debe
   marcar *Paso* y la numeración debe ser automática (no se puede seleccionar
   el número como texto).
6. **Revisión.** En `pc3-revision-de-…docx` tienen que verse las marcas
   (`Revisar > Todas las revisiones`). En el manual final no debe quedar
   ninguna: si quedan, no se resolvió o no se inspeccionó.
7. **PDF con marcadores.** Abrir el PDF y mirar el panel de marcadores del
   lector.

## Errores previstos

| Síntoma | Causa |
|---|---|
| Las macros desaparecen al guardar el manual | Lo guardaron como `.docx` desde el `.dotm` abierto, en vez de crear el documento desde la plantilla |
| *FormatoCaptura* falla si no hay imagen seleccionada | Normal: la macro trabaja sobre la selección. Se acepta; es un buen motivo para mencionarlo en el anexo |
| La numeración de pasos sigue de un procedimiento al siguiente | Falta *Reiniciar en 1* |
| El título de figura se separa de la imagen | No activaron *Conservar con el siguiente* en el estilo Captura |
| `ActualizarCampos` pregunta por la tabla cada vez | Es el comportamiento de Word con la tabla de contenido; se acepta |
