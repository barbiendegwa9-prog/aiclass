greeting= {"en": "Hello, World!", "es": "¡Hola, Mundo!", "fr": "Bonjour, le monde!"}
print(greeting)
print(greeting["es"])

keyin = input("Enter a key: ")
valuein = input("Enter a value: ")
greeting[keyin] = valuein
print(greeting)

del greeting["en"]
print(greeting)