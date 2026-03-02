import gradio as gr
import requests

def chat_with_ai(message, history):
    url = "http://localhost:11434/api/chat"
    
    # Ollama အတွက် Message History ကို Format အမှန်ပြင်မယ်
    formatted_messages = []
    formatted_messages.append({"role": "system", "content": "You are a helpful assistant. Always reply in Myanmar (Burmese)."})
    
    # Gradio 6.0 ရဲ့ history format ကို Ollama format ပြောင်းခြင်း
    for msg in history:
        # history ထဲက message တစ်ခုချင်းစီမှာ role နဲ့ content ပါရမယ်
        formatted_messages.append({"role": msg['role'], "content": msg['content']})
    
    # အခုလက်ရှိမေးခွန်းကို ထည့်မယ်
    formatted_messages.append({"role": "user", "content": message})

    payload = {
        "model": "qwen2.5:0.5b",
        "messages": formatted_messages,
        "stream": False,
        "options": {"num_predict": 100}
    }
    
    try:
        response = requests.post(url, json=payload, timeout=60)
        bot_response = response.json().get("message", {}).get("content", "နားမလည်ပါဘူး။")
        return bot_response
    except:
        return "Server လေးနေတယ် သားကြီး၊ ခဏစောင့်ပေးပါ။"

# Gradio 6.0 ရဲ့ ChatInterface ကို အသုံးပြုခြင်း
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Uzayar1's Memory AI (Fixed)")
    # type="messages" လို့ ထည့်ပေးမှ Gradio 6.0 မှာ Error မတက်မှာပါ
    gr.ChatInterface(
        fn=chat_with_ai,
        type="messages", 
        title="Myanmar AI Assistant",
        description="စကားပြောမှတ်မိတဲ့ ကိုယ်ပိုင် AI Server ဖြစ်ပါတယ်။"
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=3000)


