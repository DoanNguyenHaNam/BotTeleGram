import os
import subprocess
import random
import string
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
import zipfile
def zip_folder_with_password(zip_path, folder_path, password):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.setpassword(password.encode())  # Đặt mật khẩu
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)
TOKEN = "7906415743:AAEsImnrcmbCljBW0jxUOsb2EFJbmIKkcpc"

# Hàm tạo mật khẩu ngẫu nhiên 10 ký tự
def generate_random_password():
    return ''.join(random.choices(string.digits, k=10))

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Lấy Key 🔑", callback_data='get_key')],
        [InlineKeyboardButton("Lấy Mod Skin 🎭", callback_data='get_mod')],
        [InlineKeyboardButton("Tạo File Mod 🛠", callback_data='create_mod')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Chọn chức năng:", reply_markup=reply_markup)

async def button_click(update: Update, context):
    query = update.callback_query
    await query.answer()

    if query.data == 'get_key':
        # Kiểm tra xem có mật khẩu đã lưu không
        if 'password' in context.user_data:
            password = context.user_data['password']
            note_url = f"https://vuotnhanh.com/st?api=a2d839ad-ae1e-455b-8ef4-08d5bc49f403&url=https://downloadmodpmin.blogspot.com/2025/03/lay-key-bot.html#{password}"
            message_text = f'<a href="{note_url}">Lấy key tại đây</a>'  # Tạo liên kết ẩn
            await query.message.reply_text(message_text, parse_mode="HTML")
        else:
            await query.message.reply_text("Bạn chưa tạo file mod nào.")
    elif query.data == 'get_mod':
        await query.message.reply_text("Link lấy mod: https://example.com/mod")
    elif query.data == 'create_mod':
        await query.message.reply_text("Nhập chuỗi số để tạo file mod.")
        context.user_data['awaiting_input'] = True

async def handle_message(update: Update, context):
    print("Nhận được tin nhắn từ người dùng:", update.message.text)
    if context.user_data.get('awaiting_input', False):
        user_input = update.message.text
        print("Chuỗi số nhận được:", user_input)

        # Lấy username của người dùng
        username = update.message.from_user.username
        if not username:
            username = "unknown_user"  # Giá trị mặc định nếu không có username
        print("Username của người dùng:", username)

        # Hiển thị thông báo "Vui lòng đợi"
        await update.message.reply_text("Vui lòng đợi...")

        # Ghi chuỗi số vào file list_mod.txt
        list_mod_path = os.path.join(os.getcwd(), "list_mod.txt")
        print("Đường dẫn file list_mod.txt:", list_mod_path)
        with open(list_mod_path, "w") as file:
            file.write(user_input)
        print("Đã ghi chuỗi số vào file list_mod.txt")

        # Chạy tool main.py trong cùng thư mục và truyền username, user_input làm tham số
        main_script_path = os.path.join(os.getcwd(), "main.py")
        print("Đường dẫn script main.py:", main_script_path)
        result = subprocess.run(
            ["python", main_script_path, username, user_input],  # Truyền username và user_input vào script
            capture_output=True,
            text=True
        )
        print("Kết quả chạy script main.py:")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

        # Tạo mật khẩu ngẫu nhiên
        password = generate_random_password()
        print("Mật khẩu nén file:", password)

        # Tạo tên file .zip theo username
        zip_file_name = f"file_mod/{username}.zip"
        zip_folder_with_password(zip_file_name, f'file_mod/{username}',password)

        # Gửi file zip cho người dùng
        with open(zip_file_name, "rb") as file:
            print("Đang gửi file .zip cho người dùng...")
            await update.message.reply_document(document=file)
            print("Đã gửi file .zip thành công.")

        # Xóa file zip và list_mod.txt sau khi gửi
        os.remove(zip_file_name)
        print("Đã xóa file .zip:", zip_file_name)
        os.remove(list_mod_path)
        print("Đã xóa file list_mod.txt:", list_mod_path)

        # Lưu mật khẩu vào context để sử dụng sau này
        context.user_data['password'] = password

        # Reset trạng thái
        context.user_data['awaiting_input'] = False

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()