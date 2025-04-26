from flask import Flask, render_template, request

app = Flask(__name__)

def converter(unidade, valor):
    try:
        valor = float(valor)
    except ValueError:
        return "Valor inválido"

    match unidade:
        # TEMPERATURA
        case 'F->C':
            resultado = (valor - 32) * 5 / 9
            return f"{resultado:.2f} °C"
        case 'C->F':
            resultado = (valor * 9 / 5) + 32
            return f"{resultado:.2f} °F"
        case 'K->C':
            resultado = valor - 273.15
            return f"{resultado:.2f} °C"
        case 'C->K':
            resultado = valor + 273.15
            return f"{resultado:.2f} K"
        case 'K->F':
            resultado = (valor - 273.15) * 9 / 5 + 32
            return f"{resultado:.2f} °F"
        case 'F->K':
            resultado = (valor - 32) * 5 / 9 + 273.15
            return f"{resultado:.2f} K"

        # COMPRIMENTO
        case 'km->m':
            resultado = valor * 1000
            return f"{resultado:.2f} metros"
        case 'km->cm':
            resultado = valor * 100_000
            return f"{resultado:.2f} centímetros"
        case 'm->cm':
            resultado = valor * 100
            return f"{resultado:.2f} centímetros"
        case 'm->mm':
            resultado = valor * 1000
            return f"{resultado:.2f} milímetros"
        case 'm->km':
            resultado = valor / 1000
            return f"{resultado:.4f} quilômetros"
        case 'cm->m':
            resultado = valor / 100
            return f"{resultado:.2f} metros"
        case 'cm->km':
            resultado = valor / 100_000
            return f"{resultado:.6f} quilômetros"

        # MASSA
        case 'kg->g':
            resultado = valor * 1000
            return f"{resultado:.2f} gramas"
        case 'g->kg':
            resultado = valor / 1000
            return f"{resultado:.3f} quilogramas"
        case 'mg->kg':
            resultado = valor / 1_000_000
            return f"{resultado:.6f} quilogramas"
        case 'kg->mg':
            resultado = valor * 1_000_000
            return f"{resultado:.0f} miligramas"
        case 'mg->g':
            resultado = valor / 1000
            return f"{resultado:.3f} gramas"

        case _:
            return "Unidade não reconhecida"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def convert():
    unidade = request.form.get('unidade')
    valor = request.form.get('valor')

    nome=unidade
    resultado = converter(unidade, valor)

    return render_template('results.html', nome=nome, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
