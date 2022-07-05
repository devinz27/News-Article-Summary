from flask import Flask, request, render_template
from text import *

app = Flask(__name__)

@app.route('/',)
def index():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def summarize():
    
    if request.method == 'POST':
        if not request.form['articleText']:
            text = request.form.get('inputText')
        else:
            text = request.form.get('articleText')
         

        try:
            numOfLines = int(request.form.get('numOfLines'))
        except:
            numOfLines = 3

        summary = main(text,numOfLines)
        
        return render_template('index.html',
                               text_summary=summary,
                               )
    
if __name__ == '__main__':
    app.run(debug=True)