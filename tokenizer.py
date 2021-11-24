""" 
File: tokenizer.py

File berisi fungsi-fungsi yang dibutuhkan untuk mengubah kode python
menjadi token dalam bentuk array of string.
"""

import sys

# Inisiasi huruf, angka, dan simbol
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
number = "1234567890"
symbol = "+-*/%{}()[]!#^|~&=,:"


def isLetter(x):
    """ 
    Fungsi mengembalikan True jika x merupakan huruf.
    """
    if x in letter:
        return True
    else:
        return False


def isNumber(x):
    """ 
    Fungsi mengembalikan True jika x merupakan angka.
    """
    
    if x in number:
        return True
    else:
        return False


def isSymbol(x):
    """ 
    Fungsi mengembalikan True jika x merupakan simbol.
    """
    
    if x in symbol:
        return True
    else:
        return False


def getChar(str, idx):
    """ 
    Fungsi mengembalikan char index tertentu dalam sebuah string.
    """

    if (idx < len(str)):
        return str[idx]
    else:
        return "~"


def getString(str, idx_x, idx_y):
    """ 
    Fungsi mengembalikan substring dalam dalam rentang index tertentu dalam string.
    """
    
    subStr = ""
    for i in range(idx_x, idx_y + 1):
        if (i < len(str)):
            subStr = subStr + str[i]
        else:
            return "~"
    return subStr


def nextWord(line, idx_word):
    """ 
    Fungsi mengembalikan kata selanjutnya dalam sebuah line of words.
    """
    
    idx_nextWord = 0
    for word in line:
        if (idx_nextWord == idx_word + 1):
            return word
        idx_nextWord += 1


def tokenize(python_filename):
    """ 
    Fungsi mengembalikan array of string berisi token dari 
    kode python yang dimasukkan nama filenya pada parameter.
    
    Contoh:
    print("hello world")
    diubah menjadi token menjadi
    ['v', 'o', 'v', 'v', 'c', 'n']    
    """
    
    # Inisiasi awal
    token = []
    idx_line = 0
    valid = True
    comment = False

    # Proses
    with open(python_filename, "r", encoding="utf8") as py_file:
        # Pisah menjadi per baris
        lines = py_file.read().splitlines()

        # Menambahkan delimiter di setiap akhir line
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
                    # Komen
                    if (getString(word, i, i + 2) == "'''") and not(comment):
                        comment = True
                        i += 3
                        continue
                    elif (getString(word, i, i + 2) == "'''") and (comment):
                        comment = False
                        i += 3
                        continue
                    if (comment):
                        i += 1
                        continue
                    # Operand and Symbols
                    if (getChar(word, i) == "~") and (i < len(word)):
                        token.append("a")                
                    if (getChar(word, i) == "#"):
                        out = True
                        break
                    elif (getChar(word, i) == "("):
                        token.append("o")
                    elif (getChar(word, i) == ")"):
                        token.append("c")
                    elif (getChar(word, i) == "."):
                        token.append("dot")
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
                            token.append("con")
                        else:
                            valid = False
                            print("Tokenizer failed!")
                            print("Unclosed '[' in line", idx_line)
                            sys.exit()
                    elif (getChar(word, i) == "]"):
                        valid = False
                        print("Tokenizer failed!")
                        print("Overtyped ']' found in line", idx_line)
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
                            token.append("con")
                        else:
                            valid = False
                            print("Tokenizer failed!")
                            print("Unclosed '{' found in line", idx_line)
                            sys.exit()
                    elif (getChar(word, i) == "}"):
                        valid = False
                        print("Tokenizer failed!")
                        print("Overtyped '}' found in line", idx_line)
                        sys.exit()                     
                    elif (getString(word, i, i + 1) == "->") and isSymbol(getChar(word, i + 2)):
                        word = nextWord(line, idx_word)
                        i = 0
                        while not(isSymbol(getChar(word, i + 1))):
                            i += 1
                        i -= 1
                    elif (getChar(word, i) == "<") or (getChar(word, i) == ">"):
                        token.append("l")
                    elif ((getChar(word, i) == "=") and (getChar(word, i + 1) == "=")) or ((getChar(word, i) == "<") and (getChar(word, i + 1) == "=")) or ((getChar(word, i) == ">") and (getChar(word, i + 1) == "=")) or ((getChar(word, i) == "!") and (getChar(word, i + 1) == "=")):                
                        token.append("l")
                        i += 1
                    elif (getChar(word, i) == ":"):
                        token.append("co")
                    elif (getChar(word, i) == ","):
                        token.append("com")
                    elif (getChar(word, i) == "="):
                        token.append("e")
                    elif (getChar(word, i) == "/") or (getChar(word, i) == "*") or (getChar(word, i) == "+") or (getChar(word, i) == "-") or (getChar(word, i) == "%") or (getChar(word, i) == "|") or (getChar(word, i) == "&"):
                        token.append("a")
                    elif ((getChar(word, i) == "/") and (getChar(word, i + 1) == "/")) or ((getChar(word, i) == "*") and (getChar(word, i + 1) == "*")):
                        token.append("a")
                        i += 1
                    elif (getChar(word, i) == "\\"):
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
                            print("Unclosed string found in line", idx_line)
                            sys.exit()
                        else:
                            token.append("con")                  
                    # Keywords
                    elif (getString(word, i, i + 4) == "False") and (isSymbol(getChar(word, i + 5))):
                        token.append("f")
                        i += 4
                    elif (getString(word, i, i + 3) == "True") and (isSymbol(getChar(word, i + 4))):
                        token.append("t")
                        i += 3
                    elif (getString(word, i, i + 3) == "None") and (isSymbol(getChar(word, i + 4))):
                        token.append("con")
                        i += 3
                    elif (getString(word, i, i + 2) == "and") and (isSymbol(getChar(word, i + 3))):
                        token.append("an")
                        i += 2
                    elif (getString(word, i, i + 1) == "as") and (isSymbol(getChar(word, i + 2))):
                        token.append("as")
                        i += 1
                    elif (getString(word, i, i + 4) == "break") and (isSymbol(getChar(word, i + 5))):
                        token.append("v")
                        i += 4          
                    elif (getString(word, i, i + 4) == "class") and (isSymbol(getChar(word, i + 5))):
                        token.append("cl")
                        i += 4             
                    elif (getString(word, i, i + 7) == "continue") and (isSymbol(getChar(word, i + 8))):
                        token.append("v")
                        i += 7
                    elif (getString(word, i, i + 2) == "def") and (isSymbol(getChar(word, i + 3))):
                        token.append("d")
                        i += 2                                                                                                                     
                    elif (getString(word, i, i + 3) == "elif") and (isSymbol(getChar(word, i + 4))):
                        token.append("e")
                        i += 3
                    elif (getString(word, i, i + 3) == "else") and (isSymbol(getChar(word, i + 4))):
                        token.append("el")
                        i += 3
                    elif (getString(word, i, i + 2) == "for") and (isSymbol(getChar(word, i + 3))):
                        token.append("fo")
                        i += 2     
                    elif (getString(word, i, i + 3) == "from") and (isSymbol(getChar(word, i + 4))):
                        token.append("fr")
                        i += 3                                                       
                    elif (getString(word, i, i + 1) == "if") and (isSymbol(getChar(word, i + 2))):
                        token.append("i")
                        i += 1
                    elif (getString(word, i, i + 5) == "import") and (isSymbol(getChar(word, i + 6))):
                        token.append("im")
                        i += 5                    
                    elif (getString(word, i, i + 1) == "in") and (isSymbol(getChar(word, i + 2))):
                        token.append("in")
                        i += 1
                    elif (getString(word, i, i + 1) == "is") and (isSymbol(getChar(word, i + 2))):
                        token.append("l")
                        i += 1           
                    elif (getString(word, i, i + 2) == "not") and (isSymbol(getChar(word, i + 3))):
                        token.append("not")
                        i += 2          
                    elif (getString(word, i, i + 1) == "or") and (isSymbol(getChar(word, i + 2))):
                        token.append("or")
                        i += 1  
                    elif (getString(word, i, i + 3) == "pass") and (isSymbol(getChar(word, i + 4))):
                        token.append("p")
                        i += 3         
                    elif (getString(word, i, i + 4) == "raise") and (isSymbol(getChar(word, i + 5))):
                        token.append("rai")
                        i += 4   
                    elif (getString(word, i, i + 5) == "return") and (isSymbol(getChar(word, i + 6))):
                        token.append("r")
                        i += 5  
                    elif (getString(word, i, i + 4) == "while") and (isSymbol(getChar(word, i + 5))):
                        token.append("w")
                        i += 4   
                    elif (getString(word, i, i + 3) == "with") and (isSymbol(getChar(word, i + 4))):
                        token.append("wi")
                        i += 3  
                    # Letter
                    elif (isLetter(getChar(word, i))):
                        while ((getChar(word, i) != "~") and (isLetter(getChar(word, i))) or (isNumber(getChar(word, i))) or (getChar(word, i) == "_")):
                            i += 1
                        i -= 1
                        if (len(token) > 2) and (token[len(token) - 1] == "dot") and (token[len(token) - 2] == "con") and (token[len(token) - 3] == "con"):
                            token.pop()
                            token.pop()
                            token.pop()
                        elif (len(token) > 1) and (token[len(token) - 1] == "dot") and (token[len(token) - 2] == "con"):
                            token.pop()
                            token.pop()
                        elif (len(token) > 0) and (token[len(token) - 1] == "dot"):
                            token.pop()
                        else:
                            token.append("v")
                    # Number
                    elif (isNumber(getChar(word, i))):
                        count_number = 1
                        while (isNumber(getChar(word, i))):
                            count_number += 1 
                            i += 1
                            if (isLetter(getChar(word, i)) and (getChar(word, i - count_number) != "\"")): 
                                print("Tokenizer failed!")
                                print("Variable unaccepted in line", idx_line)
                                sys.exit()
                        i -= 1
                        token.append("con")         
                    i += 1                                                                                                   
                idx_word += 1
                
            token.append("n")

    # Cek kurung
    count_kurung = 0
    idx_line = 1
    token_awal = token[0]
    for i in range(len(token)):
        if (token[i] == "o"):
            count_kurung += 1
        elif (token[i] == "c"):
            count_kurung -= 1
        elif (token[i] == "n"):
            if (count_kurung > 0):
                print("Tokenizer failed!")
                print("Unclosed '(' found in line", idx_line)
                sys.exit()
            elif (count_kurung < 0):
                print("Tokenizer failed!")
                print("Overtyped ')' found in line", idx_line)
                sys.exit()
            if (i != 0) and (token[i - 1] != "co") and ((token_awal == "d") or (token_awal == "i") or (token_awal == "e") or (token_awal == "el") or (token_awal == "wi") or (token_awal == "cl") or (token_awal == "fo") or (token_awal == "w")):
                print("Tokenizer failed!")
                print("':' found missing in line", idx_line)
                sys.exit()
            idx_line += 1
            if (i != len(token) - 1):
                token_awal = token[i + 1]

    # Final check
    if (valid):
        print("Tokenizer succeed!")
        return token