import re

def filter_lines(input_file, output_file, exception_ids):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    filtered_lines = []
    for line in lines:
        match = re.match(r'-->(\d+) :\s*(.*)', line)
        if match:
            skin_id, content = match.groups()
            if content.strip() or skin_id in exception_ids:
                filtered_lines.append(line)
        else:
            filtered_lines.append(line)  # Giữ lại các dòng không phải là dòng skin
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(filtered_lines)

# Danh sách ID ngoại lệ, chỉnh sửa tùy ý
exception_ids = {"59802","59901",'52414','13118','50119'}  # Ví dụ ID ngoại lệ

# Gọi hàm xử lý
filter_lines("id_skinnn.txt", "filtered_output.txt", exception_ids)
