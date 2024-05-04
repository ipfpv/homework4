immutable_var = 4, "flower", [3, 5]
print(immutable_var)
immutable_var[1] = "cold"
print(immutable_var)

# Кортеж задумывался так, чтобы сохраненные данные оставались неизменными.
# Но, если внутри кортежа создать список, можно изменить его содержимое immutable_var[2][0] = 4

mutable_list = 5, "apple", [4, 5]
mutable_list[2][1] = 10
print(mutable_list)