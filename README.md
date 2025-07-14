# AI Video Sorter

This project helps you automatically and intelligently organize your video files into folders based on anime names or any other category, using Liara's AI models and API.

---

## Prerequisites

- Python 3.8 or higher
- Create an AI model in Liara and obtain the connection info (base_url, api_key, model)
- Install the required package:

```bash
pip install openai
```

---

## Setting Up Your AI Model in Liara

1. Log in to your Liara panel and create an AI service.
2. After creating the model, note the following information:
   - **base_url** (service address)
   - **api_key** (API key)
   - **model** (model name, e.g., `openai/gpt-4o-mini`)

Sample code to connect to your model:

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

Replace `<baseUrl>`, `<LIARA_API_KEY>`, and `<model_name>` with your own values.

---

## Configurable Parameters in OpenAI SDK

- **frequency_penalty**: Number between -2 and 2. Controls repetition of frequent words.
- **logit_bias**: Adjusts the likelihood of specific tokens appearing.
- **n**: Number of responses to generate simultaneously.
- **response_format**: Forces the model to return output in a specific format.
- **seed**: Fixed value for reproducible outputs.
- **stop**: Array of strings; model stops generating when it encounters them.
- **stream**: If true, responses are streamed (useful for real-time or UI).
- **stream_options**: Stream settings (used only if stream: true).
- **temperature**: Number between 0 and 2. Controls randomness/creativity.
- **tool_choice**: Controls when the model calls a Tool (smart/always).
- **tools**: Define a set of Tools the model can use if needed.
- **user**: End-user identifier for better request tracking and abuse prevention.

---

## How to Run and Use the Project

1. Place your video files in a folder. Example:

```
MyVideos/
├── overlordkaguya sama - 01.mkv
├── overlordkaguya sama - 02.mkv
├── konosuba - 01.mp4
├── overlord - 01.mkv
├── overlord - 02.mkv
```

2. Run the `sortvideo.py` script:

```bash
python sortvideo.py
```

3. You will be prompted for:
   - base_url
   - api_key
   - model (if left blank, the default will be used)
   - path to your video folder

4. The script will automatically send the list of videos to the AI model and, based on the response, organize the files into folders named after each anime.

---

## Test Example

Suppose you have the following files:

```
overlordkaguya sama - 01.mkv
overlordkaguya sama - 02.mkv
konosuba - 01.mp4
overlord - 01.mkv
overlord - 02.mkv
```

After running the script, the files will be organized as follows:

```
MyVideos/
├── overlordkaguya sama/
│   ├── overlordkaguya sama - 01.mkv
│   └── overlordkaguya sama - 02.mkv
├── konosuba/
│   └── konosuba - 01.mp4
├── overlord/
│   ├── overlord - 01.mkv
│   └── overlord - 02.mkv
```

---

## Code Overview

- `sortvideo.py`: The main script for sorting videos using AI.
- `AI.py`: Handles communication with the Liara API and sends prompts to the AI model.
- Everything is fully automated; no manual file editing is required.

---

## Additional Notes

- If you enter incorrect model or connection info, the script will fail.
- If you leave the model field blank, the default (`openai/gpt-4o-mini`) will be used.
- For testing, you can use anime names like `overlordkaguya sama`, `konosuba`, and `overlord`.

---

Good luck! 🚀 