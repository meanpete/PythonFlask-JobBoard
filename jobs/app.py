from flask import Flask, render_temmplate

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_temmplate('index.html')