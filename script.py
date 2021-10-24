from pymongo import MongoClient
from time import sleep

client_local = MongoClient(port=27017)
database_local = client_local.bellamassa
documents = database_local.pedidos.find()
collection_destination = database_local.pedidoscs


for doc in documents:
  
  try:
    collection_destination.insert(doc)
  except:
    print("erro ao adicionar: ", doc)
  database_local.pedidos.remove(doc['_id'])
  print(doc['_id'])
  
