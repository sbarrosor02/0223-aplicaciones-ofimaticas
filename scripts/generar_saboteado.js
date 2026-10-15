// Genera web/descargas/reto-documento-saboteado.docx
//
// Documento de partida del reto colaborativo "El documento saboteado" (Tema 2).
// Impreso parece correcto, pero esta construido con TRAMPAS: formato manual
// donde deberia haber estilos, campos o herramientas automaticas. Los equipos
// tienen que encontrarlas, explicarlas y arreglarlas.
//
// La lista de trampas y su solucion NO esta aqui comentada en detalle a
// proposito: el repositorio es publico. Esta en
// temario/soluciones/ut02-reto-documento-saboteado-solucion.md.
// Si se cambia el documento, hay que revisar ese solucionario.
//
// Uso:  NODE_PATH=<ruta global de npm> node scripts/generar_saboteado.js

const {
  Document, Packer, Paragraph, TextRun, Footer, TabStopType,
  CommentRangeStart, CommentRangeEnd, CommentReference,
} = require('docx');
const fs = require('fs');
const path = require('path');

const ES = { value: 'es-ES' };
const run = (text, extra = {}) => new TextRun({ text, language: ES, ...extra });
const p = (children, extra = {}) => new Paragraph({ children: [].concat(children), ...extra });
const texto = (t, extra = {}) => p(run(t), extra);
const vacio = () => new Paragraph({ children: [] });

// Aspecto de "Titulo 1" conseguido a mano, sin estilo.
const tituloFalso = t => p(run(t, { bold: true, size: 32, color: '2F5496', font: 'Calibri Light' }),
  { spacing: { before: 360, after: 160 } });
const subtituloFalso = t => p(run(t, { bold: true, size: 26, color: '2F5496', font: 'Calibri Light' }),
  { spacing: { before: 240, after: 120 } });

const lineaIndice = (t, pag) => p([run(t), run('\t' + pag)],
  { tabStops: [{ type: TabStopType.RIGHT, position: 9000, leader: 'dot' }] });

const children = [
  // ---------- Portada ----------
  p(run('Guía de bienvenida al aula taller', { bold: true, size: 52, color: '1F3864', font: 'Calibri Light' }),
    { spacing: { before: 1200, after: 200 } }),
  p(run('CFGM Sistemas Microinformáticos y Redes · IES Valle del Jerte', { size: 26, color: '595959' })),
  p(run('Curso 2026/2027', { size: 26, color: '595959' }), { spacing: { after: 600 } }),

  p(run('Índice', { bold: true, size: 28, color: '2F5496' }), { spacing: { after: 160 } }),
  lineaIndice('1. Normas del aula', '2'),
  lineaIndice('2. Horario de uso', '2'),
  lineaIndice('3. Cómo pedir material', '3'),
  lineaIndice('4. Contactos', '3'),
];

// Relleno hasta la pagina siguiente a base de Intro.
for (let i = 0; i < 24; i++) children.push(vacio());

// ---------- 1. Normas ----------
children.push(
  tituloFalso('1. Normas del aula'),
  texto('        El aula taller es un espacio compartido por varios grupos. Para que todo el mundo  encuentre los equipos en buen estado, es imprescindible respetar unas normas básicas de uso y de seguridad.'),
  texto('        Estas normas se aplican tanto en las horas de clase como en las horas de uso libre, y su incumplimiento  se comunicará al tutor o tutora del grupo.'),
  texto('1. Entra en el aula solo cuando esté el profesor o la profesora.'),
  texto('2. No comas ni bebas junto a los equipos.'),
  texto('4. Antes de abrir un equipo, desconéctalo de la corriente y usa la pulsera antiestática.'),
  texto('5. Al terminar, apaga el equipo, recoge el puesto y coloca la silla.'),
  texto('6. Si algo no funciona, no intentes repararlo por tu cuenta: anótalo en el parte de incidencias.'),
);

// ---------- 2. Horario ----------
children.push(
  tituloFalso('2. Horario de uso'),
  texto('El aula está disponible en las franjas siguientes. Fuera de ellas, se reserva  para mantenimiento y para las guardias del departamento.'),
  texto('Día              Mañana               Tarde'),
  texto('Lunes            8:30 – 14:30         16:00 – 18:00'),
  texto('Martes           8:30 – 14:30         cerrado'),
  texto('Miércoles        8:30 – 14:30         16:00 – 18:00'),
  texto('Jueves           8:30 – 14:30         cerrado'),
  texto('Viernes          8:30 – 13:30         cerrado'),
  p(run('Tabla 1. Horario del aula taller', { italics: true, size: 18, color: '44546A' }), { spacing: { after: 200 } }),
  texto('Como se ve en la Tabla 2, las tardes de martes, jueves y viernes el aula permanece cerrada.'),
);

// ---------- 3. Prestamo ----------
children.push(
  tituloFalso('3. Préstamo de material'),
  p([
    run('El departamento presta herramientas y componentes para las prácticas.'),
    run('Para pedir algo, rellena la hoja de préstamo que hay junto a la puerta,', { break: 1 }),
    run('indica tu nombre, el material y la fecha, y devuélvelo antes de que', { break: 1 }),
    run('termine la sesión.', { break: 1 }),
  ]),
  texto('Se puede pedir prestado:'),
  texto('-  Destornilladores de precisión y pulseras antiestáticas.'),
  texto('-  Comprobadores de cable de red y crimpadoras.'),
  texto('-  Discos duros y módulos de memoria para pruebas.'),
  p([
    run('Para las prácticas de redes se utiliza siempre cable de red'),
    run('1', { superScript: true }),
    run(' del armario del fondo; no cojas rollos de otras aulas.'),
  ]),
  p(run('Recuerda que el material es de todos: si algo se rompe mientras lo usas, avisa inmediatamente. Nadie te va a reñir por un accidente, pero sí por esconderlo.',
    { font: 'Times New Roman', size: 25, shading: { fill: 'F2F2F2' } })),
);

// ---------- 3.1 ----------
children.push(
  subtituloFalso('3.1. Material que no sale del aula'),
  texto('Las fuentes de alimentación, las placas base de prueba y el polímetro se usan siempre dentro del aula taller y bajo supervisión.'),
);

// ---------- 4. Contactos ----------
children.push(
  tituloFalso('4. Contactos'),
  p([
    new CommentRangeStart(0),
    run('Para cualquier duda sobre el aula, habla con el jefe del departamento de Informática y Comunicaciones o escribe al correo del departamento.'),
    new CommentRangeEnd(0),
    new TextRun({ children: [new CommentReference(0)] }),
  ]),
  texto('Las incidencias urgentes (olor a quemado, chispas, un equipo que no se apaga) se comunican en el momento al profesor que esté en el aula.'),
  p([
    run('Bienvenido o bienvenida, y que lo disfrutes.'),
    run(' Nota privada: cambiar la contraseña del wifi del aula antes de irme, que me la sé de memoria.', { vanish: true }),
  ]),
  vacio(),
  p(run('¹ Se refiere a cable UTP de categoría 6.', { size: 18 })),
);

const doc = new Document({
  creator: 'El becario saboteador',
  lastModifiedBy: 'El becario saboteador',
  title: 'Guía de bienvenida al aula taller',
  description: 'Versión final. Que no la toque nadie.',
  styles: { default: { document: { run: { font: 'Calibri', size: 22 }, paragraph: { spacing: { after: 160, line: 259 } } } } },
  comments: {
    children: [{
      id: 0,
      author: 'El becario saboteador',
      initials: 'BS',
      date: new Date('2026-06-20T13:45:00'),
      children: [new Paragraph({ children: [new TextRun('No arregléis nada de esto, que así nadie se entera de que lo hice todo a mano 😈')] })],
    }],
  },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 } } },
    footers: {
      default: new Footer({
        children: [p(run('Guía de bienvenida al aula taller · Página 1', { size: 18, color: '7F7F7F' }), { alignment: 'right' })],
      }),
    },
    children,
  }],
});

const destino = path.join(__dirname, '..', 'web', 'descargas', 'reto-documento-saboteado.docx');
Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(destino, buf);
  console.log('Generado', destino);
});
