from flask import Flask, redirect, render_template, request, url_for
import bd_tutorial as db

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    lista = listarTarefas()
    return render_template('home.html', data=lista)

@app.route('/iniciar_tarefa/<string:id>', methods=['POST','GET'])
def iniciar_tarefa(id):
    identificador = int(id)
    resposta = db.select_from_table(custom_query=f"SELECT status FROM activities WHERE id = {identificador}")
    if resposta[0][0] == 'não iniciada':
        db.execute_query(f"UPDATE activities SET status='iniciada' WHERE id = {identificador}")
    return redirect(url_for('home'))

@app.route('/finalizar_tarefa/<string:id>', methods=['POST','GET'])
def finalizar_tarefa(id):
    identificador = int(id)
    resposta = db.select_from_table(custom_query=f"SELECT status FROM activities WHERE id = {identificador}")
    if resposta[0][0] == 'iniciada':
        db.execute_query(f"UPDATE activities SET status='finalizada' WHERE id = {identificador}")
    return redirect(url_for('home'))

@app.route('/deletar_tarefa/<string:id>', methods=['POST','GET'])
def deletar_tarefa(id):
    identificador = int(id)
    db.execute_query(f"DELETE FROM activities WHERE id = {identificador}")
    return redirect(url_for('home'))

@app.route('/editar_tarefa/<string:id>', methods=['POST','GET'])
def editar_tarefa(id):
    identificador = int(id)
    resposta = db.select_from_table(custom_query=f"SELECT id, name, description, date FROM activities WHERE id = {identificador}")
    id = resposta[0][0]
    nome = resposta[0][1]
    descricao = resposta[0][2]
    data = resposta[0][3]
    return render_template('update.html', nome=nome, descricao=descricao, data=data, id=id)

@app.route('/atualizar/<string:id>', methods=['POST','GET'])
def atualizar(id):
    descricao = request.form['descricao']
    nome = request.form['nome']
    data = request.form['data']

    if descricao != '':
         db.execute_query(f"UPDATE activities SET description='{descricao}' WHERE id = {int(id)}")
    if nome != '':
         db.execute_query(f"UPDATE activities SET name='{nome}' WHERE id = {int(id)}")
    if data != '':
         db.execute_query(f"UPDATE activities SET date='{data}' WHERE id = {int(id)}")

    return redirect(url_for('home'))

@app.route('/irParaAdicionar', methods=['POST'])
def irParaAdicionar():
    return redirect(url_for('registrar_atividade'))

def listarTarefas():
    resposta = db.select_from_table(table_name="activities")
    lista = []
    for i in range(len(resposta)):
        id = resposta[i][0]
        tarefa = resposta[i][2]
        data = resposta[i][3]
        status = resposta[i][6]

        classe = 'categoryRed'

        if status == 'finalizada':
            classe = 'categoryGreen'
        elif status == 'iniciada':
            classe = 'categoryYellow'

        objeto = {'tarefa': tarefa, 'id': id, 'dia': data, 'classe': classe}
        lista.append(objeto)

    return lista


@app.route('/register')
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
    
    return redirect(url_for('home'))


app.run(debug=True)

    