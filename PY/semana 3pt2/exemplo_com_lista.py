sinal = [29.2, 29.3, 29.4, 29.2, 29.2, 29.2, 29.3, 29.2, 29.1, 29.4, 29.2, 29.1, 29.1, 29.2, 29.1, 29.1, 29.2, 29.2, 29.0, 29.1, 29.1, 29.1, 29.2, 29.1, 29.0, 29.2, 29.2, 29.0, 29.2, 29.4, 29.3, 29.3, 29.3, 29.5, 29.4, 29.4, 29.5, 29.5, 29.5, 29.5, 29.5, 29.5, 29.6, 29.5, 29.6, 29.7, 29.7, 29.7, 29.8, 29.8, 29.8, 29.9, 29.8, 29.9, 29.9, 29.9, 29.9, 29.9, 30.0, 30.0, 30.0, 30.1, 30.2, 30.1, 30.1, 30.3, 30.2, 30.2, 30.3, 30.3, 30.3, 30.3, 30.3, 30.3, 30.3, 30.3, 30.3, 30.4, 30.4, 30.3, 30.3, 30.3, 30.4, 30.3, 30.3, 30.3, 30.4, 30.3, 30.3, 30.3, 30.4, 30.3, 30.3, 30.4, 30.3, 30.3, 30.3, 30.3, 30.3, 30.2, 30.3, 30.3, 30.3, 30.2, 30.2, 30.2, 30.2, 30.2, 30.2, 30.2, 30.2, 30.2, 30.1, 30.1, 30.2, 30.0, 30.0, 30.1, 30.0, 30.0, 30.0, 30.1, 30.0, 29.9, 30.0, 30.0, 30.0, 30.1, 30.0, 29.9, 30.0, 30.0, 30.0, 29.9, 30.0, 29.9, 29.9, 30.0, 30.0, 30.0, 29.9, 29.9, 30.1, 29.9, 30.0, 29.9, 30.0, 30.0, 29.9, 30.0, 30.1]

soma = [(x + y)/2 for x, y in zip(sinal[::2], sinal[1::2])]
print(soma)