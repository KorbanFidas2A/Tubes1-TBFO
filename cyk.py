""" 
File: cyk.py

File ini berisi fungsi-fungsi yang dibutuhkan
untuk melakukan algoritma CYK.
"""


def index_of(array, string, length):
    """ 
    Fungsi mengembalikan indeks yang merupakan posisi 
    sebuah string dalam array of string dengan 
    panjang array length.
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


def read_cnf(cnf_filename):
    """ 
    Fungsi membaca file berisi CNF kemudian mengembalikan 
    array of strings berisi production rule dan panjang 
    dari array tersebut.
    """
    
    # Inisialisasi
    production_array = [["~" for _ in range(3)] for _ in range(1005)]
    
    with open(cnf_filename, "r") as cnf_file:
        productions = cnf_file.readlines()
        i = 1
        for production in productions:
            production = production.split()
            left_side = production.pop(0)
            _ = production.pop(0)
            left_variable = True
            for right_side in production:
                if right_side == '|':
                    left_variable = True
                    i += 1
                else:
                    production_array[i][0] = left_side
                    if left_variable:
                        production_array[i][1] = right_side
                    else:
                        production_array[i][2] = right_side
                    left_variable = False
            i += 1
        production_quantity = i - 1
    
    # Mengubah beberapa keyword pada cnf
    # agar sesuai dengan token
    for i in range(1, production_quantity + 1):
        for j in range(3):
            if production_array[i][j] == "barisbaru":
                production_array[i][j] = "n"
            elif production_array[i][j] == "variabel":
                production_array[i][j] = "v"
            elif production_array[i][j] == "equal":
                production_array[i][j] = "e"
            elif production_array[i][j] == "if":
                production_array[i][j] = "i"
            elif production_array[i][j] == "return":
                production_array[i][j] = "r"
            elif production_array[i][j] == "kurungbuka":
                production_array[i][j] = "o"
            elif production_array[i][j] == "kurungtutup":
                production_array[i][j] = "c"
            elif production_array[i][j] == "colon":
                production_array[i][j] = "co"
            elif production_array[i][j] == "elif":
                production_array[i][j] = "e"
            elif production_array[i][j] == "else":
                production_array[i][j] = "el"
            elif production_array[i][j] == "True":
                production_array[i][j] = "t"
            elif production_array[i][j] == "False":
                production_array[i][j] = "f"
            elif production_array[i][j] == "konstan":
                production_array[i][j] = "con"
            elif production_array[i][j] == "arithmeticop":
                production_array[i][j] = "a"
            elif production_array[i][j] == "logicalop":
                production_array[i][j] = "l"
            elif production_array[i][j] == "and":
                production_array[i][j] = "an"
            elif production_array[i][j] == "or":
                production_array[i][j] = "or"
            elif production_array[i][j] == "not":
                production_array[i][j] = "no"
            elif production_array[i][j] == "for":
                production_array[i][j] = "fo"
            elif production_array[i][j] == "in":
                production_array[i][j] = "in"
            elif production_array[i][j] == "range":
                production_array[i][j] = "ra"
            elif production_array[i][j] == "comma":
                production_array[i][j] = "com"
            elif production_array[i][j] == "while":
                production_array[i][j] = "w"
            elif production_array[i][j] == "import":
                production_array[i][j] = "im"
            elif production_array[i][j] == "from":
                production_array[i][j] = "fr"
            elif production_array[i][j] == "as":
                production_array[i][j] = "as"
            elif production_array[i][j] == "def":
                production_array[i][j] = "d"
            elif production_array[i][j] == "class":
                production_array[i][j] = "cl"
            elif production_array[i][j] == "pass":
                production_array[i][j] = "p"
            elif production_array[i][j] == "raise":
                production_array[i][j] = "rai"
            elif production_array[i][j] == "with":
                production_array[i][j] = "wi"
    
    # Mengurutkan production_array kecuali elemen pertama
    head = production_array.pop(0)
    production_array = sorted(production_array, key=lambda x: x[0])
    production_array.insert(0, head)
    
    return production_array, production_quantity


def production_position(production_array, production_quantity):
    """ 
    Fungsi mengembalikan array of strings berisi variabel pada
    production_array dan menyimpan posisinya pada left_idx_array
    dan right_idx_array.
    """
    
    # Inisialisasi array yang dibutuhkan
    variable_array = []
    left_idx_array = [0 for _ in range(300)]
    right_idx_array = [0 for _ in range(300)]

    # Mengisi variable_array, left_idx_array, right_idx_array
    for i in range(1, production_quantity + 1):
        if variable_array == []:
            variable_array.append(production_array[i][0])
            left_idx_array[0] = 1
            right_idx_array[0] = 1
        elif production_array[i][0] != production_array[i-1][0]:
            variable_array.append(production_array[i][0])
            left_idx_array[index_of(variable_array, production_array[i][0], len(variable_array) - 1)] = i
            right_idx_array[index_of(variable_array, production_array[i][0], len(variable_array) - 1)] = i
        else:
            right_idx_array[index_of(variable_array, production_array[i][0], len(variable_array) - 1)] = i
            
    return variable_array, left_idx_array, right_idx_array


def cyk_algorithm(variable_array, production_array, production_quantity, token_array, token_quantity, left_idx_array, right_idx_array):
    """ 
    Fungsi mengembalikan matrix of boolean yang merupakan tabel CYK.
    """

    # Mengisi baris pertama
    table = [[[False for _ in range(550)] for _ in range(550)] for _ in range(550)]
    for i in range(1, token_quantity + 1):
        for j in range(1, production_quantity + 1):
            if production_array[j][1] == token_array[i]:
                table[1][i][j] = True

    # Mengisi baris selanjutnya
    for i in range(2, token_quantity + 1):
        for j in range(1, token_quantity - i + 2):
            for k in range(1, i):
                # Mencari kombinasi
                # S -> A B
                # a_location adalah lokasi A
                # b_location adalah lokasi B
                for l in range(1, production_quantity + 1):
                    a_location = index_of(variable_array, production_array[l][1], len(variable_array) - 1)
                    for m in range(left_idx_array[a_location], right_idx_array[a_location] + 1):    
                        b_location = index_of(variable_array, production_array[l][2], len(variable_array) - 1)
                        for n in range(left_idx_array[b_location], right_idx_array[b_location] + 1):
                            if production_array[m][0] == production_array[l][1] and production_array[n][0] == production_array[l][2]:
                                if table[k][j][m] and table[i - k][j + k][n]:
                                    table[i][j][l] = True
    
    return table                  


def final_check(production_array, production_quantity, token_quantity, P):
    """
    Prosedur menampilkan pesan diterima jika syntax kode sesuai dengan
    grammar pada CFG dan menampilkan pesan lain jika tidak diterima.
    """
    
    is_acc = False
    i = 1
    while i <= production_quantity and not is_acc:
        if production_array[i][0] == "Sn" and P[token_quantity][1][i]:
            is_acc = True
        else:
            i += 1
            
    if is_acc:
        print("Syntax accepted! ♪(^∇^*)")
    else:
        print("Syntax error! (˘･_･˘)")

    
    