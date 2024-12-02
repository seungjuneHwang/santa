from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        name = request.form['name']
        email = request.form['email']
        msg = request.form['msg']
        print(name, email)
        return f"산타에게 전달된 메세지 <br> {name}<br>{email}<br>{msg}"

if __name__ == '__main__':
    app.run(debug=True)