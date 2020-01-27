from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
app.count = 0
globalcounter=0
@app.route('/')
def index():
    global globalcounter
    globalcounter+=1
    x=int(session['count'])+1
    session['count'] =  x
    return render_template('sessions.html', count=session['count'], gc=globalcounter)
@app.route('/increment', methods=['POST'])
def increment_by_two():
    x=int(session['count'])+1
    session['count'] = x
    #We only increment by 1 since reloading the page also increments
    return redirect('/')

@app.route('/destroy', methods=['POST'])
def clear():
    x=str(0)
    session['count'] = x
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    # print(request.form('resetting'))
    number=request.form['resetting']
    # number=request.form.get('resetting',False)    
    x=int(session['counter'])+int(number)
    print("*"*50)
    print("Value of x is ",x," value of number is ",number)
    print("The value of session count is", session['count'])
    session['count']=x
    print("THe new value of session is ", session['count'])
    print("*"*50)
    return redirect('/')
app.run(debug=True)