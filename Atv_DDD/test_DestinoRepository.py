from Destino import Destino
from DestinoRepository import DestinoRepository

def test_adicioanar_destino():

  destino_repository = DestinoRepository()
  destino_repository.lista_destino = []
  destino1 = Destino(12, "Test 1")
  destino2 = Destino(13, "Test 2")
  destino1 = Destino(14, "Test 3")

  destino_repository.adicioanar_destino(destino1) 
  destino_repository.adicioanar_destino(destino2)

  assert len(destino_repository.lista_destino) == 2
  assert not destino3 in destino_repository.lista_destino
  assert type(destino_repository.lista_destino) == list


def test_checa_se_destino_existe():

  destino_repository = DestinoRepository()
  destino_repository.lista_destino = []
  
  destino1 = Destino(13, "Test 1")
  destino2 = Destino(12, "Test 2")

  destino_repository.adicionar_destino(destino1)
  resultOK = destino_repository.checa_se_destino_existe(destino1)
  resultNOK = destino_repository.checa_se_destino_existe(destino2)

  assert len(destino_repository.lista_destino) == 1
  assert resultOK == True
  assert resultNOK == False
  