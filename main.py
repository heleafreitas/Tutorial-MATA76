from flask import Flask, render_template, request
import bd_tutorial as db

app = Flask(__name__)

@app.route('/')
def registrar_atividade():
    return render_template('register.html')

@app.route('/acao', methods=['POST'])
def acao():
    nome = request.form['nome']
    descricao = request.form['descricao']
    data = request.form['data']
    inicio = 'null'
    fim = 'null'
    status = 'não iniciada'

    # if inicio == ' ' or not inicio:
    #     inicio = 'null'
    # else:
    #     status = 'iniciada'
    
    # if fim == ' ' or not fim:
    #     fim = 'null'
    # else:
    #     status = 'finalizada'

    values = (nome, descricao, data, inicio, fim, status)

    db.execute_query(query=db.QUERY_INSERT_TABLE_ACTIVITIES, data=values)
    
    return render_template('register.html')


app.run(debug=True)

    