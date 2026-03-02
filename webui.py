import gradio as gr
import requests

# AI အဖြေထုတ်ပေးမယ့်အပိုင်း
def chat_with_ai(message, history):
    url = "http://localhost:11434/api/generate"
    # AI ကို မြန်မာလိုပဲ အပီအပြင်ဖြေဖို့ ခိုင်းထားတယ်
    payload = {
        "model": "qwen:0.5b",
        "system": "You are a helpful assistant. Always reply in Myanmar (Burmese) language clearly and politely.",
        "prompt": message,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload)
        return response.json().get("response", "နားမလည်ပါဘူးခင်ဗျာ။")
    except:
        return "Server Error: Ollama serve ကို နှိုးထားပါ သားကြီး!"

# ပုံထဲကလို ChatGPT Style Interface (Open WebUI Look)
with gr.Blocks(theme=gr.themes.Default(primary_hue="blue", spacing_size="sm", radius_size="lg")) as demo:
    with gr.Column(elem_id="container"):
        gr.Markdown(f"# 🤖 Hello, Zayar Linn")
        gr.Markdown("### How can I help you today?")
        
        chatbot = gr.Chatbot(label="Myanmar AI Chat", height=500, show_label=False)
        
        with gr.Row():
            msg = gr.Textbox(
                placeholder="Message Myanmar AI...",
                show_label=False,
                scale=9
            )
            submit = gr.Button("↑", variant="primary", scale=1)

        # ဥပမာ မေးခွန်းလေးများ (Suggested Ideas)
        with gr.Row():
            gr.Examples(
                examples=["Give me ideas", "Overcome procrastination", "Tell me a fun fact"],
                inputs=msg,
                label="Suggested"
            )

    # ခလုတ်နှိပ်ရင် အလုပ်လုပ်ဖို့ ချိတ်ဆက်ခြင်း
    submit.click(chat_with_ai, [msg, chatbot], [chatbot])
    msg.submit(chat_with_ai, [msg, chatbot], [chatbot])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=3000)


