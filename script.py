from pymongo import MongoClient
from time import sleep
from tqdm import tqdm
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning) 

client_local = MongoClient(port=27017)
database_local = client_local.bellamassa
collection_documents = database_local.pedidos.find()
collection_destination = database_local.pedidocs
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
    sleep(0.05)
    try:
      collection_destination.insert_one(doc)
    except:
      pass
  print("Verificando a integridade dos dados...")
  for doc in tqdm(documents):
    sleep(0.05)
    cheking = collection_destination.count_documents({'_id':doc['_id']}) > 0
    if cheking == True:
      try:
        database_local.pedidos.delete_many({'_id':doc['_id']})
      except:
        pass
    else:
      pass
    
else:
  print("Nenhum documento encontado..")
  
print("Finalizado!")