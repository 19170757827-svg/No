from flask import Flask,request,jsonify
import requests
import os

app = Flask(__name__)
NOTION_TOKEN = os.environ.get("NOTION_API_KEY")
NOTION_API = "https://api.notion.com/v1"
HEADERS = {
    "Authorization":f"Bearer {NOTION_TOKEN}",
    "Notion‑Version":"2022‑06‑28",
    "Content‑Type":"application/json"
}

@app.route("/mcp/notion/search",methods=["POST"])
def search_page():
    body=request.get_json()
    res=requests.post(f"{NOTION_API}/search",headers=HEADERS,json=body)
    return jsonify(res.json())

@app.route("/mcp/notion/page/<page_id>",methods=["GET"])
def get_page(page_id):
    res=requests.get(f"{NOTION_API}/pages/{page_id}",headers=HEADERS)
    return jsonify(res.json())

@app.route("/mcp/notion/block/<block_id>",methods=["GET"])
def get_block(block_id):
    res=requests.get(f"{NOTION_API}/blocks/{block_id}/children",headers=HEADERS)
    return jsonify(res.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT",10000)))
