
def function_Y(X):
    return X**2 - 4*X + 4  

#
X0 = float(input("Введите начальное значение X0: "))
h = float(input("Введите шаг изменения аргумента h: "))


characteristic_point = float(input("Введите значение характерной точки функции: "))

X = X0  
Y = function_Y(X)  


while Y >= characteristic_point:
    print(f"X = {X}, Y = {Y}")
    X += h  
    Y = function_Y(X)  # 

print("Пройдена характерная точка функции.")
