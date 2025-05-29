
# Windows 11
# VSCode Gitの初期設定
# Git for Windows:Git Bashでのコマンド入力

$ git config --global user.name 'holydiver'
$ git config --global user.email 'holydiver@nifty.com'
$ git config --global core.editor 'code --wait'
$ git config --global merge.tool 'code --wait "$MERGED"'
$ git config --global push.default simple
$ git config --global pull.rebase false
$ git config --global core.quotepath false

# 「参照使用でリモートにプッシュできません。最初にPULLを実行して変更してください」への対処方法
# …or create a new repository on the command line

$ echo "# VSCode_Work" >> README.md
$ git init
$ git add README.md
$ git commit -m "first commit"
$ git branch -M main
$ git remote add origin https://github.com/holydiver-zerog/VSCode_Work.git
$ git push -u origin main

# …or push an existing repository from the command line

$ git remote add origin https://github.com/holydiver-zerog/VSCode_Work.git
$ git branch -M main
$ git push -u origin main

# ブランチ ご参考

$ git branch
$ git branch app01
$ git checkout app01
$ git checkout main
$ git merge app01

# ------------------------------------------------------------------------------------------------------

# macOS
# VSCode Gitの初期設定
# Git for macOS:Bashでのコマンド入力

$ git config --global user.name 'holydiver'
$ git config --global user.email 'holydiver@nifty.com'
$ git config --global core.editor 'code --wait'
$ git config --global merge.tool 'code --wait "$MERGED"'
$ git config --global push.default simple
$ git config --global pull.rebase false
$ git config --global core.quotepath false
$ git config --list
