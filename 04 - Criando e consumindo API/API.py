from flask import Flask, request, render_template, redirect, url_for
from datetime import date
import sqlite3
from sqlite3 import Error
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database', 'db-produtos.db')

@app.route('/')
def home():
    return render_template('home.html')

#######################################################
# 1. Cadastrar produto


@app.route('/produtos/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    mensagem = ''
    if request.method == 'POST':
        descricao = request.form['descricao']
        precocompra = request.form['precocompra']
        precovenda = request.form['precovenda']
        datacriacao = date.today()

        mensagem = 'Erro - nao cadastrado'

        if descricao and precocompra and precovenda:
            registro = (descricao, precocompra, precovenda, datacriacao)

            try:
                conn = sqlite3.connect(DB_PATH)
                sql = ''' INSERT INTO produtos(descricao, precocompra, precovenda, datacriacao) VALUES(?,?,?,?) '''
                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()
                mensagem = 'Sucesso - cadastrado'
            except Error as e:
                print(e)
            finally:
                conn.close()
                return redirect(url_for('listar'))

    return render_template('cadastrar.html')

#######################################################
# 2. Listar produtos


@app.route('/produtos/listar', methods=['GET'])
def listar():
    try:
        conn = sqlite3.connect(DB_PATH)
        sql = '''SELECT * FROM produtos'''
        cur = conn.cursor()
        cur.execute(sql)
        registros = cur.fetchall()
        return render_template('listar.html', regs=registros)
    except Error as e:
        print(e)
        return render_template('listar.html', regs=[])
    finally:
        conn.close()

#######################################################
# 3. Excluir produto


@app.route('/produtos/excluir/<int:id>', methods=['GET'])
    # Infelizmente como estou usando html puro, nao consigo usar os metodos de delete e put/patch, recebo o erro "Method Not Allowed - The method is not allowed for the requested URL."

def excluir(id):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('DELETE FROM produtos WHERE idproduto = ?', (id,))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()
    return redirect(url_for('listar'))

#######################################################
# 4. Editar produto


@app.route('/produtos/editar/<int:id>', methods=['GET', 'POST'])
    # Infelizmente como estou usando html puro, nao consigo usar os metodos de delete e put/patch, recebo o erro "Method Not Allowed - The method is not allowed for the requested URL."

def editar(id):
    if request.method == 'POST':
        descricao = request.form['descricao']
        precocompra = request.form['precocompra']
        precovenda = request.form['precovenda']

        try:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute('''
                UPDATE produtos
                SET descricao = ?, precocompra = ?, precovenda = ?
                WHERE idproduto = ?
            ''', (descricao, precocompra, precovenda, id))
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()
        return redirect(url_for('listar'))
    
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('SELECT * FROM produtos WHERE idproduto = ?', (id,))
    produto = cur.fetchone()
    conn.close()
    return render_template('editar.html', produto=produto)

#######################################################
# 5. Página 404


@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404


#######################################################
if __name__ == '__main__':
    app.run(debug=True)
