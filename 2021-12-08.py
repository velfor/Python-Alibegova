#Игра кости. Играют 2 игрока, по очереди бросают по 2 игральных кубика.
# Победил тот, у кого больше очков. Ничья если очки равные.
##import random
##
##answer = 'д'
##while answer == 'д':
##    cube1 = random.randint(1,6)
##    cube2 = random.randint(1,6)
##    player1_score = cube1 + cube2
##    print("Первый игрок набрал", player1_score,"очков")
##    cube1 = random.randint(1,6)
##    cube2 = random.randint(1,6)
##    player2_score = cube1 + cube2
##    print("Второй игрок набрал", player2_score,"очков")
##    if player1_score > player2_score:
##        print("1-й выиграл")
##    elif player2_score > player1_score:
##        print("2-й выиграл")
##    elif player1_score == player2_score:
##        print("Ничья")
##    print("Играем ещё? Для продолжения введите букву д")
##    answer = input()

#Камень - ножницы - бумага с компьютером
##import random
##answer = 'д'
##while answer == 'д':
##    comp = random.randint(1,3)
##    if comp == 1:
##        comp = "камень"
##    elif comp == 2:
##        comp = "ножницы"
##    elif comp == 3:
##        comp = "бумага"
##
##    print("Введите свой выбор: 1 - для камень, 2 - для ножницы")
##    print("3 - для бумаги")
##    player = int(input())
##    if player == 1:
##        player = "камень"
##    elif player == 2:
##        player = "ножницы"
##    elif player == 3:
##        player = "бумага"
##    #выводим кто что загадал
##    print("У игрока", player, ", у компа", comp)
##    #проверка выигрыша, ничьи, проигрыша
##    if player == "камень" and comp == "ножницы":
##        print("Выиграл игрок")
##    elif player == "ножницы" and comp == "бумага":
##        print("Выиграл игрок")
##    elif player == "бумага" and comp == "камень":
##        print("Выиграл игрок")
##    elif player == comp:
##        print("Ничья")
##    else:
##        print("Выиграл комп")
##    print("Играем ещё? Для продолжения введите букву д")
##    answer = input()    

#Array1. Дано целое число N (>0). Сформировать и вывести
#целочисленный список размера N,содержащий N первых положительных
#нечетных чисел: 1, 3, 5, ... .

### создание списка
##mas = []
##n = int(input())
##i = 1 # счетчик цикла
##k = 1 # первое нечетное число
##while i <= n: # повторять n раз
##    mas.append(k) # добавить нечетное число в список
##    k = k + 2 # вычислить следующее нечетное
##    i = i + 1 # изменили счетчик цикла
##print(*mas) # печать списка

#Array2. Дано целое число N (>0). Сформировать и вывести
#целочисленный массив размера N, содержащий степени двойки от
#первой до N-й: 2, 4, 8, 16, ... .
##mas = []
##n = int(input())
##k = 2
##i = 1
##while i <= n:
##    mas.append(k)
##    k = k * 2
##    i = i + 1
##print(mas)

#Series1◦. Даны десять вещественных чисел. Найти их сумму.
##import random
##mas = []
##n = int(input())
##for i in range(n):
##    mas.append(random.randint(-10,10))
##print(*mas)
##summa = 0
##for i in range(n):
##    summa += mas[i]
##print(summa)

#Series2. Даны десять вещественных чисел. Найти их произведение. 
##import random
##mas = []
##n = 10
##for i in range(n):
##    mas.append(random.randint(1,5))
##print(*mas)
##p = 1
##for i in range(n):
##    p *= mas[i]
##print(p)

#Series3. Даны десять чисел.Найти их среднее арифметическое.
##import random
##mas = []
##n = 10
##for i in range(n):
##    mas.append(random.randint(-10,10))
##print(*mas)
##summa = 0
##for i in range(n):
##    summa += mas[i]
##print(summa/n)

#Распределительная шляпа
import random
students = ['Гарри','Рон','Гермиона','Драко','Симус','Фред',
            'Лаванда','Оливер']

print(students[0])

griffindor = []
hufflepuf = []
slizerin = []

for i in range(3):
    stud = random.choice(students)
    students.remove(stud)
    griffindor.append(stud)

for i in range(3):
    stud = random.choice(students)
    students.remove(stud)
    hufflepuf.append(stud)

for i in range(2):
    stud = random.choice(students)
    students.remove(stud)
    slizerin.append(stud)

print("Гриффиндор:", *griffindor)
print("Хаффлпаф:", *hufflepuf)
print("Cлизерин:", *slizerin)

















    
