from flask import Flask, jsonify  # Importamos Flask y jsonify

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Definimos una ruta que se activará al acceder a '/saludo' por el método GET
@app.route('/saludo', methods=['GET'])
def saludo():
    # Usamos jsonify para devolver una respuesta en formato JSON
    return jsonify({"mensaje": "¡Hola! Bienvenido a la API."})

# Esto asegura que el servidor solo se ejecute si este archivo es ejecutado directamente,
# no si es importado como un módulo en otro script.
if __name__ == '__main__':
    # Ejecuta la aplicación en modo de depuración. Esto significa que Flask reiniciará
    # automáticamente el servidor si detecta cambios en el código.
    app.run(debug=True)


