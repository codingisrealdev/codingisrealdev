import socket
from flask import Flask, request, jsonify
from wakeonlan import send_magic_packet
import httpserver
from flask_cors import CORS, cross_origin
import requests
scriptwol= Flask(__name__)

CORS(scriptwol)
scriptwol.config["CORS_HEADERS"] = "Content-type: multipart/form-data"


url = "https://codingisrealdev.github.io/codingisrealdev/"
headers = {
    "X-Content-Type-Options": "nosniff"
}

response = requests.get(url, headers=headers)

ordenadoresparaboot = { 

    1: {"direccionip" : "123.123.123.123", "mac": "9UG:4HNG:UN3:4N9F:UFUN9"},

    2: {"direccionip" : "123.123.123.123", "mac": "9UG:4HNG:UN3:4N9F:UFUN9"},

    3: {"direccionip" : "123.123.123.123", "mac": "9UG:4HNG:UN3:4N9F:UFUN9"},

    4: {"direccionip" : "123.123.123.123", "mac": "9UG:4HNG:UN3:4N9F:UFUN9"} 
                        
                                                                   
} 

# Se crea un proceso que controla todo el envío del paquete WOL

def envioWOL(ordenadoresparaboot):

    # el try controla el proceso de enviar el paquete correctamente
    try: 

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', 9))
        magic_packet = b'\xFF' * 6 + bytes.fromhex(ordenadoresparaboot["mac"].replace(':' ''))


        # enviando el magic packet a la dirección IP por el puerto 9
        sock.sendto(magic_packet, (ordenadoresparaboot["direccionip"], 9))

        # cuando se envía el paquete correctamente, se envía un mensaje indicando a que ordenador se ha enviado el mensaje
        return 'El paquete se ha enviado al ordenador', 200

    # el except controla todos los resultados que no tienen que ver con el recurso

    except Exception as e:
        return 'El paquete no se ha enviado al ordenador'

    # el finally controla todas las cosas que se hacen se complete el proceso o no
        
    finally:
        
        sock.close()



@scriptwol.route('primero', methods=['GET'])
def infodehtml ():
    #    La variable num_pc es igual a lo que se reciba de usar el método get en el HTML (num_pc=4)
    
    if request.method == "GET":

        num_pc= request.args.get(num_pc, mimetype="text/plain")
        return jsonify(num_pc)

    

    if num_pc == "1":

        envioWOL(ordenadoresparaboot[1])
        print("Paquete enviado a ordenador número 1")

    elif num_pc == "2":
        envioWOL(ordenadoresparaboot[2])
        print("Paquete enviado a ordenador número 2")


    elif num_pc == "3":

        envioWOL(ordenadoresparaboot[3])
        print("Paquete enviado a ordenador número 3")

    elif num_pc == "4":

        envioWOL(ordenadoresparaboot[4])
        print("Paquete enviado a ordenador número 4")

    elif num_pc == "5":

        envioWOL(ordenadoresparaboot[5])
        print("Paquete enviado a ordenador número 5") 

    else:
        if num_pc is not None: 
            print("Numero de ordenador es incorrecto")


@scriptwol.route('secundario', methods=['GET'])
def infodehtml ():

    @scriptwol.route('tercero', methods=['GET'])
    def infodehtml ():

        @scriptwol.route('numcuatro', methods=['GET'])
        def infodehtml ():

            @scriptwol.route('quinto', methods=['GET'])
            def infodehtml ():

                if __name__ == "scriptwol":
                    scriptwol.run()
        
