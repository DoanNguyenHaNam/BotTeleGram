import xml.etree.ElementTree as ET
from lxml import etree
def fix_condition_ids(file_path, output_path):
    """
    Chỉnh sửa các thẻ <Condition> trong file XML sao cho id phù hợp với guid trong các Track.
    
    Args:
        file_path (str): Đường dẫn tới file XML gốc.
        output_path (str): Đường dẫn lưu file XML sau khi chỉnh sửa.
    """
    try:
        # Phân tích tệp XML
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Tạo ánh xạ giữa guid và trackName từ các thẻ <Track>
        guid_to_track_index = {}
        tracks = root.findall(".//Track")
        for index, track in enumerate(tracks):
            guid = track.get("guid")
            if guid:
                guid_to_track_index[guid] = index

        # Chỉnh sửa các thẻ <Condition>
        for condition in root.findall(".//Condition"):
            guid = condition.get("guid")
            if guid in guid_to_track_index:
                condition.set("id", str(guid_to_track_index[guid]))

        # Ghi file XML sau khi chỉnh sửa
        tree.write(output_path, encoding="utf-8", xml_declaration=True)
        print(f"File đã được chỉnh sửa và lưu tại: {output_path}")

    except ET.ParseError as e:
        print(f"Lỗi phân tích XML: {e}")
    except Exception as e:
        print(f"Lỗi khác: {e}")

def fix_broken_xml(file_path, output_path):
    from lxml import etree
    try:
        parser = etree.XMLParser(recover=True)
        tree = etree.parse(file_path, parser)
        tree.write(output_path, pretty_print=True, encoding="utf-8", xml_declaration=True)
    except Exception as e:
        pass

# Đường dẫn file XML đầu vào và đầu ra
input_file=output_file = "Dance_fixed.xml"

# Gọi hàm để chỉnh sửa file
fix_broken_xml(input_file, output_file)
fix_condition_ids(input_file, output_file)
