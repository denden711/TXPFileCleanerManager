import os
import re
from tkinter import Tk, filedialog, messagebox

def get_txp_numbers(directory):
    """
    指定されたディレクトリ内の .txp ファイルの番号を取得します。
    
    Parameters:
        directory (str): ディレクトリのパス。
        
    Returns:
        set: .txp ファイルの番号のセット。
    """
    try:
        txp_files = [f for f in os.listdir(directory) if f.endswith('.txp')]
        txp_numbers = set()
        pattern = re.compile(r"x=(\d+)\.txp")
        
        for f in txp_files:
            match = pattern.match(f)
            if match:
                txp_numbers.add(int(match.group(1)))
        
        return txp_numbers
    except FileNotFoundError:
        raise Exception(f"ディレクトリ '{directory}' が見つかりません。")
    except Exception as e:
        raise Exception(f"ファイル番号の取得中にエラーが発生しました: {str(e)}")

def delete_files(path, keep_numbers, log_file):
    """
    指定されたディレクトリ内のファイルを削除し、結果をログファイルに記録します。
    
    Parameters:
        path (str): ディレクトリのパス。
        keep_numbers (set): 保持するファイルの番号のセット。
        log_file (file): ログファイルオブジェクト。
    """
    try:
        pattern = re.compile(r"x=(\d+)\.pl3")
        deleted_files = []

        for filename in os.listdir(path):
            match = pattern.match(filename)
            if match:
                file_number = int(match.group(1))
                if file_number not in keep_numbers:
                    file_path = os.path.join(path, filename)
                    os.remove(file_path)
                    deleted_files.append(file_path)
                    log_file.write(f"Deleted: {file_path}\n")
        
        if deleted_files:
            messagebox.showinfo("完了", f"削除されたファイルはログファイルに記録されました。")
        else:
            messagebox.showinfo("完了", "指定された数字以外のファイルは見つかりませんでした。")
    except FileNotFoundError:
        raise Exception(f"ディレクトリ '{path}' が見つかりません。")
    except PermissionError:
        raise Exception(f"ディレクトリ '{path}' にアクセスできません。権限を確認してください。")
    except Exception as e:
        raise Exception(f"ファイル削除中にエラーが発生しました: {str(e)}")

def select_directory(prompt):
    """
    ディレクトリを選択するための関数。
    
    Parameters:
        prompt (str): ダイアログに表示するプロンプトメッセージ。
        
    Returns:
        str: 選択されたディレクトリのパス。選択されなかった場合は例外を投げる。
    """
    directory = filedialog.askdirectory(title=prompt)
    if not directory:
        raise Exception(f"{prompt} が選択されていません。")
    return directory

def main():
    root = Tk()
    root.withdraw()  # メインウィンドウを非表示にします

    try:
        # ディレクトリの選択
        directory_x0 = select_directory("1つ目のディレクトリを選択してください")
        directory_x2 = select_directory("2つ目のディレクトリを選択してください")

        # .txp ファイルの番号を取得
        txp_numbers_x0 = get_txp_numbers(directory_x0)
        txp_numbers_x2 = get_txp_numbers(directory_x2)

        # 共通する番号を抽出
        common_numbers = txp_numbers_x0.intersection(txp_numbers_x2)

        # 結果をテキストファイルに出力
        output_file = 'common_txp_numbers.txt'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"1つ目のディレクトリ: {directory_x0}\n")
            f.write(f"2つ目のディレクトリ: {directory_x2}\n\n")
            f.write(f"1つ目のディレクトリ と 2つ目のディレクトリ の両方に存在する .txp ファイルの番号:\n")
            for number in sorted(common_numbers):
                f.write(f"{number}\n")

        # 結果を表示
        print(f"1つ目のディレクトリ と 2つ目のディレクトリ の両方に存在する .txp ファイルの番号: {sorted(common_numbers)}")
        print(f"結果は {output_file} に保存されました。")

        # ログファイルを作成
        log_file_path = 'deleted_files.log'
        with open(log_file_path, 'w', encoding='utf-8') as log_file:
            log_file.write(f"1つ目のディレクトリ: {directory_x0}\n")
            log_file.write(f"2つ目のディレクトリ: {directory_x2}\n\n")
            log_file.write(f"1つ目のディレクトリ と 2つ目のディレクトリ の両方に存在する .txp ファイルの番号:\n")
            for number in sorted(common_numbers):
                log_file.write(f"{number}\n")
            log_file.write("\n削除されたファイル:\n")

            # 削除を行うディレクトリを選択
            delete_directory1 = select_directory("削除を行う最初のディレクトリを選択してください")
            delete_files(delete_directory1, common_numbers, log_file)

            delete_directory2 = select_directory("削除を行う二つ目のディレクトリを選択してください")
            delete_files(delete_directory2, common_numbers, log_file)

        # 結果を表示
        print(f"削除されたファイルは {log_file_path} に記録されました。")

    except Exception as e:
        messagebox.showerror("エラー", f"処理中にエラーが発生しました: {str(e)}")

if __name__ == "__main__":
    main()
