# TXPFileCleanerManager

## 概要
`TXPFileCleanerManager` は、指定されたディレクトリ内の `.txp` および `.pl3` ファイルを管理し、不要なファイルを自動的に削除するツールです。このプログラムは、複数のディレクトリを比較して共通のファイルを抽出し、それ以外のファイルを削除することで、ディレクトリの整理を効率的に行います。

## 特徴
- 指定されたディレクトリ内の `.txp` ファイルの番号を取得します。
- 複数のディレクトリを比較し、共通する `.txp` ファイル番号を特定します。
- 共通する `.txp` ファイル以外の `.pl3` ファイルを削除し、削除結果をログファイルに記録します。
- 削除操作の結果は、GUIメッセージボックスで通知されます。

## 必要条件
- Python 3.x
- `Tkinter` (GUIのための標準Pythonライブラリ)

## インストール
`TXPFileCleanerManager` はPythonスクリプトとして提供されます。以下の手順でインストールおよび使用できます。

1. リポジトリからソースコードをクローンまたはダウンロードします。
2. 必要に応じて、Pythonの仮想環境を作成し、アクティベートします。
3. スクリプトを実行するために、次のコマンドを使用します:

   ```bash
   python txp_file_cleaner_manager.py
   ```

## 使用方法
1. スクリプトを実行すると、まず最初に2つのディレクトリを選択するように求められます。それぞれのディレクトリに含まれる `.txp` ファイルの番号が取得されます。
2. 両方のディレクトリに共通する `.txp` ファイル番号が特定され、そのリストが出力されます。
3. 次に、不要な `.pl3` ファイルを削除するためのディレクトリを選択します。
4. 削除が完了すると、削除されたファイルの一覧がログファイルに記録されます。また、GUIメッセージボックスを通じて結果が通知されます。

## ファイル構造
- `txp_file_cleaner_manager.py`: メインのPythonスクリプトファイル。
- `common_txp_numbers.txt`: 共通する `.txp` ファイル番号のリストを記録したファイル。
- `deleted_files.log`: 削除されたファイルを記録したログファイル。

## 注意事項
- このプログラムは、指定されたディレクトリ内の `.pl3` ファイルを削除します。削除されたファイルは元に戻せませんので、使用前にバックアップを作成することを強くお勧めします。