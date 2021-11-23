# tokenizer.py
import sys

# Inisiasi huruf, angka, dan simbol
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
number = "1234567890"
symbol = "+-*/%{}()[]!#^|~&=,:"

def isLetter(x):
# Mengembalikan 1 jika x merupakan letter
    if x in letter:
        return True
    else:
        return False

def isNumber(x):
# Mengembalikan 1 jika x merupakan number
    if x in number:
        return True
    else:
        return False

def isSymbol(x):
# Mengembalikan 1 jika x merupakan symbol
    if x in symbol:
        return True
    else:
        return False

def getChar(str, idx):
# Mengembalikan char index tertentu dalam sebuah string
    if (idx < len(str)):
        return str[idx]
    else:
        return "~"

def getString(str, idx_x, idx_y):
# Mengembalikan substring dalam rentang index tertentu dalam string
    subStr = ""
    for i in range(idx_x, idx_y + 1):
        if (i < len(str)):
            subStr = subStr + str[i]
        else:
            return "~"
    return subStr

def nextWord(line, idx_word):
# Mengembalikan word selanjutnya dalam sebuah line of words
    idx_nextWord = 0
    for word in line:
        if (idx_nextWord == idx_word + 1):
            return word
        idx_nextWord += 1


# ALGORITMA UTAMA

# Inisiasi output file tokenized.txt kosong
f = open("tokenized.txt", "w+")
f.write("")

# Inisiasi awal
token = []
idx_line = 0
valid = True
comment = False

# Proses
with open("python.txt", "r", encoding="utf8") as py_file:
    # Pisah menjadi per baris
    lines = py_file.read().splitlines()

    for i in range(len(lines)):
        lines[i] += " \x90"
    
    for line in lines:
        # Pisah menjadi per kata
        line = line.split()
        
        out = False
        idx_line += 1
        idx_word = 0
        
        for word in line:
            if (out) or (word == "\x90"):
                continue
            i = 0      
            
            while (i < len(word)):
                if (getString(word, i, i + 2) == "\\\\\\") and not(comment):
                    comment = True
                    i += 3
                    continue
                elif (getString(word, i, i + 2) == "\\\\\\") and (comment):
                    comment = False
                    i += 3
                    continue

                if (comment):
                    i += 1
                    continue

                # Operand and Symbols
                if (getChar(word, i) == "~") and (i < len(word)):
                    token.append("opr_mat")                
                if (getChar(word, i) == "#"):
                    out = True
                    break
                elif (getChar(word, i) == "("):
                    token.append("kurung_l")
                elif (getChar(word, i) == ")"):
                    token.append("kurung_r")
                elif (getChar(word, i) == "."):
                    token.append("titik")
                elif (getChar(word, i) == "["):
                    count = 1
                    while (i < len(word)) and (count > 0) and (valid):
                        if (i == len(word)):
                            word = nextWord(line, idx_word)
                            if (word == "\x90"):
                                valid = False
                                print("Tokenizer failed!")
                                break
                            i = 0
                        if (getChar(word, i) == "["):
                            count += 1
                        if (getChar(word, i) == "]"):
                            count -= 1
                        i += 1
                    if (i < len(word)) and (count == 0):
                        token.append("kons")
                    else:
                        valid = False
                        print("Tokenizer failed!")
                        sys.exit()
                elif (getChar(word, i) == "]"):
                    valid = False
                    print("Tokenizer failed!")
                    sys.exit()
                elif (getChar(word, i) == "{"):
                    count = 1
                    while (i < len(word)) and (count > 0) and (valid):
                        if (i == len(word)):
                            word = nextWord(line, idx_word)
                            if (word == "\x90"):
                                valid = False
                                print("Tokenizer failed!")
                                break
                            i = 0
                        if (getChar(word, i) == "{"):
                            count += 1
                        if (getChar(word, i) == "}"):
                            count -= 1
                        i += 1
                    if (i < len(word)) and (count == 0):
                        token.append("kons")
                    else:
                        valid = False
                        print("Tokenizer failed!")
                        sys.exit()
                elif (getChar(word, i) == "}"):
                    valid = False
                    print("Tokenizer failed!")
                    sys.exit()    
                elif (getString(word, i, i + 1) == "->") and isSymbol(getChar(word, i + 2)):
                    word = nextWord(line, idx_word)
                    i = 0
                    while not(isSymbol(getChar(word, i + 1))):
                        i += 1
                    i -= 1
                elif (getChar(word, i) == "<") or (getChar(word, i) == ">"):
                    token.append("opr_log")
                elif ((getChar(word, i) == "=") and (getChar(word, i + 1) == "=")) or ((getChar(word, i) == "<") and (getChar(word, i + 1) == "=")) or ((getChar(word, i) == ">") and (getChar(word, i + 1) == "=")) or ((getChar(word, i) == "!") and (getChar(word, i + 1) == "=")):                
                    token.append("opr_log")
                    i += 1
                elif (getChar(word, i) == ":"):
                    token.append("titik_dua")
                elif (getChar(word, i) == ","):
                    token.append("koma")
                elif (getChar(word, i) == "="):
                    token.append("sama")
                elif (getChar(word, i) == "/") or (getChar(word, i) == "*") or (getChar(word, i) == "+") or (getChar(word, i) == "-") or (getChar(word, i) == "%") or (getChar(word, i) == "|") or (getChar(word, i) == "&"):
                    token.append("opr_mat")
                elif ((getChar(word, i) == "/") and (getChar(word, i + 1) == "/")) or ((getChar(word, i) == "*") and (getChar(word, i + 1) == "*")):
                    token.append("opr_mat")
                    i += 1
                elif (getChar(word, i) == "\'"):
                    while (i < len(word)) and (valid):
                        if (i == len(word)):
                            word = nextWord(line, idx_word)
                            if (word == "\x90"):
                                valid = False
                                print("Tokenizer failed!")
                                break
                            i = 0
                        if (getChar(word, i) == "\'"):
                            break
                        i += 1
                    if not(valid):
                        print("Tokenizer failed!")
                        sys.exit()
                    else:
                        token.append("kons")                  
                # Keywords
                elif (getString(word, i, i + 4) == "False") and (isSymbol(getChar(word, i + 5))):
                    token.append("false")
                    i += 4
                elif (getString(word, i, i + 3) == "True") and (isSymbol(getChar(word, i + 4))):
                    token.append("true")
                    i += 3
                elif (getString(word, i, i + 3) == "None") and (isSymbol(getChar(word, i + 4))):
                    token.append("kons")
                    i += 3
                elif (getString(word, i, i + 2) == "and") and (isSymbol(getChar(word, i + 3))):
                    token.append("and")
                    i += 2
                elif (getString(word, i, i + 1) == "as") and (isSymbol(getChar(word, i + 2))):
                    token.append("as")
                    i += 1
                elif (getString(word, i, i + 4) == "break") and (isSymbol(getChar(word, i + 5))):
                    token.append("var")
                    i += 4          
                elif (getString(word, i, i + 4) == "class") and (isSymbol(getChar(word, i + 5))):
                    token.append("class")
                    i += 4             
                elif (getString(word, i, i + 7) == "continue") and (isSymbol(getChar(word, i + 8))):
                    token.append("var")
                    i += 7
                elif (getString(word, i, i + 2) == "def") and (isSymbol(getChar(word, i + 3))):
                    token.append("def")
                    i += 2                                                                                                                     
                elif (getString(word, i, i + 3) == "elif") and (isSymbol(getChar(word, i + 4))):
                    token.append("elif")
                    i += 3
                elif (getString(word, i, i + 3) == "else") and (isSymbol(getChar(word, i + 4))):
                    token.append("else")
                    i += 3
                elif (getString(word, i, i + 2) == "for") and (isSymbol(getChar(word, i + 3))):
                    token.append("for")
                    i += 2     
                elif (getString(word, i, i + 3) == "from") and (isSymbol(getChar(word, i + 4))):
                    token.append("from")
                    i += 3                                                       
                elif (getString(word, i, i + 1) == "if") and (isSymbol(getChar(word, i + 2))):
                    token.append("if")
                    i += 1
                elif (getString(word, i, i + 5) == "import") and (isSymbol(getChar(word, i + 6))):
                    token.append("import")
                    i += 5                    
                elif (getString(word, i, i + 1) == "in") and (isSymbol(getChar(word, i + 2))):
                    token.append("in")
                    i += 1
                elif (getString(word, i, i + 1) == "is") and (isSymbol(getChar(word, i + 2))):
                    token.append("opr_log")
                    i += 1           
                elif (getString(word, i, i + 2) == "not") and (isSymbol(getChar(word, i + 3))):
                    token.append("not")
                    i += 2          
                elif (getString(word, i, i + 1) == "or") and (isSymbol(getChar(word, i + 2))):
                    token.append("or")
                    i += 1  
                elif (getString(word, i, i + 3) == "pass") and (isSymbol(getChar(word, i + 4))):
                    token.append("pass")
                    i += 3         
                elif (getString(word, i, i + 4) == "raise") and (isSymbol(getChar(word, i + 5))):
                    token.append("raise")
                    i += 4   
                elif (getString(word, i, i + 5) == "return") and (isSymbol(getChar(word, i + 6))):
                    token.append("ret")
                    i += 5  
                elif (getString(word, i, i + 4) == "while") and (isSymbol(getChar(word, i + 5))):
                    token.append("while")
                    i += 4   
                elif (getString(word, i, i + 3) == "with") and (isSymbol(getChar(word, i + 4))):
                    token.append("with")
                    i += 3  
                # Letter
                elif (isLetter(getChar(word, i))):
                    while ((getChar(word, i) != "~") and (isLetter(getChar(word, i))) or (isNumber(getChar(word, i))) or (getChar(word, i) == "_")):
                        i += 1
                    i -= 1
                    if (len(token) > 2) and (token[len(token) - 1] == "titik") and (token[len(token) - 2] == "kons") and (token[len(token) - 3] == "kons"):
                        token.pop()
                        token.pop()
                        token.pop()
                    elif (len(token) > 1) and (token[len(token) - 1] == "titik") and (token[len(token) - 2] == "kons"):
                        token.pop()
                        token.pop()
                    elif (len(token) > 0) and (token[len(token) - 1] == "titik"):
                        token.pop()
                    else:
                        token.append("var")
                # Number
                elif (isNumber(getChar(word, i))):
                    while (isNumber(getChar(word, i))):
                        i += 1
                    i -= 1
                    token.append("kons")         
                i += 1                                                                                                   
            idx_word += 1
            
        token.append("nl")

# Cek kurung
count_kurung = 0
token_awal = token[0]
for i in range(len(token)):
    if (token[i] == "kurung_l"):
        count_kurung += 1
    elif (token[i] == "kurung_r"):
        count_kurung -= 1
    elif (token[i] == "nl"):
        if (count_kurung > 0):
            print("Tokenizer failed!")
            sys.exit()
        elif (count_kurung < 0):
            print("Tokenizer failed!")
            sys.exit()
        if (i != 0) and (token[i - 1] != "titik_dua") and ((token_awal == "def") or (token_awal == "if") or (token_awal == "elif") or (token_awal == "else") or (token_awal == "with") or (token_awal == "class") or (token_awal == "for") or (token_awal == "while")):
            print("Tokenizer failed!")
            sys.exit()
        if (i != len(token) - 1):
            token_awal = token[i + 1]

# Final check
if (valid):
    print("Tokenizer succeed!")
    for i in range(len(token)):
        f.write(token[i])
        f.write(" ")
    f.close()