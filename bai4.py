def merge_sorted_arrays(arr1, arr2):
    # Khởi tạo các chỉ số cho hai mảng và mảng kết quả
    i = j = 0
    merged_array = []
    
    # Lặp qua cả hai mảng để nhập chúng
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    
    # Thêm phần còn lại của mỗi mảng vào mảng kết quả
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])
    
    return merged_array

# Hai mảng đã được sắp xếp tăng dần
arr1 = [-99999999.0, -12.2, 0.0, 20.0, 50.2, 90.12]
arr2 = [-1000.0, -12.2, 3.14159]

# Gọi hàm để nhập hai mảng
result_array = merge_sorted_arrays(arr1, arr2)

print(result_array)
