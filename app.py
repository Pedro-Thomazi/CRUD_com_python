import mysql.connector
from pathlib import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
  host="localhost",
  database=str(os.getenv("DATABASE")),
  user=str(os.getenv("USER")),
  password=str(os.getenv("PASSWORD"))
)

if mydb.is_connected():
  print("Conectado com o banco de dados.")
  cursor = mydb.cursor()

mycursor = mydb.cursor()

# GET ALL
def getAllProducts():
  mycursor.execute("SELECT * FROM products")

  products = mycursor.fetchall()

  for product in products:
    print(product)

# GET BY ID
def getProduct(index):
  mycursor.execute(f"SELECT * FROM products WHERE id = {index}")
  myresult = mycursor.fetchone()
  print(myresult)

# CREATE PRODUCT
def createProduct():
  sql = f"INSERT INTO products (nome, price, descricao) VALUE (%s, %s, %s)"

  nome = str(input("Digite o nome do produto: "))
  price = float(input("Digite o preço do produto: "))
  descricao = str(input("Digite a descrição do produto: "))
  
  val = (nome, price, descricao)
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "Produto criado")

# UPDATE BY ID
def updateProduct(id):
  nome = str(input("Digite o nome do produto: "))
  price = float(input("Digite o preço do produto: "))
  descricao = str(input("Digite a descrição do produto: "))

  sql = f"UPDATE products SET nome = '{nome}', price = {price}, descricao = '{descricao}' WHERE id = {id}"

  mycursor.execute(sql)

  mydb.commit()

  print(mycursor.rowcount, "Tabela modificada")


# DELETE BY ID
def deleteProduct(index):
  sql = f"DELETE FROM products WHERE id = {index}"

  mycursor.execute(sql)
  mydb.commit()
  print(mycursor.rowcount, "Produto deletado")


option = -1

while option != 0:
  print("Qual opção você gostaria de escolher: ")
  print("[ 1 ] -- Ver todos os produtos")
  print("[ 2 ] -- Ver produto especifico")
  print("[ 3 ] -- Atualizar produto")
  print("[ 4 ] -- Deletar produto")
  print("[ 5 ] -- Criar produto")
  print("[ 0 ] -- Sair")

  option = int(input("Opção: "))
  if option == 1:
    print("*" * 15)
    getAllProducts()
    print("*" * 15)

  elif option == 2:
    print("*" * 15)
    index = str(input("Qual produto você quer ver: "))
    getProduct(index)
    print("*" * 15)

  
  elif option == 3:
    print("*" * 15)
    index = str(input("Qual produto você quer atualizar: "))
    updateProduct(index)
    getProduct(index)
    print("*" * 15)

  elif option == 4:
    print("*" * 15)
    index = str(input("Qual produto você quer atualizar: "))
    deleteProduct(index)
    print("*" * 15)

  elif option == 5:
    print("*" * 15)
    createProduct()
    print("*" * 15)

  elif option == 0:
    print("... SAINDO ...")


mydb.close()
cursor.close()

# def crudDeProdutos(produto):
#   print(produto)

# crudDeProdutos("Arroz")