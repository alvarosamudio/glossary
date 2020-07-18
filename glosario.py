import wikipedia

wikipedia.set_lang("es")

vocabulario = [
    'Palabra1',
    'Palabra2',
    'Palabra3',
]

parrafos = 1

glosario = open("glosario.txt", "w+")

print("Buscando tu glosario, espere...")

for i in range(len(vocabulario)):
    busqueda = wikipedia.search(vocabulario[i])
    if(len(busqueda) > 0):
        result = wikipedia.summary(busqueda[0], sentences=parrafos)
        glosario.write(vocabulario[i] + ": " + result + "\n\n")
    else:
        glosario.write(vocabulario[i] + ": No se ha encontrado ninguna palabra, Posiblemente por mala escritura...\n\n")
else:
    glosario.close()
    print("La tarea ya esta lista")
