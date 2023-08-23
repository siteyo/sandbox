# rye

[rye](https://rye-up.com/guide/installation/)

Rust製のPythonパッケージマネージャ。

いじってみる。

## インストール

1. 以下のコマンドを実行

    ```bash
    curl -sSf https://rye-up.com/get | bash
    ```

1. 環境変数を設定

    おためしなので、 `.local` のほうに追加

    ```sh
    echo 'source "$HOME/.rye/env"' >> ~/.zshrc.local
    ```

1. Shellを再起動

    よく見るコマンドを実行

    ```sh
    exec -l $SHELL
    ```

    現在のプロセスで、ログインシェルとして(`-l`)、`$SHELL` を実行する。
    とかそんな感じのコマンドだった気がする。

1. パスが通ってるか確認

    ```sh
    rye --version
    ```

    実行結果はこんな感じ。

    ```sh
    rye 0.11.0
    commit: 0.11.0 (f6f63d6c1 2023-07-18)
    platform: linux (x86_64)
    self-python: cpython@3.11
    symlink support: true
    ```

    パスは通ってそう。

1. アップデート

    ```sh
    rye self update
    ```
