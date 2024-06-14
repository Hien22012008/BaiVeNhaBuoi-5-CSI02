def reverse_sorted_array(arr):
    return arr[::-1]

# Dãy số đã được sắp xếp giảm dần
input_array = [90.12, 50.2, 20.0, 3.14159, 0.0, -12.2, -12.2, -1000.0, -99999999.0]

# Đảo ngược dãy số để sắp xếp tăng dần
output_array = reverse_sorted_array(input_array)

print(output_array)