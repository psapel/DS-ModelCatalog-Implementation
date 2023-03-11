from flask import Flask, request, render_template, url_for, redirect
from dotenv import load_dotenv
load_dotenv()

import meilisearch
from meilisearch import Client

import json
import os

import subprocess

app = Flask(__name__)

#CHECKBOXES

@app.route('/', methods=['GET','POST'])
@app.route('/checkbox')

def checkbox():
    if request.method == 'POST':
        x = request.form.getlist('checked')
        print(x)
        return 'ok'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

#RADIO BUTTONS

# Path to directory containing JSON files
json_dir = 'C:/Users/annga/OneDrive/Desktop/HiWi - IKV/GUI/gui/DS-ModelCatalog/json_files/'
scripts_dir = 'C:/Users/annga/OneDrive/Desktop/HiWi - IKV/GUI/gui/DS-ModelCatalog/scripts/'
client = meilisearch.Client('http://127.0.0.1:7700', 'masterKey')
index = client.index('json_files')
index.update_filterable_attributes(['gender', 'nationality'])
results = []
for file in os.listdir(json_dir):
        if file.endswith('.json'):
            with open(os.path.join(json_dir, file), 'r') as f:
                data = json.load(f)
                results.append(data)
index.add_documents(results)


@app.route('/radio_button', methods=['GET', 'POST'])
def radio_button():
 
    ans = request.form['gender']
    gender = index.search(ans)
                  
    if ans == 'Non-binary' or ans == 'other':
        return f"No module found"
    elif ans == 'Male':
        output = ''
        for a in gender['hits']:
            output = output + 'module' + " " + str(a['id']) + '<br>'
        return output
    else:
        output1 = ''
        for b in gender['hits']:
            if b['nationality']=='non-EU':
                output1 = output1 + 'module' + " " + str(b['id']) + '<br>'
        return output1
         
 
if __name__=='__main__':
    app.run(debug=True, use_reloader=True)
        
#DROPDOWN MENU

@app.route('/')
@app.route("/dropdown" , methods=['GET', 'POST'])
def dropdown():
    ans_2 = request.form.get('choice')
    #return(str(ans_1))
    return f"I like % s" % ans_2

if __name__=='__main__':
    app.run(debug=True, use_reloader=True)
    
    
#RADIO BUTTONS - new!   

@app.route('/search', methods=['GET', 'POST'])
def search():
    
    ans = request.form['gender']
    gender = index.search(ans)
                        
    if ans == 'Non-binary' or ans == 'other':
        return f"No module found"
    elif ans == 'Male':
        output = ''
        for a in gender['hits']:
            output = output + 'module' + " " + str(a['id']) + '<br>'
        return output
    else:
        return redirect('/nationality')



@app.route('/nationality', methods=['GET', 'POST'])
def nationality():
    if request.method == 'POST':
        ans1 = request.form.get('nationality')
        nasF = index.search('',
            {
                'filter': f'gender=Female AND nationality={ans1}'
            }
        )
        
           
        if ans1=='EU':
            output1 = ''
            for b in nasF['hits']:
                output1 = output1 + 'Module' + " " + str(b['id']) + '<br>'
            return redirect(url_for('convert', out=output1))  
             
        elif ans1=='Non-EU':
            output2 = ''
            for c in nasF['hits']:
                output2 = output2 + 'Module' + " " + str(c['id']) + '<br>'
            return redirect(url_for('convert', out=output2))
         
          
    return render_template('nationality.html')


@app.route('/convert/<out>', methods=['GET','POST'])

# convert output of the nationality function into a string 
def convert(out):
    if request.method=='GET':
        out  = out[:-4]
        out = out.split("<br>")
        out = ','.join(out)
        return redirect(url_for('selection', out=out))

             
             
#CHECKBOXES - new!
@app.route('/selection/<out>', methods=['GET','POST'])

def selection(out):
     # Convert the input string into a list of strings
    out_list = out.split(",")
    print(out_list)
    if request.method == 'POST':
        #Get the selected module value from the form submission
        selected_modules = request.form.getlist('module')
        #selected_modules = '<br>'.join(' '.join(item.split())  for item in selected_modules)
        module_list =  [int(module.split()[1]) for module in selected_modules]
        #return selected_modules
        output_dict = {}
        for module in module_list:
            output = subprocess.check_output(['python', scripts_dir + f'script{module}.py'], stderr=subprocess.STDOUT, text=True)
            output_dict[module] = output.strip()
        return render_template('result.html', output_dict=output_dict)
    else:
        #Render the selection.html template with the out_list variable
        return render_template('selection.html', out_list=out_list)
    
if __name__ == '__main__':
    app.run(debug=True) 

