import os, shutil

def delete_folder():
    """ 指定されたフォルダーを削除する関数
    """
    # フォルダーのパスを取得
    path = input('フォルダーのパスを入力してください >')
    # 指定されたフォルダーが存在する場合の処理
    if os.path.isdir(path):
        # 指定されたパスを出力
        print(path)
        # 削除するか確認
        ans = input('削除しますか？(Y)')
        # 'Y'が入力されたら完全に削除する
        if ans == 'Y':
            shutil.rmtree(path) 
            print('削除しました。')
    # 指定されたパスが存在しない場合
    else:
        print('指定したフォルダーは存在しません。')

# 実行ブロック
if __name__ == '__main__':
    # delete_folder()を実行
    delete_folder()