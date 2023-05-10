from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def log_headers():
    print("Request Headers:")
    for header, value in request.headers.items():
        print(f"{header}: {value}")

    return "Headers logged."


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
