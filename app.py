import os,json
import pymongo 
# mng_client = pymongo.MongoClient('localhost', 27017)

mng_client = pymongo.MongoClient('host',username='admin',password='admin123', authSource='admin')
mng_db = mng_client['Hotels'] 
collection_name = 'hotels_pro'
db_cm = mng_db[collection_name]
path_to_json = '1/1_100/'
content=[]
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
  print(file_name)
  with open(path_to_json + file_name) as json_file:
    data = json.load(json_file)
    for c in data:
      c.pop('updated_at')
      content.append(c)
for x in content:
  db_cm.insert(x)