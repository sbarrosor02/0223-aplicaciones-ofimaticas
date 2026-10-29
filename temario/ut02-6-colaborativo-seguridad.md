---
modulo: "0223"
ut: "2.6"
titulo: "Trabajo colaborativo y seguridad documental"
ra: "RA2"
ce: []
apoya: ["f"]
horas: 6
evaluacion: 1
estado: publicado
actualizado: 2026-10-01
fuente: "UT2_Elaboración de Documentos y Plantillas mediante Procesadores de Texto.pdf, apartados UT2.20 (seguridad, pp. 181-191) y UT2.22 (revisar documentos, pp. 202-229)"
---

# UT2.6 — Trabajo colaborativo y seguridad documental

## Posición en el currículo

Subtema **transversal**: no tiene criterio propio en el Decreto 272/2009. Da
apoyo directo al criterio **f)** (elaboración de manuales), porque un manual
real lo revisan varias personas antes de publicarse y hay que saber entregarlo
protegido.

Conviene decirlo en clase: que no tenga CE propio no significa que no entre en
la evaluación, significa que se evalúa dentro del proyecto final del 2.7.

## Idea vertebradora

Hasta el 2.5 el documento era de una sola persona. Aquí entra el resto del
mundo: **trabajar con otros sin pisarse** y **entregar sin regalar de más**.

Las dos mitades (revisión y seguridad) se unen en el apartado 8: un
**formulario** se diseña como documento colaborativo y se entrega protegido con
la restricción *Rellenando formularios*.

## Guion de la página web

1. Resaltado y comentarios — dos formas de resaltar, buscar texto resaltado, los
   comentarios no se imprimen salvo que se pida, `Ctrl+I` para ir a los de un
   autor concreto.
2. Control de cambios — `Ctrl+Mayús+E`; cómo marca inserciones, borrados,
   formato y líneas cambiadas; las cuatro vistas.
3. Aceptar y rechazar — uno a uno o en bloque; *Aceptar todos y detener el
   seguimiento*.
4. Comparar dos versiones — cuando alguien editó sin control de cambios;
   *Mostrar cambios en*; *Mostrar ambos*.
5. Los cinco niveles de seguridad que enumera el apunte.
6. Contraseña (`Archivo > Información > Proteger documento > Cifrar`),
   restringir formato y los cuatro tipos de restricción de edición.
7. Firma digital (FNMT, clave pública y privada, se rompe al editar) y los
   cuatro niveles de seguridad de macros. IRM mencionado de pasada.
8. Formularios — activar la ficha Programador, los controles, sus propiedades,
   proteger con *Rellenando formularios* y guardar como plantilla.

## La trampa que hay que enseñar sí o sí

**La vista «Ninguna revisión» no elimina las revisiones, las oculta.** Es el
error más caro de este subtema y el más frecuente fuera del aula: alguien pone
esa vista, ve el documento limpio y lo envía a una empresa. Quien lo recibe
abre el panel de revisiones y ve todo el historial: lo que se escribió, lo que
se borró y lo que corrigió el jefe.

Está destacado en un aviso y es la pregunta 2 del cuestionario. Merece la pena
demostrarlo en clase con un documento real: poner la vista, guardar, cerrar,
abrir y enseñar las marcas intactas.

## Añadido más allá de los apuntes

El reto opcional usa **`Archivo > Información > Comprobar si hay problemas >
Inspeccionar documento`**, que no está en el PDF. Se incluye porque es la
contrapartida práctica del problema anterior: es la herramienta que de verdad
limpia comentarios, revisiones, datos de autor y rutas del equipo antes de
entregar. Los apuntes solo mencionan las *Opciones de privacidad* del Centro de
confianza (p. 189).

## Errores típicos previstos

| Síntoma | Causa real |
|---|---|
| «He quitado los cambios» pero siguen ahí | Se cambió la vista a *Ninguna revisión* en vez de aceptar/rechazar |
| No aparecen las marcas al editar | El control de cambios no estaba activado |
| No puedo quitar el control de cambios | Hay una restricción de edición *Marcas de revisión* aplicada con contraseña |
| No encuentro los controles de formulario | La ficha Programador no está activada en la cinta |
| El formulario se puede destrozar | Falta proteger con *Rellenando formularios* |
| El documento cifrado no se abre | Se olvidó la contraseña: no hay recuperación posible |
| Los comentarios no salen al imprimir | Es el comportamiento normal; hay que marcar *Imprimir documento con revisiones* |

## Trabajo diario (CE f)

Lo que se entrega del subtema es el **boletín de ejercicios del bloque 2.6**
(`temario/ut02-ejercicios.md`, `web/temas/ut02-ejercicios.html`), en Moodle.
Cuenta como **trabajo diario** del RA2. Las prácticas P2.6.x se retiraron el
29/10/2026: no se llegaron a hacer en clase. El subtema no tiene CE propio; como apoya a f, su boletín cuenta para ese criterio.

- **Reto (opcional)**: *Inspeccionar documento* y explicar por qué conviene.

Nota de organización: los ejercicios de revisión cruzada del boletín (revisar el
CV del compañero y resolver la revisión recibida) son la misma actividad vista
desde los dos lados, así que hay que emparejar al alumnado y reservar las dos
sesiones seguidas. Si alguien falta, que revise el profesor su documento.

## Enlaces con el resto del tema

- **Viene de 2.4**: el formulario se guarda como plantilla `.dotx`.
- **Va a 2.7**: la seguridad de macros se retoma al grabar macros propias, y el
  formulario del subtema es candidato natural a ser el documento del
  proyecto final.
- **PC3 / proyecto final**: el manual se entrega inspeccionado (sin comentarios
  ni revisiones). La revisión cruzada se quitó del PC3 el 19/10/2026: el
  control de cambios se evalúa en el boletín 2.6.
