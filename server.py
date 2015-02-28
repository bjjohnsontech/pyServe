#! /usr/bin/python
import sys, json
from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TESTING'] = True
@app.route('/')
def root():
    return "There's nothing here"

@app.route("/lights/solve", methods=['POST'])
def solveLights():
    #try:
    sys.path.append('/var/www/html/codeprojects/lights/')
    #return json.dumps(sys.path)
    import solve
    return solve.solution(request.form['grid'])
    #except Exception, err:
    #    return jsonify(err)

if __name__ == "__main__":
    app.run()