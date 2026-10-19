---
modulo: "0223"
ut: "3.2"
titulo: "Obtener imágenes: escáner, cámara y capturas"
ra: "RA5"
ce: ["b"]
horas: 3
evaluacion: 1
estado: publicado
actualizado: 2026-10-19
---

# UT3.2 — Obtener imágenes: escáner, cámara y capturas

Página: `web/temas/ut03-2.html`. Herramienta: apartado 5 del laboratorio
(visor de metadatos EXIF, con ubicación en OpenStreetMap y limpieza).

## Guion

1. Fuentes de imagen y qué vigilar en cada una.
2. Escanear: resolución según destino (tabla), óptica frente a interpolada, OCR,
   programas (escáner de Windows, NAPS2, Simple Scan) y, en clase, la app de
   escaneo del móvil (Google Drive, Notas del iPhone). OCR sin instalar nada:
   Acciones de texto de Recortes (Windows 11), Google Drive > Abrir con Documentos
   de Google, Google Lens. Cómo escanear bien con el móvil; los ppp del móvil no
   significan nada, cuentan los píxeles.
3. Cámara y móvil: megapíxeles frente a luz, zoom óptico frente a digital,
   HEIC y RAW, cómo pasar las fotos sin perder calidad (la mensajería recomprime).
4. Capturas de pantalla: atajos de Windows, Linux y captura con retardo de GIMP;
   PNG; capturar solo lo necesario y sin datos personales.
5. Metadatos EXIF y privacidad: qué guardan, por qué el GPS es un riesgo, cómo
   verlos y quitarlos (Windows, GIMP al exportar, laboratorio, móvil).

## Necesidades de aula

- **No hay escáner en el aula**: el periférico de adquisición es la cámara del
  móvil (CE b habla de «periféricos» en general). El escáner se ve como teoría
  (resolución según destino, óptica/interpolada, OCR) y puede entrar en la prueba.
- La P3.2.1 se hace en parejas con un móvil por pareja. Si nadie puede usar
  móvil: fotos simuladas `web/descargas/documento-fotografiado-1.jpg` y `-2.jpg`
  (generadas con `scripts/generar_documento_fotografiado.py`; hoja torcida, con
  sombra, contenido inventado) para el OCR y el PDF con Word.
- OCR: Recortes de Windows 11 (Acciones de texto) o Google Drive con la cuenta
  educativa. Comprobar antes que Recortes está actualizado en los equipos.
- Las prácticas con el móvil son voluntarias en cuanto al aparato: quien no
  tenga o no quiera usar el suyo usa la **foto de ejemplo** del laboratorio,
  que lleva un EXIF inventado con coordenadas de Cabezuela del Valle.

## Prácticas (CE b)

- **P3.2.1** Digitalizar un documento con el móvil: foto normal frente a app de
  escaneo, PDF de dos hojas, OCR y revisión de errores.
- **P3.2.2** Del móvil al ordenador por cable y por mensajería; comparar.
- **P3.2.3** Cuatro capturas (completa, ventana, zona, con retardo).
- **P3.2.4** Metadatos: tabla, quitarlos con dos métodos y comprobar.

## Ejercicios guiados (bloque 3.2)

Fotos o capturas del proyecto (sin personas salvo permiso; juegos libres para
las capturas), boceto del logo escaneado con el móvil (≥ 2000 px en el lado largo), limpieza de
metadatos y tabla de origen de cada imagen (prepara las licencias del 3.6).
