from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.Reporte import Reporte

app = Flask(__name__)
CORS(app)

@app.route("/reporte", methods=['GET'])
def getAll():
    return (Reporte.list())

@app.route("/reporte", methods=['POST'])
def postOne():
    body = request.json
    return (Reporte.create(body))

@app.route("/reporte", methods=['PUT'])
def putOne():
    body = request.json
    return (Reporte.update(body))

@app.route("/reporte/<int:id_reporte>", methods=['DELETE'])
def deleteOne(id_reporte):   
    return (Reporte.delete(id_reporte))

if __name__ == '__main__':
 app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)