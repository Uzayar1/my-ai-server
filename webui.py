import gradio as gr
import requests

def chat_with_ai(message, history):
    url = "http://localhost:11434/api/chat" # Generate ကနေ Chat ကို ပြောင်းလိုက်တယ်
    
    # History ကို Ollama နားလည်တဲ့ Format ပြောင်းမယ်
    formatted_history = []
    # System Instruction ကို အမြဲထိပ်ကထားမယ်
    formatted_history.append({"role": "system", "content": "You are a helpful assistant. Always reply in Myanmar (Burmese) language shortly."})
    
    # အရင်ပြောခဲ့တဲ့ စကားတွေကို ထည့်မယ်
    for user_msg, bot_msg in history:
        formatted_history.append({"role": "user", "content": user_msg})
        formatted_history.append({"role": "assistant", "content": bot_msg})
    
    # အခုနောက်ဆုံးမေးတဲ့စကားကို ထည့်မယ်
    formatted_history.append({"role": "user", "content": message})

    payload = {
        "model": "qwen2.5:0.5b",
        "messages": formatted_history,
        "stream": False,
        "options": {
            "num_predict": 100,
            "temperature": 0.5
        }
    }
    
    try:
        response = requests.post(url, json=payload, timeout=60)
        return response.json().get("message", {}).get("content", "နားမလည်ပါဘူး။")
    except Exception as e:
        return "အဖြေထွက်ဖို့ ကြာနေတယ် သားကြီး၊ History တွေ များသွားလို့လား မသိဘူး။"

with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Uzayar1's Memory AI")
    chatbot = gr.Chatbot(height=450)
    with gr.Row():
        msg = gr.Textbox(placeholder="Message Myanmar AI...", show_label=False, scale=9)
        submit = gr.Button("↑", variant="primary", scale=1)

    def respond(message, chat_history):
        # AI ဆီကို message ရော history ရော ပို့လိုက်ပြီ
        bot_message = chat_with_ai(message, chat_history)
        chat_history.append((message, bot_message))
        return "", chat_history

    submit.click(respond, [msg, chatbot], [msg, chatbot])
    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=3000)


