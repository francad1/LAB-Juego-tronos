
from typing import Optional, List,NamedTuple
import csv


BatallaGOT = NamedTuple('BatallaGOT',
    [('nombre', str), ('rey_atacante', str), ('rey_atacado', str), ('gana_atacante', bool),
     ('muertes_principales', bool), ('comandantes_atacantes', List[str]), ('comandantes_atacados', List[str]),
     ('region', str), ('num_atacantes', Optional[int]), ('num_atacados', Optional[int])])

reader = csv.reader(open('C:\\Users\\river\\Documents\\FP\\PracticaGoT\\LAB-Juego-tronos\\data\\battles.csv', encoding='UTF-8' ))
batallas=[]
for line in reader:
    nombre = str(line[0])
    atacante = str(line[1])
    atacado = str(line[2])
    if str(line[3]) == "win":
      victoria=True
    elif str(line[3]) =="loss":
      victoria=False
    if line[4] == "1":
      muerte_principal=True
    elif line[4] == "0":
      muerte_principal=False   
    com_atacantes=[]
    x = line[5].split(",")
    for i in x:
      com_atacantes.append(str(i))
    com_defensores=[]
    y = line[6].split(",")
    for i in y:
      com_atacantes.append(str(i))
    region= str(line[7])      
    if line[8] != " ":
      num_atacantes=line[8]
    else:
      num_atacantes=None   
    if line[9] != " ":
      num_defensores=line[9]
    else:
      num_defensores=None      
    batalla = BatallaGOT(nombre,atacante,atacado,victoria,com_atacantes,com_defensores,region,num_atacantes,num_defensores)
    batallas.append(batalla)