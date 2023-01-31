from flask import Flask, request, render_template, url_for
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

#CHECKBOXES

@app.route('/', methods=['GET','POST'])
@app.route('/checkbox')

def checkbox():
    if request.method == 'POST':
        print(request.form.getlist('checked'))
        return 'OK'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

#RADIO BUTTONS

@app.route('/radio_button', methods=['POST'])

@app.route('/radio_button')
def radio_button():
    ans = request.form['gender']
    if ans == "Male" or ans== "Female" or ans=="Non-binary":
        return f"{ans} student"
    else:
        return f"Student of {ans} gender"

  
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

#DROPDOWN MENU

@app.route('/')
@app.route("/dropdown" , methods=['GET', 'POST'])
def dropdown():
    ans_1 = request.form.get('choice')
    #return(str(ans_1))
    return f"I like % s" % ans_1

if __name__=='__main__':
    app.run(debug=True, use_reloader=True)

