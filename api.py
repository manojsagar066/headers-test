from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    print("Request Headers:")
    headers = {}
    for header, value in request.headers.items():
        headers[header] = value
    return render_template('headers.html', headers=headers)


@app.route('/test', methods=['GET', 'POST'])
def log_headers():
    # return headers sent by the user
    print("Request Headers:")
    headers = list(request.headers)
    print("Request Headers:")
    for header, value in headers:
        print(f"{header}: {value}")

    return jsonify(headers)


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
