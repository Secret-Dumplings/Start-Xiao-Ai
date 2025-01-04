import tkinter as tk
from tkinter import messagebox
import webbrowser

def send_message():
    # 获取用户输入的文本
    entry_content = entry.get()
    print(entry_content)
    with open("prompt_word.txt", "w") as f:
        f.write(entry_content)
    # 这里可以添加其他监听用户输入后的操作
    import ASR

def open_github():
    # 这里替换为您想要打开的GitHub链接
    github_link = "https://github.com/"
    webbrowser.open(github_link)

# 创建主窗口
root = tk.Tk()
root.title("小爱同学语音修复")

# 创建一个文本输入框
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# 创建一个发送按钮，点击时调用send_message函数
send_button = tk.Button(root, text="确认", command=send_message)
send_button.pack()

# 创建一个GitHub链接按钮，点击时调用open_github函数
github_button = tk.Button(root, text="项目地址(我们不会保存您的语音文件欢迎打开github检查)", command=open_github)
github_button.pack(pady=10)

# 运行主循环
root.mainloop()