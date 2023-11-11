import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
import smtplib
import datetime
import cv2

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def reconocer_comando():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)

        try:
            comando = r.recognize_google(audio, language="es-ES")
            print(f"Has dicho: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            print("Lo siento, no entendí el comando. ¿Puedes repetirlo?")
            return ""
        except sr.RequestError:
            print("Lo siento, hubo un error al intentar reconocer el comando.")
            return ""

def reproducir_video(query):
    pywhatkit.playonyt(query)

def obtener_hora():
    ahora = datetime.datetime.now()
    hora = ahora.strftime("%H:%M")
    return hora

def buscar_wikipedia(consulta):
    resultado = wikipedia.summary(consulta, sentences=1)
    return resultado

def abrir_google():
    webbrowser.open("https://www.google.com")

def enviar_correo(destinatario, asunto, cuerpo):
    # Configurar la conexión SMTP (puedes usar tu propio servidor SMTP)
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login('tu_correo@gmail.com', 'tu_contraseña')

    # Crear el mensaje
    mensaje = f"Asunto: {asunto}\n\n{cuerpo}"

    # Enviar el correo
    servidor.sendmail('tu_correo@gmail.com', destinatario, mensaje)

    # Cerrar la conexión SMTP
    servidor.quit()

def tomar_foto():
    # Iniciar la cámara
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()

    # Guardar la imagen
    cv2.imwrite("foto.png", frame)

    # Liberar la cámara
    cam.release()

    # Cerrar la ventana de OpenCV
    cv2.destroyAllWindows()

# Nombre del asistente
nombre_asistente = "Mateo"

# Loop principal
while True:
    comando = reconocer_comando()

    if "nombre" in comando:
        hablar(f"¡Hola! Soy {nombre_asistente}. ¿En qué puedo ayudarte?")

    elif "Reproduce un video" in comando:
        hablar("¿Qué video deseas reproducir?")
        video = reconocer_comando()
        reproducir_video(video)

    elif "hora" in comando:
        hora = obtener_hora()
        hablar(f"La hora actual es {hora}")

    elif "Buscar en Wikipedia" in comando:
        hablar("¿Qué quieres buscar en Wikipedia?")
        consulta = reconocer_comando()
        resultado = buscar_wikipedia(consulta)
        hablar(resultado)

    elif "Abrir Google" in comando:
        abrir_google()

    elif "Enviar correo" in comando:
        hablar("¿A quién quieres enviar el correo?")
        destinatario = reconocer_comando()

        hablar("¿Cuál es el asunto del correo?")
        asunto = reconocer_comando()

        hablar("¿Qué quieres escribir en el cuerpo del correo?")
        cuerpo = reconocer_comando()

        enviar_correo(destinatario, asunto, cuerpo)

    elif "Toma una foto" in comando:
        tomar_foto()
        hablar("¡Foto tomada!")

    elif "Salir del asistente" in comando:
        hablar("vale, que estes bien.")
        break

    else:
        hablar("No entendí el comando. ¿Puedes repetirlo?")
