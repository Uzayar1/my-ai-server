import gradio as gr
import requests

def chat_with_ai(message, history):
    url = "http://localhost:11434/api/generate"
    # AI ကို မြန်မာလိုပဲ တိတိကျကျ ဖြေခိုင်းတဲ့ ညွှန်ကြားချက်
    prompt_template = f"System: မင်းက မြန်မာလို ကျွမ်းကျင်စွာ ပြောနိုင်တဲ့ AI ဖြစ်တယ်။ အမြဲတမ်း မြန်မာလိုပဲ ဖြေပါ။\nUser: {message}\nAI:"
    
    data = {
        "model": "qwen:0.5b",
        "prompt": prompt_template,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        # AI ရဲ့ အဖြေကို ပြန်ထုတ်ပေးမယ်
        return response.json().get("response", "နားမလည်ပါဘူးခင်ဗျာ။")
    except:
        return "Ollama Server ကို နှိုးဖို့ လိုအပ်နေပါတယ် သားကြီး!"

# မနက်ကလို Chat Box အလန်းစားလေး
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🤖 Uzayar1's Myanmar AI Server")
    gr.ChatInterface(
        fn=chat_with_ai,
        title="Myanmar AI Assistant",
        description="မြန်မာလို မေးမြန်းနိုင်တဲ့ ကိုယ်ပိုင် AI Server ဖြစ်ပါတယ်။",
        examples=["နေကောင်းလား?", "Coding အကြောင်း ပြောပြပါ", "သူဌေး ဘယ်လိုဖြစ်ရမလဲ?"],
        clear_btn="အကုန်ဖျက်မယ်",
        undo_btn="နောက်ဆုတ်မယ်"
    )

if __name__ == "__main__":
    # Server ကို Port 3000 မှာ ဖွင့်မယ်
    demo.launch(server_name="0.0.0.0", server_port=3000)


