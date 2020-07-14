#recetas
opciones = (input("Puede elegir entre dos recetas 1- lentejas y apio, 2- morron y cebolla: "))

if opciones> "2":
	print("no es una opción válida")

	opciones = (input("Puede elegir entre dos recetas 1- lentejas y apio, 2- morron y cebolla: "))

normales = (input("Ahora elije un ingrediente común, verduras o berenjena: "))
opciones= str(opciones)

print ("Esta es su receta elegida: ")

#print (opciones + " y " + normales)

if opciones== "1":
	print ("lentejas, apio " +"y "+ normales)
if opciones== "2":
	print ("morron, cebolla " +"y "+ normales)