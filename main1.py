print('___________________________________________________')
print('                                                   ')
print('              Добро пожаловать                     ')
print('___________________________________________________')
print('Необходимо по очереди вводить координаты поля x, y,')
print('где x - строка, y - столбец')
print('___________________________________________________')




myList = [
    [" ", "0", "1","2"],
    ["0", " ", " "," "],
    ["1", " ", " "," "],
    ["2", " ", " "," "]
]
def print_list():
    for i in myList:
        print(*i)

def check():
    if myList[1][1]=="X" and myList[1][2]=="X" and myList[1][3]=="X":
        print("Победили крестики")
        return False
    elif myList[2][1]=="X" and myList[2][2]=="X" and myList[2][3]=="X":
        print("Победили крестики")
        return False
    elif myList[3][1] == "X" and myList[3][2] == "X" and myList[3][3] == "X":
        print("Победили крестики")
        return False
    elif myList[1][1] == "X" and myList[2][1] == "X" and myList[3][1] == "X":
        print("Победили крестики")
        return False
    elif myList[1][2] == "X" and myList[2][2] == "X" and myList[3][2] == "X":
        print("Победили крестики")
        return False
    elif myList[1][3] == "X" and myList[2][3] == "X" and myList[3][3] == "X":
        print("Победили крестики")
        return False
    elif myList[1][1] == "X" and myList[2][2] == "X" and myList[3][3] == "X":
        print("Победили крестики")
        return False
    elif myList[1][3] == "X" and myList[2][2] == "X" and myList[3][1] == "X":
        print("Победили крестики")
        return False
    elif myList[1][1]=="0" and myList[1][2]=="0" and myList[1][3]=="0":
        print("Победили нолики")
        return False
    elif myList[2][1]=="0" and myList[2][2]=="0" and myList[2][3]=="0":
        print("Победили нолики")
        return False
    elif myList[3][1] == "0" and myList[3][2] == "0" and myList[3][3] == "0":
        print("Победили нолики")
        return False
    elif myList[1][1] == "0" and myList[2][1] == "0" and myList[3][1] == "0":
        print("Победили нолики")
        return False
    elif myList[1][2] == "0" and myList[2][2] == "0" and myList[3][2] == "0":
        print("Победили нолики")
        return False
    elif myList[1][3] == "0" and myList[2][3] == "0" and myList[3][3] == "0":
        print("Победили нолики")
        return False
    elif myList[1][1] == "0" and myList[2][2] == "0" and myList[3][3] == "0":
        print("Победили нолики")
        return False
    elif myList[1][3] == "0" and myList[2][2] == "0" and myList[3][1] == "0":
        print("Победили нолики")
        return False
    else:
        return True

print_list()

for j in range(1,5):
    a, b = map(int, input("Введи номер строки и столбца куда поставить X через пробел").split())
    a=a+1
    b=b+1
    myList[a][b]="X"
    print_list()
    if check() is False:
        break
    c, d = map(int, input("Введи номер строки и столбца куда поставить 0 через пробел").split())
    c=c+1
    d=d+1
    myList[c][d] = "0"
    print_list()
    if check() is False:
        break
if check():
    print("Ничья")