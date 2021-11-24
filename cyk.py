
from re import A
import time

def index_of(array, string, length):
    """ 
    Binary search
    """
    
    left_index = 0
    right_index = length
    answer = 0
    
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        
        if array[mid_index] < string:
            left_index = mid_index + 1
        elif array[mid_index] == string:
            right_index = mid_index - 1
            answer = mid_index
        else:
            right_index = mid_index - 1
    
    return answer



start = time.time();

# INISIALISASI SEMUA ARRAY
# S -> AB
# A -> 
# B -> 
array_production = [["~" for _ in range(3)] for _ in range(1005)]
v = []
kiri = [0 for _ in range(300)]
kanan = [0 for _ in range(300)]

# BACA TOKEN
array_token = []
with open("token.txt", "r") as token_file:
    tokens = token_file.read().split()

    i = 0
    for token in tokens:
        array_token.append(token)
        i += 1
        
    token_quantity = i

print(f"Jumlah token: {token_quantity}")


# BACA CNF

with open("cnf.txt", "r") as cnf_file:
    productions = cnf_file.readlines()

    i = 0
    for production in productions:
        production = production.split()
        # S -> A B | C
        left_side = production.pop(0)
        arrow = production.pop(0)

        left_variable = True
        for right_side in production:
            if right_side == '|':
                left_variable = True
                i += 1
            else:
                array_production[i][0] = left_side
                if left_variable:
                    array_production[i][1] = right_side
                else:
                    array_production[i][2] = right_side
                left_variable = False
        i += 1
    production_quantity = i
    

for i in range(production_quantity):
    if array_production[i][0] == "barisbaru":
        array_production[i][0] = "b"
    elif array_production[i][0] == "variabel":
        array_production[i][0] = "v"
    elif array_production[i][0] == "equal":
        array_production[i][0] = "e"
    elif array_production[i][0] == "if":
        array_production[i][0] = "i"
    elif array_production[i][0] == "return":
        array_production[i][0] = "r"
    elif array_production[i][0] == "kurungbuka":
        array_production[i][0] = "kb"
    elif array_production[i][0] == "kurungtutup":
        array_production[i][0] = "kt"
    elif array_production[i][0] == "colon":
        array_production[i][0] = "co"
    elif array_production[i][0] == "elif":
        array_production[i][0] = "e"
    elif array_production[i][0] == "else":
        array_production[i][0] = "el"
    elif array_production[i][0] == "True":
        array_production[i][0] = "t"
    elif array_production[i][0] == "False":
        array_production[i][0] = "f"
    elif array_production[i][0] == "konstan":
        array_production[i][0] = "con"
    elif array_production[i][0] == "arithmeticop":
        array_production[i][0] = "a"
    elif array_production[i][0] == "logicalop":
        array_production[i][0] = "l"
    elif array_production[i][0] == "and":
        array_production[i][0] = "an"
    elif array_production[i][0] == "or":
        array_production[i][0] = "or"
    elif array_production[i][0] == "not":
        array_production[i][0] = "no"
    elif array_production[i][0] == "for":
        array_production[i][0] = "fo"
    elif array_production[i][0] == "in":
        array_production[i][0] = "in"
    elif array_production[i][0] == "range":
        array_production[i][0] = "ra"
    elif array_production[i][0] == "comma":
        array_production[i][0] = "com"
    elif array_production[i][0] == "while":
        array_production[i][0] = "w"
    elif array_production[i][0] == "import":
        array_production[i][0] = "im"
    elif array_production[i][0] == "from":
        array_production[i][0] = "fr"
    elif array_production[i][0] == "as":
        array_production[i][0] = "as"
    elif array_production[i][0] == "def":
        array_production[i][0] = "d"
    elif array_production[i][0] == "class":
        array_production[i][0] = "cl"
    elif array_production[i][0] == "pass":
        array_production[i][0] = "p"
    elif array_production[i][0] == "raise":
        array_production[i][0] = "rai"
    elif array_production[i][0] == "with":
        array_production[i][0] = "wi"
           
    if array_production[i][1] == "barisbaru":
        array_production[i][1] = "b"
    elif array_production[i][1] == "variabel":
        array_production[i][1] = "v"
    elif array_production[i][1] == "equal":
        array_production[i][1] = "e"
    elif array_production[i][1] == "if":
        array_production[i][1] = "i"
    elif array_production[i][1] == "return":
        array_production[i][1] = "r"
    elif array_production[i][1] == "kurungbuka":
        array_production[i][1] = "kb"
    elif array_production[i][1] == "kurungtutup":
        array_production[i][1] = "kt"
    elif array_production[i][1] == "colon":
        array_production[i][1] = "co"
    elif array_production[i][1] == "elif":
        array_production[i][1] = "e"
    elif array_production[i][1] == "else":
        array_production[i][1] = "el"
    elif array_production[i][1] == "True":
        array_production[i][1] = "t"
    elif array_production[i][1] == "False":
        array_production[i][1] = "f"
    elif array_production[i][1] == "konstan":
        array_production[i][1] = "con"
    elif array_production[i][1] == "arithmeticop":
        array_production[i][1] = "a"
    elif array_production[i][1] == "logicalop":
        array_production[i][1] = "l"
    elif array_production[i][1] == "and":
        array_production[i][1] = "an"
    elif array_production[i][1] == "or":
        array_production[i][1] = "or"
    elif array_production[i][1] == "not":
        array_production[i][1] = "no"
    elif array_production[i][1] == "for":
        array_production[i][1] = "fo"
    elif array_production[i][1] == "in":
        array_production[i][1] = "in"
    elif array_production[i][1] == "range":
        array_production[i][1] = "ra"
    elif array_production[i][1] == "comma":
        array_production[i][1] = "com"
    elif array_production[i][1] == "while":
        array_production[i][1] = "w"
    elif array_production[i][1] == "import":
        array_production[i][1] = "im"
    elif array_production[i][1] == "from":
        array_production[i][1] = "fr"
    elif array_production[i][1] == "as":
        array_production[i][1] = "as"
    elif array_production[i][1] == "def":
        array_production[i][1] = "d"
    elif array_production[i][1] == "class":
        array_production[i][1] = "cl"
    elif array_production[i][1] == "pass":
        array_production[i][1] = "p"
    elif array_production[i][1] == "raise":
        array_production[i][1] = "rai"
    elif array_production[i][1] == "with":
        array_production[i][1] = "wi"
    
    if array_production[i][2] == "barisbaru":
        array_production[i][2] = "b"
    elif array_production[i][2] == "variabel":
        array_production[i][2] = "v"
    elif array_production[i][2] == "equal":
        array_production[i][2] = "e"
    elif array_production[i][2] == "if":
        array_production[i][2] = "i"
    elif array_production[i][2] == "return":
        array_production[i][2] = "r"
    elif array_production[i][2] == "kurungbuka":
        array_production[i][2] = "kb"
    elif array_production[i][2] == "kurungtutup":
        array_production[i][2] = "kt"
    elif array_production[i][2] == "colon":
        array_production[i][2] = "co"
    elif array_production[i][2] == "elif":
        array_production[i][2] = "e"
    elif array_production[i][2] == "else":
        array_production[i][2] = "el"
    elif array_production[i][2] == "True":
        array_production[i][2] = "t"
    elif array_production[i][2] == "False":
        array_production[i][2] = "f"
    elif array_production[i][2] == "konstan":
        array_production[i][2] = "con"
    elif array_production[i][2] == "arithmeticop":
        array_production[i][2] = "a"
    elif array_production[i][2] == "logicalop":
        array_production[i][2] = "l"
    elif array_production[i][2] == "and":
        array_production[i][2] = "an"
    elif array_production[i][2] == "or":
        array_production[i][2] = "or"
    elif array_production[i][2] == "not":
        array_production[i][2] = "no"
    elif array_production[i][2] == "for":
        array_production[i][2] = "fo"
    elif array_production[i][2] == "in":
        array_production[i][2] = "in"
    elif array_production[i][2] == "range":
        array_production[i][2] = "ra"
    elif array_production[i][2] == "comma":
        array_production[i][2] = "com"
    elif array_production[i][2] == "while":
        array_production[i][2] = "w"
    elif array_production[i][2] == "import":
        array_production[i][2] = "im"
    elif array_production[i][2] == "from":
        array_production[i][2] = "fr"
    elif array_production[i][2] == "as":
        array_production[i][2] = "as"
    elif array_production[i][2] == "def":
        array_production[i][2] = "d"
    elif array_production[i][2] == "class":
        array_production[i][2] = "cl"
    elif array_production[i][2] == "pass":
        array_production[i][2] = "p"
    elif array_production[i][2] == "raise":
        array_production[i][2] = "rai"
    elif array_production[i][2] == "with":
        array_production[i][2] = "wi"

array_production = sorted(array_production,key=lambda x: x[0])
# DEBUGGING SORTING ARRAY
# for i in range(production_quantity):
#     print(i, array_production[i][0], "->", array_production[i][1], end=" ")
#     if (array_production[i][2] != "~"):
#         print(array_production[i][2])
#     else:
#         print()


for i in range(production_quantity):
    if v == []:
        v.append(array_production[i][0])
        kiri[0] = 1
        kanan[0] = 1
    elif array_production[i][0] != array_production[i-1][0]:
        v.append(array_production[i][0])
        kiri[index_of(v, array_production[i][0], len(v) - 1)] = i
        kanan[index_of(v, array_production[i][0], len(v) - 1)] = i
    else:
        kanan[index_of(v, array_production[i][0], len(v) - 1)] = i

# print(v)
# print("="*100)  
# print(kiri)
# print("="*100)
# print(kanan)

# DEBUGGING
# for i in range(len(v)):
#     print(i, v[i], kiri[index_of(v, v[i], len(v) - 1)], kanan[index_of(v, v[i], len(v) - 1)])

P = [[[False for _ in range(550)] for _ in range(550)] for _ in range(550)]
print("ap:", array_production[13][1], "token:", array_token[1])
# INISIALISASI BARIS PERTAMA MENJADI TRUE
a = 0
for i in range(token_quantity):
    for j in range(production_quantity):
        if array_production[j][1] == array_token[i]:
            P[0][i][j] = True
            a += 1
            if P[0][1][13] == 1:
                print(array_production[j][1], array_token[i])

print("setelah diubah")
for i in range(1):
    for j in range(6):
        for k in range(15):
            print(P[i][j][k], end=" ")
        print()
    print()
 
print(f"masuk {a} kali")

a= 0
print(P[0][2][230], P[0][3][230], array_production[231][0], array_production[32][1], array_production[230][0], array_production[32][2])
for i in range(1, token_quantity):
    print(i, time.time() - start)
    for j in range(token_quantity - i):
        for k in range(i):
            # Test combination
            for l in range(production_quantity):
                b_location = index_of(v, array_production[l][1], len(v) - 1)
                print(f"({kiri[b_location]},{kanan[b_location]})", end=" ")
                for m in range(kiri[b_location], kanan[b_location] + 1):
                    a += 1
                    c_location = index_of(v, array_production[l][2], len(v) - 1)
                    for n in range(kiri[c_location], kanan[c_location] + 1):
                        if array_production[m][0] == array_production[l][1] and array_production[n][0] == array_production[l][2]:
                            # if P[k][j][m]:
                            #     print(f"P[{k}][{j}][{m}] true")
                            # if P[i-k][j+k + 1][n]:
                            #     print(f"P[{i-k}][{j+k + 1}][{n}] true")
                            
                            if P[k][j][m] and P[i-k][j+k + 1][n]:
                                P[i][j][l] = True
                                print("i:", i, "j:", j, "k:" , k, "l:", l, "m:", m, "n:",n)

print(f"masuk m: {a}")

is_acc = False
i = 0
while i < production_quantity and not is_acc:
    b = i
    if array_production[i][0] == "S0" and P[token_quantity - 1][1][b]:
        is_acc = True
    else:
        i += 1

if is_acc:
    print("Accepted")
else:
    print("Syntax Error")
    
end = time.time()
print(end-start)
