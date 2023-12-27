from flask import Flask, render_template, request
import psycopg2 

app = Flask(__name__)

lista=['hallennen','123','oi']

def conexao_banco():
    global valida_senha
    global valida_usuario

    con = psycopg2.connect(host='localhost', database='user', user='postgres',password='1804' )
    cur = con.cursor()
    v_usuario = """SELECT nome FROM registros WHERE nome = '{}'""".format(usuario) 
    cur.execute(v_usuario)  
    valida_usuario = cur.fetchone()

    v_senha = """SELECT senha FROM registros WHERE nome = '{}'""".format(usuario.capitalize())
    cur.execute(v_senha)
    valida_senha = cur.fetchone()

    con.close()
    

@app.route('/', methods=['GET','POST'])
def login():
    global usuario
    global senha

    try:
        usuario = request.form['usuario'].capitalize()
        senha = request.form['senha']

        conexao_banco()

        if usuario == valida_usuario[0] and senha == valida_senha[0] :

            valida_login = 'Login Efetuado com sucesso!'
            print(valida_login)

    except:
        print('Usuario/Senha incorreto.')

    return render_template('login.html')

app.run(host='localhost', port=5001, debug=True)