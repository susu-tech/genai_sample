# genai_sample

生成 AI 関連の調査用

## server-sent-events

server-sent events 通信の確認用

```sh
cd server-sent-events
flask --app app run
```

## json-rpc-2.0

JSON-RPC 2.0 通信の確認

シンプルな実行

```sh
cd json-rpc-2.0

# サーバー起動
python server.py

# 別ターミナルでクライアント起動
python client.py
```

## mcp-server

https://modelcontextprotocol.io/quickstart/server#why-claude-for-desktop-and-not-claude-ai

`.vscode/mcp.json`の設定をして vscode agent でツールを利用可能
