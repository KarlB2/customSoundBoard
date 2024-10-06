from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button-clicked', methods=['POST'])
def button_clicks():
    with open('button_clicks.txt', 'a') as f:
        f.write("The button has been pushed\n")
    return '', 200

@app.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404

if __name__ == '__main__':
    app.run(debug=True)