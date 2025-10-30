import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
import time

# Configuración del servidor SMTP de Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'cayunaocecilia@gmail.com'
smtp_password = 'nfah vvtb gzys kgkm'  # Reemplaza con tu contraseña de aplicación generada

# Lista de destinatarios
to_emails = [
'wendylizardo.g@gmail.com', 
'xime_aqualife@hotmail.com', 
'xusto.brand@gmail.com',
'yesenia.soto.t@gmail.com',
'yessica.perez@uach.cl	',
'yocelinne.cortes@gmail.com', 
'yonaibarra@gmail.com',
'zamoramillan@gmail.com',
'zcertanec@gmail.com',
'ZULETAPAULA@GMAIL.COM'
]

# Adjuntar la imagen al mensaje
image_path = 'dia_padre2.jpeg'  # Ruta de la imagen a adjuntar

# Contenido HTML del correo
body = """
<!DOCTYPE html PUBLIC "">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0" />
    <title>Día del Padre | La Gran Guía para un Gran Padre</title>
</head>
<body style="margin: 0; padding: 0;" bgcolor="#f5f5f5" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
    <table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" bgcolor="#f5f5f5">
        <tr>
            <td class="container-outer" align="center" valign="top" style="padding: 30px 0 30px 0;">
                <!-- Container 700px -->
                <table border="0" width="700" cellpadding="0" cellspacing="0" bgcolor="#ffffff" class="container" style="width: 700px;">
                    <tr>
                        <td style="border-top: 10px solid #F15156;">
                            <!-- Banner -->
                            <table align="center" border="0" width="640" cellpadding="0" cellspacing="0" class="container" style="width: 640px;">
                                <tr>
                                    <td><img src="https://gallery.mailchimp.com/4cb93458932f8621f1d708c6b/images/3682e236-4b1d-40d5-895a-214134ef8a2f.jpg"></td>
                                </tr>
                            </table>
                            <!-- Banner End -->

                            <!-- Título -->
                            <table align="center" border="0" width="640" cellpadding="0" cellspacing="0" class="container" style="width: 640px;">
                                <tr>
                                    <td mc:edit="subheader" class="header-title" style="padding: 30px 0 20px 0; font-weight: bold; font-size: 45px; font-family: 'Noto sans', sans-serif; text-align: center;">La Gran Guía <br>para un Gran Padre</td>
                                </tr>
                            </table>
                            <!-- Título End -->

                            <!-- Contenido -->
                            <table mc:repeatable align="center" border="0" width="640" cellpadding="0" cellspacing="0" class="container" style="width: 640px;">
                                <tr>
                                    <td>
                                        <table class="container" align="left" border="0" width="600" cellpadding="0" cellspacing="0" style="width: 400px;">
                                            <tr>
                                                <td mc:edit="article-image" class="article-thumb">
                                                    <a href="https://www.tiendaenfoque.cl/producto/pack-dia-del-padre-la-gran-guia-de-chile-guia-digital-pdf-1-marcador-de-libro-2-mini-jarros-cafe/">
                                                        <img src="cid:image1" width="600" height="600" >
                                                    </a>
                                                </td>
                                            </tr>
                                        </table>

                                        <table class="container" align="center" border="0" width="600" cellpadding="0" cellspacing="0" style="width: 400px;">
                                            <tr>
                                                <td mc:edit="article-content" class="article-content" style="padding: 2px; text-align: center; font-size: 20px;">
                                                    El pack de regalo se envía embalado en una hermosa caja de cartón negra con envoltura de papel seda.
                                                </td>
                                            </tr>
                                            <tr>
                                                <td mc:edit="article-content" class="article-content" style="padding:2px; text-align: center; font-size: 20px;">¿A tu papá le gusta viajar? ¿Sueña con hacer el gran viaje de su vida en auto? ¿Qué te parece si lo animas revisando lugares, circuitos, rutas y destinos con la mejor guía rutera de Chile?</td>
                                            </tr>
                                        </table>

                                        <br />
                                        <br />
                                        <br />

                                        <table class="container" align="center" border="0" width="400" cellpadding="0" cellspacing="0" style="width: 400px;">
                                            <tr>
                                                <td mc:edit="article-content" class="article-content" style="padding: 0 0 2px 30px; text-align: center; margin-bottom: 100px;">
                                                    <a href="https://www.tiendaenfoque.cl/" style="text-decoration: none; color: #F15156; font-weight: bold; font-size: 28px; display: inline-block;">Ir a la Tienda</a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td><img src="https://gallery.mailchimp.com/4cb93458932f8621f1d708c6b/images/3682e236-4b1d-40d5-895a-214134ef8a2f.jpg"></td>
                                </tr>
                            </table>
                            <!-- Contenido End -->

                            <!-- Banner Final -->
                            <table align="center" border="0" width="640" cellpadding="0" cellspacing="0" class="container" style="width: 640px;">
                                <tr>
                                    <td><img src="https://gallery.mailchimp.com/4cb93458932f8621f1d708c6b/images/68167ec6-2a7f-4ddc-a890-0a627414d878.jpg"></td>
                                </tr>
                            </table>
                            <!-- Banner Final End -->

                            <!-- CTA -->
                            <table align="center" border="0" width="700" cellpadding="0" cellspacing="0" class="container" style="width: 700px; background-color: #F15156;">
                                <tr>
                                    <td mc:edit="article-content" class="article-content" style="padding: 0 0 2px 30px; text-align: center;">
                                        <p style="text-decoration: none; color: #FFFFFF; font-weight: bold; font-size: 20px;">Compra ahora, entrega inmediata hasta el viernes 14 al mediodía.</p>
                                    </td>
                                </tr>
                            </table>
                            <!-- CTA End -->
                        </td>
                    </tr>
                </table>
                <!-- Container 700px End -->
            </td>
        </tr>
    </table>
    <!-- Wrapper 100% End -->
</body>
</html>
"""

# Conexión al servidor SMTP de Gmail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)

    start_time = time.time()  # Inicio del temporizador

    for to_email in to_emails:
        msg = MIMEMultipart()
        msg['Subject'] = 'DIA DEL PADRE | La Gran Guía para un Gran Padre'
        msg['From'] = smtp_username
        msg['To'] = to_email

        # Adjuntar el cuerpo HTML al mensaje
        msg.attach(MIMEText(body, 'html'))

        # Adjuntar la imagen al mensaje
        if os.path.exists(image_path):
            with open(image_path, 'rb') as img_file:
                img = MIMEImage(img_file.read(), name=os.path.basename(image_path))
                img.add_header('Content-ID', '<image1>')
                msg.attach(img)

        server.send_message(msg)
        print(f"Correo electrónico enviado correctamente a: {to_email}")

    elapsed_time = time.time() - start_time  # Fin del temporizador
    print(f"Todos los correos electrónicos han sido enviados correctamente en {elapsed_time:.2f} segundos.")
