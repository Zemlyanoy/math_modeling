# Функция ord переводит символы в их ASCII коды
# А функция chr производит обратную операцию
 
text = "Hello"
 
for symbol in text:
    print(ord(symbol), end="; ")
print()
 
codes = [119, 111, 114, 108, 100]
symbols = ""
 
for code in codes:
    symbols += chr(code)
 
print(symbols) 

	
# Списковые включения - listcomp - на выходе получаем список
# (хранит в себе все значения сразу):
symbols = 'Python'
symbol_codes = [ord(symbol) for symbol in symbols]
print(symbol_codes) # Список
 
# Генераторные выражения - genexp - на выходе получаем
# объект-генератор (вычисляет значения по порядку):
symbols = 'Snake'
symbol_codes = (ord(symbol) for symbol in symbols)
print(symbol_codes) # Объект-генератор
 
for object in symbol_codes:
    print(object) 