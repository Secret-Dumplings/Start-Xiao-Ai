import tkinter as tk
from tkinter import messagebox
import webbrowser
import threading
import pyaudio
from vosk import Model, KaldiRecognizer
import os
import wave
import json
import subprocess
import time

# 初始化识别器
def initialize_recognizer():
    if not os.path.exists(r"C:\ai-model\vosk\vosk-model-cn-0.22"):
        print(
            r"Please download the model from https://alphacephei.com/vosk/models/vosk-model-cn-0.22.zip and unpack as 'C:\ai-model\vosk\vosk-model-cn-0.22' in the current folder.")
        exit(1)
    model = Model(r"C:\ai-model\vosk\vosk-model-cn-0.22")
    return model

# 定义要监听的提示词
def get_keyword():
    with open("prompt_word.txt", "r") as file:
        content = file.read()
    if content == "":
        content = "小爱同学"
    return content

# 定义要打开的软件的绝对路径
software_path = r"C:\Users\admin\Desktop\VoiceXiaoai\xiaoai.exe"

# 定义一个函数来处理语音识别
def listen_for_keyword(model, keyword, software_path):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()
    recognizer = KaldiRecognizer(model, 16000)

    print("请说话...")

    try:
        while True:
            data = stream.read(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                if 'text' in result:
                    text = result['text']
                    text = text.replace(" ", "")
                    # 检查是否包含特定的提示词
                    if keyword in text:
                        print("检测到提示词，正在打开软件...")
                        # 使用subprocess打开软件
                        subprocess.Popen(software_path)
                        # break  # 打开软件后退出循环
    except OSError as e:
        if e.errno == -9981:  # Input overflowed
            print("Input overflowed, resetting stream...")
            stream.stop_stream()
            stream.close()
            stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
            stream.start_stream()
        else:
            raise  # 重新抛出其他异常
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

# 创建主窗口
root = tk.Tk()
root.title("小爱同学语音修复")

# 创建一个文本输入框
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# 创建一个发送按钮，点击时调用send_message函数
def send_message():
    # 获取用户输入的文本
    entry_content = entry.get()
    print(entry_content)
    with open("prompt_word.txt", "w") as f:
        f.write(entry_content)
    # 这里可以添加其他监听用户输入后的操作
    model = initialize_recognizer()
    keyword = get_keyword()
    thread = threading.Thread(target=listen_for_keyword, args=(model, keyword, software_path))
    thread.start()

send_button = tk.Button(root, text="确认", command=send_message)
send_button.pack()

# 创建一个GitHub链接按钮，点击时调用open_github函数
def open_github():
    # 这里替换为您想要打开的GitHub链接
    github_link = "https://github.com/Secret-Dumplings/Start-Xiao-Ai"
    webbrowser.open(github_link)

github_button = tk.Button(root, text="项目地址(我们不会保存您的语音文件欢迎打开github检查)", command=open_github)
github_button.pack(pady=10)

# 运行主循环
root.mainloop()