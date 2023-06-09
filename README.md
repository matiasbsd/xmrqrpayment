
<h1>XMRQRPAYMENT</h1>
<h2>XMR QR PAYMENT</h2>

Script para generar un código de pago QR en Monero y enviarlo via correo.
Se le debe pasar como parámetro el importe a convertir en XMR, que si no se especifica es en pesos argentinos (también se puede poner dolares y euros).

Programado por Matias Colli <matiasbsd en gmail dot com>

1. Tomará como parámetro el monto en pesos argentinos (por defecto, aunque se puede especificar euros o dolares) y obtendrá de la API de Binance la cotización actual.
2. Generará un código QR mediante la API de ImageBB.
3. Enviará en formato HTML via mail el código QR generado en forma de ticket de pago.
4. Enviará un enlace para pagao alternativo en BTC que se convertirán a XMR a través de Trocador.app.

<h2>Ejecución:</h2>

![image](https://github.com/matiasbsd/xmrqrpayment/assets/135914624/29e946e7-bd98-44ca-bd12-05a38154ba6a)


<h2>Muestra en texto: </h2>

<b>$ ./payment.py 40000</b><br>
Obteniendo precios de Internet...[OK]<br>
Obteniendo el mes pasado...[OK]<br>
Cargando código QR desde ImgBB...[OK]<br>
Enviando correo...[OK]<br>

<b>$ ./payment.py 150 eur</b><br>
Obteniendo precios de Internet...[OK]<br>
Obteniendo el mes pasado...[OK]<br>
Cargando código QR desde ImgBB...[OK]<br>
Enviando correo...[OK]<br>

<b>$ ./payment.py 100 usd</b><br>
Obteniendo precios de Internet...[OK]<br>
Obteniendo el mes pasado...[OK]<br>
Cargando código QR desde ImgBB...[OK]<br>
Enviando correo...[OK]<br>

<b>$ ./payment.py asdasd eur</b><br>
El primer parámetro debe ser un número válido mayor a 0.<br>

<b>$ ./payment.py 134 zzz</b><br>
La moneda debe ser 'eur', 'usd' o 'ars'.<br>

<h2>Una muestra de un correo enviado con el script:</h2>

![image](https://github.com/matiasbsd/xmrqrpayment/assets/135914624/81067c5e-e72e-4480-b589-75bd877bf0e4)

<h2>Apoyame con un cafecito si querés</h2>
Si te gusta y me querés apoyar, enviamos unos piconeros a esta dirección de XMR:
85pCo3AdghRMwvgybiJPeTZApoY1ZVMmhFbBLXFwN2BDD52UiddspnVQaEAc4fYhgzdjx4p3R3fxZFXExE9frnrT5iaJgzr
