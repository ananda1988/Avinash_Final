from flask import Flask, render_template,request,session
import random
app=Flask(__name__)
app.config['SECRET_KEY']='wasd'


@app.route('/dummy', methods=['GET', 'POST'])
def dummy():
    return render_template('louis_vitton.html')
@app.route('/')
@app.route('/home')
def index():
    quotes=['''Goals on the road to achievement cannot be achieved 
          without discipline and consistency. —D.Washington''',
        'Your love makes me stronger, but your hate makes me unstoppable-Cristiano Ronaldo',
        'If you tell the truth, you do not have to remember anything.-Mark Twain',
        'Reality is wrong. Dreams are for real.-Tupac Shakur',
        'Surround yourself with love, not friends.-Lil Wayne',
        '''Try not to become a man of success. 
           Rather become a man of value.- Albert Einstein''',
        'Victory has a thousand fathers, but defeat is an orphan. John F. Kennedy']
    quote=random.choice(quotes)
    message='Hello Guest !'
    return render_template("index.html",quote=quote,message=message)
    
@app.route('/aboutme', methods=['GET', 'POST'])
def aboutme():
    return render_template('aboutme.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')    

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')   

@app.route('/readersclub', methods=['GET', 'POST'])
def readersclub():
    return render_template('readersclub.html')

@app.route('/environmentalclub', methods=['GET', 'POST'])
def environmentalclub():
     return render_template('environmental_club.html')  

@app.route('/quiz', methods=['GET', 'POST'])
def quizsociety():
    return render_template('quiz.html')

@app.route('/happinessclub', methods=['GET', 'POST'])
def happinessclub():
    return render_template('happiness_club.html')    

@app.route('/ethical', methods=['GET', 'POST'])
def ethical():
    return render_template('ethical.html')

@app.route('/editorial', methods=['GET', 'POST'])
def editorial():
    return render_template('editorial.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='GET':
        return render_template('register.html')   
    firstname=request.form.get('firstname')
    session['firstname']=firstname
    lastname=request.form.get('lastname')
    session['lastname']=lastname
    email=request.form.get('email')
    session['email']=email
    password=request.form.get('password')
    cpassword=request.form.get('cpassword')
    message=''
    if password==cpassword:
        message='Registration successful !'
        session['success']=True
    elif password!=cpassword:
        message='Password Mismatch !'
    return render_template('register.html', message=message)

@app.route('/quotes', methods=['GET', 'POST'])
def quotes():
    return render_template('quotes.html')

if __name__ == "__main__":
    app.run(debug=True)
 