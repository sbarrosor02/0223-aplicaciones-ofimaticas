// Genera web/descargas/dossier-proyectos-sin-estructurar.docx
//
// Documento largo de partida para el bloque 2.4 (esquema, tabla de contenido,
// tabla de ilustraciones, referencias cruzadas y notas al pie).
//
// TODO va en estilo Normal, sin negritas ni estilos de titulo: son los alumnos
// quienes deben aplicar Titulo 1 y Titulo 2 para que la tabla de contenido
// pueda generarse. Si este archivo llevara ya los estilos puestos, el ejercicio
// no tendria sentido.
//
// Uso:  NODE_PATH=<ruta global de npm> node scripts/generar_dossier.js

const { Document, Packer, Paragraph, TextRun } = require('docx');
const fs = require('fs');
const path = require('path');

// Cada entrada es una linea del documento. Marcamos con un prefijo interno
// que NO se escribe en el docx; solo sirve para saber si dejamos hueco extra.
const T = t => ({ t });          // texto normal
const H = t => ({ t, hueco: true }); // linea que hara de titulo (hueco antes)

const lineas = [
  T('Dossier de proyectos'),
  T('Ciclo Formativo de Grado Medio en Sistemas Microinformaticos y Redes'),
  T('Curso 2026/2027'),
  T(''),

  H('Presentacion'),
  T('Este dossier recoge los cuatro proyectos practicos realizados durante el primer trimestre del ciclo. Cada uno describe el objetivo planteado, el procedimiento seguido, las incidencias encontradas y el resultado obtenido.'),
  T('El objetivo del documento es doble: dejar constancia del trabajo realizado y servir como material de consulta para cursos posteriores. Por ese motivo se ha intentado describir cada procedimiento con el detalle suficiente para que pueda repetirse.'),
  T('Todas las capturas de pantalla se han tomado en los equipos del aula taller, con el sistema operativo instalado por el propio alumnado.'),

  H('Proyecto 1. Montaje de un equipo de sobremesa'),
  T('Objetivo'),
  T('Montar desde cero un equipo de sobremesa funcional a partir de componentes sueltos, comprobar que arranca correctamente y documentar el proceso.'),
  T('Componentes utilizados'),
  T('El equipo se monto con una placa base microATX, un procesador de cuatro nucleos, dos modulos de memoria RAM de 8 GB cada uno, una unidad de estado solido de 500 GB, una fuente de alimentacion de 500 W y una torre con ventilacion frontal.'),
  T('[TABLA: relacion de componentes con modelo, cantidad y precio aproximado]'),
  T('Proceso de montaje'),
  T('Antes de manipular ningun componente se utilizo la pulsera antiestatica y se trabajo sobre una superficie despejada. El orden seguido fue: instalacion del procesador y el disipador sobre la placa base, colocacion de los modulos de memoria, fijacion de la placa en la torre, conexion de la fuente de alimentacion, montaje de la unidad de almacenamiento y conexionado final de los cables del panel frontal.'),
  T('[FIGURA: placa base con el procesador y el disipador ya instalados]'),
  T('El paso que mas tiempo requirio fue el conexionado del panel frontal, ya que los conectores de encendido, reinicio y LED de actividad son de pequeno tamano y su polaridad debe respetarse. Se consulto el manual de la placa base para identificar cada pin.'),
  T('Incidencias'),
  T('En el primer arranque el equipo no dio senal de video. Tras revisar el montaje se comprobo que uno de los modulos de memoria no estaba correctamente encajado: las pestanas laterales no habian cerrado del todo. Una vez reasentado el modulo, el equipo arranco con normalidad.'),
  T('Resultado'),
  T('El equipo arranco correctamente y la BIOS reconocio los 16 GB de memoria y la unidad de estado solido. El tiempo total de montaje fue de aproximadamente dos sesiones de clase.'),

  H('Proyecto 2. Instalacion y configuracion de un sistema operativo'),
  T('Objetivo'),
  T('Instalar un sistema operativo sobre el equipo montado en el proyecto anterior, realizando un particionado manual y dejando el sistema configurado y actualizado.'),
  T('Preparacion del medio de instalacion'),
  T('Se descargo la imagen ISO oficial y se verifico su integridad comparando la suma de comprobacion publicada por el fabricante con la calculada localmente. A continuacion se preparo una unidad USB de arranque.'),
  T('[FIGURA: comprobacion de la suma de verificacion de la imagen ISO]'),
  T('La verificacion de la suma de comprobacion es un paso que suele omitirse, pero permite detectar descargas corruptas o manipuladas antes de instalar nada.'),
  T('Particionado'),
  T('Se opto por un particionado manual con una particion de sistema y una particion de datos independiente. De esta forma, una reinstalacion futura del sistema operativo no obliga a mover los datos del usuario.'),
  T('[TABLA: esquema de particiones con tamano, sistema de archivos y punto de montaje]'),
  T('Configuracion posterior'),
  T('Tras la instalacion se aplicaron las actualizaciones pendientes, se instalaron los controladores del fabricante, se configuro la cuenta de usuario sin privilegios de administrador para el uso diario y se activo el cortafuegos.'),
  T('[FIGURA: ventana de actualizaciones del sistema tras la instalacion]'),
  T('Incidencias'),
  T('El adaptador de red inalambrico no fue reconocido durante la instalacion. Fue necesario descargar el controlador desde otro equipo, copiarlo en una unidad USB e instalarlo manualmente.'),

  H('Proyecto 3. Red local del aula'),
  T('Objetivo'),
  T('Configurar una red local para un grupo de equipos del aula, asignar direccionamiento, comprobar la conectividad y documentar la topologia resultante.'),
  T('Direccionamiento'),
  T('Se utilizo un direccionamiento privado de clase C con mascara de 24 bits. Los equipos de los alumnos recibieron direccion por DHCP dentro de un rango reservado, mientras que el servidor y la impresora de red se configuraron con direccion estatica fuera de ese rango, para evitar conflictos.'),
  T('[TABLA: asignacion de direcciones por equipo, con nombre, direccion y tipo de asignacion]'),
  T('Topologia'),
  T('La topologia empleada fue en estrella, con un conmutador central al que se conectan todos los equipos mediante cable de par trenzado. El conmutador se conecta a su vez al router del centro, que proporciona la salida a internet.'),
  T('[FIGURA: esquema de la topologia en estrella del aula]'),
  T('Comprobaciones'),
  T('La conectividad se comprobo en tres niveles: primero contra la propia interfaz, despues contra la puerta de enlace y por ultimo contra un nombre de dominio externo, para distinguir un problema de red de un problema de resolucion de nombres.'),
  T('Este orden de comprobacion es importante: permite localizar en que punto se rompe la comunicacion en lugar de limitarse a constatar que no hay internet.'),
  T('Incidencias'),
  T('Dos equipos no obtenian direccion por DHCP. Se localizo el problema en un cable de red con un conector mal crimpado, que se sustituyo por uno nuevo comprobado con el tester.'),

  H('Proyecto 4. Copias de seguridad y recuperacion'),
  T('Objetivo'),
  T('Disenar y probar una estrategia de copias de seguridad para los datos del aula, incluyendo una prueba real de restauracion.'),
  T('Estrategia adoptada'),
  T('Se siguio la regla de las tres copias: el dato original, una copia en un soporte distinto dentro del aula y una tercera copia fuera del aula. Se establecio una copia completa semanal y copias incrementales diarias.'),
  T('Segun diversos estudios del sector, un porcentaje muy elevado de las organizaciones que sufren una perdida grave de datos sin copia de seguridad no continua su actividad. Esta cifra se repite con frecuencia en la documentacion tecnica y conviene citarla siempre indicando la fuente.'),
  T('[TABLA: calendario de copias con tipo, dia, soporte y responsable]'),
  T('Prueba de restauracion'),
  T('Una copia de seguridad que no se ha probado no es una copia de seguridad. Por ese motivo se realizo una restauracion completa sobre un equipo distinto del original, midiendo el tiempo necesario y comprobando la integridad de los archivos recuperados.'),
  T('[FIGURA: proceso de restauracion en curso sobre el equipo de pruebas]'),
  T('Resultado'),
  T('La restauracion se completo correctamente. El tiempo empleado fue superior al previsto, lo que llevo a revisar el procedimiento y a documentar el tiempo real para futuras incidencias.'),

  H('Conclusiones'),
  T('Los cuatro proyectos comparten una misma leccion: la parte tecnica rara vez es la que da problemas. Las incidencias que aparecieron tuvieron que ver con un modulo mal encajado, un cable mal crimpado, un controlador que faltaba y un tiempo de restauracion mal estimado.'),
  T('De ahi la importancia de documentar el trabajo. Un procedimiento escrito permite repetir lo que funciono y evitar lo que fallo, tanto a uno mismo como a quien venga despues.'),
  T('El material recogido en este dossier se incorporara al portafolio del ciclo y servira de base para la memoria de practicas.'),

  H('Fuentes y recursos consultados'),
  T('Manual tecnico de la placa base utilizada en el proyecto 1.'),
  T('Documentacion oficial del sistema operativo instalado en el proyecto 2.'),
  T('Apuntes del modulo de Redes Locales, curso 2026/2027.'),
  T('Apuntes del modulo de Montaje y Mantenimiento de Equipos, curso 2026/2027.'),
];

const doc = new Document({
  creator: 'IES Valle del Jerte',
  title: 'Dossier de proyectos (sin estructurar)',
  description: 'Documento de partida del bloque 2.4. Todo en estilo Normal, a proposito.',
  sections: [{
    children: lineas.map(l => new Paragraph({
      // Sin heading, sin bold: estilo Normal puro.
      spacing: { before: l.hueco ? 240 : 0, after: 120 },
      children: [new TextRun({ text: l.t })],
    })),
  }],
});

const destino = path.join(__dirname, '..', 'web', 'descargas', 'dossier-proyectos-sin-estructurar.docx');
Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(destino, buf);
  console.log('escrito:', destino, '(' + buf.length + ' bytes,', lineas.length, 'parrafos)');
});
