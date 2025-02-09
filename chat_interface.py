import random
import gradio as gr
from analysis_agents import agents_response

def chat_response(message, history):
    return agents_response(message)

demo = gr.ChatInterface(chat_response, type="messages", autofocus=False)

if __name__ == "__main__":
    demo.launch()