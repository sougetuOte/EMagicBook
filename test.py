import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk

class ChatWindow(tk.Toplevel):
    BG_COLOR = "white"
    TEXT_BG_COLOR = "#DAA520"  # 背景色を黄土色に変更

    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.attributes("-transparentcolor", self.BG_COLOR)
        self.attributes("-topmost", True)

        # ウィンドウのサイズと位置
        self.point_x = self.parent.winfo_x() - 540
        self.point_y = self.parent.winfo_y() - 500

        self.bg_image = Image.open("images/bubble000.png")
        self.photo_image = ImageTk.PhotoImage(self.bg_image)

        self.geometry(str(self.bg_image.width()) + "x" +
                      str(self.bg_image.height()) + "+" +
                      str(self.point_x) + "+" +
                      str(self.point_y))

        # キャンバスの作成と配置
        self.canvas = tk.Canvas(self, bg=self.BG_COLOR, width=self.bg_image.width(), height=self.bg_image.height(), highlightthickness=0)
        self.canvas.pack()

        # 背景画像の描画
        self.canvas.create_image(self.bg_image.width() / 2, self.bg_image.height() / 2, image=self.photo_image)

        # オブジェクトの作成
        self.create_text_area()
        self.create_text_box()
        self.create_command_button()
        self.create_close_button()

        self.update_position()

    def create_text_area(self):
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=10, bg=self.TEXT_BG_COLOR)  # 背景色を黄土色に変更
        self.text_area.place(x=30, y=30, width=610, height=600)

    def create_text_box(self):
        self.text_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=5, bg=self.TEXT_BG_COLOR)  # 背景色を黄土色に変更
        self.text_box.place(x=30, y=610, width=610, height=100)

    def create_command_button(self):
        self.command_button = tk.Button(self, text="Enter", command=self.send_message)
        self.command_button.place(x=500, y=620, width=80, height=50)

    def create_close_button(self):
        self.close_button = tk.Button(self, text="x", command=self.close_window)
        self.close_button.place(x=700, y=10, width=20, height=20)

    def send_message(self):
        message = self.text_box.get("1.0", tk.END).strip()
        if message:
            self.text_area.insert(tk.END, f"You: {message}\n")
            self.text_box.delete("1.0", tk.END)

    def close_window(self):
        self.destroy()

    def update_position(self):
        self.point_x = self.parent.winfo_x() - 540
        self.point_y = self.parent.winfo_y() - 500
        self.geometry("+{}+{}".format(self.point_x, self.point_y))
        self.after(10, self.update_position)
