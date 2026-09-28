---
modulo: "0223"
ut: "2.4"
titulo: "Plantillas y documentos estructurados"
ra: "RA2"
ce: ["b"]
horas: 8
evaluacion: 1
estado: publicado
actualizado: 2026-09-28
fuente: "UT2_Elaboración de Documentos y Plantillas mediante Procesadores de Texto.pdf, apartados UT2.14 (plantillas), UT2.16 (esquemas), UT2.17 (documentos maestros), UT2.18 (tabla de contenido e índices) y UT2.19 (marcadores, referencias cruzadas y notas al pie)"
---

# UT2.4 — Plantillas y documentos estructurados

## Criterio de evaluación

**RA2.b)** Se han diseñado plantillas.

Es el único CE del subtema, pero la página cubre además toda la maquinaria de
documento estructurado (esquema, TDC, índice, referencias), porque es lo que
convierte una plantilla en algo realmente útil y porque es el andamiaje del
manual del subtema 2.7 (CE f).

## Idea vertebradora

**Aquí se cobra la deuda del 2.2.** Los apuntes lo dicen literalmente: *"Si hemos
dado a los títulos del documento un formato que incluya los niveles de esquema
casi tendremos construida la tabla de contenido"*.

El alumno que en 2.2 maquetó los títulos a mano (negrita + tamaño 16) descubre
aquí que su tabla de contenido sale **vacía**. Esa frustración es didácticamente
más valiosa que cualquier advertencia previa: es la demostración de por qué
existen los estilos. Conviene dejar que ocurra y luego explicarla, no evitarla.

## Guion de la página web

1. Qué es una plantilla — `.docx` / `.dotx` / `.dotm`; el molde y la pieza; una
   plantilla guarda un *entorno de trabajo* (barras, autotexto, macros).
2. `Normal.dotm` — la plantilla invisible; el botón *Predeterminar* la modifica;
   `Archivo > Opciones > Avanzadas > Ubicaciones de archivos… > Plantillas
   personales`.
3. Usar y crear plantillas — `Archivo > Nuevo` (DESTACADA / PERSONAL / en
   línea); campos con fondo gris etiquetado; `Guardar como > Plantilla de Word
   (*.dotx)` **en la carpeta que propone Word**.
4. Niveles de esquema — 9 niveles; Título *n* → nivel *n*; no confundir con el
   mapa del documento ni con la TDC; vista Esquema y sus botones; tres formas de
   asignar nivel; *Texto independiente*.
5. Tabla de contenido — preparar + generar; automática / manual / personalizada;
   `Opciones…` para relacionar estilo ↔ nivel; **actualizar** (solo números o
   toda la tabla).
6. Índice alfabético y tabla de ilustraciones — `Alt+Mayús+X`; automarcado con
   tabla de 2 columnas y `:` para subentradas; `Insertar título` +
   `Insertar tabla de ilustraciones`.
7. Marcadores, referencias cruzadas y notas al pie — nombre sin espacios, empieza
   por letra, máx. 40 caracteres, `Ctrl+Mayús+F5`; el elemento debe existir antes;
   nota al pie vs. nota al final.
8. Documentos maestros — enlaces a subdocumentos; vista Esquema > *Mostrar
   documento*; Crear / Insertar / Desvincular / Combinar / Dividir / Bloquear.

## Trampas terminológicas que hay que avisar en clase

- Word llama **tabla de contenido** a nuestro *índice* (el del principio) y
  **índice** a nuestro *índice alfabético* o glosario (el del final). Si no se
  avisa, el alumno pulsa "Insertar índice" esperando el de delante.
- **Esquema ≠ mapa del documento ≠ tabla de contenido.** El mapa (Panel de
  navegación) lo genera Word con criterios internos y no se puede modificar; el
  esquema es una vista que no se imprime; la TDC sí se imprime y lleva páginas.

## Errores típicos previstos

| Síntoma | Causa real |
|---|---|
| La TDC sale vacía | Los títulos no tienen estilo de título ni nivel de esquema |
| La TDC apunta a páginas equivocadas | No se actualizó tras editar (`Actualizar tabla` → *toda la tabla*) |
| La plantilla no aparece en PERSONAL | Se guardó fuera de la carpeta de plantillas |
| El desplegable de referencia cruzada sale vacío | El elemento no tiene título (`Insertar título`) o estilo de título |
| El automarcado del índice ignora términos | El texto de la columna 1 no coincide *carácter a carácter* (tildes, mayúsculas) |
| Cambió el aspecto de todos los documentos nuevos | Se editó `Normal.dotm` |

## Prácticas (CE b)

- **P2.4.1** CV como plantilla `.dotx` en PERSONAL, y crear un documento desde ella.
- **P2.4.2** Estructurar un documento largo con niveles y **reordenar dos apartados
  con las flechas de la vista Esquema** (sin cortar y pegar).
- **P2.4.3** TDC automática + añadir apartado + actualizar toda la tabla.
- **P2.4.4** `Insertar título` en imágenes y tablas + tabla de ilustraciones.
- **P2.4.5** Un marcador, una referencia cruzada con número de página y una nota
  al pie.
- **Reto (opcional)**: documento maestro con tres subdocumentos y TDC común.

Nota: la P2.4.2 necesita **un documento largo de partida** que aún hay que
preparar y subir a `web/descargas/`. Mientras tanto el enunciado dice "el
documento que te dé el profesor".

## Enlaces con el resto del tema

- **Viene de 2.2**: sin estilos de título, nada de esto funciona.
- **Viene de 2.3**: las imágenes y tablas insertadas allí son las que aquí
  reciben `Insertar título` y alimentan la tabla de ilustraciones.
- **Va a 2.7**: el manual final (CE f) se monta con esta maquinaria — plantilla,
  esquema, TDC, referencias cruzadas y capturas.
- **PC2** (tras 2.5) debería exigir TDC actualizada como criterio de rúbrica.
