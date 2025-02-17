from flask import Flask, render_template, Response
import cv2
import numpy as np
import time

app = Flask(__name__)

cap = cv2.VideoCapture(0)  # Iniciar la cámara

# Definir el área de detección
zona_deteccion_x, zona_deteccion_y = 200, 200
tamano_zona = 100

contador_piezas_zona = 0
piezas_activas = []
umbral_tiempo = 1 / 1000
divisor_contador = 2  # Ajuste del contador

# Variables para controlar la actualización del gráfico cada 10 segundos
ultimo_tiempo_actualizacion_grafico = time.time()
producciones = []
piezas_detectadas = []

def generar_video():
    global contador_piezas_zona, ultimo_tiempo_actualizacion_grafico, producciones, piezas_detectadas

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red1 = np.array([0, 120, 70])
        upper_red1 = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

        lower_red2 = np.array([170, 120, 70])
        upper_red2 = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

        mask = cv2.bitwise_or(mask1, mask2)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 500:
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

                    if zona_deteccion_x < cx < zona_deteccion_x + tamano_zona and zona_deteccion_y < cy < zona_deteccion_y + tamano_zona:
                        pieza_encontrada = False
                        for pieza in piezas_activas:
                            if abs(cx - pieza[0]) < 30 and abs(cy - pieza[1]) < 30:
                                pieza_encontrada = True
                                break

                        if not pieza_encontrada:
                            piezas_activas.append((cx, cy, time.time()))

        for pieza in piezas_activas[:]:
            cx, cy, tiempo_entrada = pieza
            if time.time() - tiempo_entrada >= umbral_tiempo:
                contador_piezas_zona += 1
                piezas_activas.remove(pieza)

        contador_piezas_zona_ajustado = contador_piezas_zona // divisor_contador

        # Dibujar área de detección y contador
        cv2.rectangle(frame, (zona_deteccion_x, zona_deteccion_y), 
                      (zona_deteccion_x + tamano_zona, zona_deteccion_y + tamano_zona), (0, 255, 0), 2)
        cv2.putText(frame, f"Piezas: {contador_piezas_zona_ajustado}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Codificar el frame en JPEG para enviarlo al navegador
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        # Actualizar el gráfico cada 10 segundos (solo el gráfico)
        if time.time() - ultimo_tiempo_actualizacion_grafico >= 10:
            ultimo_tiempo_actualizacion_grafico = time.time()

            # Agregar nueva producción al gráfico
            piezas_detectadas.append(contador_piezas_zona)
            producciones.append(f"Producción {len(producciones) + 1}")

            # Limitar el tamaño de las listas para no sobrecargar la memoria
            if len(producciones) > 100:
                producciones.pop(0)
                piezas_detectadas.pop(0)

            # El gráfico se actualizará en la interfaz web con los nuevos datos
            print(f"Gráfico actualizado: {len(producciones)} producciones registradas")

@app.route('/')
def index():
    # Aquí aseguramos que las variables de producciones y piezas detectadas estén disponibles
    return render_template('index.html', contador=contador_piezas_zona, producciones=producciones, piezas_detectadas=piezas_detectadas)

@app.route('/video_feed')
def video_feed():
    return Response(generar_video(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
