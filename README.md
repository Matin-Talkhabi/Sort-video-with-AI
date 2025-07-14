# AI Video Sorter

این پروژه به شما کمک می‌کند فایل‌های ویدیویی خود را به صورت خودکار و هوشمند بر اساس نام انیمه یا دسته‌بندی دلخواه، مرتب و پوشه‌بندی کنید. این کار با کمک مدل‌های هوش مصنوعی لیارا و API آن انجام می‌شود.

---

## پیش‌نیازها

- پایتون ۳.۸ یا بالاتر
- ساخت یک مدل هوش مصنوعی در لیارا و دریافت اطلاعات اتصال (base_url، api_key، model)
- نصب پکیج مورد نیاز:

```bash
pip install openai
```

---

## راه‌اندازی مدل هوش مصنوعی در لیارا

۱. وارد پنل لیارا شوید و یک سرویس هوش مصنوعی ایجاد کنید.
۲. پس از ساخت مدل، اطلاعات زیر را یادداشت کنید:
   - **base_url** (آدرس سرویس)
   - **api_key** (کلید API)
   - **model** (نام مدل، مثلاً: `openai/gpt-4o-mini`)

نمونه کد اتصال به مدل:

```python
from openai import OpenAI

client = OpenAI(
  base_url="<baseUrl>",
  api_key="<LIARA_API_KEY>",
)

completion = client.chat.completions.create(
  model="<model_name>",
  messages=[
    {
      "role": "user",
      "content": 'Hello!'
    }
  ]
)

print(completion.choices[0].message.content)
```

در کد بالا، `<baseUrl>`، `<LIARA_API_KEY>` و `<model_name>` را با مقادیر خود جایگزین کنید.

---

## پارامترهای قابل تنظیم در OpenAI SDK

- **frequency_penalty**: عددی بین -2 تا 2. کنترل تکرار کلمات.
- **logit_bias**: تغییر احتمال ظاهر شدن توکن‌های خاص.
- **n**: تعداد پاسخ‌های همزمان.
- **response_format**: فرمت خروجی خاص.
- **seed**: مقدار ثابت برای تکرارپذیری.
- **stop**: آرایه‌ای از رشته‌ها برای توقف پاسخ.
- **stream**: فعال‌سازی حالت استریم.
- **stream_options**: تنظیمات حالت استریم.
- **temperature**: عددی بین 0 تا 2. کنترل خلاقیت.
- **tool_choice**: تعیین زمان فراخوانی Tool.
- **tools**: تعریف Toolهای قابل استفاده.
- **user**: شناسه کاربر نهایی.

---

## نحوه اجرا و استفاده از پروژه

۱. فایل‌های ویدیویی خود را در یک پوشه قرار دهید. مثال:

```
MyVideos/
├── kaguya sama love is war - 01.mkv
├── kaguya sama love is war - 02.mkv
├── konosuba - 01.mp4
├── overlord - 01.mkv
├── overlord - 02.mkv
```

۲. اسکریپت `sortvideo.py` را اجرا کنید:

```bash
python sortvideo.py
```

۳. اطلاعات زیر از شما پرسیده می‌شود:
   - base_url
   - api_key
   - model (در صورت خالی گذاشتن، مقدار پیش‌فرض استفاده می‌شود)
   - مسیر پوشه ویدیوها

۴. اسکریپت به صورت خودکار لیست ویدیوها را به مدل هوش مصنوعی می‌فرستد و بر اساس پاسخ، فایل‌ها را در پوشه‌هایی با نام هر انیمه مرتب می‌کند.

---

## مثال تستی

فرض کنید فایل‌های زیر را دارید:

```
kaguya sama love is war - 01.mkv
kaguya sama love is war - 02.mkv
konosuba - 01.mp4
overlord - 01.mkv
overlord - 02.mkv
```

پس از اجرا، فایل‌ها به صورت زیر مرتب می‌شوند:

```
MyVideos/
├── kaguya sama love is war/
│   ├── kaguya sama love is war - 01.mkv
│   └── kaguya sama love is war - 02.mkv
├── konosuba/
│   └── konosuba - 01.mp4
├── overlord/
│   ├── overlord - 01.mkv
│   └── overlord - 02.mkv
```

---

## توضیحات کد

- `sortvideo.py`: اسکریپت اصلی برای مرتب‌سازی ویدیوها با کمک هوش مصنوعی.
- `AI.py`: ماژول ارتباط با API لیارا و ارسال پرامپت به مدل هوش مصنوعی.
- همه چیز به صورت اتوماتیک انجام می‌شود و نیازی به ویرایش دستی فایل‌ها نیست.

---

## نکات تکمیلی

- اگر مدل یا اطلاعات اتصال را اشتباه وارد کنید، اسکریپت خطا می‌دهد.
- اگر مقدار مدل را خالی بگذارید، مقدار پیش‌فرض (`openai/gpt-4o-mini`) استفاده می‌شود.
- برای تست، می‌توانید از نام انیمه‌های `kaguya sama love is war`، `konosuba` و `overlord` استفاده کنید.

---

موفق باشید! 🚀 