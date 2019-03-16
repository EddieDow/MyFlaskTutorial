from flask import Flask,render_template,request,redirect
app = Flask(__name__)
app.vars={}

app.questions={}
app.questions['How many eyes do you have?']=('1','2','3')
app.questions['Which fruit do you like best?']=('banana','mango','pineapple')
app.questions['Do you like cupcakes?']=('yes','no','maybe')
app.nquestions=len(app.questions)

@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index_method():
    nquestions = app.nquestions
    if request.method == 'GET':
        return render_template('userinfo.html',num=nquestions)
    else:
        #request was a POST
        app.vars['name'] = request.form['name_lulu']
        app.vars['age'] = request.form['age_lulu']

        f = open('%s_%s.txt'%(app.vars['name'],app.vars['age']),'w')
        f.write('Name: %s\n'%(app.vars['name']))
        f.write('Age: %s\n\n'%(app.vars['age']))
        f.close()

        return redirect('/main_lulu')

@app.route('/main_lulu')
def main_lulu2():
    if len(app.questions)==0 : return render_template('end_lulu.html')
    return redirect('/next')


@app.route('/next',methods=['POST','GET'])
def next_lulu():
    if request.method == 'GET':
        n=app.nquestions-len(app.questions)+1
        q = list(app.questions.keys())[0] #python indexes at 0
        a1=app.questions[q][0]
        a2=app.questions[q][1]
        a3=app.questions[q][2]

         # save current question
        app.currentq=q

        return render_template('layout_lulu.html',num=n,question=q,ans1=a1,ans2=a2,ans3=a3)
    else:
        f=open('%s_%s.txt'%(app.vars['name'],app.vars['age']),'a') #a is for append
        f.write('%s\n'%(app.currentq))
        f.write('%s\n\n'%(request.form['answer_from_layout_lulu'])) #do you know where answer_lulu comes from?
        f.close()

        app.questions.pop(app.currentq)

    return redirect('/main_lulu')
        


if __name__ == '__main__':
    app.run()

