// Genera web/descargas/pc2-material-partida.docx
//
// Material de partida de la Practica de Control 2 (integra 2.0 a 2.5).
//
// Dos premisas deliberadas, como en el PC1:
//  1. TODO va en estilo Normal, sin un solo titulo aplicado ni negritas.
//     Son los alumnos quienes deben estructurarlo para poder generar la
//     tabla de contenido.
//  2. Lleva 15 faltas de ortografia plantadas (tildes que faltan y una
//     transposicion), para que "revisar la ortografia" sea un criterio
//     objetivamente comprobable y no una impresion.
//
// El resto del texto va correctamente acentuado, para que el corrector no
// genere falsos positivos y las faltas plantadas destaquen.
//
// Uso:  NODE_PATH=<ruta global de npm> node scripts/generar_pc2.js

const { Document, Packer, Paragraph, TextRun } = require('docx');
const fs = require('fs');
const path = require('path');

const T = t => ({ t });                 // parrafo normal
const H = t => ({ t, hueco: true });    // linea que hara de titulo

const lineas = [
  T('Dossier de servicios'),
  T('Soporte Integral Jerte'),
  T('Servicios de informatica para empresas y centros educativos'),   // falta 1: informatica
  T(''),

  H('Quienes somos'),
  T('Soporte Integral Jerte es una empresa dedicada al montaje, mantenimiento y reparacion de equipos informáticos, con sede en Plasencia y servicio en toda la comarca.'),  // falta 2: reparacion
  T('Nuestro equipo está formado por tecnicos titulados en Sistemas Microinformáticos y Redes, con experiencia tanto en entornos domésticos como en pequeñas y medianas empresas.'),  // falta 3: tecnicos
  T('Trabajamos con un principio sencillo: explicar siempre al cliente qué se ha hecho y por qué. Cada intervención se documenta y se entrega por escrito.'),
  T('[FIGURA: fotografía del taller de reparación]'),

  H('Servicio 1. Montaje y ampliacion de equipos'),   // falta 4: ampliacion
  T('En qué consiste'),
  T('Montamos equipos a medida según las necesidades reales del cliente, sin vender componentes que no vaya a aprovechar. También ampliamos equipos existentes cuando sale más rentable que sustituirlos.'),
  T('Qué incluye'),
  T('El servicio incluye el asesoramiento previo, la compra de los componentes, el montaje, la instalacion del sistema operativo y una comprobación de funcionamiento de al menos 24 horas antes de la entrega.'),  // falta 5: instalacion
  T('[TABLA: comparativa de tres configuraciones tipo con componentes y precio orientativo]'),
  T('Plazos y garantia'),   // falta 6: garantia
  T('El plazo habitual es de tres a cinco días laborables desde la aprobación del presupuesto. Todos los equipos montados por nosotros llevan dos años de garantía sobre el montaje, independientemente de la de cada componente.'),
  T('[FIGURA: equipo montado con los cables organizados]'),

  H('Servicio 2. Instalacion y configuracion de sistemas'),   // faltas 7 y 8
  T('En qué consiste'),
  T('Instalamos y configuramos sistemas operativos de escritorio y de servidor, dejando el equipo listo para trabajar: controladores actualizados, cuentas de usuario creadas con los permisos adecuados y las aplicaciones que el cliente necesite.'),
  T('Qué incluye'),
  T('Incluye la verificación de la imagen de instalación, el particionado del disco separando sistema y datos, la configuración del cortafuegos y la primera copia de seguridad.'),
  T('Un detalle que marca la diferencia: dejamos siempre una cuenta de usuario sin privilegios de administrador para el trabajo diario. Es la medida de seguridad más barata y la que más incidencias evita.'),
  T('[FIGURA: pantalla de particionado durante una instalación]'),
  T('Casos especiales'),
  T('Para centros educativos preparamos una imagen común que se despliega en todas las aulas, de forma que cualquier equipo pueda sustituirse por otro sin reconfigurar nada.'),

  H('Servicio 3. Redes y conexion'),   // falta 9: conexion
  T('En qué consiste'),
  T('Diseñamos, montamos y documentamos redes locales para oficinas y aulas: cableado, electrónica de red, direccionamiento y salida a internet.'),
  T('Qué incluye'),
  T('Realizamos el estudio previo del local, el tendido y crimpado del cableado, la configuración del direccionamiento con reserva de direcciones para servidores e impresoras, y las pruebas de conectividad documentadas.'),
  T('[TABLA: plan de direccionamiento tipo con rangos y asignación]'),
  T('Entregamos siempre un plano de la instalación y una tabla con qué hay conectado en cada punto. Sin esa documentación, cualquier avería futura se convierte en una búsqueda a ciegas.'),
  T('[FIGURA: esquema de la topología de una red de aula]'),

  H('Servicio 4. Copias de seguridad y recuperacion de datos'),   // falta 10: recuperacion
  T('En qué consiste'),
  T('Diseñamos una estrategia de copias adaptada al volumen de datos y al tiempo que el cliente puede permitirse estar parado, y la probamos.'),
  T('Qué incluye'),
  T('Incluye la configuración de copias automáticas, la verificación periódica de que se están haciendo, y al menos una prueba de restauración completa al año.'),
  T('Insistimos mucho en esto último: una copia de seguridad que no se ha restaurado nunca no es una copia de seguridad, es una suposición.'),
  T('Diagnostico y recuperación'),   // falta 11: Diagnostico
  T('Cuando ya se ha perdido la información, realizamos un diagnóstico del soporte y, si es viable, la recuperación en laboratorio. El presupuesto de recuperación se da siempre antes de empezar y sin compromiso.'),
  T('[FIGURA: unidad de disco conectada a la estación de diagnóstico]'),

  H('Tarifas y condiciones'),
  T('Nuestras tarifas se calculan por hora de trabajo del tecnico más el coste de los materiales, sin recargos por desplazamiento dentro de la comarca.'),   // falta 12: tecnico
  T('[TABLA: tarifas por tipo de servicio, con precio por hora y mínimo facturable]'),
  T('La sustitucion de un componente en garantía no tiene coste de mano de obra si el montaje lo hicimos nosotros.'),   // falta 13: sustitucion
  T('Para contratos de mantenimineto anual aplicamos un descuento del quince por ciento sobre la tarifa horaria y damos prioridad en la atención de incidencias.'),   // falta 14: mantenimineto
  T('Todos los precios indicados son sin IVA.'),

  H('Contacto'),
  T('Puede solicitar presupuesto sin compromiso por correo electronico, por teléfono o pasando por el taller en horario comercial.'),   // falta 15: electronico
  T('Soporte Integral Jerte. Avenida de la Vera 14, 10600 Plasencia (Cáceres).'),
  T('Atendemos de lunes a viernes, de 9:00 a 14:00 y de 16:30 a 20:00.'),
];

const doc = new Document({
  creator: 'IES Valle del Jerte',
  title: 'PC2 · Material de partida',
  description: 'Texto en bruto del dossier de servicios. Todo en Normal y con faltas plantadas, a proposito.',
  sections: [{
    children: lineas.map(l => new Paragraph({
      spacing: { before: l.hueco ? 240 : 0, after: 120 },
      children: [new TextRun({ text: l.t })],
    })),
  }],
});

const destino = path.join(__dirname, '..', 'web', 'descargas', 'pc2-material-partida.docx');
Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(destino, buf);
  console.log('escrito:', destino);
  console.log(buf.length, 'bytes |', lineas.length, 'parrafos');
});
