def arithmetic(num1: int,num2: int, op:str):
    match op:
        case '+':
           return num1+num2
        case '-':
            return num1-num2
        case '*':
            return num1*num2
        case '/':
            return num1/num2
    return "Неизвестная операция"

print(arithmetic(2,3,'+'))