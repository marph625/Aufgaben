numInput1 = float(input("First Number --> "))
numInput2 = float(input("Second Number --> "))
operatorInput = input("Operator (+, -, *, /) --> ")
def calculator(numInput1, numInput2, operatorInput):
    
    match operatorInput:
        case "+":
            resAdd = numInput1 + numInput2
            print(resAdd)
        case "-":
            resSub = numInput1 - numInput2
            print(resSub)
        case "*":
            resMul = numInput1 * numInput2
            print(resMul)
        case "/":
            if numInput2 == 0:
                print("Never. Divide. By. Zero.")
            else:
                resDiv = numInput1 / numInput2
                print(resDiv)


calculator(numInput1, numInput2, operatorInput)