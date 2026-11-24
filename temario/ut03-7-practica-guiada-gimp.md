---
modulo: "0223"
tipo: "práctica guiada"
codigo: "p37"
titulo: "Práctica guiada de GIMP: el cartel del concierto"
ra: "RA5"
ce: ["c", "d", "e", "f"]
integra: ["3.1", "3.3", "3.4", "3.5", "3.6"]
horas: 3
evaluable: true
estado: publicado
actualizado: 2026-11-24
---

# Práctica guiada de GIMP (p37)

Página: `web/temas/ut03-gimp-guiada.html`.

## Por qué existe

A petición del profesor (24/11/2026): los pasos de GIMP estaban repartidos entre
3.3, 3.4, 3.5 y 3.6 y costaba explicarlos. Esta práctica los junta en **una sola
pieza de principio a fin**, con los menús, los valores y una imagen del resultado
esperado en cada paso. Después viene el punto de control (p38), que es el mismo
recorrido sin guía.

## Material

`web/descargas/gimp-guiada-material.zip`, generado con
`python scripts/generar_material_gimp.py`:

| Archivo | Qué es |
|---|---|
| `guiada-escenario.jpg` | Escenario inventado, 2400 × 1600: girado 3°, oscurecido (`0,02 + 0,55·x^1,5`), dominante naranja (× 1,00 / 0,84 / 0,60), 10 motas (pared gris y conos de luz) y un letrero de SALIDA colgado de un cable |
| `guiada-guitarra.jpg` | La guitarra del 3.4 sobre pared clara con sombra |
| `guiada-textura.jpg` | La textura de papel del 3.4 |
| `guiada-logo.png` | Logotipo de Cerezo Rock con las letras en crema, 800 × 800, transparente |

Imágenes de cada paso (`p37-01` a `p37-14`) con `scripts/generar_resultados_gimp.py`,
que también llama `generar_resultados_esperados.py`.

## Guion (3 h)

- **A · Retocar la foto (1 h, pasos 1–7)**: XCF con el original oculto; Medir y
  Enderezar (≈ 3°); Recortar 3:2 (≈ 2200 × 1467); Niveles en Valor 5 · 1,50 · 145;
  cuentagotas gris en la rejilla del amplificador; Clonar (letrero y cable) y
  Saneado (10 motas); Enfocar 1,5 / 0,5; exportar JPG 85 sin Exif.
- **B · Cartel A5 (1 h 30 min, pasos 8–13)**: lienzo 1819 × 2551 a 300 ppp relleno
  `#1e1a24`; ocho guías (35, 94, 1725, 1784 / 35, 94, 2457, 2516); foto escalada a
  1819 de ancho arriba con máscara blanca y degradado blanco→negro de y ≈ 750 al
  final de la foto; guitarra con Selección difusa (umbral 30), Invertir, Encoger 1,
  Difuminar 2, Pegar como capa nueva, altura 1000, sombra arrojada 14/18/16/0,6;
  textura escalada a altura 2551 (desplazamiento X −791) en Multiplicar al 60 %;
  textos (título 170 px Sans-serif Bold `#f6efe6`, subtítulo 84 px `#f28c9e`),
  franja negra 0,2110 de 1819 × 220 al 50 %, datos 54 y 44 px, logotipo 280 × 280
  en (1405, 230); capas nombradas.
- **C · Exportar (30 min, pasos 14–15)**: metadatos de autor y copyright; PDF
  (154 × 216 mm); duplicar, aplanar, recortar posición 35, 182 tamaño 1749 × 2186
  (4:5 sin sangrado y sin perder textos), escalar a 1080 × 1350, JPG 85.

## Entrega `<usuario>_p37.zip`

Memoria `<usuario>_p37.pdf` (cinco capturas: ángulo, Niveles, limpieza al 100 %,
diálogo Capas, PDF con su tamaño), `a01.xcf` + `a01.jpg` (foto), `a02.xcf`
(cartel), `a03.pdf` + `a03.jpg` (salidas).

## Avisos para el profesor

- Sin GIMP en el entorno de generación: las imágenes de cada paso se dibujan con
  Pillow imitando el resultado, no son capturas de la interfaz. Si quieres
  capturas reales de los cuadros de diálogo, se pueden añadir debajo de cada
  paso.
- Menús de GIMP 3 en español; por confirmar en el aula: *Desplazamiento X / Y*
  en los atributos de capa (doble clic en la miniatura), *Elegir el punto gris*
  en Niveles y *Capas como páginas* al exportar PDF. Se da siempre una
  alternativa (arrastrar con Mover, Balance de blancos).
- La sombra arrojada de GIMP 3 es un filtro no destructivo: queda dentro de la
  capa y la capa de texto sigue siendo editable.
- Se corrige en esta rama el nombre del menú de guías del 3.6 (*Guía nueva…*,
  como en el 3.4).
