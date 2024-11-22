import sys
import os

def validate_args(args):
    if len(args) < 3:
        return False, "コマンドを指定してください"
    
    command = args[1]
    valid_commands = ["reverse", "copy", "duplicate-contents", "replace-string"]

    if command not in valid_commands:
        return False, f"無効なコマンドです。有効なコマンド: {', '.join(valid_commands)}"

    # 各コマンドの引数の数を確認
    if command == "reverse" or command == "copy":
        if len(args) != 4:
            return False, f"{command}コマンドには入力パスと出力パスが必要です。"
    elif command == "duplicate-contents":
        if len(args) != 4:
            return False, "duplicate-contentsコマンドには入力パスと複製回数が必要です。"
        try:
            n = int(args[3])
            if n < 0:
                return False, "複製回数は正の数である必要があります。"
        except ValueError:
            return False, "複製回数は整数である必要があります。"
    elif command == "replace-string":
        if len(args) != 5:
            return False, "replace-string コマンドには入力パス、検索文字列、置き換える文字列が必要です。"
    
    return True, ""

def reverse_file(input_path, output_path):
    # ファイルの内容を逆順にする
    try:  
        with open(input_path, 'r') as f:
            content = f.read().strip()
        with open(output_path, 'w') as f:
            f.write(content[::-1])
    except IOError as e:
        print(f"エラー: ファイル操作に失敗しました {e}")
        sys.exit(1)

def copy_file(input_path, output_path):
    # ファイルをコピーする
    try:
        with open(input_path, 'r') as f:
            content = f.read()
        with open(output_path, 'w') as f:
            f.write(content)
    except IOError as e:
        print(f"エラー: ファイル操作に失敗しました {e}")
        sys.exit(1)

def duplicate_contents(input_path, n):
    # ファイルの内容をn回複製する
    try:
        with open(input_path, 'r') as f:
            content = f.read()
        with open(input_path, 'w') as f:
            f.write(content * int(n))
    except IOError as e:
        print(f"エラー: ファイル操作に失敗しました {e}")
        sys.exit(1)

def replace_string(input_path, needle, newstring):
    try:
        with open(input_path, 'r') as f:
            content = f.read()
        
        content = content.replace(needle, newstring)

        with open(input_path, 'w') as f:
            f.write(content)
    except IOError as e:
        print(f"エラー: ファイル操作に失敗しました {e}")
        sys.exit(1)
 
def main():
    # 引数の検証
    is_valid, error_massage = validate_args(sys.argv)
    if not is_valid:
        print(f"エラー: {error_massage}")
        sys.exit(1)

    command = sys.argv[1]  

    # 入力ファイルの存在確認
    if command in ["reverse", "copy", "duplicate-contents", "replace-string"]:
        input_path = sys.argv[2]
        if not os.path.exists(input_path):
            print(f"エラー: '{input_path}'が存在しません")
            sys.exit(1)


    # コマンドの実行
    if command == "reverse":
        reverse_file(sys.argv[2], sys.argv[3])
    elif command == "copy":
        copy_file(sys.argv[2], sys.argv[3])
    elif command == "duplicate-contents":
        duplicate_contents(sys.argv[2], sys.argv[3])
    elif command == "replace-string":
        replace_string(sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == "__main__":
    main()
    