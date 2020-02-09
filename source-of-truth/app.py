import falcon
from resources.data import DataResource
from util.get_data import get_data, load_data

app = falcon.API()
load_data('data/peoplePlaces.json')

data_resource = DataResource()
app.add_route('/data', data_resource)
