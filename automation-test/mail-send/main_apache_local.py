import smtplib
from email.mime.text import MIMEText

# Configura los detalles del mensaje
msg = MIMEText('Este es el cuerpo del correo de prueba.')
msg['Subject'] = 'Correo de Prueba desde Mercury'
msg['From'] = 'calderoncay123@gmail.com'  # Cambia esto a tu dirección de correo
msg['To'] = 'calderoncay123.firebase@gmail.com'  # Cambia esto a la dirección de Gmail del destinatario

# Configura el servidor SMTP
smtp_server = 'localhost'
smtp_port = 25  # Asegúrate de que este puerto esté abierto y escuchando

# Credenciales de autenticación (cambia estas credenciales por las que configuraste en Mercury)
username = 'jose'  # Cambia esto a tu usuario en Mercury
password = 'Jm616.#natnat'  # Cambia esto a tu contraseña en Mercury

# Envía el correo
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.login(username, password)  # Autenticación
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
    print("Correo enviado exitosamente")
except Exception as e:
    print(f"Error al enviar el correo: {e}")
