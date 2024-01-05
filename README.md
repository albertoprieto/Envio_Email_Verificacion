# EnviaEmail Script
![Tests](https://github.com/albertoprieto/Envio_Email_Verificacion/actions/workflows/python-app.yml/badge.svg)

Este script en Python utiliza la biblioteca Boto3 para enviar correos electrónicos a través de Amazon SES (Simple Email Service). El script crea un objeto de la clase `EnviaEmail` para enviar un correo de prueba a una dirección específica.

## Requisitos

Antes de ejecutar este script, asegúrate de tener instaladas las bibliotecas necesarias. Puedes instalarlas usando el siguiente comando:

```bash
pip install boto3
```

## Configuración

Antes de ejecutar el script, debes configurar algunas variables dentro de la clase `EnviaEmail`:

- `registered_sender`: La dirección de correo electrónico del remitente.
- `issued_to`: La dirección de correo electrónico del destinatario.
- `moded_subject`: El sujeto del correo electrónico.

Asegúrate de configurar estas variables antes de ejecutar el script para que el correo se envíe correctamente.

## Contenido del Correo Electrónico

El cuerpo del correo electrónico está formateado en HTML y contiene la siguiente información:

- Logo de la empresa.
- Mensaje de verificación de cuenta.
- Información de la compañía.
- Instrucciones para cancelar la suscripción.
- Nota de confidencialidad.

## Uso

Para ejecutar el script, simplemente ejecuta el archivo `main.py`. Asegúrate de tener las variables `registered_sender`, `issued_to`, y `moded_subject` configuradas correctamente.
```bash
python main.py
```

## Resultado

Después de ejecutar el script, se generará un archivo llamado `respuestas_envio.txt` que contiene la respuesta del envío del correo o cualquier error que haya ocurrido.

¡Listo! Ahora estás listo para enviar correos electrónicos utilizando Amazon SES con este script en Python.
