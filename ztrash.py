import os
from collections import defaultdict

# Đường dẫn tới file txt
file_path = "#id_effect.txt"

# Đường dẫn tới thư mục chứa các folder con
main_folder_path = "Pmin_sources/check"

# Đường dẫn tới file lưu kết quả nhóm
output_file_path = "#list_khong_loi.xml"

# Từ điển để lưu các nhóm dòng không tồn tại
grouped_lines = defaultdict(list)

# Đọc file txt
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Duyệt qua từng dòng trong file txt
for line in lines:
    # Lấy 5 ký tự đầu tiên (giả sử các hàng có cấu trúc chuẩn)
    folder_name = line[:5].strip()
    
    # Lấy 3 ký tự đầu tiên để phân nhóm
    group_key = folder_name[:3]
    
    # Đường dẫn tới folder cần kiểm tra
    folder_path = os.path.join(main_folder_path, folder_name)
    
    # Kiểm tra xem folder có tồn tại không
    if not os.path.isdir(folder_path):
        # Thêm cả dòng vào nhóm nếu folder không tồn tại
        grouped_lines[group_key].append(line.strip())

# Ghi các nhóm dòng không tồn tại vào file output
with open(output_file_path, "w", encoding="utf-8") as output_file:
    for group_key, items in sorted(grouped_lines.items()):
        # Ghi tiêu đề nhóm
        output_file.write(f"**{group_key}**\n")
        # Ghi từng dòng trong nhóm
        for item in items:
            output_file.write(f"{item}\n")
        # Thêm dòng trống giữa các nhóm
        output_file.write("\n")

print(f"Dữ liệu đã được phân nhóm và ghi vào file '{output_file_path}'.")

check=input('Có tạo list ko? (Y/N)')
if check == '' or 'y' in check or 'Y' in check:
    import random

    # Đường dẫn tới file phân nhóm
    input_file_path = "#list_khong_loi.xml"

    # Đường dẫn tới file output chứa ID được chọn
    output_file_path = "list_mod.txt"

    # Đọc nội dung file đã phân nhóm
    with open(input_file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Biến để lưu nhóm hiện tại và các ID đã chọn
    current_group = None
    group_items = []
    random_ids = []

    # Duyệt qua từng dòng trong file
    for line in lines:
        line = line.strip()
        if line.startswith("**") and line.endswith("**"):  # Dòng là tiêu đề nhóm
            # Nếu nhóm trước có dữ liệu, chọn ngẫu nhiên 1 ID
            if group_items:
                selected_id = random.choice(group_items)
                random_ids.append(selected_id)
            
            # Cập nhật nhóm hiện tại và reset danh sách nhóm
            current_group = line.strip("**")
            group_items = []
        elif line:  # Dòng là một mục trong nhóm
            # Lấy ID 5 số đầu tiên
            group_items.append(line[:5])

    # Chọn ngẫu nhiên một ID cho nhóm cuối cùng (nếu còn dữ liệu)
    if group_items:
        selected_id = random.choice(group_items)
        random_ids.append(selected_id)

    # Ghi các ID được chọn vào file output
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(random_ids))  # Không để dòng trống cuối file

    # Đếm số lượng ID trong file output
    total_ids = len(random_ids)

    print(f"Các ID ngẫu nhiên đã được chọn và ghi vào file '{output_file_path}'.")
    print(f"Tổng số ID trong file: {total_ids}")
