# 使用官方的 Python 运行时作为父镜像
FROM python:3.9-slim

# 设置工作目录在容器内
WORKDIR /app

# 将当前目录内容复制到位于 /app 的容器中
COPY . /app

# 使用 pip 命令安装 requirements.txt 中列出的所有依赖
RUN pip install --no-cache-dir -r requirements.txt

# 让容器监听 80 端口
EXPOSE 80

# 定义环境变量
ENV NAME=World

# 运行你的 FastAPI 应用
# 假设你的 FastAPI 应用入口点是 main.py 中的 Uvicorn 服务器
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]