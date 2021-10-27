Numero =  int (input(“Informe um número entre 1 e 10”))
While numero < 1 or numero >10:
    Numero =  int (input(“Informe um número entre 1 e 10”))
Print(“Tabuada de {}.format(numero))
For n in range (1, 11):
     Print( “{0} x {1} = {2}”.format(numero, n, (numero = n)))
