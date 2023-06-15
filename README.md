Script para generar un código de pago QR en Monero y enviarlo via correo.

Programado por Matias Colli <matiasbsd@gmail.com>

1. Tomará como parámetro el monto en pesos argentinos y obtendrá de la API de Binance la cotización actual.
2. Generará un código QR mediante la API de ImageBB .
3. Enviará en formato HTML via mail el código QR generado en forma de ticket de pago.
4. Enviará un enlace para pagao alternativo en BTC que se convertirán a XMR a través de Trocador.app

<h2>Ejecución:</h2>

![image](https://github.com/matiasbsd/xmrqrpayment/assets/135914624/70c95378-6de8-405c-89da-7fb2fcc6802f)

<h2>Muestra en texto: </h2>

<b>$ ./payment.py 40000</b><br>
El precio de XMR hoy es $69451.2<br>
La cantidad de XMR a transferir son 0.575944<br>
Pago en XMR de mayo<br>
07-06-2023<br>
La imagen del QR se cargó correctamente en ImgBB.<br>
El correo se envió correctamente.<br>

<h2>Una muestra de un correo enviado con el script:</h2>
![image](https://github.com/matiasbsd/xmrqrpayment/assets/135914624/437ac0df-a327-4daa-a064-5fe6f3c95f60)

<h2>Apoyame con un cafecito si querés</h2>
Si te gusta y me querés apoyar, enviamos unos piconeros a esta dirección de XMR:
85pCo3AdghRMwvgybiJPeTZApoY1ZVMmhFbBLXFwN2BDD52UiddspnVQaEAc4fYhgzdjx4p3R3fxZFXExE9frnrT5iaJgzr
