from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def init():
    print("Inside init")
    x=8
    y=8
    return render_template('checkerboard.html',x=x,y=y)
    
@app.route('/<var>')
def input_para(var):
    print(var)
    x=8
    c='white'
    return render_template('checkerboard.html',x=x,y=int(var))

@app.route('/<varx>/<vary>')
def input_two(varx,vary):
    print(varx,vary)
    return render_template('checkerboard.html',x=int(varx),y=int(vary))

@app.route('/<varx>/<vary>/<color1>/<color2>')
def input_4(varx,vary,color1,color2):
    print(varx,vary)
    return render_template('checkerboard.html',x=int(varx),y=int(vary))



app.run(debug=True)

