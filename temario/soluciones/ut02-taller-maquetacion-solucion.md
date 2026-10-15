---
modulo: "0223"
ut: "2-taller"
titulo: "Claves y guía de corrección · Taller de maquetación y carta"
generador: "scripts/generar_taller_maquetacion.py"
actualizado: 2026-10-15
---

# Claves y guía de corrección · Taller de maquetación y carta

Uso del profesor. No se enlaza desde la web. Si se cambian los datos del
generador, revisar las cifras de este archivo.

## T1 · Tabulaciones

**Parte A.** Las cuatro tabulaciones tienen que estar en **todos** los
párrafos de la lista, cabecera incluida. Comprobación rápida: seleccionar la
lista entera y abrir *Tabulaciones*; si sale vacío o con valores distintos,
están puestas solo en algunas líneas.

| Columna | Posición | Alineación | Relleno |
|---|---|---|---|
| Cód. producto | 1 cm | Izquierda | — |
| Fecha de pedido | 10 cm | Derecha | Puntos |
| Precio | 12,5 cm | Decimal | — |
| Unidades | 14,5 cm | Centrada | — |

El archivo descargable ya trae una tabulación al principio de cada línea:
por eso la primera columna empieza en 1 cm.

**Parte B.** Con *Mostrar todo* no debe aparecer ni un `_`. Fallo típico:
escribir guiones bajos y alinear «a ojo». Comprobar también que el archivo es
`.dotx`: en el Explorador, el icono es de plantilla y el doble clic abre
*Documento1*.

## T2 · Tabla

| Fila | Real 2024 | Objetivo 2025 | Real 2025 |
|---|---|---|---|
| 1 Cereza cosechada | 24.500 t (+6,2 %) | 25.700 t (+4,9 %) | 23.900 t (−2,4 %) |
| 2 Cereza vendida en fresco | 19.800 t (+5,1 %) | 21.000 t (+6,1 %) | 19.200 t (−3,0 %) |
| 3 Ventas totales | 61,4 m € (+9,8 %) | 66,0 m € (+7,5 %) | 63,1 m € (+2,8 %) |
| 4 Ventas en el extranjero | 18,7 m € (+14,3 %) | 21,0 m € (+12,3 %) | 20,2 m € (+8,0 %) |
| 5 Venta directa y comercio en línea | 3,1 m € (+22,5 %) | 3,8 m € (+22,6 %) | 3,6 m € (+16,1 %) |

Cómo distinguir una combinación real de un truco: hacer clic en la fila 1 y
mirar `Disposición > Seleccionar > Seleccionar celda`; si se selecciona todo
el ancho, está combinada. Con *Ver cuadrículas* activado, los bordes borrados
aparecen como líneas discontinuas y las celdas combinadas no.

## T3 · Portada

- Las formas tienen que ser formas, no una imagen pegada: al hacer clic
  aparece *Formato de forma*.
- Transparencia: abrir el panel de formato del pentágono y mirar el valor.
- WordArt: tiene que poder editarse el texto.
- No se exige precisión de posición; sí que haya dos formas que salgan de la
  hoja y el orden de capas indicado.

## T4 · Gráfico

- `Clic derecho > Editar datos` debe abrir la hoja: si no, es una imagen.
- Agujero al 60 % en *Opciones de serie*.
- Formato de las etiquetas `0,00" %"`. Variante también válida: introducir los
  valores como 0,385… y mostrar *Porcentaje* con dos decimales.
- Las etiquetas fuera del anillo solo se consiguen arrastrándolas; es la parte
  que más cuesta y la que distingue a quien ha leído el enunciado.

## T5 · Combinar con reglas

Datos de `t5-invitados.xlsx`:

| Nombre | Asiste | Regalo | ¿Carta? | ¿Párrafo del regalo? |
|---|---|---|---|---|
| Ana | Sí | Sí | Sí | Sí |
| Bruno | Sí | No | Sí | No |
| Carmen | No | Sí | **No** | — |
| Daniel | Sí | Sí | Sí | Sí |
| Elena | Pendiente | No | No | — |
| Fernando | Sí | No | Sí | No |
| Gloria | Sí | Sí | Sí | Sí |
| Hugo | No | No | No | — |
| Irene | Sí | No | Sí | No |
| Javier | Sí | Sí | Sí | Sí |
| Laura | Pendiente | Sí | **No** | — |
| Mario | Sí | Sí | Sí | Sí |

**Respuesta esperada:** salen **8 cartas** y **5** llevan el párrafo del
regalo. Carmen no recibe carta porque el filtro deja solo a quien tiene «Sí»
en *Asiste*, y ella tiene «No»: la regla del regalo solo actúa sobre las
cartas que ya han pasado el filtro. Laura es el mismo caso con «Pendiente».

Cómo comprobar que hay regla y no texto escrito: en el documento principal,
`Alt+F9` muestra los códigos de campo; debe verse `{ IF { MERGEFIELD Regalo }
= "Sí" " Como te apuntaste…" "" }`.

Si alguien obtiene 0 cartas con regalo, casi seguro que escribió `Si` sin
tilde en la regla.

## Carta del restaurante

Orden de corrección recomendado, de lo estructural a lo visual:

1. **Mostrar todo (¶)** en la página 2: debe verse un *Salto de sección
   (página siguiente)* al final de la página 1 y *Salto de columna* entre
   columnas. Filas de marcas de párrafo vacías = R2 no conseguido.
2. **Panel de navegación**: las seis secciones. Si no aparecen, R3 no
   conseguido aunque se vean bien.
3. **Panel Estilos** con *Mostrar vista previa* desactivado y un clic en
   varios platos: todos deben marcar *Plato* o *Descripción*. Con
   `Mayús+F1` se ve si hay formato directo encima del estilo.
4. **Precios**: un clic en un plato y mirar la regla; debe haber una
   tabulación derecha. Abrir `Modificar estilo > Formato > Tabulaciones` del
   estilo *Plato* para ver que está en el estilo.
5. **Logotipo**: un clic encima debe seleccionar un grupo (marco único).
6. **Imágenes**: `clic derecho > Ver texto alternativo` en cada una; origen
   indicado en la contraportada.
7. **PDF**: dos páginas, apaisadas, iguales que el Word.

Escala de cada apartado de la rúbrica: completo (entero), fallos puntuales
(mitad), no conseguido (0).
