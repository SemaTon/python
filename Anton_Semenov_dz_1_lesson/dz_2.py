list_odd_numbers = [i ** 3 + 17 for i in range(1000) if i % 2 != 0]

print(list_odd_numbers)

for i in range(len(list_odd_numbers)):
    str_numders = str(list_odd_numbers[i])
    list_numbers = list(str_numders)

    #print(list_numbers)
    for i in range(len(list_numbers)):
         list_numbers[i] = int(list_numbers[i])
    sum_numbers = sum(list_numbers) + 17


    print(sum_numbers)