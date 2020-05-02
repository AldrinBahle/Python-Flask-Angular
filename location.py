from flask_restful import Resource
from config import app, mysql
from flask import request, jsonify
from flask import Blueprint
from flask_restful import Api

#active location / Regions
class locationDetailResource(Resource):
    @app.route('/api/v2/location/active', methods=['GET'])
    def location():
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM location.locationDetail;')
        columns = cur.description
        locationDetail = [{columns[index][0]:column for index, column in enumerate(value)} for value in cur.fetchall()]
        cur.close()
        return jsonify(locationDetail)


api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(locationDetailResource, '/v2/location/active')