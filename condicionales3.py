salario_presidente=int(input("Introduce salario presidente"))

salario_director=int(input("Introduce salario director"))
print("salario director: +"str(salario_director))

salario_jefe area=int(input("Introduce salario jefe area"))
print("salario jefe area: +"str(salario_jefe area))

salario_administrativo=int(input("Introduce salario salario_administrativo"))
print("salario_administrativo: +"str(salario_administrativo))

if salario_administrativo<salario_jefe area<salario_director<salario presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")