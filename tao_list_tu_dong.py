import os
from collections import defaultdict
import random
import json

history_file = "random_history.json"

# Hàm tải lịch sử
def load_history():
    if os.path.exists(history_file):
        with open(history_file, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

# Hàm lưu lịch sử
def save_history(history):
    with open(history_file, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

# Hàm kiểm tra file _back.xml tồn tại trong thư mục con
def check_back_file_exists(id_value, search_path):
    for root, _, files in os.walk(search_path):
        for variant in ["_back.xml", "_Back.xml", "_BACK.xml"]:
            if f"{id_value}{variant}" in files:
                return True
    return False

# Tải lịch sử random
random_history = load_history()

file_path = "#id_effect.txt"
main_folder_path = "pmin_sources/check"
search_path = "pmin_sources/Resources/1.57.1/ages/Prefab_Characters/Prefab_Hero"
output_file_path = "#list_khong_loi.xml"

exception_list =    {   '10615', '10619', '10621', '10910', '10911', '11009', '11202', '11502', '11506', '11633',
                        '12002', '12009', '12308', '13607', '15609', '14112', '14405', '15003', '15005', '15006',
                        '15008', '15010', '15011', '15014', '15033', '15301', '15302', '15303', '15703', '15706',
                        '15711', '16205', '16310', '16608', '16609', '16610', '16906', '17401', '17402', '17403',
                        '17406', '17517', '18712', '19002', '19204', '20602', '50305', '50309', '50603', '51408',
                        '51804', '51810', '51909', '52012', '52107', '52110', '52207', '52808', '53005', '53007',
                        '53510', '54301', '54302', '52111', '11113', '12309', '12310', '11607', '12901', '12903',
                        '12906', '12907', '12908', '12910', '15611', '18702', '11604', '10914', '51002', '15004',
                        '10713', '12406', '18714', 
                    }

pass_id =           {   
                        '15009', '15015', '15012', '15007', '54802', '15710', '54307', '19009', '19007', '19012',
                        '11115', '12912', '15013', '13011', '13116', '19605', '13204', '15412', '14111', '12907',
                        '53702', '53701', '53703', '53704', '16803', '11403', '14002', '50701', '50401', '18006',
                        '59702', '14802', '51101', '10903', '11301', '56801', '56703', '52503', '19202', '18905',
                        '59802', '20601'
                    }


grouped_lines = defaultdict(list)

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    id_value = line[:5].strip()
    group_key = id_value[:3]
    folder_path = os.path.join(main_folder_path, id_value)
    
    if id_value in exception_list:
        continue  # Bỏ qua nếu ID nằm trong danh sách ngoại lệ
    
    if os.path.isdir(folder_path):
        continue  # Bỏ qua nếu thư mục tồn tại trong `pmin_sources/check`
    
    if check_back_file_exists(id_value, search_path):
        continue  # Bỏ qua nếu tìm thấy file _back.xml trong thư mục con
    
    grouped_lines[group_key].append(line.strip())

# Thêm các ID luôn phải có vào nhóm tương ứng
for skin in pass_id:
    group_key = skin[:3]
    if skin not in grouped_lines[group_key]:
        grouped_lines[group_key].append(skin)

with open(output_file_path, "w", encoding="utf-8") as output_file:
    for group_key, items in sorted(grouped_lines.items()):
        output_file.write(f"**{group_key}**\n")
        for item in items:
            output_file.write(f"{item}\n")
        output_file.write("\n")

print(f"Dữ liệu đã được phân nhóm và ghi vào file '{output_file_path}'.")

check = ''
if check == '' or 'y' in check or 'Y' in check:
    input_file_path = "#list_khong_loi.xml"
    output_file_path = "list_mod.txt"

    with open(input_file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    current_group = None
    group_items = []
    random_ids = []

    print("\nCác ID được chọn ngẫu nhiên kèm tên:")
    for line in lines:
        line = line.strip()
        if line.startswith("**") and line.endswith("**"):
            if group_items:
                # Kiểm tra lịch sử của group
                if current_group not in random_history:
                    random_history[current_group] = []

                # Lọc các ID chưa được random
                remaining_items = [item for item in group_items if item not in random_history[current_group]]

                if not remaining_items:  # Nếu tất cả ID đã random, reset group
                    random_history[current_group] = []
                    remaining_items = group_items

                selected_item = random.choice(remaining_items)
                random_ids.append(selected_item)
                random_history[current_group].append(selected_item)
                print(f"Nhóm: {current_group} - ID: {selected_item[:5]} - Tên: {selected_item}")

            current_group = line.strip("**")
            group_items = []
        elif line:
            group_items.append(line)

    if group_items:
        if current_group not in random_history:
            random_history[current_group] = []

        remaining_items = [item for item in group_items if item not in random_history[current_group]]

        if not remaining_items:
            random_history[current_group] = []
            remaining_items = group_items

        selected_item = random.choice(remaining_items)
        random_ids.append(selected_item)
        random_history[current_group].append(selected_item)
        print(f"Nhóm: {current_group} - ID: {selected_item[:5]} - Tên: {selected_item}")

    # Lưu lại lịch sử random
    save_history(random_history)

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write('160%\n'+"\n".join([item[:5] for item in random_ids]))

    total_ids = len(random_ids)

    print(f"\nCác ID ngẫu nhiên đã được chọn và ghi vào file '{output_file_path}'.")
    print(f"Tổng số ID trong file: {total_ids}")
