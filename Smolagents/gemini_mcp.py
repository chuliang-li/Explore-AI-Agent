
from smolagents import MCPClient, CodeAgent
from smolagents import tool,LiteLLMModel
from mcp import ClientSession
from mcp.client.sse import sse_client
import json
from dotenv import load_dotenv
import os

# 步骤一： 加载.env文件的 高德api key和大模型api key
load_dotenv() 
api_key_amap = os.getenv('AMAP_KEY')
api_key_gemini = os.getenv('GEMINI_API_KEY')

# 步骤二： 生成模型实例 这个是智能体的大脑部分
model = LiteLLMModel(
    model_id="gemini/gemini-2.5-flash",
    api_key=api_key_gemini
)

# 高德地图的MCP调用URL
AMAP_MCP_URL=f"https://mcp.amap.com/sse?key={api_key_amap}"

# 步骤三：初始化MCP客户端
# with MCPClient({"url": "http://127.0.0.1:8000/mcp", "transport": "streamable-http"}) as tools:
with MCPClient({"url": AMAP_MCP_URL, "transport": "sse"}) as tools:    

# 步骤四：生成智能体实例
    agent = CodeAgent(model=model,tools=tools)
   
# 步骤五：使用智能体解决问题 
    agent.run("从成都市郫都区万景峰到成都东站乘公交工具怎么走？",)
    # agent.run("9.9 和 9.11, 哪个数字大？",)
    # agent.run("丢两次骰子，总点数是多少？",)
    # agent.run("经纬度116，40的天气？",)
    # agent.run("从北京天安门到国贸大厦乘公交工具怎么走？",)


