from flask import Flask, render_template, request, session , g , redirect , url_for ,abort, render_template , flash, jsonify
import sqlite3



#configuration
DATABASE = 'questions.db'
DEBUG = True
SECRET_KEY = 'development_key'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g,'db',None)
    if db is not None:
        db.close()

@app.route('/<qno>')
def home(qno):
    cur = g.db.execute('select passage,nowords from paracompile where qno=?',[qno])
    rows = cur.fetchall()
    for row in rows:
        paras={'para':str(row[0]),'nofwords':row[1],'url':'/testset/'+qno}
    return render_template('index.html',paras = paras)

@app.route('/testset/<qno>')
def getTest(qno):
    test = {}
    
    #Inserting Passage to json
    '''
    cur = g.db.execute('select passage,nowords from paracompile where qno=?',[qno])
    rows = cur.fetchall()
    for row in rows:
        paras={'para':row[0],'nofwords':row[1]}
    test['paralist'] = paras
    '''
    #Inserting questions to json
    cur = g.db.execute('select questext,opta,optb,optc,optd,optans from quesset where qno=? order by quesord',[qno])
    rows = cur.fetchall()
    quess = []
    for row in rows:
        quess.append({'questext':row[0],'opta':row[1],'optb':row[2],'optc':row[3],'optd':row[4],'optans':row[5]})
    test['queslist'] = quess
    return jsonify(testlist = test)

if __name__ == '__main__':
    app.run(debug = True)