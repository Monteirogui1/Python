while True:
	a=int(input("1o valor: "))
	b=int(input("2o valor: "))
	print(a+b)
	resp=(input("Deseja Continuar? s/n "))
	if resp not in ("s"):
		break