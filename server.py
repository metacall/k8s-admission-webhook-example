from flask import Flask, request, jsonify

from metacall import metacall_load_from_file
import metacall

app = Flask(__name__)
metacall_load_from_file("node", ["scripts/validate.js"])

@app.route('/', methods=["GET"])
def hello():
    return "Hello World!"

@app.route('/validate', methods=["POST"])
def validate():
    body = request.json
    valid = metacall.metacall("validate", body)
    return jsonify({"response": {"allowed": valid, "status": {"message": "THIS IS A FUCKING DEMO"}}})

app.run(host='0.0.0.0', port=443,
        ssl_context=("/certs/tls.crt", "/certs/tls.key"))
