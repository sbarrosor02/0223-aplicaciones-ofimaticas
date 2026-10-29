---
modulo: "0223"
ut: "2-taller"
titulo: "Taller de maquetación (T1-T5) y caso práctico de la carta"
ra: "RA2"
ce: ["b", "c", "d"]
evaluable: true
entrega: "Moodle de Educarex, una tarea por práctica"
estado: publicado
actualizado: 2026-10-15
---

# Taller de maquetación y caso práctico de la carta

Páginas del alumnado:

- `web/temas/ut02-practicas-taller.html`: T1 a T5.
- `web/temas/ut02-practicas-carta.html`: la carta del restaurante.

Materiales generados con `scripts/generar_taller_maquetacion.py`. Claves y
guía de corrección en `temario/soluciones/ut02-taller-maquetacion-solucion.md`.

## Origen

Parten de un paquete de prácticas heredado (P1 a P7, una portada y una
práctica final), con enunciados de una o dos líneas y apoyados en imágenes de
terceros. Se revisaron una a una frente a lo que ya cubrían los apuntes, los
ejercicios guiados y las prácticas P2.x.y (estas se retiraron el 29/10/2026
sin llegar a hacerse; la tabla se conserva como registro de la decisión):

| Original | Decisión | Por qué |
|---|---|---|
| P1 Tabulaciones | **T1, parte A** | Los cuatro tipos con posición exacta; la P2.2.1 solo pedía «alinear con tabulaciones» |
| P5 Autorización como plantilla | **T1, parte B** | Sola repetía la P2.4.1 y la P2.6.5; unida a la P1 aporta el relleno de línea para impresos |
| P2 Tabla copiada | **T2** | Combinar celdas, anchos exactos, sombreado y dos líneas por celda; la P2.3.1 era una tabla sencilla |
| Portada con formas | **T3** | Formas, transparencia, capas, objetos fuera de página y WordArt transformado solo estaban en un reto opcional |
| P4 Gráfico de anillo | **T4** | Edición a fondo de un gráfico; la P2.3.5 era opcional y de columnas |
| P6 SmartArt | **Eliminada** | Es la P2.3.4 |
| P7 Combinar con Access | **T5** | Las reglas *Si… Entonces… Sino* no estaban en ningún sitio. Se sustituye el Access de aulaClic por un `.xlsx` propio |
| Práctica final (carta) | **Caso práctico de la carta** | Integradora de maquetación; cierra el bloque antes del PC3 (manual con macros) |

Cambios comunes a todas:

- **Imágenes propias.** Las originales llevaban marca de agua de aulaClic o
  reproducían la carta de un restaurante real con su logotipo y su teléfono. No
  pueden ir en un repositorio público. Las referencias se generan por script.
- **Datos inventados y coherentes.** En la T2, las variaciones porcentuales se
  calculan a partir de los valores, no se escriben a mano.
- **Restaurante inventado** (La Cereza Brava, Valle del Jerte) y textos
  entregados en un `.docx`, para que el trabajo sea de maquetación y no de
  copiar texto de una imagen.
- **Enunciados con especificaciones medibles**, una lista de comprobación y
  el nombre de archivo de entrega en cada práctica.

## Evaluación

Decisión del departamento: las prácticas cortas cuentan como **trabajo diario**
y la carta como **caso práctico**.

| Práctica | CE | Instrumento |
|---|---|---|
| T1 | b | Trabajo diario |
| T2, T3, T4 | c | Trabajo diario |
| T5 | d | Trabajo diario |
| Carta | c | Caso práctico (rúbrica de 10 puntos en la página) |

Para el trabajo diario se propone una escala simple a partir de la lista de
comprobación de cada práctica: **completa (10)**, **con fallos (5)**, **no
entregada o hecha con trucos (0)**. «Con trucos» quiere decir alinear con
espacios, bordes borrados en lugar de celdas combinadas, gráficos pegados
como imagen o el texto del regalo escrito a mano.

## Montaje en Moodle

Crear **seis tareas** en el curso del módulo, una por práctica, con entrega de
archivos:

| Tarea | Archivos | Tipos admitidos |
|---|---|---|
| T1 · Tabulaciones | 2 | .docx, .dotx |
| T2 · Tabla | 1 | .docx |
| T3 · Portada | 1 | .docx |
| T4 · Gráfico | 1 | .docx |
| T5 · Combinar con reglas | 2 | .docx |
| Caso práctico: carta del restaurante | 2 | .docx, .pdf |

Conviene enlazar en cada tarea el apartado correspondiente de la página
(`ut02-practicas-taller.html#apartado-t1-…`), para que el enunciado viva en
un solo sitio.

## Temporización orientativa

| Práctica | Sesiones | Cuándo |
|---|---|---|
| T1 | 1 | Tras el 2.4 (usa plantillas) |
| T2, T3 | 1 cada una | Tras el 2.3 |
| T4 | 0,5 | Tras el 2.3 |
| T5 | 1 | Tras el 2.5 |
| Carta | 4 | Al final del bloque, antes del PC3 |

Como el curso ya va por el 2.6 y el 2.7, en la práctica se trabajan en
bloque, como taller de repaso de maquetación.
