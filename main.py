from datetime import datetime
from config import app, mysql
from flask import request, jsonify

@app.route("/")
def home():
    return ("Uzuri Africa")


#active location / Regions
@app.route('/api/v2/location/active', methods=['GET'])
def location():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM location.locationDetail;')
    columns = cur.description
    locationDetail = [{columns[index][0]:column for index, column in enumerate(value)} for value in cur.fetchall()]
    cur.close()
    return jsonify(locationDetail)

#offering_detail 
@app.route('/api/v2/offering/details', methods=['GET'])
def offering_detail():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM bty_Offering.offering_detail;')
    columns = cur.description
    offering_detail = [{columns[index][0]:column for index, column in enumerate(value)} for value in cur.fetchall()]
    cur.close()
    return jsonify(offering_detail)

#offeringC
@app.route('/api/v2/offering/category', methods=['GET'])
def offering_Cat():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM bty_Offering.offering_Cat;')
    columns = cur.description
    offering_Cat = [{columns[index][0]:column for index, column in enumerate(value)} for value in cur.fetchall()]
    cur.close()
    return jsonify(offering_Cat)

#CategoriesAndValues
@app.route('/api/v2/offering/CategoriesAndValues', methods=['GET'])
def CategoriesAndValues():
    cur = mysql.connection.cursor()
    cur.execute('SELECT bty_Offering.offering_Cat.*, COUNT(bty_Offering.offering_detail.fk_offeringCat) AS available_options FROM bty_Offering.offering_Cat INNER JOIN bty_Offering.offering_detail ON bty_Offering.offering_detail.fk_offeringCat = bty_Offering.offering_Cat.btyCatId GROUP BY bty_Offering.offering_Cat.btyCatId;')
    columns = cur.description
    CategoriesAndValues = [{columns[index][0]:column for index, column in enumerate(value)} for value in cur.fetchall()]
    cur.close()
    return jsonify(CategoriesAndValues)

if __name__ == '__main__':
    app.run(debug=True)
