import sys, itertools


def baca_grammar():
    """ 
    Mengubah CFG menjadi array

    """
    file = open('cfg.txt', 'r')
    bacagrammar = file.readlines()
    for i in range(len(bacagrammar)):
        bacagrammar[i] = bacagrammar[i].replace('\n', '')
    return bacagrammar

def add_terminal(dictionary, hasilprod, var, terms):
    """
    Membuat hash table untuk mengakses terminal menggunakan dictionary
    
    """
    for product in hasilprod:
        if ((product[0] in var) and (product[1][0] in terms) and (len(product[1]) == 1)):
            dictionary[product[1][0]] = product[0]


def pecah_array(bacagrammar, var, hasilprod, terms):
    """
    Memisahkan array di sebelah kiri dan kanan

    """
    for i in range(len(bacagrammar)):
        if (bacagrammar[i][0] == '#'):
            continue
        left_side = bacagrammar[i].split(' -> ')[0]
        if (left_side[0] >= 'A' and left_side[0] <= 'Z' and left_side not in var):
            var.append(left_side)
        right_side = bacagrammar[i].split(' -> ')[1].split(' | ')
        for j in range(len(right_side)):
            Terms = right_side[j].split(' ')
            for term in Terms:
                if (term >= 'a' and term <= 'z'):
                    if(term not in terms):
                        terms.append(term)
            hasilprod.append((left_side, Terms))

def unit_production_elim(hasilprod, var):
    """
    melakukan unit production elimination

    """
    for i in range(500): 
        prod_res2 = []
        elim_unit = []
        for product in hasilprod:
            if ((product[0] in var) and (product[1][0] in var) and (len(product[1]) == 1)):
                elim_unit.append((product[0], product[1][0]))
            else:
                prod_res2.append(product)
        for units in elim_unit:
            for product in hasilprod:
                if ((units[1] == product[0]) and (units[0] != product[0])):
                    prod_res2.append((units[0], product[1]))
        hasilprod = prod_res2
    return hasilprod

def addSn(var, hasilprod):
    """
    menambahkan Sn -> S
    """
    if (not 'Sn' in var):
        var.append('Sn')
        hasilprod = [('Sn', [var[0]])] + hasilprod
    return hasilprod


def create_new_var(var2):
    """
    Membuat variabel baru

    """
    i = 1
    var = 'A'
    variabel_baru = var.upper() + str(i)
    while (variabel_baru in var2):
        i = i + 1
        variabel_baru = var.upper() + str(i)
    return variabel_baru


def write_to_cnf(hasilprod):
    """
    menulis hasil terjemahan CFG ke CNF dalam txt

    """
    file = open('cnfdummy.txt', 'w')
    final = []

    hasilprod = sorted(hasilprod)
    for product in hasilprod:
        if (product[0] == 'Sn'):
            if (product[0] in final):
                if (len(product[1]) == 1):
                    file.write(' | ' + product[1][0])
                else:
                    file.write(' | ' + product[1][0] + ' ' + product[1][1])
            else:
                if (product == 'Sn'):
                    file.write('\n')
                final.append(product[0])
                file.write(product[0] + ' -> ')
                if (len(product[1]) == 1):
                    file.write(product[1][0])
                else:
                    file.write(product[1][0] + ' ' + product[1][1])
    for product in hasilprod:
        if (product[0] != 'Sn'):
            if (product[0] in final):
                if (len(product[1]) == 1):
                    file.write(' | ' + product[1][0])
                else:
                    file.write(' | ' + product[1][0] + ' ' + product[1][1])
            else:
                if (product != 'Sn'):
                    file.write('\n')
                final.append(product[0])
                file.write(product[0] + ' -> ')
                if (len(product[1]) == 1):
                    file.write(product[1][0])
                else:
                    file.write(product[1][0] + ' ' + product[1][1])

def change_var(hasilprod, newprod, var, term, dictionary):
    """
    mengganti terminal menjadi variabel

    """
    for product in hasilprod:
        if ((product[0] in var) and (product[1][0] in term) and (len(product[1]) == 1)):
            newprod.append(product)
        else:
            for Terminal in term:
                i = 0
                for Term in product[1]:
                    if ((Terminal == Term) and (not Terminal in dictionary)):
                        dictionary[Terminal] = create_new_var(var)
                        var.append(dictionary[Terminal])
                        newprod.append((dictionary[Terminal], [Terminal]))
                        product[1][i] = dictionary[Terminal]
                    elif (Terminal == Term):
                        product[1][i] = dictionary[Terminal]
                    i = i + 1
            newprod.append((product[0], product[1]))
    return newprod

def eliminate_two_var(hasilprod, newprod, var):
    """
    untuk mengeliminasi variabel menjadi 2 variabel, maksimum

    """
    for product in hasilprod:
        if (len(product[1]) <= 2):
            newprod.append(product)
        else:
            newvar = create_new_var(var)
            var.append(newvar)
            newprod.append((product[0],[product[1][0]] + [newvar]))
            newvar2 = newvar
            newvar3 = create_new_var(var)
            for i in range(1, len(product[1]) - 2):
                var.append(newvar3)
                newprod.append((newvar2, [product[1][i], newvar3]))
                newvar2 = newvar3
                newvar3 = create_new_var(var)
            newprod.append((newvar2, product[1][len(product[1])-2:len(product[1])]))
    return newprod
