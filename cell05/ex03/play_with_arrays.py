# play_with_arrays.py

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
print(original_array)

# สร้างเซตจากค่าที่ index 1 ถึง 5 แล้วบวก 2
sub_array = original_array[1:6]
new_set = {x + 2 for x in sub_array}
print(new_set)
