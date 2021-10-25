from pymongo import MongoClient
from time import sleep
from tqdm import tqdm
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning) 

client_local = MongoClient(port=27017)
database_local = client_local.bellamassa
collection_documents = database_local.pedidoscs.find()
collection_destination = database_local.pedidos
documents = []

print("Iniciando transferencia de banco de dados")
#coloca todos os documentos dentro da Dict documents

print("Fazendo contagem de Documentos")
for i in collection_documents:
  documents.append(i)
print(f"{len(documents)} Documentos encontrados.")
  
if len(documents) >= 1:
  print("Copiando documentos...")
  for doc in tqdm(documents):
    sleep(0.1)
    try:
      collection_destination.insert_one(doc)
    except:
      pass
    try:
      database_local.pedidoscs.remove(doc['_id'])
    except:
      pass
else:
  print("Nenhum documento encontado..")