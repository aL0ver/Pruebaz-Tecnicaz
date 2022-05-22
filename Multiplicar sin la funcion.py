def multiplicar(a,b):
	resultado=0
	menor=min(a,b) ; mayor=max(a,b)

	for i in range(menor):
		resultado += mayor
	return resultado
