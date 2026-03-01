import gradio as gr
import requests
import json

def chat_with_ai(message, history):
    url = "http://localhost:11434/api/generate"
    # AI ကို မြန်မာလိုပဲ အတင်းဖြေခိုင်းတဲ့ ရှယ် Instruction
    payload = {
        "model": "qwen:0.5b",
        "system": "You are a Myanmar AI. You MUST always reply in Myanmar (Burmese) language only. မင်းက မြန်မာ AI ဖြစ်တယ်၊ အမြဲတမ်း မြန်မာလိုပဲ ဖြေရမယ်။",
        "prompt": message,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "num_predict": 150 # အဖြေမြန်အောင် စာလုံးရေ ကန့်သတ်ထားတယ်
        }
    }
    
    try:
        response = requests.post(url, json=payload)
        return response.json().get("response", "နားမလည်ပါဘူး။")
    except:
        return "Server Error: Ollama serve ကို နှိုးထားလား ပြန်စစ်ပါ သားကြီး!"

# Website Interface အလန်းစား (မနက်က UI ပုံစံမျိုး)
with gr.Blocks(theme=gr.themes.Soft(primary_hue="orange", secondary_hue="blue")) as demo:
    gr.Markdown("# 🇲🇲 Uzayar1's Professional AI Server")
    gr.ChatInterface(
        fn=chat_with_ai,
        title="Myanmar Intelligence",
        description="ကိုယ်ပိုင် Offline Server ကြီး ဖြစ်ပါတယ်။ အမြဲတမ်း မြန်မာလိုပဲ ပြန်ဖြေပေးမှာပါ။",
        examples=["နေကောင်းလား?", "ဒီနေ့ ဘာသတင်းထူးလဲ?", "Python အကြောင်း ရှင်းပြပါ"],
        cache_examples=False
    )

if __name__ == "__main__":
    # Server ကို Port 3000 မှာ တရားဝင် ဖွင့်ပြီ
    demo.launch(server_name="0.0.0.0", server_port=3000)


