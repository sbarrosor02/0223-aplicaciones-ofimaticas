# Solucionario · UT3.3 Retoque básico en GIMP

No se publica en la web del alumnado. Valores medidos sobre las fotos generadas
por `scripts/generar_fotos_retoque.py` (semillas fijas: si se regeneran, salen
iguales).

## Cómo se estropeó cada foto (para saber qué esperar)

| Foto | Transformación aplicada al original |
|---|---|
| 1 · torcida y oscura | Giro de 3,5° en sentido antihorario, recorte del 3,5 % / 5 % de márgenes y reescalado a 2400 × 1600; luego `0,02 + 0,50 · x^1,6` |
| 2 · lavada y amarilla | `0,24 + 0,58 · x` y canales × (1,08 · 1,02 · 0,72) |
| 3 · manchas y cable | 14 motas oscuras difuminadas en el tercio superior y un cable (catenaria) de 5 px |

## P3.3.1

1. **Ángulo**: unos 3,5° (Medir marca 3,5 o −3,5 según el sentido en que se
   arrastre; Enderezar gira en sentido horario). Se acepta de 3 a 4°.
   Tras recortar las esquinas vacías con la misma proporción 3:2 queda de unos
   **2200 × 1470 px** (factor 1 / (cos 3,5° + 1,5 · sen 3,5°) ≈ 0,918). Si
   recortan sin fijar la proporción, cualquier tamaño parecido sin esquinas
   transparentes es válido.
2. **Documento**: con Perspectiva en modo correctivo y las cuatro esquinas en las
   de la hoja, la hoja queda de unos 1400 × 2000 px; escalada a 1240 × 1754
   (proporción A4, 1 : 1,414). Error típico: escalar con la cadena abierta y
   deformar; o no recortar la mesa.

## P3.3.2

Percentiles 0,5 % y 99,5 % medidos en las fotos (lo que hace el botón
Automático, aproximadamente):

| Foto | Canal | Negro | Blanco |
|---|---|---|---|
| 1 | Valor (luminancia) | ~26 | ~109 |
| 1 | R · G · B | 17 · 31 · 10 | 122 · 102 · 118 |
| 2 | R | ~104 | ~218 |
| 2 | G | ~118 | ~190 |
| 2 | B | ~60 | ~144 |

- **Foto 1**: niveles de entrada en torno a **20 · 1,4–1,6 · 115** en el canal
  Valor (la gamma > 1 aclara los medios; la foto se oscureció con exponente 1,6).
  Respuesta esperada: «el histograma estaba amontonado a la izquierda; he traído
  el blanco hasta donde acababa y he aclarado los medios con el gris».
- **Foto 2**: la dominante amarilla es falta de azul: el canal azul es el más
  estrecho y el más desplazado a la izquierda. Corrección por canales con los
  valores de la tabla (gamma 1) o Automático; balance de blancos automático
  también vale si el resultado es neutro (las nubes deben quedar blancas, no
  amarillas ni azules).

## P3.3.3

- 14 motas (todas en el cielo, de 9 a 22 px de radio) y el cable, que cruza toda
  la imagen por la parte alta (más bajo en el centro, ~y = 230 px).
- Saneado para las motas; Clonar para el cable, cogiendo el origen justo encima
  o debajo y cambiándolo a menudo (si no, se repiten nubes).
- Revisar al 100 %: restos grises del cable en la zona de nubes y patrones
  repetidos son los fallos típicos.
- Enfoque con máscara de desenfoque moderado (por ejemplo, radio 1–2, cantidad
  0,3–0,6); penalizar halos visibles.

## P3.3.4 (partiendo de ~2200 × 1470 tras enderezar)

| Destino | Recorte | Píxeles antes de escalar | Resultado |
|---|---|---|---|
| Post 1080 × 1080 | 1:1 | ~1470 × 1470 | Se reduce: correcto |
| Miniatura 1280 × 720 | 16:9 | ~2200 × 1237 | Se reduce: correcto |
| Foto 15 × 10 cm a 300 ppp | 3:2 | ~2200 × 1470 | Necesita 1772 × 1181: se reduce, correcto |
| Portada 3000 × 3000 a 300 ppp | 1:1 | ~1470 × 1470 | **No llega**: habría que ampliar ×2 |

La que no se puede hacer bien es la **portada**: con 1470 px a 300 ppp solo da
para unos 12,4 cm de lado, y ampliarla a 3000 inventa la mitad de los píxeles en
cada dirección. Respuestas válidas: usar otra foto con más resolución, usar esta
más pequeña dentro de la portada o como fondo difuminado, o asumir la ampliación
diciendo que bajará la calidad. No es válido «cambio los ppp a 300 y ya».
