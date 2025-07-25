def sum_of_numbers(numbers):
    numbers2 = sum(numbers)
    return numbers2

def average_of_numbers(numbers, number_numbers):
    numbers3 = sum(numbers)/number_numbers
    return numbers3

def numbers_multiples_of_trhee(numbers):
    trhree_numbers = 0
    for i in numbers:
        if i%3==0:
            trhree_numbers += 1
    return trhree_numbers

def area_of_rectangle(base, height):
    area = base*height
    return area

def perimeter_of_rectangle(base, height):
    perimeter = (2*base)+(2*height)
    return perimeter

def prime_number(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def grade_point_average():
    user_grades = int(input("Cuantas calificaciones quieres ingresar? "))
    max_grades = 0
    min_grades = 0
    for i in range(user_grades):
        user_grades = float(input("Ingrese el número: "))
        if user_grades >= 85:
            max_grades += 1
        elif user_grades < 60:
            min_grades += 1
    print(f"La cantidad de notas que estan entre 85 puntos o más es de: {max_grades}")
    print(f"La cantidad de notas que estan en zona de riesgo es de: {min_grades}")

def max_number(numbers):
    number = max(numbers)
    return number

def min_number(numbers2):
    number2 = min(numbers2)
    return number2

def repeated_numbers(numbers3):
    numbers_unic = set(numbers3)
    for i in numbers_unic:
        amount = numbers3.count(i)
        if amount > 1:
            print(f"El número {i}, se repite {amount} veces")

def suma_number(number1, number2):
    total_suma = number1+number2
    return total_suma

def resta_number(number1, number2):
    total_resta = number1-number2
    return total_resta

def multi_number(number1, number2):
    total_multi = number1*number2
    return total_multi

def div_number(number1, number2):
    total_div = number1/number2
    return total_div

while True:
    print("--Menú--")
    print("1.- Lista de números reales")
    print("2.- Calcular el área y perímetro de un rectángulo")
    print("3.- Verificar si un número ingresado es primo o no")
    print("4.- Calcular el promedio de n calificaciones")
    print("5.- Ingresar una lista de n números enteros")
    print("6.- Calculadora de operaciones básicas")
    print("7.- Salir del programa")
    menu_option = input("Ingrese el número de la opción que quiera ingresar: ")
    print()
    match menu_option:
        case "1":
            print("Lista de números reales")
            number_of_numbers = int(input("Cuantos númmeros quieres ingresar? "))
            numbers_list = []
            for i in range(number_of_numbers):
                numbers_to_add = float(input("Ingrese el número: "))
                numbers_list.append(numbers_to_add)
            print(f"La suma de todos los números es de: {sum_of_numbers(numbers_list)}")
            print(f"El promedio de todos los números es de: {average_of_numbers(numbers_list, number_of_numbers)}")
            print(f"La cantidad de números que son multiplos de 3 es de: {numbers_multiples_of_trhee(numbers_list)}")
            print()
        case "2":
            print("Calcular el área y perímetro de un rectángulo")
            base_rectangle = float(input("Ingrese el valor de la base del rectangulo: "))
            height_rectangle = float(input("Ingrese el valor de la altura del rectangulo: "))
            print(f"El área del rectangulo es de: {area_of_rectangle(base_rectangle, height_rectangle)}")
            print(f"El perimetro del rectangulo es de: {perimeter_of_rectangle(base_rectangle, height_rectangle)}")
            print()
        case "3":
            print("Verificar si un número ingresado es primo")
            user_number = int(input("Ingrese el número a evaluar: "))
            if prime_number(user_number) == False:
                print("El número no es primo")
            else:
                print("El número es primo")
            print()
        case "4":
            print("Calcular el promedio de n calificaciones")
            grade_point_average()
            print()
        case "5":
            print("Ingresar una lita de n númmeros enteros")
            number_of_numbers = int(input("Cuantos númmeros quieres ingresar? "))
            numbers_list = []
            for i in range(number_of_numbers):
                numbers_to_add = float(input("Ingrese el número: "))
                numbers_list.append(numbers_to_add)
            print(f"El numero maximo es el {max_number(numbers_list)}")
            print(f"El numero minimo es el {min_number(numbers_list)}")
            repeated_numbers(numbers_list)
        case "6":
            print("Calculador de operaciones básicas")
            print("--Menú--")
            print("1.- Suma")
            print("2.- Resta")
            print("3.- Multiplicación")
            print("4.- División")
            option = input("Escriba el número de opción al que quiera ingresar: ")
            match option:
                case "1":
                    print("Suma")
                    first_number = float(input("Ingrese el primer número: "))
                    second_number = float(input("Ingrese el segundo número: "))
                    print(f"El resultado de la suma es de {suma_number(first_number, second_number)}")
                    print()
                case "2":
                    print("Resta")
                    first_number = float(input("Ingrese el primer número: "))
                    second_number = float(input("Ingrese el segundo número: "))
                    print(f"El resultado de la resta es de {resta_number(first_number, second_number)}")
                    print()
                case "3":
                    print("Multiplicación")
                    first_number = float(input("Ingrese el primer número: "))
                    second_number = float(input("Ingrese el segundo número: "))
                    print(f"El resultado de la multiplicación es de {multi_number(first_number, second_number)}")
                    print()
                case "4":
                    print("División")
                    first_number = float(input("Ingrese el primer número: "))
                    second_number = float(input("Ingrese el segundo número: "))
                    print(f"El resultado de la división es de {div_number(first_number, second_number)}")
                    print()
                case _:
                    print("Valor invalido, vuelva a intentar")
                    print()
        case "7":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido, vuelva a intentar")