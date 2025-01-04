# 小爱同学语音修复项目

本项目实现了语音识别功能，通过监听特定的提示词来触发打开指定软件的操作。同时，提供了一个图形用户界面，允许用户自定义提示词。

## 文件说明
- `ASR.py`: 实现语音识别和软件触发功能。
- `语音集成界面.py`: 提供一个图形用户界面，允许用户输入自定义的提示词，并触发语音识别功能。

## ASR.py 工作流程
1. 加载语音识别模型。
2. 从文件 `prompt_word.txt` 中读取提示词，默认为 "小爱同学"。
3. 定义要打开的软件的绝对路径。
4. 使用 pyaudio 打开麦克风，开始监听语音输入。
5. 实时处理语音数据，识别出文本内容。
6. 如果识别结果中包含提示词，则使用 subprocess 打开指定软件。

## 注意事项
- 确保已下载并解压 vosk-model-cn-0.22 模型到指定路径。
- 需要安装 vosk 和 pyaudio 库，可以使用 `pip install vosk pyaudio` 命令进行安装。

## 语音集成界面.py 工作流程
1. 创建主窗口和相关控件，包括文本输入框、发送按钮和GitHub链接按钮。
2. 用户在文本输入框中输入自定义的提示词。
3. 点击 "确认" 按钮后，将输入的提示词写入文件 `prompt_word.txt`，并导入 ASR 模块启动语音识别功能。
4. 点击 "项目地址" 按钮可以打开项目的GitHub链接。

## 注意事项
- 需要安装 tkinter 库，通常Python自带该库，无需额外安装。

## 使用方法
1. 确保已安装所有依赖库。
2. 下载并解压 vosk-model-cn-0.22 模型到指定路径。
3. 运行 `语音集成界面.py` 文件，启动图形用户界面。
4. 在文本输入框中输入自定义的提示词，点击 "确认" 按钮。
5. 对着麦克风说出提示词，如果识别成功，将自动打开指定的软件。

## 项目维护
- 作者：[[秘密小汤圆](https://github.com/Secret-Dumplings)]
- GitHub链接：[[项目的GitHub链接](https://github.com/Secret-Dumplings/Start-Xiao-Ai)]

## 使用源项目
启动小爱脚本
- GitHub链接：[[项目的GitHub链接](https://github.com/chhc007/OneClickXiaoai)]
- 作者：[[chhc007](https://github.com/chhc007)]

识别模型
[项目的链接](https://alphacephei.com/vosk/models)

  
