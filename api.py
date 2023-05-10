from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def log_headers():
    try:
        print("Request Headers:")
        for header, value in request.headers.items():
            print(f"{header}: {value}")

        return "Headers logged."
    except Exception as e:
        response = {
            "error": str(e),
            "type": type(e).__name__
        }
        return jsonify(response), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
