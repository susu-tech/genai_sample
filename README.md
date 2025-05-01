# genai_sample

生成 AI 関連の調査用

- 通信
- MCP

## Server-sent events

server-sent events 通信の確認

```sh
cd server-sent-events
flask --app app run
```

## JSON-RPC 2.0

https://www.jsonrpc.org/specification#response_object

JSON-RPC 2.0 通信の確認

### 通常のパターン

```sh
cd json-rpc-2.0

# サーバー起動
python server.py

# 別ターミナルでクライアント起動
python client.py
```

### バッチ処理のパターン

```sh
cd json-rpc-2.0

# サーバー起動
python server.py

# 別ターミナルでクライアント起動
python batch_client.py
```

## WebSocket

WebSocket 通信の確認

```sh
cd websockets

# サーバー起動
python server.py

```

ブラウザで`client.html`を開いて通信確認

## mcp-server

https://modelcontextprotocol.io/quickstart/server#why-claude-for-desktop-and-not-claude-ai

`.vscode/mcp.json`の設定をして vscode agent でツールを利用可能
