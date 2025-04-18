import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def detectar_cajas(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    azul_bajo = np.array([90, 50, 150])
    azul_alto = np.array([130, 255, 255])
    mascara = cv2.inRange(hsv, azul_bajo, azul_alto)

    kernel = np.ones((5, 5), np.uint8)
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_DILATE, kernel)

    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contador = 0
    for c in contornos:
        if cv2.contourArea(c) > 1000:
            contador += 1
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.putText(frame, f"Cajas azules: {contador}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    return frame, mascara

def ejecutar_imagen():
    path = filedialog.askopenfilename(title="Selecciona una imagen")
    if not path:
        return
    img = cv2.imread(path)
    img = cv2.resize(img, (640, 800))
    resultado, mascara = detectar_cajas(img)
    cv2.imshow("Detección en imagen", resultado)
    cv2.imshow("Máscara azul", mascara)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def ejecutar_video():
    path = filedialog.askopenfilename(title="Selecciona un video")
    if not path:
        return
    cap = cv2.VideoCapture(path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (640, 480))
        resultado, mascara = detectar_cajas(frame)
        cv2.imshow("Video", resultado)
        cv2.imshow("Máscara", mascara)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def ejecutar_camara():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (640, 480))
        resultado, mascara = detectar_cajas(frame)
        cv2.imshow("Cámara", resultado)
        cv2.imshow("Máscara", mascara)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Detección de cajas azules")
ventana.geometry("300x200")

tk.Label(ventana, text="Selecciona una opción:", font=("Arial", 12)).pack(pady=10)
tk.Button(ventana, text="Procesar Imagen", width=25, command=ejecutar_imagen).pack(pady=5)
tk.Button(ventana, text="Procesar Video", width=25, command=ejecutar_video).pack(pady=5)
tk.Button(ventana, text="Usar Cámara en Vivo", width=25, command=ejecutar_camara).pack(pady=5)

ventana.mainloop()