# def print_name (name) :
#         print("my name is : " ,name)


# def Variadic_func (*Input):
#         x=Input
#         print(type(Input))
#         print("here is the input"+str(x) )

# print_name("ahmed")

Data = 100
print(Data)

def changeGlobal(Data_1):
    global Data 
    Data  = Data_1
    print(Data)

changeGlobal(50)
print(Data)