import translator
import dictionary

input_str = input("Введите число: ")
from_ = int(input("Введите систему счисления введенного Вами числа: "))
to_ = int(input("Введите систему счисления, в которую необходимо перевести введенное Вами число: "))
input_str = input_str.upper()

#creating the dictionary for translating
dictionary = dictionary.Dictionary("base.csv", "r", ",")
#creating the translator
translator = translator.Translator(dictionary.get_dictionary(from_), input_str)
if translator.get_collection() == None:
    print("Некорректные данные!")
else:
    print(translator.translate_from_to(from_, to_, translator.get_collection()))
