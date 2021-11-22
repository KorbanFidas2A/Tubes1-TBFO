# tokenizer.py

# Inisiasi huruf, angka, dan simbol
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
number = "1234567890"
symbol = "+-*/%{}()[]!#^|~&=,:"

def isLetter(x):
# Mengembalikan 1 jika x merupakan letter
    for i in range(len(letter)):
        if (x == letter[i]):
            return True
        else:
            return False

def isNumber(x):
# Mengembalikan 1 jika x merupakan number
    for i in range(len(number)):
        if (x == number[i]):
            return True
        else:
            return False

def isSymbol(x):
# Mengembalikan 1 jika x merupakan symbol
    for i in range(len(symbol)):
        if (x == symbol[i]):
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
    for i in range(idx_x, idx_y):
        if (i < len(str)):
            subStr = subStr + str[i]
        else:
            return "~"
    return subStr

def nextWord(line, idx_word):
# Mengembalikan word selanjutnya dalam sebuah line of words
    idx_nextWord = 0
    for next_word in line:
        if (idx_nextWord == idx_word + 1):
            return next_word
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
with open("python.py", "r") as py_file:
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
            if (out):
                continue
            while (i < len(word)):
                if (getString(word, i, i + 2) == "\'\'\'") and (comment):
                    comment = False
                    i += 3
                    continue
                elif (getString(word, i, i + 2) == "\'\'\'") and not(comment):
                    comment = True
                    i += 3
                    continue

                if (comment):
                    i += 1
                    continue

                # Operand and Symbols
                if (getChar(word, i) == "#"):
                    out = True
                    break
                elif (getChar(word, i) == "~") and (i < len(word)):
                    token.append("opr_mat")
                elif (getChar(word, i) == "("):
                    token.append("kurung_l")
                elif (getChar(word, i) == ")"):
                    token.append("kurung_r")
                elif (getChar(word, i) == "."):
                    token.append("titik")
                elif (getChar(word, i) == "["):
                    count = 1
                    while (i < len(word)) and (count > 0) and (valid):
                        i += 1
                        if (i == len(word)):
                            next_word = nextWord(line, idx_word)
                            if (next_word == "\x90"):
                                valid = False
                                break
                            i = 0
                        if (getChar(word, i) == "["):
                            count += 1
                        if (getChar(word, i) == "]"):
                            count -= 1
                    if (i < len(word)) and (count == 0):
                        token.append("kons")
                    else:
                        valid = False
                        # error print message
                        exit()
                elif (getChar(word, i) == "]"):
                    valid = False
                    # error print message
                    exit()
                elif (getChar(word, i) == "{"):
                    count = 1
                    while (i < len(word)) and (count > 0) and (valid):
                        i += 1
                        if (i == len(word)):
                            next_word = nextWord(line, idx_word)
                            if (next_word == "\x90"):
                                valid = False
                                break
                            i = 0
                        if (getChar(word, i) == "{"):
                            count += 1
                        if (getChar(word, i) == "}"):
                            count -= 1
                    if (i < len(word)) and (count == 0):
                        token.append("kons")
                    else:
                        valid = False
                        # error print message
                        exit()
                elif (getChar(word, i) == "}"):
                    valid = False
                    # error print message
                    exit()    
                elif (getString(word, i, i + 1) == "->") and isSymbol(getChar(word, i + 2)):
                    next_word = nextWord(line, idx_word)
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
                        i += 1
                        if (i == len(word)):
                            next_word = nextWord(line, idx_word)
                            if (next_word == "\x90"):
                                valid = False
                                break
                            i = 0
                        if (getChar(word, i) == "\'"):
                            break
                    if not(valid):
                        # error print message
                        exit()
                    else:
                        token.append("kons")
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
                # Keywords
                elif (getString(word, i, i + 4) == "False") and (isSymbol(word, i + 5)):
                    token.append("false")
                    i += 4
                elif (getString(word, i, i + 3) == "True") and (isSymbol(word, i + 4)):
                    token.append("true")
                    i += 3
                elif (getString(word, i, i + 3) == "None") and (isSymbol(word, i + 4)):
                    token.append("kons")
                    i += 3
                elif (getString(word, i, i + 2) == "and") and (isSymbol(word, i + 3)):
                    token.append("and")
                    i += 2
                elif (getString(word, i, i + 1) == "as") and (isSymbol(word, i + 2)):
                    token.append("as")
                    i += 1
                elif (getString(word, i, i + 4) == "break") and (isSymbol(word, i + 5)):
                    token.append("var")
                    i += 4          
                elif (getString(word, i, i + 4) == "class") and (isSymbol(word, i + 5)):
                    token.append("class")
                    i += 4             
                elif (getString(word, i, i + 7) == "continue") and (isSymbol(word, i + 8)):
                    token.append("var")
                    i += 7
                elif (getString(word, i, i + 2) == "def") and (isSymbol(word, i + 3)):
                    token.append("def")
                    i += 2                                                                                                                     
                elif (getString(word, i, i + 3) == "elif") and (isSymbol(word, i + 4)):
                    token.append("elif")
                    i += 3
                elif (getString(word, i, i + 3) == "else") and (isSymbol(word, i + 4)):
                    token.append("else")
                    i += 3
                elif (getString(word, i, i + 2) == "for") and (isSymbol(word, i + 3)):
                    token.append("for")
                    i += 2     
                elif (getString(word, i, i + 3) == "from") and (isSymbol(word, i + 4)):
                    token.append("from")
                    i += 3                                                       
                elif (getString(word, i, i + 1) == "if") and (isSymbol(word, i + 2)):
                    token.append("if")
                    i += 1
                elif (getString(word, i, i + 5) == "import") and (isSymbol(word, i + 6)):
                    token.append("import")
                    i += 5                    
                elif (getString(word, i, i + 1) == "in") and (isSymbol(word, i + 2)):
                    token.append("in")
                    i += 1
                elif (getString(word, i, i + 1) == "is") and (isSymbol(word, i + 2)):
                    token.append("opr_log")
                    i += 1           
                elif (getString(word, i, i + 2) == "not") and (isSymbol(word, i + 3)):
                    token.append("not")
                    i += 2          
                elif (getString(word, i, i + 1) == "or") and (isSymbol(word, i + 2)):
                    token.append("or")
                    i += 1  
                elif (getString(word, i, i + 3) == "pass") and (isSymbol(word, i + 4)):
                    token.append("pass")
                    i += 3         
                elif (getString(word, i, i + 4) == "raise") and (isSymbol(word, i + 5)):
                    token.append("raise")
                    i += 4   
                elif (getString(word, i, i + 5) == "return") and (isSymbol(word, i + 6)):
                    token.append("ret")
                    i += 5  
                elif (getString(word, i, i + 4) == "while") and (isSymbol(word, i + 5)):
                    token.append("while")
                    i += 4   
                elif (getString(word, i, i + 3) == "with") and (isSymbol(word, i + 4)):
                    token.append("with")
                    i += 3
                i += 1                                                                                                            
            idx_word += 1
        token.append("nl")

# Final check
if (valid):
    print("Tokenizer succeed!")
    for i in range(len(token)):
        f.write(token[i])
        f.write(" ")
    f.close()
else:
    print("Tokenizer failed!")