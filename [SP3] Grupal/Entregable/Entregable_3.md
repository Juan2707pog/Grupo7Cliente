# GET
El método **GET** solicita una representación de un recurso específico. Las peticiones que usan el método **GET** sólo deben recuperar datos.

## Primer GET

En este primer **GET** vamos a utilizar una **API** de pokemon el cual te da todas las estadísticas, nombres, tipos de movimientos, etc sobre un pokemon...
![enter image description here](https://i.imgur.com/krei40i.jpg)

### Parametro de entrada
En esta API no hace falta un token ya que no tiene ningún inicio de sesión y ademas es una API expresamente para hacer peticiones GET.

### Parametro de salida
Esta solicitud devuelve **200 OK** eso significa que devuelve un **JSON** con todas las estadísticas del pokemon que se ha hecho en la petición.

## Segundo GET
En este segundo **GET** vamos a utilizar otra **API** de pokemon, pero esta nos da todas las cartas de pokemon que existen.
![enter image description here](https://i.imgur.com/8ytQb3q.jpg)
### Parametro de entrada
En esta API tampoco hace falta un token ya que tampaco tiene ningún inicio de sesión y ademas es una API expresamente para hacer peticiones GET.

### Parametro de salida
Esta solicitud devuelve **200 OK** eso significa que devuelve un **HTML** con todas las cartas del pokemon por el cual se ha hecho en la petición.

# POST
El método **POST** se utiliza para enviar una entidad a un recurso en específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor.

## Primer POST

En este primer **POST** vamos a utilizar una **API** de comics en el cual cuando buscas cualquier tipo de nombre te sale todos los que hay en la pagina.
![enter image description here](https://i.imgur.com/b9BVAfd.jpg)

### Parametro de entrada
- age: Es un **String** con un valor search con el cual buscas el comic
- params: Es un **String** con un valor que devuelve el método de búsqueda.
- signature: Es un **String** con un valor *false*.

### Parametro de salida
- data: Es un **String** que muestra los datos del usuario.
  - userId: Es un **String** que muestra la id del usuario
  - userIp: Es un **Double** que muestra la ip del usuario que hace la búsqueda.


## Segundo POST

En este primer **POST** vamos a utilizar una **API** de cócteles en el cual cuando buscas cualquier tipo de bebida te sale todas fotos de las bebidas que se encuentran en la pagina.
![enter image description here](https://i.imgur.com/VC4CT4i.jpg)
### Parametro de entrada
- title: Es un **String** que muestra el titulo de la búsqueda.

### Parametro de salida
- script: Es una **función** en **js** en el cual esta programado como hacer la búsqueda.

# PUT
El método **PUT** reemplaza todas las representaciones actuales del recurso de destino con la carga útil de la petición.

## Primer PUT
En este primer **PUT** vamos a utilizar la**API** de trello en el cual vamos a actualziar el nombre del tablero.
![enter image description here](https://i.imgur.com/CfObU7e.jpg)
### Parametro de entrada
- name: Es un **String** que se pone el body por el cual editas el titulo del tablero.

### Parametro de salida
- id: Es un **alfanumérico** que devuelve la id del usuario. 
- name: Es un **String** que devuelve el nombre ya cambiado del tablero.
- idOrganization: Es un **alfanumérico** que devuelve la id de equipo de trello.
- url: Es un **alfanumérico** que devuelve la url del tablero.
- shortUrl: Es un **alfanumérico** que devuelve la url del tablero sin el nombre suyo.

## Segundo PUT
En este primer **PUT** vamos a utilizar la**API** de spotify en el cual vamos a seguir una playlist de sporify.
![enter image description here](https://i.imgur.com/d1odhGI.jpg)
### Parametro de entrada
token: Es un **String** para poder acceder a la aplicación de spotify y poder hacer el put.

### Parametro de salida
- Pondremos lo que querremos hacer en el **body** en este caso es seguir una nueva playlist y ya daría **200 OK**.

# DELETE
El método **DELETE** borra un recurso en específico.

## Primer DELETE
En este primer **DELETE** vamos a utilizar la **API** de trello en el cual vamos a eliminar un tablero que ya tenemos.
![enter image description here](https://i.imgur.com/4H3UUv7.jpg)
### Parametro de entrada
- token: Es un **String** para poder acceder a la api de trello para poder hacer el delete del tablero.
- key: Es un **String** que sirve para que te de permisos y puedas acceder a trello.

### Parametro de salida
Devuelve un **"_value": null** con un **200 OK**, eso significa que ha eliminado correctamente el tablero de trello.

## Segundo DELETE
En este primer **DELETE** vamos a utilizar la **API** de gitter en el cual vamos a eliminar una room que ya tenemos creada.
![enter image description here](https://i.imgur.com/IKEErJc.jpg)
### Parametro de entrada
- token: Es un **String** para poder acceder a la api de gitter para poder hacer el delete de la room ya creada. Lo colocamos en **"Authorization"** después en **"type"** seleccionamos **OAuth 2.0** y ahí colocamos el token que nos da gitter.


### Parametro de salida
Devuelve un **"success": true** que significa que la eliminacion de la room ha sido correcta, ya que también devuelve un **200 OK**.
