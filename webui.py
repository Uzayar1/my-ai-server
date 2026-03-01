import gradio as gr
import requests

def chat_with_ai(message, history):
    url = "http://localhost:11434/api/generate"
    # AI ကို မြန်မာလို အပီအပြင် ခိုင်းထားတယ်
    prompt_template = f"System: You are a helpful assistant. Always reply in Myanmar (Burmese) language. User: {message}\nAssistant:"
    
    data = {
        "model": "qwen:0.5b",
        "prompt": prompt_template,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        return response.json().get("response", "နားမလည်ပါဘူး။")
    except:
        return "Ollama serve ကို နှိုးထားဖို့ လိုပါတယ် သားကြီး!"

# Gradio 6.0 အတွက် အရှင်းဆုံး Interface
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Uzayar1's Myanmar AI Server")
    gr.ChatInterface(
        fn=chat_with_ai,
        title="Myanmar AI Assistant",
        description="မြန်မာလို မေးမြန်းနိုင်တဲ့ ကိုယ်ပိုင် AI ဖြစ်ပါတယ်။"
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=3000)


