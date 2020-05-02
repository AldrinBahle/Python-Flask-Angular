from flask_restful import Resource
from config import app, mysql
from flask import request, jsonify
from flask import Blueprint
from flask_restful import Api


#offering_detail
class offering_detail(Resource):
    @app.route('/api/v2/offering/details', methods=['GET'])
    def offering_detail():
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM bty_Offering.offering_detail;')
        columns = cur.description
        offering_detail = [{columns[index][0]:column for index, column in enumerate(value)} for value in cur.fetchall()]
        cur.close()
        return jsonify(offering_detail)

#offeringCategory
class offering_Cat(Resource):
    @app.route('/api/v2/offering/category', methods=['GET'])
    def offering_Cat():
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM bty_Offering.offering_Cat;')
        columns = cur.description
        offering_Cat = [{columns[index][0]:column for index, column in enumerate(value)} for value in cur.fetchall()]
        cur.close()
        return jsonify(offering_Cat)

#active location / Regions
class CategoriesAndValues(Resource):
    @app.route('/api/v2/offering/CategoriesAndValues', methods=['GET'])
    def CategoriesAndValues():
        cur = mysql.connection.cursor()
        cur.execute('SELECT bty_Offering.offering_Cat.*, COUNT(bty_Offering.offering_detail.fk_offeringCat) AS available_options FROM bty_Offering.offering_Cat INNER JOIN bty_Offering.offering_detail ON bty_Offering.offering_detail.fk_offeringCat = bty_Offering.offering_Cat.btyCatId GROUP BY bty_Offering.offering_Cat.btyCatId;')
        columns = cur.description
        CategoriesAndValues = [{columns[index][0]:column for index, column in enumerate(value)} for value in cur.fetchall()]
        cur.close()
        return jsonify(CategoriesAndValues)


api_btysrvc = Blueprint('api/v2', __name__)
api = Api(api_btysrvc)
api.add_resource(CategoriesAndValues, '/offering/CategoriesAndValues')
api.add_resource(offering_Cat, '/offering/category')
api.add_resource(offering_detail, '/offering/details')