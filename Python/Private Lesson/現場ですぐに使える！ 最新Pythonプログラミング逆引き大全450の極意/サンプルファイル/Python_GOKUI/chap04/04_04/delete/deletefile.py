import os, shutil

def delete_file():
    """指定されたフォルダー内の特定の拡張子のファイルを削除する
    """
    # フォルダーのパスを取得
    path = input('フォルダーのパスを入力してください >')
    # 削除するファイルの拡張子を取得
    extension = input('削除するファイルの拡張子を入力してください>')

    # 指定されたフォルダーが存在する
    if os.path.isdir(path):
        # カレントディレクトリのファイル名を取得
        for filename in os.listdir(path):
            # 指定された拡張子のファイルを削除する処理
            if filename.endswith(extension):
                # ファイル名出力
                print(filename)
                # 削除するか確認
                ans = input('削除しますか？(Y)')
                # 'Y'が入力されたら完全に削除する
                if ans == 'Y':                   
                    os.unlink(os.path.join(path, filename)) 
                else:
                    print('削除は行われません。')
    # 指定されたパスが存在しない
    else:
        print('指定したフォルダーは存在しません。')

# 実行ブロック
if __name__ == '__main__':
    # delete_file()を実行
    delete_file()