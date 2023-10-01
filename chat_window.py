import tkinter as tk
from tkinter import scrolledtext, PhotoImage, Label
from PIL import Image, ImageTk

class ChatWindow:
    BG_COLOR = "white"
    FRAME_OFFSET = -2

    def __init__(self, parent):
        self.parent = parent
        self.parent.config(bg=self.BG_COLOR)
        

        
        # ウィンドウのサイズと位置
        self.width = 520
        self.height = 620
        self.update_position(initial=True)  # 初期位置の設定
        
        # チャットウィンドウの作成
        self.window = tk.Toplevel(parent)
        self.window.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.window.overrideredirect(1)  # タイトルバーを削除
        # 透過表示(くり抜き)色を指定

        # 背景画像の設定
        image = Image.open("images/bubble.png")
        self.background_image = ImageTk.PhotoImage(image)
        bg_label = tk.Label(self.window, image=self.background_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        # オブジェクトの作成
        self.create_text_area()
        self.create_text_box()
        self.create_command_button()
        self.create_close_button()
        
        self.update_position()
        
    def create_text_area(self):
        # 半透明の背景画像をラベルに設定
        bg_image = Image.open("images/text_area01.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self.window, image=bg_photo)
        bg_label.place(x=30, y=30, width=440, height=400)
        
        self.text_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, width=50, height=10,  bg=self.BG_COLOR)
        self.text_area.place(x=30, y=30, width=440, height=400)
        
    def create_text_box(self):
        # 半透明の背景画像をラベルに設定
        bg_image = Image.open("images/text_box01.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self.window, image=bg_photo)
        bg_label.place(x=30, y=440, width=440, height=100)

        self.text_box = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, width=50, height=5, bg=self.BG_COLOR)
        self.text_box.place(x=30, y=440, width=440, height=100)
        
    def create_command_button(self):
        self.command_button = tk.Button(self.window, text="Enter", command=self.send_message)
        self.command_button.place(x=410, y=530, width=80, height=50)
        
    def create_close_button(self):
        self.close_button = tk.Button(self.window, text="x", command=self.close_window)
        self.close_button.place(x=480, y=0, width=20, height=20)
        
    def send_message(self):
        message = self.text_box.get("1.0", tk.END).strip()
        if message:
            self.text_area.insert(tk.END, f"You: {message}\n")
            self.text_box.delete("1.0", tk.END)
            
    def close_window(self):
        self.window.destroy()
        
    def update_position(self, initial=False):
        self.x = self.parent.winfo_x() - 540
        self.y = self.parent.winfo_y() - 500
        if not initial:
            self.window.geometry(f"+{self.x}+{self.y}")
            self.window.after(10, self.update_position)

# これはデモ用のコードです。背景画像が必要で、そのパスを正しく設定してください。
# また、ウィンドウのデザインや動作は要件に応じて調整してください。
