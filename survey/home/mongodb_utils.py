import pymongo

url = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(url)

db = client['survey_db']
survey_collection = db['Survey']
