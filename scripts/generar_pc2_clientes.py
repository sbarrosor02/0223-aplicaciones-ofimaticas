# -*- coding: utf-8 -*-
"""Genera web/descargas/pc2-clientes.xlsx

Origen de datos de la Practica de Control 2.

Es DISTINTO del empresas-destinatarias.xlsx de los ejercicios a proposito: el
PC2 evalua transferencia, no memoria. Mantiene las mismas trampas didacticas
pero con otros nombres de campo y otro criterio de filtrado, de forma que el
alumno no pueda repetir de memoria lo que hizo en el bloque 2.5.

- Campos con nombres NO estandar (Razon, Trato, Calle, Localidad) -> obliga a
  usar Asignar campos.
- Campo TipoCliente con tres valores -> filtrado por algo que no es la
  provincia, que es por donde se filtro en los ejercicios.
- Apellidos repetidos -> ordenar por dos campos tiene efecto visible.
- Dos registros sin Correo -> filtro "No esta vacio".
"""
from openpyxl import Workbook
from pathlib import Path

CAMPOS = ['Razon', 'Trato', 'Nombre', 'Apellidos', 'Cargo', 'Calle',
          'CP', 'Localidad', 'Provincia', 'Correo', 'TipoCliente', 'Antiguedad']

FILAS = [
 ('Asesoría Valle Verde S.L.', 'Sra.', 'Pilar', 'Moreno Casas', 'Administradora',
  'C/ Sol 12', '10600', 'Plasencia', 'Cáceres',
  'pmoreno@valleverde.example', 'Empresa', 6),
 ('IES Gabriel y Galán', 'Sr.', 'Tomás', 'Herrero Luna', 'Secretario',
  'Avda. Martín Palomino 2', '10600', 'Plasencia', 'Cáceres',
  'secretaria@iesgygalan.example', 'Centro educativo', 11),
 ('Clínica Dental Ambroz', 'Sra.', 'Rocío', 'Núñez Pardo', 'Gerente',
  'C/ Mayor 7', '10750', 'Hervás', 'Cáceres',
  'rnunez@dentalambroz.example', 'Empresa', 3),
 ('CEIP Las Vegas', 'Sr.', 'Alberto', 'Moreno Gil', 'Director',
  'C/ Escuelas 1', '10300', 'Navalmoral de la Mata', 'Cáceres',
  'direccion@ceiplasvegas.example', 'Centro educativo', 8),
 ('Transportes Tiétar', 'Sr.', 'Ignacio', 'Vicente Soler', 'Jefe de flota',
  'Pol. Ind. El Pino, nave 3', '10300', 'Navalmoral de la Mata', 'Cáceres',
  '', 'Empresa', 2),                                   # sin correo
 ('Panadería La Espiga', 'Sra.', 'Beatriz', 'Calvo Ramos', 'Propietaria',
  'C/ Horno 5', '10600', 'Plasencia', 'Cáceres',
  'info@laespiga.example', 'Empresa', 9),
 ('Luis Serrano Marín', 'Sr.', 'Luis', 'Serrano Marín', '',
  'C/ Trujillo 44', '10001', 'Cáceres', 'Cáceres',
  'lserrano@correo.example', 'Particular', 1),
 ('Academia Cálamo', 'Sra.', 'Inés', 'Vicente Bravo', 'Coordinadora',
  'C/ Pintores 18', '10003', 'Cáceres', 'Cáceres',
  'ines@academiacalamo.example', 'Centro educativo', 4),
 ('Taller Mecánico Jaraíz', 'Sr.', 'Fernando', 'Calvo Ortega', 'Encargado',
  'Ctra. de Cáceres km 3', '10400', 'Jaraíz de la Vera', 'Cáceres',
  '', 'Empresa', 7),                                   # sin correo
 ('Óptica Mirador', 'Sra.', 'Sandra', 'Herrero Pozo', 'Óptica',
  'C/ Zapatería 9', '10600', 'Plasencia', 'Cáceres',
  'smirador@optica.example', 'Empresa', 5),
 ('Marta Peinado Gómez', 'Sra.', 'Marta', 'Peinado Gómez', '',
  'C/ Nueva 21', '10750', 'Hervás', 'Cáceres',
  'mpeinado@correo.example', 'Particular', 2),
 ('Bodegas Alagón', 'Sr.', 'Emilio', 'Núñez Vega', 'Responsable de compras',
  'Camino del Río s/n', '10810', 'Montehermoso', 'Cáceres',
  'compras@bodegasalagon.example', 'Empresa', 10),
 ('IESO Vía Dalmacia', 'Sra.', 'Lorena', 'Serrano Puente', 'Jefa de estudios',
  'Avda. de Extremadura 30', '10810', 'Montehermoso', 'Cáceres',
  'jefatura@iesoviadalmacia.example', 'Centro educativo', 6),
 # Comparte apellidos con Clinica Dental Ambroz a proposito: asi el criterio
 # "Luego por: Nombre" tiene un efecto visible y se puede corregir.
 ('Floristería El Almendro', 'Sra.', 'Ana', 'Núñez Pardo', 'Propietaria',
  'C/ Iglesia 3', '10400', 'Jaraíz de la Vera', 'Cáceres',
  'elalmendro@flores.example', 'Empresa', 4),
]

wb = Workbook()
ws = wb.active
ws.title = 'Clientes'
ws.append(CAMPOS)
for fila in FILAS:
    ws.append(list(fila))

for col, ancho in zip('ABCDEFGHIJKL', (30, 6, 11, 18, 24, 28, 8, 24, 10, 34, 18, 12)):
    ws.column_dimensions[col].width = ancho
ws.freeze_panes = 'A2'

destino = Path(__file__).resolve().parents[1] / 'web' / 'descargas' / 'pc2-clientes.xlsx'
wb.save(destino)
print('escrito:', destino)
print(len(FILAS), 'registros |', len(CAMPOS), 'campos')
tipos = [f[10] for f in FILAS]
print('TipoCliente:', {t: tipos.count(t) for t in sorted(set(tipos))})
print('sin correo:', sum(1 for f in FILAS if not f[9]))
ape = [f[3].split()[0] for f in FILAS]
print('apellidos repetidos:', sorted({a for a in ape if ape.count(a) > 1}))
