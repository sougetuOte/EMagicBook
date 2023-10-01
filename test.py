from PIL import Image, ImageTk
import tkinter as tk
from tkinter import scrolledtext

class ChatWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # キャンバスの作成
        self.canvas = tk.Canvas(self, width=800, height=800)
        self.canvas.pack()

        # 背景画像のロードとリサイズ
        bg_image = Image.open("bubble000.png")
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # 背景画像の描画
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)

        # テキストエリアの作成
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=40, height=10, bg="khaki")
        self.text_area_window = self.canvas.create_window(30, 30, window=self.text_area, anchor=tk.NW, width=610, height=600)

        # テキストボックスの作成
        self.text_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=40, height=5, bg="khaki")
        self.text_box_window = self.canvas.create_window(30, 640, window=self.text_box, anchor=tk.NW, width=610, height=100)

        # Enterボタンの作成
        self.enter_button = tk.Button(self, text="Enter", command=self.send_message)
        self.enter_button_window = self.canvas.create_window(500, 750, window=self.enter_button, anchor=tk.NW, width=80, height=50)

        # Closeボタンの作成
        self.close_button = tk.Button(self, text="x", command=self.destroy)
        self.close_button_window = self.canvas.create_window(700, 10, window=self.close_button, anchor=tk.NW, width=20, height=20)

    def send_message(self):
        # ここにメッセージ送信の処理を書く
        pass

if __name__ == "__main__":
    root = tk.Tk()
    chat_window = ChatWindow(root)
    root.mainloop()
