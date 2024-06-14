import math

def sort_complex_numbers(complex_list):
        # Sắp xếp danh sách số phức dựa trên modulo của chúng
        return sorted(complex_list, key = lambda z: math.sqrt(z[0]**2 + z[1]**2))

# Danh sách số phức đầu vào
input_complex = [(32.4, -30.0), (2.57, -2.3), (-111.0, 20.2), (34.5, 20.0), (8.97, -13.2), (6.67, 12.2), (9.09, 12.0)]

# Sắp xếp danh sách
sorted_complex = sort_complex_numbers(input_complex)

print(sorted_complex)