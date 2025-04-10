from flask import flask, render_template, request, redirect, url_for, session

app = flask(_name_)
app.secret_key = 's3cr3t' #Chave secreta para seções

@pp.route('/')
def index():
    return render_template('index.html')

@pp.route('/adicionar', methods = ['POST'])
def adicionar():
    item = request.form.get('item')
    quantidade = int(request.form.get('quantidade'))
    
    if pedidos not in session: 
        session['pedidos'] = []
        
        session['pedidos'].append({'item': item, 'quantidade': quantidade})
        session.modified = True
        return redirect(url_for('pedidos'))
    
@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html', pedidos=session.get('pedidos', []))

@pp.route('/editar/<int:index>', methods = ['POST'])
def editar(index):
    nova_quantidade = int(request.form.get('quantidade'))
    session['pedidos'].pop(index)
    session.modified = True
    return redirect(url_for('pedidos'))

@pp.route('/excluir/<int:index>')
def excluir(index):
    session['pedidos'].pop(index)
    session.modified = True
    return redirect(url_for('pedidos'))

if _name_ == '_main_':
    app.run(debug=True)