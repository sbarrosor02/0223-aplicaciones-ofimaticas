---
modulo: "0223"
ut: "2-reto"
titulo: "Reto en equipo: el documento saboteado"
ra: ["RA2"]
ce: []
base_de: ["RA2.b", "RA2.f"]
sesiones: 1
agrupamiento: "equipos de 3, un ordenador por equipo para arreglar"
evaluable: false
estado: publicado
actualizado: 2026-10-15
---

# Reto en equipo · El documento saboteado

Página del alumnado: `web/temas/ut02-ejercicios-reto-saboteado.html`.
Material: `web/descargas/reto-documento-saboteado.docx`, generado con
`scripts/generar_saboteado.js`.
Solucionario y pruebas de estrés: `temario/soluciones/ut02-reto-documento-saboteado-solucion.md`
(no se enlaza desde la web).

## Para qué

Una sesión suelta (55 min) que rompe la dinámica de trabajo individual con el
CV. La programación pide «retos prácticos» y «trabajo cooperativo» en la
metodología; este reto repasa de golpe los subtemas 2.0 a 2.6 desde el lado
contrario: en vez de construir bien, **detectar lo que está mal construido**.

El aprendizaje que se busca es uno solo y muy transferible: *un documento que
se ve bien puede estar mal hecho, y se nota en cuanto alguien lo modifica*. Es
la razón de fondo de los estilos (2.2), los campos (2.4) y la limpieza antes de
entregar (2.6), y la base de las plantillas (CE b) y los manuales (CE f).

## El tema

Las bases de un **torneo de EA Sports FC** del instituto, escritas por un
capitán eliminado el año anterior que se venga saboteándolas. Se eligió fútbol
y videojuego a la vez porque engancha a la mayoría, y EA Sports FC es PEGI 3,
así que no plantea el problema de edad del GTA VI de la práctica colaborativa.
El alumnado hace de «VAR». No hace falta haber jugado: el documento solo trata
de normas, calendario y material.

Como en la práctica de Google Docs, todo el reto descansa en la estructura del
documento y no en el tema: cambiar de temática es reescribir los textos de
`scripts/generar_saboteado.js` y la columna «Dónde» del solucionario.

## Dinámica

- Equipos de 3 con **un solo ordenador para arreglar** (piloto). El detective
  puede investigar en su propio equipo, pero no arregla.
- Roles rotatorios: piloto → detective → notario → piloto. El profesor dice
  «¡Cambio!» hacia el minuto 15, 25 y 35.
- El alumnado sabe que hay **15 sabotajes** y que hay **uno extra** escondido.
  Saber el total genera tensión y evita que se den por satisfechos con 5.

| Minuto | Fase | Profesor |
|---|---|---|
| 0–5 | Preparación | Formar equipos, proyectar la página, recordar: solo el piloto toca el teclado |
| 5–35 | La caza | Pasear por los equipos. Dar pistas solo si las piden (−1). Marcar los cambios de rol |
| 35–45 | Prueba de estrés | Dictar las 8 pruebas del solucionario, una a una, con 1 min cada una. Anotar en la pizarra qué equipo la supera |
| 45–55 | Puesta en común | Recuento. Cada equipo explica un sabotaje. Preguntas de cierre |

## Marcador

Dibujar en la pizarra una tabla equipos × (registro, arreglos, estrés, extra,
pistas). Los puntos no van a la nota: es formativo. Si se quiere registrar
algo, la observación de los roles sirve como evidencia de actitud y trabajo en
equipo.

## Previsión de incidencias

| Situación | Qué hacer |
|---|---|
| Equipos de 2 | Se fusionan detective y notario; la rotación pasa a ser de dos |
| Equipos de 4 | Dos detectives, uno con la mitad del documento cada uno |
| El índice falso no se ve como falso | Pista: «haced clic encima; ¿se pone gris?». Un índice real es un campo |
| «Arreglan» el número de página escribiendo 2 y 3 | No puntúa: es la misma trampa repetida. La prueba de estrés 6 lo deja en evidencia |
| LibreOffice en algún puesto | El reto funciona igual (Ver › Marcas de formato, Navegador F5, Estilos F11). Inspeccionar documento no existe: el texto oculto y el comentario se buscan a mano |
| Terminan pronto | Que exporten a PDF con marcadores (enlace con 2.5) y comprueben que aparecen los cuatro apartados |

## Enlaces con el resto del tema

- **2.0 y 2.1**: marcas de formato, buscar y reemplazar con caracteres especiales.
- **2.2**: estilos de título, listas automáticas, sangrías, saltos de página, pie con campo.
- **2.3**: tablas reales en lugar de columnas alineadas con espacios.
- **2.4**: tabla de contenido, títulos de tabla, referencias cruzadas y notas al pie.
- **2.6**: comentarios olvidados, texto oculto, propiedades e Inspeccionar documento.
- **Va a la PC2 y al 2.7**: es la lista de comprobación que tendrían que pasar sus propios documentos.
