from sqlite3 import InterfaceError
from DestinoRepository import DestinoRepository
from Destino import Destino
from InterfaceUsuario import InterfaceUsuario

def test_UserInteface():
  
  ask = Destino(75,"Feira de Santana")

  destino = DestinoRepository()

  interface = InterfaceUsuario(destino)

  teste = interface.exibir_destinos()
    
  assert ask.code == teste.code
  assert ask.quantity == teste.quantity
