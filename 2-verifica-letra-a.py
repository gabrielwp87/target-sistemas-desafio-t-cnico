def verify_letter_a(string):
    qtd = string.lower().count('a')
    
    if qtd > 0:
        return f"A letra 'a' aparece {qtd} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

text = input("Informe uma string para verificar a presença da letra 'a': ")
result = verify_letter_a(text)
print(result)
