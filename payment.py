# Tomará como parámetro el monto en pesos y obtendrá de la API de Binance la cotización actual
# Generará un código QR mediante la API de ImageBB y creará un ticket que enviará en formato HTML via mail
# Programado por Matias Colli <matiasbsd@gmail.com>
# Version 0.3
# Creado el 7-06-2023
# Actualizado el 10-07-2023

########################## DATOS PERSONALES #############################
# Dirección de Monero (XMR) para recibir los fondos
address = "4ANUF...."

# Datos del servidor SMTP para el envio de correo
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "xxxxxx@gmail.com"
smtp_password = "xxxxxxx"

# Datos del correo a enviar
msg_from = "Ticket de pago XMR<xxxxxx@gmail.com>"
msg_to = "yyyyyy@gmail.com"
msg_cc = "zzzzzz@gmail.com"

# Api Key de Image BB
imagebb_apikey = "YOUR_API_KEY_IMGBB"
######################## FIN DATOS PERSONALES ###########################

# Cargar librerías básicas
import sys
import importlib

# Verificar la disponibilidad de las otras librerías requeridas
required_libraries = ["sys", "smtplib", "qrcode", "requests", "tempfile",
                      "email.mime.multipart", "email.mime.text",
                      "urllib.request", "calendar", "datetime"]
missing_libraries = []
for lib in required_libraries:
    try:
        importlib.import_module(lib)
    except ImportError:
        missing_libraries.append(lib)
if missing_libraries:
    print("Las siguientes librerías son requeridas pero no están instaladas:")
    for lib in missing_libraries:
        print(f"{lib}")
        print(f"Para instalar, ejecuta: pip install {lib}")
    print("Abortando la ejecución del script.")
    sys.exit(1)
import smtplib
import qrcode
import requests
import tempfile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.request import urlopen
import calendar
from datetime import datetime

# Verificar conexion a Binance e ImageBB
def has_internet_connection():
    try:
        response_binance = requests.get('https://api.binance.com', timeout=1)
        response_imgbb = requests.get('https://api.imgbb.com', timeout=1)
        if response_binance.status_code == 200 and response_imgbb.status_code == 200:
            return True
        else:
            return False
    except:
        return False

# Obtener el precio del par XMRARS
def convert_ars_to_xmr(amount_ars):
    # Obtener el precio del par USDTARS
    response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=USDTARS')
    data = response.json()
    usdtars_price = float(data['price'])
    # Obtener el precio del par XMRUSDT
    response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=XMRUSDT')
    data = response.json()
    xmrusdt_price = float(data['price'])
    # Calcula la cantidad equivalente de XMR en base al monto en pesos argentinos
    xmramount = amount_ars / (usdtars_price * xmrusdt_price)
    return xmramount

# Obtener el precio del par USDTARS
def usdtars_price():
    response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=USDTARS')
    data = response.json()
    return float(data['price'])

# Obtener el precio del par XMRUSDT
def xmrusdt_price():
    response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=XMRUSDT')
    data = response.json()
    return float(data['price'])

# Obtener el precio del par XMRUSD
def xmrusd_price():
    response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=XMRUSDT')
    data = response.json()
    return float(data['price'])

# Obtener el precio del par EURUSD
def eurusd_price():
    response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=EURUSDT')
    data = response.json()
    return float(data['price'])

# Obtener el precio del par XMREUR
def xmreur_price():
    xmrusd = xmrusd_price()
    eurusd = eurusd_price()
    xmreur = xmrusd / eurusd
    return xmreur

# Convertir el monto en pesos a XMR
def convert_to_xmr(amount, currency):
    if currency == "usd":
        xmrusd = xmrusd_price()
        xmramount = amount / xmrusd
    elif currency == "eur":
        xmreur = xmreur_price()
        xmramount = amount / xmreur
    else:
        xmramount = convert_ars_to_xmr(amount)
    return xmramount

# Verificar si se proporciona un monto y una moneda personalizada como argumento
if len(sys.argv) > 1:
    if sys.argv[1].isdigit() and float(sys.argv[1]) > 0:
        amount = float(sys.argv[1])
        if len(sys.argv) > 2:
            currency = sys.argv[2].lower()
            if currency not in ["eur", "usd", "ars"]:
                print("La moneda debe ser 'eur', 'usd' o 'ars'.")
                rint(f"uso: {sys.argv[0]} <importe> <moneda>")
                print(f"ejemplo: {sys.argv[0]} 40000 ars")
                exit(1)
        else:
            currency = "ars"
    else:
        print("El primer parámetro debe ser un número válido mayor a 0.")
        print(f"uso: {sys.argv[0]} <importe> <moneda>")
        print(f"ejemplo: {sys.argv[0]} 40000 ars")
        exit(1)
else:
    amount = float(input("Ingrese el monto: "))
    currency = input("Ingrese la moneda (eur/usd/ars): ").lower()
    if currency not in ["eur", "usd", "ars"]:
        print("La moneda debe ser 'eur', 'usd' o 'ars'.")
        print(f"uso: {sys.argv[0]} <importe> <moneda>")
        print(f"ejemplo: {sys.argv[0]} 40000 ars")
        exit(1)

# Verificar la conexión a Internet
if not has_internet_connection():
    print("No hay conexión a Internet.")
    sys.exit(1)

# Comienzo de ejecución del programa
print("Obteniendo precios de Internet...", end="")
if currency != "ars":
    xmramount = convert_to_xmr(amount, currency)
else:
    xmramount = convert_to_xmr(amount, "ars")  # Actualizado aquí

# Comienzo de ejecución del programa
usdt_price = usdtars_price()
xmr_price = xmrusdt_price()
xmrars_price = round(usdt_price * xmr_price, 2)
print("[OK]")

# Obtener el mes actual
print("Obteniendo el mes pasado...", end="")
current_month = datetime.now().month
# Obtener el nombre del mes anterior en inglés
previous_month = current_month - 1 if current_month > 1 else 12
english_month_name = calendar.month_name[previous_month]
# Traducir el nombre del mes anterior al español
meses_espanol = {
    "January": "enero",
    "February": "febrero",
    "March": "marzo",
    "April": "abril",
    "May": "mayo",
    "June": "junio",
    "July": "julio",
    "August": "agosto",
    "September": "septiembre",
    "October": "octubre",
    "November": "noviembre",
    "December": "diciembre"
}
nombre_mes_anterior = meses_espanol[english_month_name]
print("[OK]")

# Configurar el asunto personalizado
msg_subject = f"Pago en XMR de {nombre_mes_anterior}"

# Obtener la fecha actual
current_date = datetime.now().strftime("%d-%m-%Y")

# Crear los datos para el código QR
print("Cargando código QR desde ImgBB...", end="")
qr_data = f"monero:{address}?tx_amount={xmramount}&tx_description={nombre_mes_anterior}"

# Crear el código QR
qr_img = qrcode.make(qr_data)

# Generar el código QR en formato PNG
qr_code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr_code.add_data(qr_data)
qr_code.make(fit=True)
qr_image = qr_code.make_image(fill_color="black", back_color="white")

# Guardar el código QR en un archivo temporal
with tempfile.NamedTemporaryFile(suffix=".png") as qr_file:
    qr_image.save(qr_file.name)

    # Cargar la imagen en ImgBB
    with open(qr_file.name, "rb") as file:
        response = requests.post("https://api.imgbb.com/1/upload",
                                 params={"key": imagebb_apikey},
                                 files={"image": file})
        json_data = response.json()
        if response.status_code == 200 and "data" in json_data and "url" in json_data["data"]:
            qr_image_url = json_data["data"]["url"]
            print("[OK]")
        else:
            print("Error al cargar la imagen del QR en ImgBB.")

# Crear mensaje de correo electrónico
print("Enviando correo...", end="")
message = MIMEMultipart("alternative")
message["From"] = msg_from
message["To"] = msg_to
message["Cc"] = msg_cc
message["Subject"] = msg_subject

# Agregar contenido HTML al mensaje
html_content = f"""
<html>
  <body>
    <table style="border: 2px solid black; background: linear-gradient(to bottom, #ff6600 0%, #ff9933 100%); color: white; padding: 20px; font-family: 'Open Sans', sans-serif;">
      <tr>
        <td>
          <center><h2>Ticket de pago en XMR</h2>
          <p>Se adjunta el código QR para realizar un pago en XMR:</p>
          <img src="{qr_image_url}" alt="QR Code" width="300" style="max-width:100%;" /></center>
        </td>
        <td style="padding-left: 20px;color: black;">
          <h3>Información del pago:</h3>
          <p>Dirección XMR: <b>{address}</b></p>
          <p>Monto: <b>{xmramount}</b> XMR</p>
          <hr>
          <p>Mes trabajado: {nombre_mes_anterior}</p>
          <p>Fecha de emisión: {current_date}</p>
          <p>Importe en {currency}: {amount} (de acuerdo a las horas trabajadas)</p>
          <p>Cotización del USDT (pesos): $ {usdt_price} (Binance)</p>
          <p>Cotización del XMR (dolar): u$s {xmr_price} (Binance)</p>
          <p>Cotización del XMR (pesos): $ {xmrars_price} (Binance)</p>
          <p><a href="https://trocador.app/anonpay/?ticker_to=xmr&network_to=Mainnet&address={address}&fiat_equiv=ARS&amount={xmramount}&name=Pago+en+BTC&{nombre_mes_anterior}&email={msg_cc}" style="background-color: orange;color: white;padding: 6px 12px;text-decoration: none;border: 1px solid transparent;display: inline-block;border-radius: 4px;text-align: center;white-space: nowrap;vertical-align: middle;user-select: none;">Link alternativo para pago en BTC</a></p>
        </td>
      </tr>
    </table>
  </body>
</html>
"""

# Agregar contenido HTML al mensaje
message.attach(MIMEText(html_content, "html"))

# Enviar correo electrónico
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(message)
    server.quit()
    print("[OK]")
except smtplib.SMTPException as e:
    print("Error al enviar el correo:")
    print(e)
