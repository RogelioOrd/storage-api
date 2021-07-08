#Sobre que es este proyecto?
En este proyecto se tratara de almacenar informacion o trabajar con documentos que los mismos usuarios suban a este
para poder recopilar informacion de distintas fuentes y que necesitara bibliografia para confirmar veracidad.
Este proyecto se llebara acabo para que estudiantes y profesionistas puedan recopilar informacion o investigaciones y la puedan documentar para investigaciones escolares o profesionales futuras puedan tener una fuente de informacion confiable.
Se planmtea que cada quien pueda subir informacion como documentacion o bibliografias de diferentes temas o de algunos en especifico para poder acceeder a ella en una red de informacion de gente que sabe sobre el tema.


#Uso
El usuario debera iniciar sesion o registrarse ya sea el caso para poder utilizar la pagina y de esa manera tener acceso al subir informacion que deberea ser comprobada comparando con si bibliografia respectiva o en caso de que esta falte no se podra subir la informacion.

#usuario
Registro: nombre, correo electronico.
Poder consultar usarios y wikis.
Se requerira que para que un usuario pueda consultar cierta informacion debera ingresar una cuenta de usuario en dodnde podra subir informacion que requerira una bibliografia o mas informacion o muestras de la veracidad que respalden para poder ser aporvada.

#Admin API
Operaciones de administrador
Consultar y eliminar usarios o Informacion
Poder modificar la informacion en caso de ser incorrecta

#USER API
Consulta de informacion
-Por ID
-Por titulo
-Por orden alfabetico
-Por fecha de publicacion
-Por autor


#Estructura del API
-Titulo
-Autor
-Contenido
-Bibliografia

#Registro de usuario
{
  "ID" : "",
   "username" : "",
   "Fecha de publicacion" : "",
   "Edad" :"",
   "Email" : "" }

#Como ingresar una wiki
{
    "titulo": "nota de ejemplo",
    "contenido": "",
    "bibliografia": ""
}


## Archivos relacionados

| Path                    | Descripción                                         |
| ----------------------- | --------------------------------------------------- |
| /wiki/login             | Sera el archivo encargado de validar el acceso al usuario para permitirle subir informacion |
| /wiki/profile           | Aqui se desplegra la informacion que el usuario haya publicado |
| /wiki/query             | Aqui es donde se consultara la informacion subida por su titulo|
| /wiki/create/data       | Se utiliza para crear notas|


#Herramientas Utilizadas
* [Python](https://www.python.org)
* [PIP](https://pip.pypa.io/en/stable/installing/)
