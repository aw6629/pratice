from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def default_page():
    return render_template('index.html')
@app.route('/login',methods=['get','post'])
def login_page():
    return render_template('result.html',id=request.values['id'],name=request.values['name'])

if __name__ =="__main__":
    app.run(debug=True, use_reloader=True)
