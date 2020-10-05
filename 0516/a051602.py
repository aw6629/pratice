from flask import Flask,render_template,request
import time
app=Flask(__name__)
@app.route('/')
def default_page():
    time.sleep(3)
    a=int(request.values['a'])
    b=int(request.values['b'])
    return str(a+b)

if __name__ =="__main__":
    app.run(debug=True, use_reloader=True)
