from flask import Flask, render_template, request, redirect, session
import random
to_guess=random.randint(1,100)

app=Flask(__name__)
counter=0
app.secret_key="blha blah"
# session['Num']=random.randint(1,100) 
# def setSession():
     
@app.route('/')
def route():
    # if (session['Num']== None):
    #     setSession()
    session['Num'] = random.randint(1,100)
    print(session['Num'])
    global counter
    counter=counter+1
   
    return render_template('number_game.html')

@app.route('/guess' , methods=['POST']) 
def guessing():
    print('Inside guessign')
    guess=request.form['guess']

    if(int(guess) == int(session['Num'])):
        return render_template('number_game_correct.html')
    elif (int(guess)>int(session['Num'])):
        return render_template('number_game_greater.html')
    else:
        return render_template('number_game_smaller.html')   

@app.route('/reset', methods=['POST','GET'])
def reset():
    return redirect('/') 
app.run(debug=True)