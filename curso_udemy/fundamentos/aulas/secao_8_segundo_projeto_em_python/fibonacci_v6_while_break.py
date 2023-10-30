# Sequencia fibonacci começa 0, 1 mais a soma do antecessor ex:
# 0 + 1 = 1 -> 1 + 1 -> 2 + 1 = 3, 3 + 2
# 0, 1, 1, 2, 3, 5, 8...

def fibonacci(quantidade=0):
    resultado = [0, 1]
    while True:
        # resultado.append(sum([resultado[-1], resultado[-2]]))
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == "__main__":
    for fib in fibonacci(20):
        print(fib, end=",")
    print("")
