from flask import Flask, request, render_template, redirect

app = Flask(__name__)
valores_lista = []

@app.route('/')
def index():
    return render_template('adiccionar.html')

@app.route('/submit', methods=['POST'])
def submit():
    valor = request.form['valor']
    valores_lista.append(valor)
    #for i in range(len(valores_lista)):
        # for j in range(i+1,(len(valores_lista))):
        #      if valores_lista[i]>valores_lista[j]:
        #        aux=valores_lista[i]
        #        valores_lista[i]=valores_lista[j]
        #        valores_lista[j]=aux
        # return valores_lista

    return render_template('result.html', valores_lista=valores_lista)

if __name__ == '__main__':
    app.run(debug=True)

