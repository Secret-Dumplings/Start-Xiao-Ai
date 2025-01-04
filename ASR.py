# 决定弃用
# from vosk import Model, KaldiRecognizer
# import os
# import wave
# import json
# import subprocess
# import time
# import threading


# # 初始化识别器
# if not os.path.exists(r"C:\ai-model\vosk\vosk-model-cn-0.22"):
#     print(r"Please download the model from https://alphacephei.com/vosk/models/vosk-model-cn-0.22.zip and unpack as 'C:\ai-model\vosk\vosk-model-cn-0.22' in the current folder.")
#     exit(1)

# model = Model(r"C:\ai-model\vosk\vosk-model-cn-0.22")

# with open("prompt_word.txt", "r") as file:
#     content = file.read()
# if content == "":
#     content = "小爱同学"
# # 定义要监听的提示词
# keyword = content

# # 定义要打开的软件的绝对路径
# software_path = r"C:\Users\admin\Desktop\VoiceXiaoai\xiaoai.exe"

# # 定义一个函数来处理语音识别
# def listen_for_keyword(model, keyword, software_path):
#     import pyaudio

#     # 打开麦克风
#     p = pyaudio.PyAudio()
#     stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
#     stream.start_stream()

#     print("请说话...")

#     while True:
#         data = stream.read(4000)
#         if len(data) == 0:
#             break
#         if recognizer.AcceptWaveform(data):
#             result = json.loads(recognizer.Result())
#             if 'text' in result:
#                 text = result['text']
#                 text = text.replace(" ", "")
#                 # print("你说：" + text)
#                 # 检查是否包含特定的提示词
#                 if keyword in text:
#                     print("检测到提示词，正在打开软件...")
#                     # 使用subprocess打开软件
#                     subprocess.Popen(software_path)
#                     # break  # 打开软件后退出循环

#     stream.stop_stream()
#     stream.close()
#     p.terminate()

# # 初始化识别器
# recognizer = KaldiRecognizer(model, 16000)

# # 使用线程来运行监听函数，避免阻塞主程序
# thread = threading.Thread(target=listen_for_keyword, args=(model, keyword, software_path))
# thread.start()
