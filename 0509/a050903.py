from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def default_page():
        userAgent=request.headers['User-Agent']
        if 'Trident' in userAgent:
            return 'IE'
        elif 'Chrome' in userAgent:
            return  'Chrome'
        else:
            return userAgent
if __name__ =="__main__":
    app.run(debug=True, use_reloader=True)
