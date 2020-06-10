from config import app, mysql
from flask import request, jsonify



@app.route("/")
def home():
    return ("Uzuri Africa")


@app.route('/api/v2/location/active', methods=['GET'])
def location():
    cur = mysql
    cur.execute('SELECT * FROM location.locationDetail;')
    columns = cur.description
    locationDetail = [{columns[index][0]:column for index, column in enumerate(value)} for value in cur.fetchall()]
    return jsonify(locationDetail)
    

@app.route('/api/v2/offering/CategoriesAndValues', methods=['GET'])
def CategoriesAndValues():
    cur = mysql
    cur.execute('SELECT bty_Offering.offering_Cat.*, COUNT(bty_Offering.offering_detail.fk_offeringCat) AS available_options FROM bty_Offering.offering_Cat INNER JOIN bty_Offering.offering_detail ON bty_Offering.offering_detail.fk_offeringCat = bty_Offering.offering_Cat.btyCatId GROUP BY bty_Offering.offering_Cat.btyCatId;')
    columns = cur.description
    CategoriesAndValues = [{columns[index][0]:column for index, column in enumerate(value)} for value in cur.fetchall()]
    return jsonify(CategoriesAndValues)


if __name__ == '__main__':
    app.run(debug=True)
