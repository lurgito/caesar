from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set-cookie')
def set_cookie():
    resp = make_response(render_template('set-cookie.html'))
    resp.set_cookie('user_id', '12345')
    return resp

if __name__ == '__main__':
    app.run()
