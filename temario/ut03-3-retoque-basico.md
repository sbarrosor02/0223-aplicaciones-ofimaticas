---
modulo: "0223"
ut: "3.3"
titulo: "Retoque básico en GIMP"
ra: "RA5"
ce: ["c", "d"]
horas: 6
evaluacion: 1
estado: publicado
actualizado: 2026-10-19
---

# UT3.3 — Retoque básico en GIMP

Página: `web/temas/ut03-3.html`. Herramienta: apartado 6 del laboratorio
(histograma y niveles por canal, con botón Automático y vista dividida).

## Material

Fotos inventadas en `web/descargas/`, generadas con
`python scripts/generar_fotos_retoque.py` (paisaje de un valle con embalse y
cerezos, sin fotos de terceros):

| Archivo | Problema | Para |
|---|---|---|
| `retoque-1-torcida-oscura.jpg` | Inclinada 3,5° y subexpuesta | Medir/Enderezar, Niveles |
| `retoque-2-lavada-amarilla.jpg` | Sin contraste y dominante amarilla | Niveles por canal, balance de blancos |
| `retoque-3-manchas-cable.jpg` | 14 motas de polvo y un cable en el cielo | Saneado, Clonar |
| `documento-fotografiado-1.jpg` (del 3.2) | Hoja en perspectiva | Perspectiva correctiva |

Con `--original` el script guarda además el paisaje sin estropear en
`temario/soluciones/ut03-3-paisaje-original.jpg` (referencia para el profesor).

## Guion (6 sesiones de 1 h)

1. Orden del retoque; XCF, capa duplicada, historial, vista dividida.
2. Enderezar con Medir, Recortar con proporción fija y regla de los tercios,
   Perspectiva correctiva. P3.3.1.
3. Escalar la imagen / Tamaño de impresión / Tamaño del lienzo; recortar a la
   proporción antes de escalar; no ampliar. Tabla de destinos.
4. Histograma (cuatro formas típicas), Niveles, Curvas, Sombras-Luces. Laboratorio.
5. Color: dominantes, balance de blancos, niveles por canal, cuentagotas gris,
   temperatura, saturación, desaturar. P3.3.2.
6. Saneado frente a Clonar, ojos rojos, ruido; enfocar al final. P3.3.3 y P3.3.4.

## Prácticas (CE c y d)

- **P3.3.1** Enderezar la foto 1, corregir la perspectiva del documento y
  escalarlo a 1240 × 1754.
- **P3.3.2** Niveles en la foto 1 y quitar la dominante de la foto 2, con
  capturas del histograma antes y después.
- **P3.3.3** Quitar motas (Saneado) y cable (Clonar) de la foto 3 y enfocar.
- **P3.3.4** Una foto, cuatro destinos (1080², 1280 × 720, 15 × 10 cm a 300 ppp,
  3000² a 300 ppp) y justificar el que no se puede.

Soluciones: `temario/soluciones/ut03-3-retoque-basico-solucion.md`.

## Ejercicios guiados (bloque 3.3)

Retocar las fotos del proyecto, limpiar el boceto (Niveles y Umbral), preparar
la mejor foto para miniatura y portada (sin ampliar) y anotar los retoques.

## Avisos para el profesor

- Los nombres de menús y opciones son los de GIMP 3 en español. Pendiente de
  confirmar la versión instalada en el aula: en GIMP 2.10 alguna opción cambia
  de nombre (por ejemplo, la dirección de la herramienta Perspectiva).
