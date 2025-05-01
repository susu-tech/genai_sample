# genai_sample

生成 AI 関連の技術について調査したサンプルコードをまとめています。

- 通信
- MCP

## 通信

### 概要

Server-Sent Events（SSE）と WebSocket は、通信チャネルの構築・維持を担う通信プロトコル。

| 特徴                               | Server-Sent Events (SSE)                 | WebSocket                                      |
| ---------------------------------- | ---------------------------------------- | ---------------------------------------------- |
| **通信の方向**                     | サーバー → クライアントのみ（単方向）    | 双方向（クライアント ↔ サーバー）              |
| **接続方式**                       | HTTP（`text/event-stream`）              | 独自の WebSocket プロトコル                    |
| **ブラウザ対応**                   | 幅広く対応（IE 除く）                    | モダンブラウザ対応（モバイルも OK）            |
| **再接続の自動処理**               | ブラウザが自動再接続対応あり             | 明示的に実装が必要                             |
| **プロキシ・ファイアウォール対応** | HTTP ベースなので通りやすい              | 独自プロトコルなのでブロックされることも       |
| **実装の手軽さ**                   | 非常にシンプル（JavaScript で簡単）      | 若干複雑（ライブラリやハンドシェイク処理必要） |
| **データ送信形式**                 | UTF-8 テキストのみ                       | バイナリも送信可能（音声・画像など）           |
| **典型的な用途**                   | ニュースフィード、通知、チャート更新など | チャット、ゲーム、株価、IoT など               |

JSON-RPC と REST API はアプリケーションレベルのデータの意味や処理レベルの API 設計プロトコル。

| 特徴               | JSON-RPC                               | REST API                          |
| ------------------ | -------------------------------------- | --------------------------------- |
| 通信方式           | JSON over HTTP or WebSocket            | HTTP（GET/POST/PUT/DELETE）       |
| データ形式         | JSON                                   | JSON（通常）、XML も可能          |
| メソッドの概念     | 明示的なメソッド呼び出し（"method"）   | HTTP メソッドで動作を表現         |
| リソース指向       | ×（関数呼び出しのような RPC スタイル） | ○（リソースを URL で表現）        |
| ステートレス性     | △（設計次第）                          | ○（原則としてステートレス）       |
| バッチリクエスト   | ○（複数のリクエストを一括送信可能）    | ×（通常は 1 リクエスト＝ 1 操作） |
| WebSocket との相性 | ○（双方向通信がしやすい）              | △（基本は HTTP のみ）             |

### Server-sent events

server-sent events 通信の確認

```sh
cd server-sent-events
flask --app app run
```

### WebSocket

WebSocket 通信の確認

```sh
cd websockets

# サーバー起動
python server.py

```

ブラウザで`client.html`を開いて通信確認

### JSON-RPC 2.0

REST API

https://www.jsonrpc.org/specification#response_object

JSON-RPC 2.0 通信の確認

#### 通常のパターン

```sh
cd json-rpc-2.0

# サーバー起動
python server.py

# 別ターミナルでクライアント起動
python client.py
```

#### バッチ処理のパターン

```sh
cd json-rpc-2.0

# サーバー起動
python server.py

# 別ターミナルでクライアント起動
python batch_client.py
```

#### WebSocket 利用のパターン

```sh
# サーバーを起動
python json-rpc-2.0/websocket_server.py

# クライアントからリクエスト
python json-rpc-2.0/websocket_client.py
```

## MCP

## MCP Server

https://modelcontextprotocol.io/quickstart/server#why-claude-for-desktop-and-not-claude-ai

`.vscode/mcp.json`の設定をして vscode agent でツールを利用可能
