from pymongo import MongoClient
from bson.objectid import ObjectId

class Database():

  @staticmethod
  def get_pedidos():
    client_local = MongoClient(port=27017)
    db_local = client_local.bellamassa

    local_count = db_local.printf.find({})

    return local_count
  @staticmethod
  def delete_pedido(id):
    client_local = MongoClient(port=27017)
    db_local = client_local.bellamassa

    delete = db_local.printf.delete_many({'_id': ObjectId(id)})
    pass