# mujin 磁石サーバ
商品棚での扉の開閉を確認するためのサーバ  

# 要件
git  
Docker  

# 使い方
1. このリポジトリをローカルに落とす  
``` .sourceCode .shell
$ git clone https://github.com/white0221/mujin-face.git
```  

2. イメージのビルド
``` .sourceCode .shell
$ docker build -t mujin-face .
```  

3. コンテナ立ち上げ  
``` .sourceCode .shell
$ docker run -it -v $(pwd):/app -p 5000:5000 mujin-face python app.py
```  

4. ローカルホストに接続  
ブラウザから[localhost:5000](http://localhost:5000)に接続する
