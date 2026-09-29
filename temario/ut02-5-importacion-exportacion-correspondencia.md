---
modulo: "0223"
ut: "2.5"
titulo: "Importación, exportación y combinación de correspondencia"
ra: "RA2"
ce: ["d"]
horas: 10
evaluacion: 1
estado: publicado
actualizado: 2026-09-29
fuente: "UT2_Elaboración de Documentos y Plantillas mediante Procesadores de Texto.pdf, apartado UT2.15 (combinar correspondencia, pp. 115-133) y UT2.4 (guardar y abrir, pp. 31-34)"
---

# UT2.5 — Importación, exportación y combinación de correspondencia

## Criterio de evaluación

**RA2.d)** Se han importado y exportado documentos creados con otras aplicaciones
y en otros formatos.

## Nota sobre la fuente

Los apuntes cubren **combinar correspondencia con mucho detalle** (UT2.15, 19
diapositivas) pero **no tienen un apartado de importación/exportación**: lo único
que dicen al respecto es el desplegable *Tipo* del cuadro Guardar como (UT2.4.1)
y la mención al PDF.

Como el CE *d* exige explícitamente los formatos, la primera mitad de la página
(apartados 1 a 4) está **ampliada más allá de los apuntes**: formatos de archivo,
modo de compatibilidad, abrir PDF en Word, insertar objeto y pegado especial con
vínculo. La segunda mitad (apartados 5 a 9) sí es fiel a UT2.15.

## Idea vertebradora

Las dos mitades parecen inconexas pero son el mismo criterio: **hacer que Word se
entienda con el resto del mundo**. Exportar a PDF es sacar información; combinar
correspondencia es meterla, tirando de un Excel o de una base de datos. Conviene
decirlo en voz alta en clase, porque si no el alumnado percibe el subtema como
dos temas pegados con celo.

## Guion de la página web

1. Formatos de archivo — `.docx` (XML comprimido), `.doc`, `.odt`, `.rtf`,
   `.txt`, `.pdf`, `.html`, `.dotx`. Regla práctica: entregar → PDF; seguir
   editando → docx/odt; solo texto → txt.
2. Exportar — `Guardar como > Tipo`, `Archivo > Exportar > Crear PDF/XPS`,
   `F12` y `Ctrl+F12`.
3. Importar — modo de compatibilidad al abrir `.doc`, `Información > Convertir`,
   abrir PDF en Word y sus pérdidas.
4. Traer contenido — `Insertar > Objeto > Texto de archivo`, `Pegado especial >
   Pegar vínculo` desde Excel y cuándo romper el vínculo.
5. Combinar correspondencia — documento principal + origen de datos; registros y
   campos.
6. El asistente de 6 pasos.
7. La pestaña Correspondencia sin asistente; los campos entre `<< >>`.
8. Destinatarios — filtrar, ordenar por varios campos, buscar, asignar campos.
9. Sobres y etiquetas — marca y modelo del papel; la hoja de etiquetas **es una
   tabla**.

## Errores típicos previstos

| Síntoma | Causa real |
|---|---|
| El bloque de direcciones sale con huecos | Falta `Asignar campos`: los nombres de columna no coinciden con los estándar de Word |
| «Solo me sale una carta» | No se ha pulsado *Finalizar y combinar > Editar cartas individuales*; se está viendo la vista previa |
| El índice del PDF apunta mal | No se actualizó la TDC antes de exportar |
| Salen rayas al imprimir las etiquetas | No se quitaron los bordes de la tabla de etiquetas |
| La tabla de Excel no se actualiza | Se pegó normal, no con *Pegar vínculo* |
| El vínculo dejó de funcionar | Se movió el libro de Excel, o se envió el .docx sin el .xlsx |
| Falta gente en la combinación | Hay un filtro puesto: la flecha del encabezado está azulada, no negra |

## Origen de datos

`web/descargas/empresas-destinatarias.xlsx`, generado con
`scripts/generar_destinatarios.py`. 12 registros y 12 campos, diseñado a
propósito para que los ejercicios tengan sustancia:

- **Los campos NO se llaman como los estándar de Word** (`Via` en vez de
  Dirección, `Ciudad` en vez de Población, `Trato` en vez de Tratamiento). Sin
  esto, Word autoasocia y *Asignar campos* no se practica nunca.
- **Dos provincias** (7 Cáceres / 5 Badajoz) para que filtrar tenga sentido.
- **Tres apellidos repetidos** (Bermejo, Domínguez, Ruiz) para que ordenar por
  *Ordenar por* + *Luego por* tenga sentido.
- **Un registro sin correo** (Talleres Informáticos Vetton) para el filtro
  *No está vacío*.

Si hay que cambiar los datos, se edita el script y se regenera; no se edita el
.xlsx a mano, o se pierden estas propiedades.

## Prácticas (CE d)

- **P2.5.1** Exportar el CV a `.pdf`, `.odt` y `.txt` y comparar qué se pierde.
- **P2.5.2** Abrir el PDF con Word y señalar tres diferencias de maquetación.
- **P2.5.3** Carta de presentación combinada, con bloque de direcciones, línea de
  saludo y dos campos sueltos (obliga a *Asignar campos*).
- **P2.5.4** Filtrar por provincia + descartar sin correo + ordenar por apellidos.
- **P2.5.5** Hoja de etiquetas con modelo comercial y sin bordes.
- **Reto (opcional)**: pegado vinculado desde Excel y romper el vínculo.

## Enlaces con el resto del tema

- **Viene de 2.4**: el aviso de actualizar la TDC antes de exportar a PDF.
- **Va a PC2**: el punto de control posterior a este subtema debería exigir una
  combinación real y una entrega en PDF.
- **Va a 2.7**: el manual final se entrega en PDF; aquí se aprende a generarlo
  bien.
