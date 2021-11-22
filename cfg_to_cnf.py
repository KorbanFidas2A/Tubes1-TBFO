import sys, itertools

#file berisi grammar / syntax python
variabel = []
file = open('cfg.txt', 'r')

#membaca file tersebut kemudian diubah formatnya menuju format python
terminal = []
bacagrammar = file.readlines()
for i in range(len(bacagrammar)):
    bacagrammar[i] = bacagrammar[i].replace('\n', '')

#prod_res berarti adalah array untuk menampung hasil produksi
prod_res = []
for i in range(len(bacagrammar)):
    if (bacagrammar[i][0] == '#'):
        continue
    left_side = bacagrammar[i].split(' -> ')[0]
    if (left_side[0] >= 'A' and left_side[0] <= 'Z' and left_side not in variabel):
        variabel.append(left_side)
    right_side = bacagrammar[i].split(' -> ')[1].split(' | ')
    for j in range(len(right_side)):
        Terms = right_side[j].split(' ')
        for term in Terms:
            if (term >= 'a' and term <= 'z' and term not in terminal):
                terminal.append(term)
        prod_res.append((left_side, Terms))

#Untuk memulai, mengeliminasi dari yang kanan
if (not 'Sn' in variabel):
    variabel.append('Sn')
    prod_res = [('Sn', [variabel[0]])] + prod_res
# Membuat dictionary untuk terminal dan variabel
#Untuk mengeliminasi aturan yang memiliki Format U -> Xa diganti menjadi 2 variabel, U -> XY kemudian Y->a)
dict = {}

#Untuk mengecek adanya duplikasi
#Misalnya apakah ada A->a yang sudah ada sebelumnya
for product in prod_res:
    if ((product[0] in variabel) and (product[1][0] in terminal) and (len(product[1]) == 1)):
        dict[product[1][0]] = product[0]

prod_res2 = []
#Fungsi untuk membuat sebuah variabel baru -> formatnya
#A[angka] -> (ekspresi)
def create_new_var():
    i = 1
    var = 'A'
    variabel_baru = var.upper() + str(i)
    while (variabel_baru in variabel):
        i = i + 1
        variabel_baru = var.upper() + str(i)
    return variabel_baru


#List untuk menyimpan hasil produksi (prod_res)
for product in prod_res:
    if ((product[0] in variabel) and (product[1][0] in terminal) and (len(product[1]) == 1)):
        prod_res2.append(product)
    else:
        for Terminal in terminal:
            i = 0
            for Term in product[1]:
                if ((Terminal == Term) and (not Terminal in dict)):
                    dict[Terminal] = create_new_var()
                    variabel.append(dict[Terminal])
                    prod_res2.append((dict[Terminal], [Terminal]))
                    product[1][i] = dict[Terminal]
                elif (Terminal == Term):
                    product[1][i] = dict[Terminal]
                i = i + 1
        prod_res2.append((product[0], product[1]))
prod_res = prod_res2

#fungsi untuk mengeliminasi sebelah kanan (Sn -> [sebelah kanan]) yang memiliki terminal lebih dari 2
prod_res2 = []
for product in prod_res:
    if (len(product[1]) <= 2):
        prod_res2.append(product)
    else:
        newvar = create_new_var()
        variabel.append(newvar)
        prod_res2.append((product[0],[product[1][0]] + [newvar]))
        newvar2 = newvar
        newvar3 = create_new_var()
        for i in range(1, len(product[1]) - 2):
            variabel.append(newvar3)
            prod_res2.append((newvar2, [product[1][i], newvar3]))
            newvar2 = newvar3
            newvar3 = create_new_var()
        prod_res2.append((newvar2, product[1][len(product[1])-2:len(product[1])]))
prod_res = prod_res2

#Bagian untuk mengeliminasi unit production
for i in range(500): 
    prod_res2 = []
    elim_unit = []
    for product in prod_res:
        if ((product[0] in variabel) and (product[1][0] in variabel) and (len(product[1]) == 1)):    # (A -> B form)
            elim_unit.append((product[0], product[1][0]))
        else:
            prod_res2.append(product)
    for units in elim_unit:
        for product in prod_res:
            if ((units[1] == product[0]) and (units[0] != product[0])):
                prod_res2.append((units[0], product[1]))
    prod_res = prod_res2

#Membuka file cnf sehingga python akan mengetikkan hasil translasi
file = open('cnf.txt', 'w')
final = []

#Hasil CFG menjadi CNF, Sn (Snew) sebagai S yang baru
prod_res = sorted(prod_res)
for product in prod_res:
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
for product in prod_res:
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

#Note: tidak ada eliminasi menggunakan epsilon
#Pada grammar CFG tidak digunakan epsilon
