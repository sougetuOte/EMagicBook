import tkinter as tk

class SubMenu:
    def __init__(self, root):
        # メニューウィンドウの作成
        self.menu_window = tk.Menu(root, tearoff=0)

        # メニューの作成
        self.menu_window.add_command(label="日記", command=self.menu1_command)
        self.menu_window.add_command(label="チャット", command=self.menu2_command)
        self.menu_window.add_separator()
        self.menu_window.add_command(label="Exit", command=root.quit)
        
        self.main = root

    # メニュー1のコマンド
    def menu1_command(self):
        print("日記")
        # 親ウィンドーを非表示にする
        self.main.withdraw()

    # メニュー2のコマンド
    def menu2_command(self):
        print("チャット")