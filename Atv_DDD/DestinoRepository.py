from Destino import Destino

class DestinoRepository:

  def __init__ (self) -> None:
    self.lista_destino: list[Destino] = []

  def adicioanar_destino(self, cidade: Destino) -> None:
    self.lista_destino.append(cidade)
       
  def checa_se_destino_existe(self, ddd:int) -> bool:
    for cidade in self.lista_destino:
      if (ddd == cidade.ddd):
        return True

    return False
    
  def obter_destino_pelo_ddd(self, ddd: int) -> str:
    for cidade in self.lista_destino:
      if (ddd == cidade.ddd):
        return cidade.nome