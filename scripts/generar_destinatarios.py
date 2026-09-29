# -*- coding: utf-8 -*-
"""Genera web/descargas/empresas-destinatarias.xlsx

Origen de datos para combinar correspondencia (subtema 2.5).

Detalle deliberado: los campos NO se llaman como los campos estandar que Word
usa en Bloque de direcciones y Linea de saludo (Via en vez de Direccion, Ciudad
en vez de Poblacion, Trato en vez de Tratamiento). Asi Word no puede hacer la
asociacion automatica y el alumno se ve obligado a usar "Asignar campos", que
si no, no se practica nunca.

Ademas:
- Hay varias provincias, para que filtrar tenga sentido.
- Hay apellidos repetidos, para que ordenar por varios campos tenga sentido.
- Una fila no tiene Email, para practicar el filtro "No esta vacio".
"""
from openpyxl import Workbook
from pathlib import Path

CAMPOS = ['Empresa', 'Trato', 'Nombre', 'Apellidos', 'Cargo', 'Via',
          'CodPostal', 'Ciudad', 'Provincia', 'Email', 'Puesto', 'Area']

FILAS = [
 ('Microsistemas del Jerte S.L.', 'Sr.', 'Andrés', 'Bermejo Cano', 'Gerente',
  'Avda. de la Vera 14', '10600', 'Plasencia', 'Cáceres',
  'abermejo@microjerte.example', 'Técnico de microinformática', 'Soporte'),
 ('Redes Extremeñas S.A.', 'Sra.', 'Lucía', 'Domínguez Gil', 'Jefa de proyectos',
  'C/ Pizarro 3', '10001', 'Cáceres', 'Cáceres',
  'ldominguez@redesex.example', 'Administrador de red', 'Sistemas'),
 ('InfoNorte Servicios', 'Sr.', 'Javier', 'Mateos Prieto', 'Responsable técnico',
  'Pol. Ind. La Dehesa, nave 7', '10300', 'Navalmoral de la Mata', 'Cáceres',
  'jmateos@infonorte.example', 'Técnico de soporte', 'Soporte'),
 ('Soluciones Guadiana', 'Sra.', 'Marta', 'Ruiz Alonso', 'Directora',
  'C/ Menacho 22', '06001', 'Badajoz', 'Badajoz',
  'mruiz@guadianasol.example', 'Técnico de sistemas', 'Sistemas'),
 ('DataMérida Consultores', 'Sr.', 'Óscar', 'Ruiz Delgado', 'Coordinador',
  'Avda. Reina Sofía 51', '06800', 'Mérida', 'Badajoz',
  'oruiz@datamerida.example', 'Técnico de microinformática', 'Soporte'),
 ('Talleres Informáticos Vetton', 'Sr.', 'Pablo', 'Sánchez Nieto', 'Encargado',
  'C/ Trujillo 8', '10200', 'Trujillo', 'Cáceres',
  '', 'Técnico de reparación', 'Hardware'),   # sin email: filtro "No esta vacio"
 ('Aula Digital Extremadura', 'Sra.', 'Elena', 'Vargas Pino', 'Responsable de formación',
  'C/ Santa Eulalia 4', '06800', 'Mérida', 'Badajoz',
  'evargas@auladigital.example', 'Técnico de aula', 'Formación'),
 ('Sistemas Ambroz S.L.', 'Sr.', 'Daniel', 'Iglesias Mora', 'Administrador',
  'C/ del Valle 19', '10750', 'Hervás', 'Cáceres',
  'diglesias@ambroz.example', 'Administrador de sistemas', 'Sistemas'),
 ('Copisterías del Sur', 'Sra.', 'Nuria', 'Domínguez Vela', 'Gerente',
  'C/ Felipe Checa 30', '06001', 'Badajoz', 'Badajoz',
  'ndominguez@copisur.example', 'Técnico de equipos de impresión', 'Hardware'),
 ('CloudTajo Hosting', 'Sr.', 'Rubén', 'Castaño Lima', 'CTO',
  'Avda. de España 100', '10004', 'Cáceres', 'Cáceres',
  'rcastano@cloudtajo.example', 'Técnico de centro de datos', 'Sistemas'),
 ('Ofimática Vegas Altas', 'Sra.', 'Carmen', 'Peña Rubio', 'Directora comercial',
  'C/ Real 45', '06400', 'Don Benito', 'Badajoz',
  'cpena@vegasaltas.example', 'Técnico de ofimática', 'Formación'),
 ('Montajes PC Sierra', 'Sr.', 'Hugo', 'Bermejo Ortiz', 'Responsable de taller',
  'C/ Gabriel y Galán 2', '10600', 'Plasencia', 'Cáceres',
  'hbermejo@pcsierra.example', 'Técnico de montaje', 'Hardware'),
]

wb = Workbook()
ws = wb.active
ws.title = 'Empresas'
ws.append(CAMPOS)
for fila in FILAS:
    ws.append(list(fila))

# Anchos comodos para que se lea al abrirlo
for col, ancho in zip('ABCDEFGHIJKL', (30, 6, 10, 18, 24, 28, 10, 22, 12, 34, 32, 12)):
    ws.column_dimensions[col].width = ancho
ws.freeze_panes = 'A2'

destino = Path(__file__).resolve().parents[1] / 'web' / 'descargas' / 'empresas-destinatarias.xlsx'
wb.save(destino)
print('escrito:', destino)
print(len(FILAS), 'registros |', len(CAMPOS), 'campos')
print('provincias:', sorted({f[8] for f in FILAS}))
print('sin email:', [f[0] for f in FILAS if not f[9]])
