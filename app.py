from models import app, db, Cupcake, serialize
from flask import jsonify

@app.route("/api/cupcakes")
def cupcake_api_get_handler():
    """get request for our api route"""

    cupcakes = Cupcake.query.all()
    print(cupcakes)
    serialized = [serialize(c) for c in cupcakes]
    return jsonify(cupcakes=serialized)

@app.route("/api/cupcakes/<int:cupcake_id>")
def cupcake_api_get_id(cupcake_id):
    """get an individual cupcake by its id"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = serialize(cupcake)
    return jsonify(serialized)





