from Destino import Destino
from DestinoRepository import DestinoRepository
from InterfaceUsuario import InterfaceUsuario

DestinoRepository = DestinoRepository()

DestinoRepository.adicioanar_destino(Destino(75, "Feira de Santana"))
DestinoRepository.adicioanar_destino(Destino(71, "Salvador"))
DestinoRepository.adicioanar_destino(Destino(11, "São Paulo"))
DestinoRepository.adicioanar_destino(Destino(74, "Xique Xique"))
DestinoRepository.adicioanar_destino(Destino(85, "Fortaleza"))

usuario = InterfaceUsuario(DestinoRepository)

cont = "SIM"

while cont == "SIM":
  resultado = usuario.exibir_destinos()
  if (resultado == "DDD não encontrado"):
    print (resultado + "\f")
  else:
    print ("O DDD corresponde a " + resultado + "\f")
  cont = input ("Continuar pesquisando? (SIM): ")
  print ("")

