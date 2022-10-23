# En este archivo presentaremos el diseño de los datos y como los 
# modelamos dentro del programa. También hablaremos sobre las decisiones
# que tomamos en cuanto a el manejo de datos y  como enfocaremos la 
# resolución del problema.
# 
# DISEÑO DE DATOS___________________________ 
# 
#   # Tablero:
#             El tablero tiene un tamaño de 8 filas por 8 columnas, 
#   representadas por los números del 1 al 8, y con las letras de la A a la
#   H, respectivamente.
#
#             La representación del tablero la realizaremos utilizando una
#   lista de listas. Dicha elección nos permite indexar a las filas y las
#   columnas, y de esta manera, poder trabajar con la idea de "coordenada"
#   para cada una de las posiciones del tablero. Además, al ser estructuras
#   de datos mutables, nos permiten ir modificando su contenido a lo largo 
#   del programa.
#
#             Para trabajar de manera más cómoda, relacionaremos cada una
#   de las filas con números del 0 al 7. Lo mismo con las letras de las 
#   columnas. De ésta manera, podremos asociar los datos pasados por el 
#   archivo de juego, con los índices que tiene nuestra representación del
#   tablero.
#           
#   # Jugadores:
#               A cada uno de los jugadores lo representaremos como una 
#   tupla de la forma (str,str), en donde el primer campo indica su nombre,
#   y el segundo hace referencia al color que le fue asignado. Los colores
#   pueden ser "B" de blanco o "N" de negro. Un ejemplo de jugador sería:
#           
#   jugador = ("Desdémona","B")
#
#   # Fichas:
#            Cuando tomemos la información de cada una de las jugadas del 
#   archivo de juego a cada coordenada la vincularemos con una tupla de la
#   forma (int,int) de acuerdo a como planteamos la asociación de las filas
#   y columas en la representación del tablero. El primer elemento de la
#   tupla hará referencia a la columna y la segunda a las filas. Posibles 
#   asociaciones de fichas serían:
#
#   "A1" -> (0,0)
#   "H8" -> (7,7)
#   "B3" -> (1,2)
#
#
# PLANTEAMIENTO DE RESOLUCIÓN_______________
# 
#   # División en archivos:
#                          Dividimos la totalidad del programa en varios 
#   archivos para trabajar de manera más cómoda y ordenada. Los distinos 
#   archivos son:
#
#       # documentacion.py
#       # main.py - Archivo de juego donde agrupamos todas las funciones.
#       # test.py - Archivo de test de las funciones.
#       # tablero.py - Archivo con funciones relacionadas con el tablero.
#       # verificacion_archivo.py - Archivo que contiene funciones que se 
#         encargan de la lectura del archivo.
#       # verificacion_fichas.py - Archivo con funciones que chequean jugadas.
#       # verificacion_jugadores.py - Archivo con funciones que verifican 
#         los datos preliminares.
#       # assets - Carpeta que contiene las distintas partidas.
#
#   # Inicio del programa:
#                         Cuando ejecutemos el archivo main.py, nos pedirá 
#   que ingresemos el nombre del archivo de la partida que queremos ejecutar.
#   En caso de que se ingrese un nombre de archivo inválido, nos seguirá 
#   pidiendo hasta que ingresemos uno existente. Todas los archivos de juego
#   son de extensión txt y SE DEBEN COLOCAR DENTRO DE LA CARPETA DE ASSETS 
#   para que el programa los encuentre.
#                       
#   # Finalización del programa: 
#                                Una vez que ejecutemos el archivo main.py, se
#   irá ejecutando hasta que finalize la lectura del archivo de juego, o en 
#   caso contrario, que nos encontremos con un error durante la lectura. También
#   puede ocurrir que alguno de los datos delos jugadores esté mal. A continuación
#   plantearemos las diferentes terminaciones del programa:
# 
#       # Errores en información de jugador:
#           # Colores inválidos de los jugadores.
#           # Colores repetidos en los jugadores.
#           # Color de inicio incorrecto.

#       # No existen errores en las jugadas:
#           # Se colocaron todas las fichas del juego.
#           # No se colocaron todas las fichas. La partida queda a medio
#             terminar.
#
#       # Existen errores en las jugadas:
#           # Se colocó una ficha en una casilla ya ocupada.
#           # Coordenada fuera del rango del tablero.
#           # Se colocó una ficha en un lugar donde no puede ir. En términos
#             del juego, dicha ficha no realiza cambios en el número de fichas.
#           # Se saltea cuando no se debe saltar.
#       
#
#   # Análisis de información de jugadores:
#                                           Antes de comenzar con la lectura
#   de las jugadas, nos encargaremos de verificar que toda la información de
#   los jugadores sea correcta. En caso de que no se cumpla alguna de las
#   verificaciones, se termina la partida sin leer las jugadas.
#
#   # Análisis de fichas válidas:
#                                 En cuanto al análisis de fichas, lo comenzaremos
#   a realizar una vez que hayamos verificado todoslos datos de los jugadores. 
#   Haremos funciones individuales, que verifican cada uno de los posibles casos
#   de finalización del programa y luego las agruparemos en una función que chequea
#   cada jugada.
#
#       Relacionado con la representación de las fichas, cuando nos encontremos una 
#   jugadas que se encuentra fuera de rango, la asociaremos con la tupla (-1,-1),ya 
#   estas coordenadas no hacen referencia a ninguna del tablero.
#   
#  Archivos de assets:  
#  
#  juego1.txt: Ficha colocada en un lugar ocupado.
#  juego2.txt: Ficha colocada en un lugar sin una ficha del otro colro tangente a ella.
#  juego3.txt: Ficha colocada en un lugar ocupado.
#  juego4.txt: Ficha fuera del tablero.
#  juego5.txt: Turno mal salteado.
#  juego6.txt: Turno mal salteado.
#  juego7.txt: Partida incompleta, por lo que no se puede determinar un ganador.
#  juego8.txt: Gana el jugador de las fichas negras porque el blanco se queda sin fichas en el tablero 
#  juegofinal.txt: Gana el jugador de las fichas blancas
#  juegoGanadoN.txt: Gana el jugador de las fichas negras
   
