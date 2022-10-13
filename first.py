spasibo = [1, 3, 6, 2, 5]
for j in range(0, len(spasibo)): #некая переменная, позволяющая сделать цикл n-1 раз
    for i in range(1, len(spasibo)): #переменная пробегающая все числа в последовательности
        if spasibo[i-1] > spasibo[i]:
            spasibo[i-1], spasibo[i] = spasibo[i], spasibo[i-1]
print(spasibo)