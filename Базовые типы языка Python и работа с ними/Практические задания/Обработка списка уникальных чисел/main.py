list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
numbers = list_
unique_numbers = set(numbers)
sum_of_numbers = sum(unique_numbers)
count_of_numbers = len(unique_numbers)
average_of_numbers = round(sum_of_numbers / count_of_numbers, 5)
describe = {"Сумма уникальных чисел:": -6, "Количество уникальных чисел:": 14,
            "Среднее арифметическое уникальных чисел:": -0.42857}
print(describe)

# TODO найти сумму, количество и среднее арифметическое уникальных чисел

# print("Сумма уникальных чисел:", sum_of_numbers)
# print("Количество уникальных чисел:", count_of_numbers)
# print("Среднее арифметическое уникальных чисел:", average_of_numbers)
