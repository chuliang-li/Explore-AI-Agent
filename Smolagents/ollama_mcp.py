
from smolagents import MCPClient, CodeAgent
from smolagents import tool,LiteLLMModel
from mcp import ClientSession
from mcp.client.sse import sse_client
import json
from dotenv import load_dotenv
import os
# from smolagents import MCPClient, CodeAgent

load_dotenv() 
api_key = os.getenv('AMAP_KEY')

# server_params1 = {"url": "http://127.0.0.1:8000/sse"}
#生成模型实例 这个是智能体的大脑部分
model = LiteLLMModel(
    model_id="ollama_chat/qwen3",
    # model_id="ollama_chat/deepseek-r1:7b",
    api_key="ollama",
    num_ctx=8192
)

AMAP_MCP_URL=f"https://mcp.amap.com/sse?key={api_key}"

# with MCPClient({"url": "http://127.0.0.1:8000/mcp", "transport": "streamable-http"}) as tools:
with MCPClient({"url": AMAP_MCP_URL, "transport": "sse"}) as tools:    
# 初始化 SmolAgent
    agent = CodeAgent(model=model,tools=tools)
   # 使用 SmolAgent 调用本地 Ollama 大模型
# agent.run("9.9 和 9.11, 哪个数字大？",)
# agent.run("丢两次骰子，总点数是多少？",)
    # agent.run("经纬度116，40的天气？",)
    # agent.run("从北京天安门到国贸大厦乘公交工具怎么走？",)
    agent.run("从成都市郫都区万景峰到成都东站乘公交工具怎么走？",)

