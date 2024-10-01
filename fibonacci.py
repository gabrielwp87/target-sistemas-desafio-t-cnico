def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

def is_fibonacci_number(n):
    sequence = fibonacci_sequence(n)
    if n in sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

number = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
result = is_fibonacci_number(number)
print(result)
