import locale

class Product():
  def __init__(self, nome, price, descricao):
    self.nome = nome
    self.price = price
    self.descricao = descricao

  def __str__(self):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    moeda = locale.currency(self.price, grouping=True)
    return f"Nome: {self.nome} - {moeda} - Descrição: {self.descricao}"