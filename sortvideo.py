import os
import shutil
import json
import re
from AI import OpenAI_API

# دریافت اطلاعات API از کاربر
base_url = input("لطفاً base_url را وارد کنید: ").strip()
api_key = input("لطفاً api_key را وارد کنید: ").strip()
model = input("لطفاً مدل را وارد کنید (مثلاً openai/gpt-4o-mini): ").strip()

# 📁 آدرس پوشه فایل‌های ویدیو
VIDEO_FOLDER = input("مسیر پوشه ویدیوها: ").strip()

# 📂 فرمت‌های قابل شناسایی ویدیو
VIDEO_EXTENSIONS = [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"]


def sanitize_folder_name(name):
    """تبدیل نام پوشه به فرمت قابل قبول ویندوز"""
    # حذف کاراکترهای غیرمجاز
    invalid_chars = r'[<>:"/\\|?*]'
    sanitized = re.sub(invalid_chars, ' - ', name)
    
    # حذف فاصله‌های اضافی
    sanitized = re.sub(r'\s+', ' ', sanitized).strip()
    
    # حذف نقطه و فاصله از ابتدا و انتها
    sanitized = sanitized.strip('. ')
    
    return sanitized


def get_video_files(folder):
    return [f for f in os.listdir(folder) if any(f.lower().endswith(ext) for ext in VIDEO_EXTENSIONS)]


def generate_prompt(files):
    prompt = "🧠 لطفاً فایل‌های زیر را بر اساس اسم انیمه به صورت مناسب گروه‌بندی کن(هر انیمه باید توی پوشه ای به اسم خود انیمه باشه):\n\n"
    for filename in files:
        prompt += f"- {filename}\n"
    prompt += ("\n\n🎯 فرمت خروجی پیشنهادی (JSON):\n"
               "{\n"
               '  "نام دسته 1": ["filename1.mkv", "filename2.mkv"],\n'
               '  "نام دسته 2": ["filename3.mkv"]\n'
               "}\n\n"
               "👇 لطفاً همین پایین دسته‌بندی رو وارد کن:\n\n")
    return prompt


def parse_ai_response(response):
    # تلاش برای پیدا کردن اولین بخش JSON در پاسخ
    try:
        json_start = response.find('{')
        json_end = response.rfind('}') + 1
        json_str = response[json_start:json_end]
        mapping = json.loads(json_str)
        return mapping
    except Exception as e:
        print("❌ خطا در خواندن دسته‌بندی JSON از پاسخ AI:", e)
        return None


def move_files_by_category(mapping, base_folder):
    for category, files in mapping.items():
        # تبدیل نام پوشه به فرمت قابل قبول
        safe_category_name = sanitize_folder_name(category)
        folder_path = os.path.join(base_folder, safe_category_name)
        
        print(f"📁 ایجاد پوشه: {safe_category_name}")
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            src = os.path.join(base_folder, file)
            dst = os.path.join(folder_path, file)

            if os.path.exists(src):
                shutil.move(src, dst)
                print(f"📦 انتقال {file} به {safe_category_name}")
            else:
                print(f"⚠️ فایل یافت نشد: {file}")


def main():
    files = get_video_files(VIDEO_FOLDER)
    if not files:
        print("❌ هیچ فایل ویدیویی یافت نشد.")
        return

    prompt = generate_prompt(files)
    print("\n⏳ ارسال پرامپت به هوش مصنوعی...")
    ai_response = OpenAI_API(
        base_url=base_url,
        api_key=api_key,
        model=model,
        content=prompt
    )
    mapping = parse_ai_response(ai_response)
    if mapping:
        move_files_by_category(mapping, VIDEO_FOLDER)
        print("\n✅ فایل‌ها با موفقیت جابه‌جا شدند.")
    else:
        print("\n❌ دسته‌بندی معتبر پیدا نشد. لطفاً پاسخ AI را بررسی کن.")


if __name__ == "__main__":
    main()
