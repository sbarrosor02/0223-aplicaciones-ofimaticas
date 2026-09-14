---
modulo: "0223"
ut: 1
titulo: "Instalación y actualización de aplicaciones ofimáticas"
ra: ["RA1"]
ce: ["RA1.a", "RA1.b", "RA1.c", "RA1.d", "RA1.e", "RA1.f", "RA1.g", "RA1.h", "RA1.i"]
horas: 12
evaluacion: 1
---

# Tema 1 · Instalación y actualización de aplicaciones ofimáticas

> Primer tema evaluable del módulo. Cubre **RA1 completo** (los nueve CE) y es
> el tema con menos carga teórica y más taller: casi todo se hace sobre máquina
> virtual.

## Resultado de aprendizaje y criterios de evaluación

**RA1.** Instala y actualiza aplicaciones ofimáticas, interpretando
especificaciones y describiendo los pasos a seguir en el proceso.

| CE | Enunciado |
|----|-----------|
| a | Se han identificado y establecido las fases del proceso de instalación. |
| b | Se han respetado las especificaciones técnicas del proceso de instalación. |
| c | Se han configurado las aplicaciones según los criterios establecidos. |
| d | Se han documentado las incidencias. |
| e | Se han solucionado problemas en la instalación o integración con el sistema informático. |
| f | Se han eliminado y/o añadido componentes de la instalación en el equipo. |
| g | Se han actualizado las aplicaciones. |
| h | Se han respetado las licencias software. |
| i | Se han propuesto soluciones software para entornos de aplicación. |

## Objetivos de la unidad

- Instalar una suite ofimática en Windows y en Linux siguiendo un procedimiento
  escrito, no a base de «siguiente, siguiente, siguiente».
- Distinguir los tipos de licencia y razonar cuál procede en un escenario dado
  (aula de centro público, PYME, uso doméstico).
- Configurar la aplicación según unos criterios dados por el cliente, no según
  el gusto de cada uno.
- Diagnosticar y documentar una incidencia de instalación con un parte
  reutilizable el resto del curso.

## Contenidos

1. **Tipos de aplicaciones ofimáticas y entornos de explotación.** Suite
   monopuesto, en red y en la nube. LibreOffice, Microsoft 365, Google
   Workspace, OnlyOffice. → CE i
2. **Licencias de software.** Privativo y libre; GPL y MPL; EULA; OEM, retail y
   por volumen; suscripción frente a licencia perpetua; freeware y shareware.
   Implicaciones en un centro público. → CE h
3. **Requisitos y especificaciones técnicas.** Requisitos mínimos y
   recomendados, arquitectura, sistema operativo soportado, espacio en disco,
   permisos de administrador. → CE b
4. **Fases del proceso de instalación.** Planificar, obtener el software de
   origen fiable y verificarlo, instalar, configurar, comprobar y documentar.
   → CE a
5. **Tipos de instalación y componentes.** Típica, mínima y personalizada;
   idiomas y diccionarios; instalación desatendida; versión portable; gestores
   de paquetes (`winget`, `apt`) y repositorios. → CE f
6. **Configuración posterior.** Formato de guardado por defecto (ODF frente a
   OOXML), rutas, autoguardado, extensiones y plantillas de centro,
   personalización de la interfaz. → CE c
7. **Actualización y desinstalación.** Canales de actualización, actualizar
   frente a reinstalar, vuelta atrás, desinstalación limpia y restos de perfil.
   → CE g, f
8. **Diagnóstico e incidencias.** Instalador corrupto, permisos insuficientes,
   dependencias, convivencia de dos suites, perfil de usuario dañado. Registros,
   modo seguro y parte de incidencias. → CE d, e

## Temporalización (12 h)

| Sesión | Horas | Contenido |
|--------|-------|-----------|
| 1 | 2 | Tipos de suites y entornos. Licencias. Práctica 1.1 |
| 2 | 1 | Requisitos y preparación de la máquina virtual |
| 3 | 2 | Instalación en Windows: verificación e instalación personalizada. Práctica 1.2 |
| 4 | 2 | Instalación en Linux desde repositorio. Práctica 1.3 |
| 5 | 2 | Configuración «de centro» y extensiones. Práctica 1.4 |
| 6 | 2 | Actualización y desinstalación limpia. Incidencias. Prácticas 1.5 y 1.6 |
| 7 | 1 | Prueba escrita y cierre del portafolio del RA1 |

## Prácticas

| Código | Título | CE |
|--------|--------|----|
| P1.1 | Comparativa de suites y licencias para tres escenarios, con recomendación razonada | h, i |
| P1.2 | Instalación personalizada de LibreOffice en Windows verificando la suma de comprobación | a, b, f |
| P1.3 | Instalación de la misma suite en Linux desde repositorio y comparación de procedimientos | a, f |
| P1.4 | Configuración según criterios dados: formato por defecto, rutas, autoguardado y una extensión | c |
| P1.5 | Actualización de versión y desinstalación limpia, documentando el estado antes y después | g, f |
| P1.6 | Resolución de tres incidencias provocadas, con parte de incidencias cumplimentado | d, e |

## Evaluación (propuesta)

- Prácticas 1.1 a 1.6: **60 %**
- Documentación y partes de incidencias: **20 %**
- Prueba escrita: **20 %**

La plantilla de parte de incidencias que se estrena aquí es la misma que se
reutiliza en el **Tema 9 (RA9, técnicas de soporte)**, con mayor exigencia. Si
se cambia, cambiarla en los dos sitios.

## Recursos

- Máquina virtual con Windows y otra con una distribución Linux (una por
  alumno/a), preparadas en la sesión 2.
- Instaladores de LibreOffice y OnlyOffice descargados del sitio oficial, con
  sus ficheros de suma de comprobación.
- `web/temas/ut01.html` — material del alumnado y autocomprobación.

## Nota de montaje

El Tema 1 es el sitio donde queda montado el entorno de trabajo del curso
(máquinas virtuales, cuentas, estructura de carpetas y forma de entrega), para
no repetirlo en cada tema posterior.
