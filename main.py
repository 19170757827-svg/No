import os
from fastmcp import FastMCP
import requests

mcp = FastMCP("Notion")
NOTION_TOKEN = os.environ.get("NOTION_API_KEY")
NOTION_API = "https://api.notion.com/v1"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion‑Version": "2022‑06‑28",
    "Content‑Type": "application/json"
}

@mcp.tool()
def notion_search(query:str):
    """搜索Notion页面"""
    res = requests.post(f"{NOTION_API}/search",headers=HEADERS,json={"query":query})
    return res.json()

@mcp.tool()
def notion_get_page(page_id:str):
    """获取指定页面内容"""
    res = requests.get(f"{NOTION_API}/pages/{page_id}",headers=HEADERS)
    return res.json()

if __name__ == "__main__":
    port=int(os.environ.get("PORT",8000))
    mcp.run(transport='streamable‑http',host="0.0.0.0",port=port)
