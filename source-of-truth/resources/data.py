import util.get_data
import json
import falcon

class DataResource:

    def on_get(self, req, res):
        data = util.get_data.get_data()
        raw_data = json.dumps(data)

        res.status = falcon.HTTP_200
        res.body = raw_data