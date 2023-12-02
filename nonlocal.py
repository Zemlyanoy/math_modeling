	
# nonlocal - позволяет локально изменять переменные,
# находящиеся предшествующей локальной области видимости
 
counter = 0
 
def create_scope(default):
    counter = default * 2
 
    def nonlocal_print():
        nonlocal counter
        print(f"scoped {counter = }")
 
    def global_print():
        global counter
        print(f"global {counter = }")
 
    nonlocal_print()
    global_print()
 
create_scope(-4) 

	
# * - оператор распаковки кортежей
 
def compress(*values):
    return values
 
 
result = compress(1, 5, 7, 8, 9)
print("Compressed:", result)
 
 
def extract(value):
    print("Extracted: ", *value)
 
 1234555A@mayIstarBucksVVIIxbcbxgenreHe🌖i
extract(result) 