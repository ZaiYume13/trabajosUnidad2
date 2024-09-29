alumnos=['juan','pedro','luis',10]

print(alumnos)

"""
print(alumnos[0])
print(alumnos[1])
print(alumnos[2])
print(alumnos[-1])
print(alumnos[-2])
print(alumnos[-3])
"""
"""
print ("recorreidno elementos")
for alum in alumnos:#recorriendo elementos 
	print(alum)
print ("recorreidno indices")
#recorriendo indices
for i in range (len(alumnos)):
	print (alumnos[i])

print ("recorreidno con while y los indices")
indice=0
while indice<len (alumnos):
	print(alumnos[indice])
	indice +=1
"""
"""
print ("agregar valores al arreglo")
numeros=[]
numeros.append(9)
numeros.append(6)
numeros.append(4)
print(numeros)

print("quitar valores al arreglo")
numeros.pop(1)
print(numeros)

print("Quitar valores con remove")
alumnos.remove('juan')
print(alumnos)
"""
print("Buscar con for")
for i in range (len(alumnos)):
	if (alumnos[i]) == 'luis':
		print ("Si existe Luis en la lista, su pocisión es: ",i+1)
	
print("Buscar con funcion")
if 'luis' in alumnos:
	print ("Si existe Luis en la lista")
else:
	print ("No existe Luis en la lista")
	
print("Buscar la pocisión")
indice = alumnos.index('luis')
print("La pocosión de Luis es: ",indice+1)

print("Buscar en pocisión con try y except")
try:
	indice = alumnos.index('Carlos')
except ValueError:
	print ("No existe Carlos en la lista")
