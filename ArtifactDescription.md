# Artifact Description

## 概要：パスワードの誤入力対応

改変対象となるのはyagmailだ.
yagmailはlinuxでgmailのアドレスからメールを送信できるアプリケーションだ.

* インストール後以下のように使用するgmailアカウントにログインする.

```
yag = yagmail.SMTP('mygmailusername', 'mygmailpassword')
```
sender.pyにSMTPのclassの定義がある.
SMTP内で定義される_loginによってログイン操作が送信される.
ログインに必要なパスワードはhandle_passwordによって入力する.
handle_passwordはpassword.pyで定義される.
handle_passwordでは入力に対しパスワードを設定する.
パスワードが間違っている場合はログインできず,エラーを返す.

* 改変内容
gmailのパスワードは８文字以上であるが,８文字未満のパスワードを入力した場合にパスワードが８文字未満の入力になっていることが分からない.
そのため,password.py内で８文字未満の文字が入力された場合に８文字未満の入力のため通らないというメッセージを返すようにする.

## クイックスタート

* dockerhubからリポジトリをpullする.
```
docker pull michiro0116/2024-a2110032-yagmail
docker run -it --rm --name container michiro0116/2024-a2110032-yagmail
```


## 評価手順

* コンテナ内のテスターを実行する.
```
python3 artifact/yagmail/test_password.py
```
テスターの内容は短いパスワードを数回入力した後に長いパスワードを入力したものである.
　
* 簡単のためkeyringにパスワードを保存しないよう操作する
```
Save username and password in keyring? [y/n]:
```

* 以下のようなログが流れる
```
# python3 artifact/yagmail/test_password.py
password should be over 8 figures
password should be over 8 figures
password should be over 8 figures
Save username and password in keyring? [y/n]: n
Final Password: correctpassword
```
これは8文字以下のパスワードを入力した際にエラーメッセージを返し,十分な長さのパスワードが入力されたらそれが受理されていることを示している.


## 制限と展望

* 改変内容の変更
はじめはEmailの本文が添付ファイルになる問題について改善を試みようと思ったが,技術的にプログラムを改善することが難しかったため簡単な機構の改善しか行えなかった.
docker上の仮想環境での作業に関し理解できない部分やエラー対応に時間を使ってしまい改変に時間をかけることができなかった.
そのため改変内容がかなり初歩的なものになってしまったため,時間があればより高度な内容の改変を行いたい.

## 用途

パスワードは間違った入力がなされても間違った原因が分かりづらいエラーメッセージを返すようになっていたため,その点について改善した.
