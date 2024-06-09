from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    provincia = request.form['provincia']
    cultivo = request.form['cultivo']
    idcompania = request.form['id-compania']
    sup_sembrada = request.form['sup-sembrada']
    sup_cosecha = request.form['sup-cosechada']
    produccion = request.form['produccion']

    #Aqui podrias llamar a tu funcion prediction
    #prediction(provincia, cultivo, idcompania, sup_sembrada, sup_cosecha, produccion)

    # Aquí puedes agregar el código para procesar los datos y hacer la predicción
    # Por ahora, solo devolvemos los datos recibidos
    result = {
        'provincia':provincia,
        'cultivo':cultivo,
        'idcompania':idcompania,
        'sup_sembrada':sup_sembrada,
        'sup_cosechada':sup_cosecha,
        'produccion':produccion
    }

    return f"Datos recibidos: {result}"

if __name__ == '__main__':
    app.run(debug=True)