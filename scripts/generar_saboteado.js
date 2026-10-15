// Genera web/descargas/reto-documento-saboteado.docx
//
// Documento de partida del reto colaborativo "El documento saboteado" (Tema 2):
// las bases de un torneo de EA Sports FC del instituto.
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
  p(run('Torneo EA Sports FC', { bold: true, size: 52, color: '1F3864', font: 'Calibri Light' }),
    { spacing: { before: 1200, after: 200 } }),
  p(run('Bases oficiales del torneo del IES Valle del Jerte', { size: 26, color: '595959' })),
  p(run('Curso 2026/2027 · Recreos de noviembre', { size: 26, color: '595959' }), { spacing: { after: 600 } }),

  p(run('Índice', { bold: true, size: 28, color: '2F5496' }), { spacing: { after: 160 } }),
  lineaIndice('1. Normas del torneo', '2'),
  lineaIndice('2. Calendario de partidos', '2'),
  lineaIndice('3. Cómo apuntarse', '3'),
  lineaIndice('4. Contactos', '3'),
];

// Relleno hasta la pagina siguiente a base de Intro.
for (let i = 0; i < 24; i++) children.push(vacio());

// ---------- 1. Normas ----------
children.push(
  tituloFalso('1. Normas del torneo'),
  texto('        El torneo se juega por parejas en los recreos, con las consolas del aula taller. Para que todo el mundo  pueda jugar sus partidos a tiempo, hay que cumplir unas normas muy claras.'),
  texto('        Estas normas valen para todas las rondas, de la fase de grupos a la final, y quien no las cumpla  quedará descalificado sin derecho a reclamar.'),
  texto('1. Cada partido dura dos partes de 6 minutos, con la dificultad en Clase mundial.'),
  texto('2. Solo se pueden usar selecciones nacionales o clubes de primera división.'),
  texto('4. Si hay empate en las eliminatorias, se va directamente a los penaltis, sin prórroga.'),
  texto('5. Desconectar el mando o pausar sin motivo cuenta como partido perdido 3-0.'),
  texto('6. Nada de insultos ni piques fuera de la pantalla: el fair play también puntúa.'),
);

// ---------- 2. Calendario ----------
children.push(
  tituloFalso('2. Calendario de partidos'),
  texto('Todos los partidos se juegan en el recreo largo. Si una pareja no se presenta a la hora, pierde  el partido y pasa la siguiente.'),
  texto('Ronda               Día                    Partidos'),
  texto('Grupos              lunes 9 y martes 10    16'),
  texto('Octavos            miércoles 11          8'),
  texto('Cuartos              jueves 12              4'),
  texto('Semifinales        lunes 16               2'),
  texto('Final                 viernes 20             1'),
  p(run('Tabla 1. Calendario del torneo', { italics: true, size: 18, color: '44546A' }), { spacing: { after: 200 } }),
  texto('Como se ve en la Tabla 2, la final se juega el viernes 20 en el salón de actos, con proyector.'),
);

// ---------- 3. Inscripcion ----------
children.push(
  tituloFalso('3. Inscripción y material'),
  p([
    run('Las parejas se apuntan en la hoja que hay en la puerta del aula taller.'),
    run('Hay que poner los dos nombres, el curso y el equipo con el que', { break: 1 }),
    run('vais a jugar toda la fase de grupos, y no se puede cambiar', { break: 1 }),
    run('una vez empezado el torneo.', { break: 1 }),
  ]),
  texto('La organización pone:'),
  texto('-  Dos consolas con el juego instalado y actualizado.'),
  texto('-  Cuatro mandos con las baterías cargadas.'),
  texto('-  Una pantalla grande para la semifinal y la final.'),
  p([
    run('Todos los partidos se juegan en modo Saque inicial'),
    run('1', { superScript: true }),
    run(' y con la misma versión del juego para todo el mundo.'),
  ]),
  p(run('Recuerda que los mandos son de todos: si alguno falla durante un partido, avisa al árbitro antes de seguir jugando. Una vez terminado el partido, el resultado ya no se repite.',
    { font: 'Times New Roman', size: 25, shading: { fill: 'F2F2F2' } })),
);

// ---------- 3.1 ----------
children.push(
  subtituloFalso('3.1. Lo que no se puede traer'),
  texto('No se permiten mandos propios, auriculares con micrófono ni cuentas personales: todo el mundo juega en igualdad de condiciones con el material del aula.'),
);

// ---------- 4. Contactos ----------
children.push(
  tituloFalso('4. Contactos'),
  p([
    new CommentRangeStart(0),
    run('Cualquier duda sobre el reglamento la resuelve el comité del torneo, formado por dos alumnos de 2.º de SMR y el profesor que esté de guardia en el recreo.'),
    new CommentRangeEnd(0),
    new TextRun({ children: [new CommentReference(0)] }),
  ]),
  texto('Las reclamaciones se presentan por escrito justo al acabar el partido. El árbitro tiene la última palabra.'),
  p([
    run('¡Suerte, y que gane el mejor!'),
    run(' Nota privada: los mandos 3 y 5 tienen el joystick derecho tocado; dárselos siempre a los rivales.', { vanish: true }),
  ]),
  vacio(),
  p(run('¹ Partido rápido, sin modo carrera ni Ultimate Team.', { size: 18 })),
);

const doc = new Document({
  creator: 'El capitán eliminado',
  lastModifiedBy: 'El capitán eliminado',
  title: 'Bases del torneo de EA Sports FC',
  description: 'Versión definitiva. Al que la toque, tarjeta roja.',
  styles: { default: { document: { run: { font: 'Calibri', size: 22 }, paragraph: { spacing: { after: 160, line: 259, lineRule: 'auto' } } } } },
  comments: {
    children: [{
      id: 0,
      author: 'El capitán eliminado',
      initials: 'CE',
      date: new Date('2026-06-20T13:45:00'),
      children: [new Paragraph({ children: [new TextRun('Eliminado en cuartos por un penalti que no era. Que arregle esto el árbitro 😤')] })],
    }],
  },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 } } },
    footers: {
      default: new Footer({
        children: [p(run('Bases del torneo de EA Sports FC · Página 1', { size: 18, color: '7F7F7F' }), { alignment: 'right' })],
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
