## Sobre que es este proyecto?
-En este proyecto se tratara de almacenar informacion o trabajar con documentos que los mismos usuarios suban a este
para poder recopilar informacion de distintas fuentes y que necesitara bibliografia para confirmar veracidad.

-Este proyecto se llebara acabo para que estudiantes y profesionistas puedan recopilar informacion o investigaciones y la puedan documentar para investigaciones escolares o profesionales futuras puedan tener una fuente de informacion confiable.

-Se plantea que cada quien pueda subir informacion como documentacion o bibliografias de diferentes temas o de algunos en especifico para poder acceeder a ella en una red de informacion de gente que sabe sobre el tema.

-Para poder comenzar a trabajar en este proyecto se requerira de el pc desde donde se desarrollara toda la aplicacion asi como sus funciones, descripcion, etc., asi como se requerira el desarrollador encargado y unico desarrollador de este proyecto.

-El trabajo operativo  que se necesitara para este proyecto sera de un equipo con conocimientos tecnicos suficientes para poder tener funcionando el proyecto mientras se este en uso para que de este modo se pueda acceder a el y trabajar en el de la misma manera.

## Uso
-El usuario debera iniciar sesion o registrarse ya sea el caso para poder utilizar la pagina y de esa manera tener acceso al subir informacion que deberea ser comprobada comparando con si bibliografia respectiva o en caso de que esta falte no se podra subir la informacion.

## usuario
* Registro: nombre, correo electronico.
* Poder consultar usarios y wikis.
* Se requerira que para que un usuario pueda consultar cierta informacion debera ingresar una cuenta de usuario en dodnde podra subir informacion que requerira una bibliografia o mas informacion o muestras de la veracidad que respalden para poder ser aporvada.

## Aspecto
```
- a90g0 Se crearon las carpetas con los archivos del proyecto
- 45f23 Se crean funciones para interactuar con el proyecto
- ah20f Se Implementaron consultas para interactuar con el servidor por rutas `http`
- 365b0 Se implementaron restricciones a los usuarios
```

## Admin API
* Operaciones de administrador
* Consultar y eliminar usarios o Informacion
* Poder modificar la informacion en caso de ser incorrecta

## USER API
# Consulta de informacion
* Por ID
* Por titulo
* Por orden alfabetico
* Por fecha de publicacion
* Por autor

## Estructura del API

```
-Titulo
-Autor
-Categoria
-Fecha
-Contenido
-Bibliografia
```

## Codigo
```
Registro de usuario
{
  "ID" : "",
   "username" : "",
   "Fecha de publicacion" : "",
   "Edad" :"",
   "Email" : "" }

Como ingresar una wiki

{
        "publication_id": publication_id,
        "titulo": titulo,
	      "autor": autor,
        "categoria": categoria,
        "fecha_publicacion": fecha,
	      "publicacion": info,
	      "bibliografia": biblografia
    }
```

## Archivos de funcionamiento

| Path                    | Descripción                                         |
| ----------------------- | --------------------------------------------------- |
| /wikiinfo/storage           | Aqui se desplegra la informacion que el usuario haya publicado |
| /wikiinfo/store             | Aqui se desplegra la informacion del usuario |

# Creacion de Funciones de almacenamiento
Funciones simuladas para el funcionamiento
|        Titulo           | Commit Hash                                         |
| ----------------------- | --------------------------------------------------- |
|Simulacio de nuevas notas|   1c43e307ebd25418016e98920926665e80179fc9          |

# Rutas Especificas
Se agrego codigo de respuesta de creacion not implemnted que responde a 501, con Content-Type: application/json.
|        Titulo           | Commit Hash                                         |
| ----------------------- | --------------------------------------------------- |
|Respuesta de creacion    |dc8b0d8f1089150eada0eda61a7141d525c45beb             |


## Interfaz web
-Pagina principal
* Esta sera la interfaz principal desde la que se podra acceder a la demas informacion mediante el buscador
* Incluira una seccion de diferentes temas en caso de querer buscar en cierta categoria Especifica
* Por ultimo se mostraria alguna imagen o logo relacionada

<img src="https://github.com/RogelioOrd/storage-api/blob/84f77a1f9f0bc2bc1b10001cc2d3765cb53e0137/docs/assets/wiki-info-0002-Home%20Page.PNG" width="550">  

-Vista previa de una publicacion
* Aqui se rellenara la informacion que se desee agregar o publicar
* Mostrara una seccion donde se podra acceder a la bibliografia
* Se podra ver la fecha de publicacion
* Se agrargara el nombre del author

<img src="https://github.com/RogelioOrd/storage-api/blob/84f77a1f9f0bc2bc1b10001cc2d3765cb53e0137/docs/assets/wiki-info-0003-Publication%20Preview.PNG" width="550">  

-Publication
* Aqui se puede ver principalmente la publicacion que se busco
* Asi mismo se añadira un enlace al perfil del autor para buscar mas de sus publicaciones
* Se tendra una barra de buscqueda para poder cambiar de Informacion

<img src="https://github.com/RogelioOrd/storage-api/blob/84f77a1f9f0bc2bc1b10001cc2d3765cb53e0137/docs/assets/wiki-info-0004-Publication.PNG" width="550">

-Perfil del Autor
* Se tendra acceso a las publicaciones del autor
* Se tendra tambien la barra de busqueda
* Si la persona se encuentra en su perfil tendra permisos de editar

  <img src="https://github.com/RogelioOrd/storage-api/blob/84f77a1f9f0bc2bc1b10001cc2d3765cb53e0137/docs/assets/wiki-info-0001-UserProfile.PNG" width="550">


# Casos de Uso

## Caso 1: Agregar un usuario
Esta funcion servira para crear usuarios en los que pedira informacion como nombre, contraseña, correo y algunos otros datos para poder guardarlo


### Estructura del CURL
'''

Add a new user
Para probar esta ruta uno puede ejecutar el siguiente comando

      curl http://localhost:8081/wikiinfo/store \
          -X POST \
          -H 'Content-Type: application/json' \
          -d '{"id" : "1" , "username" : "rogelio" , "password" : "1234" , "mail" : "tucorreofake@correo.com"}'

  '''


## Caso 2: Crear una wiki
Esta funcion servira para crear las respectivas wikis en los que pedira informacion como el titulo, categoria e incluso referencias para guardar la informacion.


### Estructura del CURL


'''

Añadir una Wiki
  curl http://localhost:8081/wikiinfo/store \
    -X POST \
      -H 'Content-Type: application/json'  \
      -d '{"publication_id" : "1" , "titulo" : "titulo Random" , "autor" : "rogelio" , "categoria" : "ciencia" , "fecha":"2021-01-01" , "publication" : "contenido de la publicacion", "bibliografia" : "fuentes de informacion"}' \

'''


## Caso 3: Consultar usuarios
Con esta función se plantea que podamos buscar a los usuarios con alguno de los siguientes parametros: 'id'.


### Estructura del CURL


'''

Ver Usuarios
  curl http://localhost:8081/wikiinfo/store/1/rogelio \
    -X GET \

'''

## Caso 4: Consultar Wikis
Con esta función se plantea que podamos buscar a los usuarios con alguno de los siguientes parametros: 'publication_id'.


### Estructura del CURL


'''

  ver wikis
    curl http://localhost:8081/wikiinfo/1 \
    -X GET \

'''

# Planeacion del frontend

Para la planeacion que se llevara a cabo para poder realizar el forntend se debe llevar a cabo un analizis de las funcionalidades que se tienen para desarrollarlas y que el frontend corresponda al backend, todo lo del forntend se realizara utilizando html, JS y CSS que le dara el aspecto mejor a la vista al proyecto.

Para que el forntend funcione debe cumplir ciertas caracteristicas, como:
- Se deben poder realizar las consultas respectivas como POST o GET.
- Que las funciones trabajen correctamente

Para la pagia principal se tiene esto pensado
Primero se necesitara una pagina principal desde donde se pueda acceder al resto de las paginas, wikis y pues consultar las respectivas wikis.

<img src="https://github.com/RogelioOrd/storage-api/blob/84f77a1f9f0bc2bc1b10001cc2d3765cb53e0137/docs/assets/wiki-info-0002-Home%20Page.PNG" width="550">

Luego al seleccionar la wiki que se desea acceder, se mostrara una pagina en la que se tendra la informacion de manera que se centre en eso y lo demas sean solo ventanas para o herramientas para poder acceder a otra consulta de informacion.

<img src="https://github.com/RogelioOrd/storage-api/blob/84f77a1f9f0bc2bc1b10001cc2d3765cb53e0137/docs/assets/wiki-info-0004-Publication.PNG" width="550">

Para agregar una wiki
La imagen muestra unos campos para agregar una nueva wiki al sistema.. Al final se encuentra un boton de publish, el cual sirve para guardar los cambios.
En esto podemos ver desde una vista previa como se plantea que se suban o se generen las wikis con sus respectivos campos que cumpliran ciertos requisitos para que funcione con el backend.

<img src="https://github.com/RogelioOrd/storage-api/blob/84f77a1f9f0bc2bc1b10001cc2d3765cb53e0137/docs/assets/wiki-info-0003-Publication%20Preview.PNG" width="550">

Perfiles
Por ultimo se desea poder visitar la pagina de los distintos autores/usuarios que se tengan registrados para saber que es lo que han hecho asi como se acomodaran de forma que sea mas sencillo acceder a esa Informacion.

<img src="https://github.com/RogelioOrd/storage-api/blob/84f77a1f9f0bc2bc1b10001cc2d3765cb53e0137/docs/assets/wiki-info-0001-UserProfile.PNG" width="550">
## Herramientas Utilizadas
* [Python](https://www.python.org)
* [PIP](https://pip.pypa.io/en/stable/installing/)
