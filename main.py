import cyk
import cfg_to_cnf
import tokenizer


# Membaca kode python lalu mengubahnya menjadi token
token = tokenizer.tokenize("test_code.txt")
token.insert(0, "")

# Membaca CNF
production_array, production_quantity = cyk.read_cnf("cnf.txt")
variable_array, left_idx_array, right_idx_array = cyk.production_position(production_array, production_quantity)

# Memproses token dan cnf
print("Checking...")
table = cyk.cyk_algorithm(variable_array, production_array, production_quantity, token, len(token), left_idx_array, right_idx_array)

# Pengecekan terakhir kemudian menulis pesan
cyk.final_check(production_array, production_quantity, len(token), table)