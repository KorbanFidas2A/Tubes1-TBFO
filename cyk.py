# cyk.py

from re import A

# BINARY SEARCH
def index_of(array, string, length):
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


# INISIALISASI SEMUA ARRAY
array_production = [["~" for _ in range(3)] for _ in range(1005)]
variabel_array = []
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
array_token.insert(0, "")


# BACA CNF
with open("cnf.txt", "r") as cnf_file:
    productions = cnf_file.readlines()
    i = 1
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
    production_quantity = i - 1
    

# KONVERSI MENJADI TOKEN
print("Checking...")
for i in range(1, production_quantity + 1):
    for j in range(3):
        if array_production[i][j] == "newline":
            array_production[i][j] = "n"
        elif array_production[i][j] == "variable":
            array_production[i][j] = "v"
        elif array_production[i][j] == "equal":
            array_production[i][j] = "e"
        elif array_production[i][j] == "if":
            array_production[i][j] = "i"
        elif array_production[i][j] == "return":
            array_production[i][j] = "r"
        elif array_production[i][j] == "openparentheses":
            array_production[i][j] = "o"
        elif array_production[i][j] == "closeparentheses":
            array_production[i][j] = "c"
        elif array_production[i][j] == "colon":
            array_production[i][j] = "co"
        elif array_production[i][j] == "elif":
            array_production[i][j] = "e"
        elif array_production[i][j] == "else":
            array_production[i][j] = "el"
        elif array_production[i][j] == "true":
            array_production[i][j] = "t"
        elif array_production[i][j] == "false":
            array_production[i][j] = "f"
        elif array_production[i][j] == "constant":
            array_production[i][j] = "con"
        elif array_production[i][j] == "arithmeticop":
            array_production[i][j] = "a"
        elif array_production[i][j] == "logicalop":
            array_production[i][j] = "l"
        elif array_production[i][j] == "and":
            array_production[i][j] = "an"
        elif array_production[i][j] == "or":
            array_production[i][j] = "or"
        elif array_production[i][j] == "not":
            array_production[i][j] = "no"
        elif array_production[i][j] == "for":
            array_production[i][j] = "fo"
        elif array_production[i][j] == "in":
            array_production[i][j] = "in"
        elif array_production[i][j] == "range":
            array_production[i][j] = "ra"
        elif array_production[i][j] == "comma":
            array_production[i][j] = "com"
        elif array_production[i][j] == "while":
            array_production[i][j] = "w"
        elif array_production[i][j] == "import":
            array_production[i][j] = "im"
        elif array_production[i][j] == "from":
            array_production[i][j] = "fr"
        elif array_production[i][j] == "as":
            array_production[i][j] = "as"
        elif array_production[i][j] == "def":
            array_production[i][j] = "d"
        elif array_production[i][j] == "class":
            array_production[i][j] = "cl"
        elif array_production[i][j] == "pass":
            array_production[i][j] = "p"
        elif array_production[i][j] == "raise":
            array_production[i][j] = "rai"
        elif array_production[i][j] == "with":
            array_production[i][j] = "wi"


# SORTING PRODUCTION RULE
head = array_production.pop(0)
array_production = sorted(array_production,key=lambda x: x[0])
array_production.insert(0, head)
for i in range(1, production_quantity + 1):
    if variabel_array == []:
        variabel_array.append(array_production[i][0])
        kiri[0] = 1
        kanan[0] = 1
    elif array_production[i][0] != array_production[i-1][0]:
        variabel_array.append(array_production[i][0])
        kiri[index_of(variabel_array, array_production[i][0], len(variabel_array) - 1)] = i
        kanan[index_of(variabel_array, array_production[i][0], len(variabel_array) - 1)] = i
    else:
        kanan[index_of(variabel_array, array_production[i][0], len(variabel_array) - 1)] = i


# INISIALISASI 
P = [[[False for _ in range(550)] for _ in range(550)] for _ in range(550)]
for i in range(1, token_quantity + 1):
    for j in range(1, production_quantity + 1):
        if array_production[j][1] == array_token[i]:
            P[1][i][j] = True


# PROSES
for i in range(2, token_quantity + 1):
    for j in range(1, token_quantity - i + 2):
        for k in range(1, i):
            for l in range(1, production_quantity + 1):
                b_location = index_of(variabel_array, array_production[l][1], len(variabel_array) - 1)
                for m in range(kiri[b_location], kanan[b_location] + 1):    
                    c_location = index_of(variabel_array, array_production[l][2], len(variabel_array) - 1)
                    for n in range(kiri[c_location], kanan[c_location] + 1):
                        if array_production[m][0] == array_production[l][1] and array_production[n][0] == array_production[l][2]:
                            if P[k][j][m] and P[i - k][j + k][n]:
                                P[i][j][l] = True                                


# FINAL CHECK
is_acc = False
i = 1
while i <= production_quantity and not is_acc:
    if array_production[i][0] == "S0" and P[token_quantity][1][i]:
        is_acc = True
    else:
        i += 1
if is_acc:
    print("Syntax accepted! ♪(^∇^*)")
else:
    print("Syntax error! (˘･_･˘)")
