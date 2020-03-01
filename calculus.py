import sympy as sm
import os as os
from sympy.parsing.sympy_parser import parse_expr as ps


def differentiate(equation, val):
    yprime = sm.Derivative(equation, sm.Symbol('x'), evaluate=True)
    
    if(val == ""):
        return str(yprime)

    else:   
        x = float(val) 
        return round(eval(str(yprime)), 3)


def integrating(equation, val1, val2):
    if val1 == "":
        return sm.integrate(equation, sm.Symbol('x'))

    else:
        return round(sm.integrate(equation, (sm.Symbol('x'), float(val1), float(val2))), 3)


def main():
    os.system('cls')
    continuing = "y"
    goodChoice = True

    while continuing == "y":
        
        eqIn = input("Equation: ")
        eq = ps(eqIn, evaluate=False)

        while goodChoice:
            toDo = input("Integrate (i) or Differentiate (d): ")

            if toDo == "d":
                goodChoice = False
                val = input("Value: ")

                print("Derivative: " + str(differentiate(eq, val)).replace("log", "ln").replace("**", "^").replace("*", "").replace("ln(e)", ""))

            elif toDo == "i":   
                goodChoice = False 
                bottomRange = input("Bottom Range: ")
                topRange = input("Top Range: ")

                if bottomRange == topRange == "":
                    print("Indefinite Integral: " + str(integrating(eq, bottomRange, topRange)).replace("log", "ln").replace("**", "^").replace("*", "").replace("ln(e)", "") + " + C")

                elif bottomRange != "" and topRange != "":
                    print("Definite Integral: " + str(integrating(eq, bottomRange, topRange)).replace("log", "ln").replace("**", "^").replace("*", "").replace("ln(e)", ""))
                
                else:
                    print("Needs either both bottom and top range, or neither")

        print()

        while not goodChoice:
            continuing = input("Would you like to do another? (y/n): ")

            if continuing == "y" or continuing == "n":
                goodChoice = True
                os.system('cls')

            else:
                goodChoice = False

if __name__ == "__main__":
    main()
