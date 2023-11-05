import gradio as gr
from helpers.chatter import EmbeddingChatbot
import pandas as pd
import openai


bot = EmbeddingChatbot(
    embeddings_path='data/embeddings.csv',
    api_key="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",
    model='text-davinci-003',
    temperature=0.7,
    stream=True
    )

def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})


    response = bot.answer_question(history_openai_format)
    print(response)

#    partial_message = ""
#    for chunk in response:
#        if len(chunk['choices'][0]['delta']) != 0:
#            partial_message = partial_message + chunk['choices'][0]['delta']['content']
#            yield partial_message

gr.ChatInterface(predict).queue().launch()