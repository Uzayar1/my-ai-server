import gradio as gr
import requests

def chat_with_ai(message, history):
    url = "http://localhost:11434/api/generate"
    # ဖုန်း RAM အတွက် အကိုက်ညီဆုံးဖြစ်အောင် qwen:0.5b ကို သုံးထားတယ်
    prompt_template = f"System: မင်းက မြန်မာလို ကျွမ်းကျင်တဲ့ AI ဖြစ်တယ်။ မြန်မာလိုပဲ ဖြေပါ။\nUser: {message}\nAI:"
    
    data = {
        "model": "qwen:0.5b",
        "prompt": prompt_template,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        return response.json().get("response", "နားမလည်ပါဘူး။")
    except:
        return "Server ချိတ်ဆက်မှု မရပါဘူး။ ollama serve ကို စစ်ပေးပါ။"

# Version 6.0 မှာ ခလုတ်တွေကို မထည့်ဘဲ Default အတိုင်းထားတာက Error ကင်းဆုံးပါ
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Uzayar1's Private AI Server")
    gr.ChatInterface(
        fn=chat_with_ai,
        title="Myanmar AI Assistant",
        description="Uzayar1 ရဲ့ ကိုယ်ပိုင် Offline AI Server ဖြစ်ပါတယ်။"
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=3000)


