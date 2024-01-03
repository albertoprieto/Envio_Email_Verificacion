import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

class EnviaEmail():

    def __init__(self):
        
        self.registered_sender = ''
        self.issued_to = ''
        self.moded_subject = ''
        
    def send_email(self):

        ses = boto3.client('ses', region_name = 'us-west-2')
        mensaje = MIMEMultipart()
        mensaje['Subject'] = f'Nómina {self.moded_subject}'
        mensaje['From'] = self.registered_sender
        mensaje['To'] = self.issued_to
        cuerpo_mensaje = f"""

        <img src="https://notificacion-proveedores.s3.us-west-2.amazonaws.com/gimlogo.jpg" alt="GIM LOGO" width="350" height="130">
        <p>Correo de verificación para comprobar si está vigente la cuenta : {self.issued_to} </p>
        
        Este correo fue enviado por la compañía:
        <br>

        <center><b>PABLO IGNACIO MICHEL ONTIVEROS.</b>
        <br>
        ANDRES QUINTANA ROO No. 1501, GUADALAJARA, JALISCO, MÉXICO, C.P. 44220, Col. GUADALUPANA SUR, 
        <br>
        (01) 33 3585-55-50, 3823-71-20 FAX (01) 33 35 85-55-79
        </center>

        <br>
        <hr>
        <p>Para cancelar la suscripción y ya no sigas recibiendo este tipo de notificaciones, por favor notifícanos al correo agustin.valencia@michel.com.mx . Nos aseguraremos de actualizar nuestras listas de distribución según tus preferencias.</p>
        
        <i>

        Este correo electrónico es confidencial y/o puede contener información privilegiada.
        Si usted no es su destinatario o no es alguna persona autorizada por este para recibir sus correos electrónicos, NO debera usted utilizar, copiar, revelar , o tomar ninguna acción basada en este correo electrónico o cualquier otra información incluida en el, favor de notificar al remitente de inmediato mediante el reenvio de este correo electrónico y borrar a continuacion totalmente este correo electrónico y sus anexos.

        <br><br>
        
        This e-mail is confidential and/or may contain privileged information.
        If you are not the addressee or authorized to receive this for the addressee, you must not use, copy, disclose, or take any action based on this message or any other information here in, please advise the sender immediately by reply this e-mail and delete this e-mail and its attachments.
        
        </i>
        """
        mensaje.attach(MIMEText(cuerpo_mensaje, 'html'))

        try:
            response = ses.send_raw_email(
                Source = mensaje['From'],
                Destinations = [mensaje['To']],
                RawMessage = {'Data': mensaje.as_string()}
            )

            with open('respuestas_envio.txt', 'a') as f:
                f.write(self.issued_to+'|'+str(response)+'\n')

        except ClientError as e:
            with open('respuestas_envio.txt', 'a') as f:
                f.write(self.issued_to+'|'+str(e)+'\n')

if __name__ == '__main__':

    send_email = EnviaEmail()
    send_email.registered_sender = 'jmanzo@michel.com.mx'
    send_email.issued_to = 'jose.prieto@michel.com.mx'
    send_email.moded_subject = 'Prueba de envío de correo para'
    send_email.send_email()

