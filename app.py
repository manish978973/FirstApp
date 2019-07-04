from flask import Flask, render_template, request
from processing import do_calculation
from processing import do_age

app = Flask(__name__)
app.config["DEBUG"] = True


#@app.route('/profile/<name>')
#def hello_world(name):
  #  return render_template("profile.html", name=name)


@app.route('/', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        number1 = float(request.form['number1'])
        number2 = float(request.form['number2'])

        result = do_calculation(number1, number2)

        return '''
           <html>
              <body>
                 <p>The result is {result} </p>
                  <p><a href="/">Click here to recalculate</a> </p>
              </body>
           </html>
        '''.format(result=result)

    return '''
        <html>
           <body>
             <p>Enter your numbers:</p>
             <form method="POST" action=".">
             <p><input name='number1'/></p>
             <p><input name='number2'/></p>
             <p><input type='submit' value='Do Addition'/></p>
             </form>
           </body>
     
         </html>
    '''



@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        age = int(request.form['age'])
        calage = do_age(age)

        return render_template('index.html',age1=calage)


    return render_template('profile.html')


if __name__ == '__main__':
    app.run()
