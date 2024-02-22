number_list = [3, 4, 1, 6, 7, 3, 10]

new_list = []

for number in number_list:
    if number not in new_list:
        new_list.append(number)

print(new_list)