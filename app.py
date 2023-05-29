from models import app, db, Cupcake, serialize
from flask import jsonify, request, render_template

@app.route("/")
def show_homepage():
   """view function to render the homepage"""
   return render_temlate("home.html")

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
    return jsonify(cupcake= serialized)

@app.route("/api/cupcakes", methods = ["POST"])
def create_new_cupcake():
    """post route to create a new cupcake on the API"""

    new_cupcake = Cupcake()

    for (k,v) in request.json.items():
      setattr(new_cupcake, k, v)

    serialized = serialize(new_cupcake)

    return (jsonify(cupcake=serialized), 201)

@app.route("/api/cupcakes/<int:cupcake_id>" , methods=['PATCH'])
def edit_cupcake(cupcake_id):
   """Patch route to update individual cupcake"""

   cupcake = Cupcake.query.get_or_404(cupcake_id)

   for (k,v) in request.json.items():
      setattr(cupcake,k,v)
    
   db.session.commit()

   serialized = serialize(cupcake)

   return jsonify(cupcake= serialized)

@app.route("/api/cupcakes/<int:cupcake_id>", methods=['DELETE'])
def cupcake_deleter(cupcake_id):
   """a route to delete the cupcake in our API"""
   cupcake = Cupcake.query.get_or_404(cupcake_id)
   db.session.delete(cupcake)
   db.session.commit()

   message = {"message": "deleted"}
   return jsonify(message)

   















