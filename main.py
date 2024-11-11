from flask import Flask, render_template, request

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    temp = float(request.form['temperature'])
    scale = request.form['scale']
    
    if scale == 'celsius':
        result_f = celsius_to_fahrenheit(temp)
        result_k = celsius_to_kelvin(temp)
        result = f"{temp} °C = {result_f:.2f} °F = {result_k:.2f} K"
    elif scale == 'fahrenheit':
        result_c = fahrenheit_to_celsius(temp)
        result_k = celsius_to_kelvin(result_c)
        result = f"{temp} °F = {result_c:.2f} °C = {result_k:.2f} K"
    elif scale == 'kelvin':
        result_c = kelvin_to_celsius(temp)
        result_f = celsius_to_fahrenheit(result_c)
        result = f"{temp} K = {result_c:.2f} °C = {result_f:.2f} °F"
    else:
        result = "Invalid scale selected."
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
