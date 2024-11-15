# ASGI_example
Ejemplo práctico de cómo usar Django Channels (ASGI Asincrono) para implementar un proceso ficticio con un temporizador

Activa tu entorno virtual
```
python -m venv ven
```
Instala todas las dependencias
```
pip install -r requirements.txt
```

Se debe ejecutar con un servidor ASGI, en esete caso daphne
```
daphne -b 127.0.0.1 -p 8000 proyecto.asgi:application
```
Acceso a la vista 
[http://127.0.0.1:8000/progress](http://127.0.0.1:8000/progress)

![image](https://github.com/user-attachments/assets/6187174f-4fc3-4903-8364-42c3865021f2)



# Procesos Asíncronos en Aplicaciones Web
En las aplicaciones web modernas, muchas veces se necesitan manejar procesos que no deben bloquear el flujo de ejecución de una aplicación. Un proceso síncrono se ejecuta de manera secuencial, lo que significa que el servidor espera a que una tarea termine antes de pasar a la siguiente. Sin embargo, en situaciones donde una tarea puede demorar (como consultas a bases de datos, solicitudes de APIs externas o tareas de procesamiento pesado), un proceso síncrono puede bloquear todo el servidor y generar una mala experiencia de usuario. Para evitar esto, se utilizan procesos asíncronos, que permiten que el servidor maneje otras solicitudes mientras espera que la tarea demorada termine.

## ¿Qué es Django Channels?
Django Channels es una extensión de Django que permite manejar comunicaciones asíncronas, como WebSockets, en aplicaciones Django. Tradicionalmente, Django utiliza el protocolo WSGI para manejar solicitudes HTTP de manera síncrona, pero Django Channels agrega soporte para protocolos asíncronos, lo que permite crear aplicaciones que no solo sirven páginas web, sino que también pueden manejar conexiones en tiempo real. Esto es ideal para aplicaciones que necesitan actualizaciones dinámicas, como aplicaciones de chat, notificaciones en vivo, o actualizaciones de datos en tiempo real sin necesidad de recargar la página.

Al integrar Django Channels, las aplicaciones Django pueden utilizar conexiones asíncronas y permitir una comunicación continua entre el cliente y el servidor, lo que mejora la experiencia de usuario.

## ¿Qué es ASGI?
ASGI (Asynchronous Server Gateway Interface) es un estándar que reemplaza al tradicional WSGI. Mientras que WSGI está diseñado para aplicaciones síncronas, ASGI permite que las aplicaciones web manejen múltiples tipos de conexiones y protocolos de manera asíncrona. Esto es esencial para aplicaciones que necesitan manejar tareas en segundo plano, como notificaciones push, actualizaciones en tiempo real, y más.

La principal ventaja de ASGI es que permite que una aplicación gestione múltiples conexiones simultáneas sin que cada una de ellas bloquee el servidor. En lugar de esperar a que una tarea se complete antes de procesar otra, ASGI permite que el servidor maneje otras tareas mientras espera la respuesta de una operación, como una consulta a una base de datos.

## Diferencia entre WSGI y ASGI
La principal diferencia entre WSGI y ASGI radica en la forma en que manejan las solicitudes. WSGI es un protocolo síncrono que se utiliza en aplicaciones web tradicionales que procesan solicitudes de una en una. Esto funciona bien cuando las operaciones son rápidas y no hay interacción constante con el cliente. Sin embargo, WSGI no es adecuado para aplicaciones que requieren un alto rendimiento o interacción en tiempo real, ya que cada solicitud bloquea el servidor hasta que se completa.

Por otro lado, ASGI es un protocolo que permite manejar tanto operaciones síncronas como asíncronas. Gracias a su naturaleza asíncrona, ASGI es ideal para aplicaciones que requieren alta concurrencia o interacciones en tiempo real, como chats en vivo, juegos en línea, o cualquier otra aplicación que implique una conexión persistente entre el cliente y el servidor.

## ¿Por qué usar Daphne?
Daphne es un servidor diseñado para trabajar con ASGI. A diferencia de los servidores tradicionales como Gunicorn o uWSGI, que se basan en WSGI para manejar peticiones HTTP síncronas, Daphne está optimizado para manejar protocolos asíncronos, como WebSockets. Daphne es la opción recomendada cuando se está utilizando Django Channels, ya que puede gestionar múltiples conexiones de manera eficiente sin bloquear el servidor.

Daphne permite que Django maneje aplicaciones de tiempo real y conecte a los usuarios sin tener que esperar la finalización de cada solicitud. Si una aplicación utiliza WebSockets o requiere de una comunicación bidireccional continua entre el servidor y el cliente, Daphne es una excelente opción para manejar este tipo de tráfico.

## Conclusión
Los procesos asíncronos son fundamentales para mejorar el rendimiento de las aplicaciones web modernas, especialmente cuando se requiere una alta interacción en tiempo real. Django Channels extiende Django para permitir el uso de estas comunicaciones asíncronas, haciendo que sea posible manejar WebSockets, entre otros protocolos. ASGI es el protocolo que hace posible este manejo asíncrono de conexiones, mientras que Daphne es el servidor que mejor se adapta a las necesidades de las aplicaciones Django que utilizan ASGI y Channels. Por último, WSGI sigue siendo adecuado para aplicaciones tradicionales síncronas, pero para aplicaciones interactivas y de alto rendimiento, ASGI es la mejor opción.
