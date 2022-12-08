# -*- coding: utf-8 -*-
"""
Console Calculator
    Type numbers and operands after which equation will be solved
"""
#console not working 
InputValue = "25+3*150/2+50"
#InputValue = input()

"""
###Functions
"""
def DecodeInput(String):
    # separate numeric values from operands
    NumericValue= []
    NumericCollection = []
    OperandCollection = []
    for char in String :
        CheckedChar = CharToNum(char)
        if CheckedChar == '+' or CheckedChar == '-' or CheckedChar == '*' or CheckedChar == '/' or CheckedChar == '^'or CheckedChar == '=':
            NumericCollection.append(DecodeNumericValue(NumericValue))
            NumericValue=[]
            OperandCollection.append(CheckedChar)
        elif isinstance(CheckedChar,int) or CheckedChar =='.':
            NumericValue.append(CheckedChar)
        elif CheckedChar == ' ':
            print("DecodeInput - space detected")
        else:
            print("DecodeInput - Unknown character")
    if char == '=':
        OperandCollection.pop()
    else:
        NumericCollection.append(DecodeNumericValue(NumericValue))
    return (NumericCollection,OperandCollection)
def CharToNum(Char):
    # check if it is possible to extract number, if not return what you have
    Int = 0
    if Char == ('0'):
        Int = 0
    elif Char == ('1'):
        Int = 1    
    elif Char == ('2'):
        Int = 2
    elif Char == ('3'):
         Int = 3    
    elif Char == ('4'):
        Int = 4
    elif Char == ('5'):
        Int = 5    
    elif Char == ('6'):
        Int = 6
    elif Char == ('7'):
         Int = 7       
    elif Char == ('8'):
        Int = 8
    elif Char == ('9'):
        Int = 9
    else :
        #print ("CharToInt function - Character has no integer atributes")
        return (Char)
    return (Int)                  
def DecodeNumericValue(NumArray):
    # create number from digits and decimal point
    DecimalPoint = 1
    DigitFactor = 1
    SumValue = 0
    for digit in reversed(NumArray):
        if digit == '.':
            DecimalPoint = DecimalPoint * 10
        else:
            TempValue = digit * DigitFactor
            SumValue = SumValue + TempValue
            DigitFactor = DigitFactor *10    
    if SumValue > 0 and DecimalPoint > 1:
        SumValue = SumValue / DecimalPoint
    return (SumValue) 
def Solve (a,b,Operand):
    # operations for solving part of equation
    if Operand == '+':
        Output = a + b
    if Operand == '-':
        Output = a - b
    if Operand == '*':
        Output = a * b
    if Operand == '/':
        if a > 0:
            Output = a / b
        else:
            print("Solve - Cannot divide with 0")
    return Output

#check if first value is operand
if isinstance(CharToNum(InputValue[0]),int):
    #Seperate numbers and operands
    Numbers,Operators = DecodeInput(InputValue)
    #initialize priority in solving equation
    Prior = False
    #keep solving equation while it is not complitly solved
    while len(Operators) != 0:
        i = 0
        # first do the */ then +-
        for Operand in Operators:
            if Prior == False:
                if Operand == '*' or Operand == '/':
                    Numbers[i] = Solve(Numbers[i],Numbers[i+1],Operand)
                    #when solved pop second number and operad that is used
                    Numbers.pop(i+1)
                    Operators.pop(i)
            if Prior == True :
                if Operand == '+' or Operand == '-':
                    Numbers[i] = Solve(Numbers[i],Numbers[i+1],Operand)
                    #when solved pop second number and operad that is used
                    Numbers.pop(i+1) 
                    Operators.pop(i)
            i = i + 1 
        #all priority operands are solved
        Prior = True
    #result
    print("Result")
    print(Numbers)
    #print
else:
    print("First element is not integer !")


