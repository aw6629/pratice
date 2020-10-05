from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def default_page():
    return render_template('index.html')
@app.route('/add',methods=['get','post'])
def add():
    A=int(request.values['a'])
    B=int(request.values['b'])
    values=str(A+B)
    return values
if __name__ =="__main__":
    app.run(debug=True, use_reloader=True)
