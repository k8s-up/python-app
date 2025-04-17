from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/hello")
def hello():
    return jsonify({"message": "hello ArgoCD"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")