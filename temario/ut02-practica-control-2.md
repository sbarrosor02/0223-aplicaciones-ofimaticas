---
modulo: "0223"
ut: "2-pc2"
titulo: "Práctica de Control 2: dossier corporativo y mailing comercial"
ra: ["RA2"]
ce: ["b", "c", "d"]
integra: ["2.0", "2.1", "2.2", "2.3", "2.4", "2.5"]
evaluable: true
evaluacion: 1
actualizado: 2026-10-01
---

# PC2 · Dossier corporativo y mailing comercial

Segundo punto de control. Se hace al terminar el subtema 2.5.

## Por qué material nuevo y no el CV

Igual que en el PC1, el encargo usa **documentos que el alumnado no ha visto
antes**. Si el punto de control se hiciera sobre el CV, se estaría evaluando
memoria de los pasos ya dados; con material nuevo se evalúa **transferencia**,
que es lo que de verdad indica si saben hacerlo.

Por el mismo motivo el origen de datos (`pc2-clientes.xlsx`) es distinto del de
los ejercicios (`empresas-destinatarias.xlsx`): mismos conceptos, otros nombres
de campo y otro criterio de filtrado, para que no puedan repetir de memoria.

## Los tres entregables

| Parte | Archivo | Qué evalúa |
|---|---|---|
| A | `pc2-plantilla.dotx` | CE b · plantillas, estilos modificados, encabezado y pie |
| B | `pc2-dossier.docx` + `.pdf` | 2.2 a 2.5 · estructura, TDC, figuras, referencias, exportación |
| C | `pc2-cartas-combinadas.docx` + `.pdf` | CE d · combinar correspondencia completo |

Las partes B y C son **independientes entre sí**: quien se atasque en el dossier
puede empezar el mailing. Está dicho en el consejo de método de la página.

## Material de partida

### `pc2-material-partida.docx`
Generado con `scripts/generar_pc2.js`. 54 párrafos, **todo en estilo Normal**
(cero `pStyle`, cero negritas), 7 secciones de nivel 1 y sus subapartados,
5 marcas `[FIGURA: …]` y 3 marcas `[TABLA: …]`.

Lleva **15 faltas de ortografía plantadas**, verificadas una a una:

`informatica`, `reparacion`, `tecnicos`, `ampliacion`, `instalacion`,
`garantia`, `Instalacion`, `configuracion`, `conexion`, `recuperacion`,
`Diagnostico`, `tecnico`, `sustitucion`, `mantenimineto`, `electronico`.

Catorce son tildes que faltan; **`mantenimineto` es una transposición de
letras**, puesta a propósito porque el corrector la marca pero es la que más se
escapa al ir aceptando sugerencias en automático. El resto del documento está
correctamente acentuado para que no haya falsos positivos.

### `pc2-clientes.xlsx`
Generado con `scripts/generar_pc2_clientes.py`. 14 registros, 12 campos.

Propiedades deliberadas:

- **Campos con nombres no estándar** (`Razon`, `Trato`, `Calle`, `Localidad`)
  → obliga a usar *Asignar campos*.
- **`TipoCliente`** con tres valores (Empresa 8 / Centro educativo 4 /
  Particular 2) → se filtra por algo distinto de la provincia, que es por donde
  se filtró en los ejercicios del bloque 2.5.
- **Dos registros sin `Correo`**, y los dos son `Empresa` → el segundo filtro
  tiene efecto real sobre el resultado.
- **Clínica Dental Ambroz y Floristería El Almendro comparten apellidos**
  (`Núñez Pardo`, Rocío y Ana) → el criterio *Luego por: Nombre* es
  comprobable. Sin esto, ordenar por dos campos daría el mismo resultado que
  ordenar por uno y el criterio no se podría corregir.

## Resultado esperado de la combinación

Con el filtro (`TipoCliente = Empresa` **Y** `Correo No está vacío`) y la
ordenación (`Apellidos`, luego `Nombre`):

**Salen exactamente 6 cartas**, en este orden:

1. Calvo Ramos, Beatriz — Panadería La Espiga
2. Herrero Pozo, Sandra — Óptica Mirador
3. Moreno Casas, Pilar — Asesoría Valle Verde S.L.
4. Núñez Pardo, **Ana** — Floristería El Almendro
5. Núñez Pardo, **Rocío** — Clínica Dental Ambroz
6. Núñez Vega, Emilio — Bodegas Alagón

Descartados por no tener correo: Transportes Tiétar y Taller Mecánico Jaraíz.

Esto permite **corregir de un vistazo**: si salen 8, falta el filtro del correo;
si salen 14, no se filtró; si la cuarta no es Floristería El Almendro, falta el
*Luego por*. En la página se le da al alumnado la comprobación del número y de
la cuarta carta, pero no la lista completa.

## Rúbrica (10 puntos)

| Criterio | Puntos |
|---|---|
| Plantilla | 1,5 |
| Estructura y tabla de contenido | 2,0 |
| Figuras y tablas | 1,5 |
| Referencias del documento (tabla de ilustraciones, referencia cruzada, nota al pie) | 1,5 |
| Combinación: conexión y campos | 1,5 |
| Combinación: filtro y orden | 1,0 |
| Ortografía | 0,5 |
| Entrega | 0,5 |

## Para corregir rápido

- **Que el salto de página venga del estilo** y no puesto a mano: se ve en
  `Título 1 > Modificar > Formato > Párrafo`. Si hay `Ctrl+Intro` manuales,
  aparecen marcas de salto con `Ctrl+(`.
- **Que el documento se creó desde la plantilla** y no escribiendo sobre el
  `.dotx`: si lo hicieron mal, no habrá entregado un `.dotx` aparte o estará
  con el contenido dentro.
- **Que la TDC se actualizó al final**: comparar los números de página del
  índice con los reales.
- **Que el bloque de direcciones está completo**: si falta la calle o la
  ciudad, no resolvieron *Asignar campos*.

## Regeneración del material

```
NODE_PATH="C:/Users/sbarr/AppData/Roaming/npm/node_modules" node scripts/generar_pc2.js
python scripts/generar_pc2_clientes.py
```

No editar los archivos a mano: el `.docx` perdería la premisa de estar todo en
Normal en cuanto Word lo guarde, y el `.xlsx` perdería las propiedades
didácticas descritas arriba.
