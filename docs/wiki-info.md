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
-Registro: nombre, correo electronico.
-Poder consultar usarios y wikis.
-Se requerira que para que un usuario pueda consultar cierta informacion debera ingresar una cuenta de usuario en dodnde podra subir informacion que requerira una bibliografia o mas informacion o muestras de la veracidad que respalden para poder ser aporvada.

## Aspecto
-a90g0 Se crearon las carpetas con los archivos del proyecto
-45f23 Se crean funciones para interactuar con el proyecto
-ah20f Se Implementaron consultas para interactuar con el servidor por rutas `http`
-365b0 Se implementaron restricciones a los usuarios

## Admin API
-Operaciones de administrador
-Consultar y eliminar usarios o Informacion
-Poder modificar la informacion en caso de ser incorrecta

## USER API
# Consulta de informacion
-Por ID
-Por titulo
-Por orden alfabetico
-Por fecha de publicacion
-Por autor

## Estructura del API
-Titulo
-Autor
-Contenido
-Bibliografia


## Registro de usuario
'''
{
  "ID" : "",
   "username" : "",
   "Fecha de publicacion" : "",
   "Edad" :"",
   "Email" : "" }
'''

## Como ingresar una wiki
'''
{
    "titulo": "nota de ejemplo",
    "contenido": "",
    "bibliografia": ""
}
'''

## Archivos de funcionamiento

| Path                    | Descripción                                         |
| ----------------------- | --------------------------------------------------- |
| /wiki-info/login             | Sera el archivo encargado de validar el acceso al usuario para permitirle subir informacion |
| /wiki-info/profile           | Aqui se desplegra la informacion que el usuario haya publicado |
| /wiki-info/query             | Aqui es donde se consultara la informacion subida por su titulo|
| /wiki-info/create/data       | Se utiliza para crear notas|

#Creacion de Funciones de almacenamiento
Funciones simuladas para el funcionamiento
|        Titulo           | Commit Hash                                         |
| ----------------------- | --------------------------------------------------- |
|                         |   |

# Rutas Especificas

## Interfaz web
-Pagina principal
  -Esta sera la interfaz principal desde la que se podra acceder a la demas informacion mediante el buscador
  -Incluira una seccion de diferentes temas en caso de querer buscar en cierta categoria Especifica
  -Por ultimo se mostraria alguna imagen o logo relacionada
<img src="https://github.com/RogelioOrd/storage-api/blob/84f77a1f9f0bc2bc1b10001cc2d3765cb53e0137/docs/assets/wiki-
info-0002-Home%20Page.PNG" width="550">  

-Vista previa de una publicacion
    -Aqui se rellenara la informacion que se desee agregar o publicar
    -Mostrara una seccion donde se podra acceder a la bibliografia
    -Se podra ver la fecha de publicacion
    -Se agrargara el nombre del author
<img src="https://github.com/RogelioOrd/storage-api/blob/84f77a1f9f0bc2bc1b10001cc2d3765cb53e0137/docs/assets/wiki-info-0003-Publication%20Preview.PNG" width="550">  

-Publication
  -Aqui se puede ver principalmente la publicacion que se busco
  -Asi mismo se añadira un enlace al perfil del autor para buscar mas de sus publicaciones
  -Se tendra una barra de buscqueda para poder cambiar de Informacion
<img src="https://github.com/RogelioOrd/storage-api/blob/84f77a1f9f0bc2bc1b10001cc2d3765cb53e0137/docs/assets/wiki-info-0004-Publication.PNG" width="550">

-Perfil del Autor
  -Se tendra acceso a las publicaciones del autor
  -Se tendra tambien la barra de busqueda
  -Si la persona se encuentra en su perfil tendra permisos de editar
  <img src="https://github.com/RogelioOrd/storage-api/blob/84f77a1f9f0bc2bc1b10001cc2d3765cb53e0137/docs/assets/wiki-info-0001-UserProfile.PNG" width="550">


# Cambios de git
'''
17f72c241a48419c00a731ab04746ca5bac0b7b0
  -Update de Archivos
  -Upload de la primer version del md

17f72c241a48419c00a731ab04746ca5bac0b7b0
  -Creacion de Archivos
  -creacion de carpetas

84f77a1f9f0bc2bc1b10001cc2d3765cb53e0137
  -Se añadieron las imagenes de los mock ups

2e6ba9a3127933291f598ea7d24ab15edcb059a6
  -Se añadieron los mock ups al documento
  -Se les añadio descripcion a los mock ups
'''


## Herramientas Utilizadas
* [Python](https://www.python.org)
* [PIP](https://pip.pypa.io/en/stable/installing/)
