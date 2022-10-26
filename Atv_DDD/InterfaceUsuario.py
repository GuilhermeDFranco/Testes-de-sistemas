from DestinoRepository import DestinoRepository

class InterfaceUsuario:

  def __init__ (self, destino_repository: DestinoRepository) -> None:
    self.destino_repository = destino_repository
  
  def solicitar_input_usuario (self) -> int:
    consulta = int(input("Informe o DDD para pesquisar o destino: "))
    return consulta
  
  def exibir_destinos (self) -> str:
    ddd = self.solicitar_input_usuario()
    if (self.destino_repository.checa_se_destino_existe(ddd) == False):
      return "DDD não encontrado"
    return self.destino_repository.obter_destino_pelo_ddd(ddd)
      
  def saida_usuario (self) -> None:
    pass