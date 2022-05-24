from flask import Flask,render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = "Dominicks secret key!"

@app.route('/')
def root():
    if 'visits' not in session:
        session['visits']= 0
    else:
        session['visits'] += 1
    if 'num' not in session:
        session['num'] = 0
    if 'yourclick' not in session:
        session['yourclick']= 0
    return render_template('index.html' )

@app.route('/count')
def count():
    session['num']+= 1
    return redirect('/')

@app.route('/counttwo')
def counttwo():
    session['num']+= 2
    return redirect('/')

@app.route('/formadd', methods= ['POST'])
def yourclickadd():
    print(request.form )
    session['yourclick'] = request.form['yourclick'] 
    return redirect('/')


@app.route('/yourclick')
def yourclick():
    session['num'] += int(session['yourclick'])
    
    return redirect('/')



@app.route('/destroy_session')
def resetcount():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

