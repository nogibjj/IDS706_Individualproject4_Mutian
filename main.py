from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    # Get data from user input
    user_input = request.form['user_input']
    user_input +=",please speak in English"
    url = "https://luckycola.com.cn/ai/openwxyy"

    args = {
        # Description
        "ques": user_input,
        # App key
        "appKey": "65653dd96dd7b2f885ab5dd1",
        # User Id
        "uid": "9nmGuQ17011337516758P97ncXnIO",
        "isLongChat": 0
    }

    try:
        response = requests.post(url, json=args)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        result = response.json().get('data', {}).get('result', 'None')
    except requests.RequestException as e:
        result = f"Error: {str(e)}"

    print("Response:", result)
    return render_template('result.html', response=result), 200, {'Content-Type': 'text/html; charset=utf-8'}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
