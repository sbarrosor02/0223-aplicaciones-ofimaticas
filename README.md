# 0223 · Aplicaciones ofimáticas

Material didáctico del módulo profesional **0223 Aplicaciones ofimáticas** del
CFGM de Sistemas Microinformáticos y Redes (IES Valle del Jerte, Cáceres).
1.º curso, 7 h/semana, curso 2026/2027.

Currículo: **Decreto 272/2009**, de 28 de diciembre (DOE nº 1, 4 de enero de
2010). Los RA y CE se transcriben literalmente del decreto.

## Estructura

```
temario/     apuntes y material de cada tema (utNN-*.md con cabecera YAML)
practicas/   enunciados y plantillas de prácticas
examenes/    pruebas escritas y soluciones — NO se publica (en .gitignore)
web/         sitio del módulo, un apartado por tema
```

### web/

```
web/
├── index.html          portada: listado de temas
├── temas/utNN.html      una página por tema
├── assets/estilo.css    hoja de estilos (copia compartida con 0221)
└── datos/temas.json     índice de temas
```

Al crear o modificar un tema en `temario/` hay que: (1) generar/actualizar
`web/temas/utNN.html`, (2) actualizar `web/datos/temas.json` y (3) regenerar
`web/index.html`.

## Estado

- **Tema 0 — Presentación y evaluación inicial**: publicado.
  Prueba diagnóstica autocorregible en `web/temas/ut00.html`. No evalúa RA ni CE
  y no cuenta para la nota.
- **Tema 1 — Instalación y actualización (RA1)**: publicado.
- **Tema 2 — Procesadores de texto (RA2, 60 h)**: en progreso. Al ser el bloque
  más grande del módulo se reparte en **siete subtemas** (2.1 a 2.7), cada uno
  con su propio archivo en `temario/` y su propia página en `web/temas/`
  (`ut02-1.html`…`ut02-7.html`), enlazados desde una página índice de tema
  (`web/temas/ut02.html`). Delante hay un subtema 2.0 de repaso (primer
  documento, edición básica), no evaluable y con horas no oficiales, para
  quien no llegue con ese nivel. Subtemas 2.0 a 2.7 publicados, con
  sus tres prácticas de control (PC3: proyecto final, manual con macros). Además hay una página de ejercicios guiados formativos
  (`web/temas/ut02-ejercicios.html`), con un hilo conductor único (construir
  el propio currículum vitae) para todo el tema.
- Taller de maquetación (T1–T5, trabajo diario) y caso práctico de la carta
  de un restaurante, con entrega en Moodle. Guía en
  `temario/ut02-taller-maquetacion.md`.
- Ejercicios guiados: bloques 2.0–2.7 disponibles. Reto en equipo «El documento
  saboteado» (formativo, 1 sesión; solucionario en `temario/soluciones/`). Práctica de control PC1
  publicada con especificaciones concretas y material descargable. Mapa de la
  cinta de Word disponible como recurso de consulta.
- **Tema 3 — Imagen digital (RA5, 28 h)**: en progreso. Seis subtemas (3.1 a
  3.6) con GIMP 3 como editor y un **laboratorio de imagen** propio
  (`web/temas/laboratorio-imagen.html`) para los conceptos. Ejercicios guiados
  con el hilo de una banda o un estudio de videojuegos. Publicados: 3.1 y
  3.2, laboratorio (5 herramientas, con visor de metadatos EXIF) y bloques 3.1 y
  3.2 de ejercicios.
- Resto de temas (4 a 10): pendientes.

## Navegación del aula

La portada ofrece accesos a apuntes, ejercicios y prácticas. El catálogo
`web/recursos.html` reúne el material y las descargas con filtros y búsqueda.
Las lecciones incluyen un índice de apartados adaptable a móvil.

Después de añadir o modificar páginas, ejecutar
`python scripts/actualizar_aula.py` para actualizar portada, catálogo e índices.
Consulta [la organización y el mantenimiento](docs/organizacion-aula.md).

### Calificación

`web/temas/calificacion.html` resume para el alumnado los capítulos 7 y 8 de
la programación: peso de cada RA, instrumentos (50 % pruebas, 40 % casos
prácticos, 10 % trabajo diario; RA9 dual con 40 % de empresa), requisitos para
aprobar, cálculo de las evaluaciones parciales y recuperaciones, con una
calculadora orientativa. Los pesos están también en `web/datos/temas.json`
(clave `calificacion`), y cada tema declara en `instrumentos` qué actividades
cuentan en cada instrumento: `actualizar_aula.py` genera con eso el recuadro
*Cómo se califica este tema* de la portada de cada tema.

### Dirección publicada

<https://sbarrosor02.github.io/0223-aplicaciones-ofimaticas/>

Se despliega sola: el workflow `.github/workflows/pages.yml` publica la carpeta
`web/` en GitHub Pages con cada `push` a `main` que la toque. Es HTML/CSS plano,
sin dependencias ni build; también se abre con doble clic desde el disco.
