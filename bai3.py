def sort_student_reports(report_list):
    # Sắp xếp danh sách báo cáo điểm dựa trên điểm toán và ngữ văn
    return sorted(report_list, key=lambda x: (-x['math'], -x['literature'], report_list.index(x)))

# Danh sách báo cáo điểm đầu vào
input_reports = [{'id': 984, 'math': 9.0, 'literature': 5.4}, {'id': 12, 'math': 9.5, 'literature': 4.3}, {'id': 324, 'math': 9.0, 'literature': 5.4}]

# Sắp xếp danh sách
sorted_reports = sort_student_reports(input_reports)

print(sorted_reports)
