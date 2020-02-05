from flask import Flask,  render_template
from data import reg

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hola mundo"


@app.route('/peru')
def reg_peru():
    cips = reg('/cips.txt')
    print(cips[0]['OrderId'])
    return render_template('index.html', Title='Regularizar pago', cips=cips)


@app.route('/ecuador')
def reg_ecu():
    cips = reg('/cips.txt')
    print(cips[0]['OrderId'])
    return render_template('ecua.html', Title='Regularizar pago', cips=cips)


if __name__ == '__main__':
    app.run()
