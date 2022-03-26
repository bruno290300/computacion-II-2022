import getopt
import sys

(opt, arg) = getopt.getopt(sys.argv[1:], 'n:m:o:')

print("options: ", opt)

for (op, ar) in opt:
    if op in '-o':
        print("Option -o: ", ar)
        option = ar
    elif op == '-n':
        print("Option -n: ", ar)
        num1 = ar
    elif op == '-m':
        print("Option -m: ", ar)
        num2 = ar
    else:
        print("Option invalida")

if  option == '+':
    result = int(num1) + int(num2) 
    print("resultado de la suma de:", num1, "+", num2, "es:",result)

elif option == '-':
    result = int(num1) - int(num2)
    print("resultado de la resta de:", num1, "-", num2, "es:",result)

elif option == '*':
    result = int(num1) * int(num2)
    print("resultado de la multiplicacion de:", num1, "*", num2, "es:",result)

elif option == '/':
    result = int(num1) / int(num2)
    print("resultado de la division de:", num1, "/", num2, "es:", )

else:
    print("Ingrese una opcion valida")

    