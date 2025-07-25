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
        case "5":
            print("Ingresar una lita de n númmeros enteros")
        case "6":
            print("Calculador de operaciones básicas")
        case "7":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido, vuelva a intentar")