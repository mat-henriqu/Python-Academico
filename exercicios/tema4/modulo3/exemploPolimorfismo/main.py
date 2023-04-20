from exercicios.tema4.modulo3.exemploPolimorfismo.classeArgentina import Argentina
from exercicios.tema4.modulo3.exemploPolimorfismo.classeBrasil import Brasil

brasil = Brasil()
argentina = Argentina()

for pais in (brasil, argentina):
    pais.capital()
    pais.lingua_oficial()
