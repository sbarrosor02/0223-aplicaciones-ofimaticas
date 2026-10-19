---
modulo: "0223"
ut: "3.1"
titulo: "La imagen digital"
ra: "RA5"
ce: ["a", "c"]
horas: 4
evaluacion: 1
estado: publicado
actualizado: 2026-10-19
---

# UT3.1 — La imagen digital

Página: `web/temas/ut03-1.html`. Herramientas: apartados 1 a 4 del laboratorio.

## Guion

1. Mapa de bits frente a vectorial (tabla comparativa y programas de cada tipo).
2. Píxel y resolución: dimensiones, megapíxeles, ppp, fórmula de conversión,
   resoluciones recomendadas por uso, el mito de los 72 ppp, ppp frente a dpi.
   En GIMP: Propiedades de la imagen, Tamaño de impresión, Escalar la imagen.
3. Color: RGB, CMYK, escala de grises, indexado; profundidad de color; canal alfa.
4. Peso: fórmula sin comprimir, compresión con y sin pérdida, artefactos,
   pérdida por generaciones (XCF para trabajar, exportar al final).
5. Formatos: tabla de 10 formatos y criterio de elección. En GIMP, Guardar (XCF)
   frente a Exportar como.

## Errores típicos que hay que desmontar

| Creencia | Realidad |
|---|---|
| «Para web hay que poner 72 ppp» | En pantalla solo cuentan los píxeles |
| «Si subo los ppp, la imagen gana calidad» | Sin píxeles nuevos reales, solo cambia el tamaño impreso; si se reescala, se inventan píxeles |
| «El PNG siempre es mejor» | Con fotos pesa mucho más que un JPG sin ganar nada visible |
| «Guardo el JPG retocado encima, que es igual» | Cada guardado con pérdida degrada un poco más |

## Prácticas (CE a y c)

- **P3.1.1** Comparativa de formatos con el laboratorio y tabla en Word.
- **P3.1.2** Tres cálculos de resolución a mano y comprobados.
- **P3.1.3** Propiedades y tamaño de impresión en GIMP; JPG frente a PNG.
- **P3.1.4** SVG frente a PNG ampliados.

Soluciones de la P3.1.2: (1) 4000 × 3000 a 300 ppp → 33,9 × 25,4 cm;
(2) A3 a 150 ppp → 1754 × 2480 px; (3) 1280 × 720 en 15 × 10 cm da unos
217 × 183 ppp efectivos (el lado corto limita: 720 / (10/2,54) ≈ 183 ppp):
aceptable pero por debajo de 300; además la proporción 16:9 no es la de una
postal 3:2, así que habría que recortar y bajaría aún más.
