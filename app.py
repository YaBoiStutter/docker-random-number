from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            min_val = int(request.form['min'])
            max_val = int(request.form['max'])
            if min_val > max_val:
                result = "Invalid input: min should be less than or equal to max."
            else:
                result = random.randint(min_val, max_val)
        except ValueError:
            result = "Invalid input: please enter integer values."
        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
