import wikipedia

wikipedia.set_lang("es")

vocabulario = [
    'Palabra1',
    'Palabra2',
    'Palabra3',

    #'disco'#Si escribes una palabra como "disco"
    		#la cual tiene muchas definiciones te saldria un error....
  	    	#¿Como lo arreglas? definiendo el tipo de disco que necesitas.
  			#Ej. 'Disco Duro', 'Musica Disco'.
]

#Cantidad de parrafos
parrafos = 1

#Crea un .txt donde se guardará la tarea
glosario = open("glosario.txt", "w+")

#Para saber cuando el script busca algo
print("Buscando tu glosario, espere...")

for i in range(len(vocabulario)):
    busqueda = wikipedia.search(vocabulario[i])
    if(len(busqueda) > 0):

        #Si encontró algo...
        result = wikipedia.summary(busqueda[0], sentences=parrafos)
        glosario.write(vocabulario[i] + ": " + result + "\n\n")
    else:

        #Si no se encuentra la palabra...
        glosario.write(vocabulario[i] + ": No se ha encontrado ninguna palabra, Posiblemente por mala escritura...\n\n")
else:
    #Cerramos el documento
    glosario.close()
    print("La tarea ya esta lista")
