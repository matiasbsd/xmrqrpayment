Script para generar un código de pago QR en Monero y enviarlo via correo.

Programado por Matias Colli <matiasbsd@gmail.com>

1. Tomará como parámetro el monto en pesos argentinos y obtendrá de la API de Binance la cotización actual.
2. Generará un código QR mediante la API de ImageBB 
3. Enviará en formato HTML via mail el código QR generado en forma de ticket de pago.

Ejecución:
![image](https://github.com/matiasbsd/xmrqrpayment/assets/135914624/70c95378-6de8-405c-89da-7fb2fcc6802f)

Muestra en texto:
$ ./payment.py 40000
El precio de XMR hoy es $69451.2
La cantidad de XMR a transferir son 0.575944
Pago en XMR de mayo
07-06-2023
La imagen del QR se cargó correctamente en ImgBB.
El correo se envió correctamente.

Una muestra de un correo enviado con el script:
![image](https://github.com/matiasbsd/xmrqrpayment/assets/135914624/c009e523-4c94-498d-bc67-e09ed760b665)

Si te gusta y me querés apoyar, enviamos unos piconeros a esta dirección de XMR:
85pCo3AdghRMwvgybiJPeTZApoY1ZVMmhFbBLXFwN2BDD52UiddspnVQaEAc4fYhgzdjx4p3R3fxZFXExE9frnrT5iaJgzr
