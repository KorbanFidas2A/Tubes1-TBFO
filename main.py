import cyk
import cfg_to_cnf
import tokenizer

variabel = []
array_cfg = []

#mengubah CFG menjadi array
array_cfg = cfg_to_cnf.baca_grammar()

#Memisahkan array di sebelah kiri dan kanan
prod_res = []
terminal = []
cfg_to_cnf.pecah_array(array_cfg, variabel, prod_res, terminal)

#menambahkan Sn -> S
prod_res = cfg_to_cnf.addSn(variabel, prod_res)

dict = {}
cfg_to_cnf.add_terminal(dict, prod_res, variabel, terminal)

#mengganti terminal menjadi variabel
prod_res2 = []
prod_res = cfg_to_cnf.change_var(prod_res, prod_res2, variabel, terminal, dict)

#untuk mengeliminasi variabel menjadi 2 variabel, maksimum
prod_res2 = []
prod_res = cfg_to_cnf.eliminate_two_var(prod_res, prod_res2, variabel)

#melakukan unit production elimination
prod_res = cfg_to_cnf.unit_production_elim(prod_res, variabel)

#menulis hasil terjemahan CFG ke CNF dalam txt
cfg_to_cnf.write_to_cnf(prod_res)

# Membaca kode python lalu mengubahnya menjadi token
token = tokenizer.tokenize("test_code.txt")
token_quantity = len(token)
token.insert(0, "")

# Membaca CNF
production_array, production_quantity = cyk.read_cnf("cnf.txt")
variable_array, left_idx_array, right_idx_array = cyk.production_position(production_array, production_quantity)

# Memproses token dan cnf
print("Checking...")
table = cyk.cyk_algorithm(variable_array, production_array, production_quantity, token, token_quantity, left_idx_array, right_idx_array)

# Pengecekan terakhir kemudian menulis pesan
cyk.final_check(production_array, production_quantity, token_quantity, table)
