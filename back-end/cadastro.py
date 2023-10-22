import bd_tutorial as db
from js import document

def registrar_atividade():
    nome = document.querySelector('#nome').value
    descricao = document.querySelector('#descricao').value
    data = document.querySelector('#data').value
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

    data = (f"'Helen'",f"'Teste'", f"'22/10/2023'", f"'{inicio}'", f"'{fim}'", f"'{status}'")

    db.execute_query(query=db.QUERY_INSERT_TABLE_ACTIVITIES, data=data)
    