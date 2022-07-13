def CelsiusToFahrenheit(temperature):
    return (9*temperature + 160)/5

def FahrenheitToCelsius(temperature):
    return (5*temperature - 160)/9

celsius = 10
fahrenheit = 86
print('Celsius To Fahrenheit ', celsius, ' => ', CelsiusToFahrenheit(celsius))
print('Fahrenheit To Celsius ', fahrenheit, ' => ', FahrenheitToCelsius(fahrenheit))