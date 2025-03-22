import os
from collections import defaultdict
import random
import json  

history_file = "random_pmin.json"  # File lưu lịch sử random

# Hàm để tải lịch sử random từ file
def load_history():
    if os.path.exists(history_file):
        with open(history_file, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

# Hàm để lưu lịch sử random vào file
def save_history(history):
    with open(history_file, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

random_history = load_history()

file_path = "#id_effect.txt"
main_folder_path = "Pmin_sources/check_loi"
output_file_path = "#list_khong_loi_2.xml"

exception_list =        {   
                                '10615', '10619', '10621', '10910', '10911', '11009', '11202', '11502', '11506', '11633',
                                '12002', '12009', '12308', '13607', '15609', '14112', '14405', '15003', '15005', '15006',
                                '15008', '15010', '15011', '15014', '15033', '15301', '15302', '15303', '15703', '15706',
                                '15711', '16205', '16310', '16608', '16609', '16610', '16906', '17401', '17402', '17403',
                                '17406', '17517', '18712', '19002', '19204', '20602', '50305', '50309', '50603', '51408',
                                '51804', '51810', '51909', '52012', '52107', '52110', '52207', '52808', '53005', '53007',
                                '53510', '54301', '54302', '52111', '11113', '12309', '12310', '11607', '12901', '12903',
                                '12906', '12907', '12908', '12910', '15611', '18702', '11604', '10914', '51002', '15004',
                        }

always_include_list =   {   
                                '15009', '15015', '15012', '15007', '54802', '15710', '54307', '19009', '19007', '19012',
                                '11115', '12912', '15013', '13011', '13116', '19605', '13204', '15412', '14111', '12907',
                                '53702', '53701', '53703', '53704', '16803', '11403', '14002', '50701', '50401', '18006',
                                '59702', '14802', '51101', '10903', '11301', '56801', '56703', '52503', '19202', '18905'
                        }

grouped_lines = defaultdict(list)

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    folder_name = line[:5].strip()
    group_key = folder_name[:3]
    folder_path = os.path.join(main_folder_path, folder_name)
    if folder_name not in exception_list and not os.path.isdir(folder_path):
        grouped_lines[group_key].append(line.strip())

for skin in always_include_list:
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

input_file_path = "#list_khong_loi_2.xml"
output_file_path = "list_mod.txt"

target_count = random.randint(15, 20)  # Chọn ngẫu nhiên số ID từ 15-20

manual_group_keys = ['130','150','141','501','111','132','131']
manual_group_keys = [id.strip() for id in manual_group_keys if id.strip()]

with open(input_file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

current_group = None
grouped_items = defaultdict(list)
for line in lines:
    line = line.strip()
    if line.startswith("**") and line.endswith("**"):
        current_group = line.strip("**")
    elif line:
        grouped_items[current_group].append(line)

random_ids = []
for group_key in manual_group_keys:
    if group_key in grouped_items and grouped_items[group_key]:
        selected_item = random.choice(grouped_items[group_key])
        random_ids.append(selected_item)
        if group_key not in random_history:
            random_history[group_key] = []
        random_history[group_key].append(selected_item)
        del grouped_items[group_key]  # Xóa cả nhóm để không chọn thêm trong cụm 3 số này

remaining_slots = target_count - len(random_ids)
if remaining_slots > 0:
    all_items = [item for group in grouped_items.values() for item in group]
    random.shuffle(all_items)
    auto_selected = all_items[:remaining_slots]
    random_ids.extend(auto_selected)
    for item in auto_selected:
        group_key = item[:3]
        if group_key not in random_history:
            random_history[group_key] = []
        random_history[group_key].append(item)

save_history(random_history)

with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write('160%\n' + "\n".join([item[:5] for item in random_ids]))

total_ids = len(random_ids)
print(f"\nCác ID ngẫu nhiên đã được chọn và ghi vào file '{output_file_path}'.")
print(f"Tổng số ID trong file: {total_ids}")
