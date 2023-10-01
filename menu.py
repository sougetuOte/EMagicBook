import tkinter as tk
from chat_window import ChatWindow

class SubMenu:
    def __init__(self, root, cw):
        # メニューウィンドウの作成
        self.menu_window = tk.Menu(root, tearoff=0)

        # メニューの作成
        self.menu_window.add_command(label="日記", command=self.menu1_command)
        self.menu_window.add_command(label="チャット", command=self.menu2_command)
        self.menu_window.add_separator()
        self.menu_window.add_command(label="Exit", command=root.quit)
        
        self.main = root
        self.chat_window = cw

    # メニュー1のコマンド
    def menu1_command(self):
        print("日記")
        # 親ウィンドーを非表示にする
        self.main.withdraw()

    # メニュー2のコマンド
    def menu2_command(self):
        print("チャット")
        if self.chat_window is None:
            self.chat_window = ChatWindow(self.main)