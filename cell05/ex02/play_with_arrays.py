original_array = [2, 8, 9, 48, 8, 22, -12, 2]
print(original_array)

sub_array = original_array[1:6]

new_array = [x + 2 for x in sub_array]
print(new_array)
