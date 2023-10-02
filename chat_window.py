import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk

class ChatWindow(tk.Toplevel):
    BG_COLOR="white"
    TEXT_BG_COLOR = "#DAA520"  # 背景色を黄土色に変更
    FRAME_OFFSET = 0
    point_x = 730
    point_y = 700
    
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        # 透過表示(くり抜き)色を指定
        self.wm_attributes("-transparentcolor", self.BG_COLOR)
        self.attributes("-topmost", True)

        # 背景画像の設定
        image = Image.open("images/bubble000.png")  # 画像のパスを指定
        self.bg_image = ImageTk.PhotoImage(image)
        # ウィンドウの枠を消す
        self.wm_overrideredirect(True)
        # ウィンドウの作成
        self.geometry(str(self.bg_image.width()) + "x" +
                           str(self.bg_image.height()) + "+" +
                           str(self.parent.winfo_x() -self.point_x) + "+" +
                           str(self.parent.winfo_y() - self.point_y))
        
        # キャンバスの作成
        self.canvas = tk.Canvas(self, width=self.bg_image.width(), height=self.bg_image.height(), bg=self.BG_COLOR , highlightthickness=0)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        self.canvas.pack()  # キャンバスをウィンドウに配置

        # 枠を消すために0を指定
        self.canvas.place(x=self.FRAME_OFFSET, y=self.FRAME_OFFSET) 

        # オブジェクトの作成
        #text_bg_image = Image.open("images/text_area.png")
        #text_area_image = text_bg_image.resize((610, 600))  # 画像をリサイズ
        #self.text_area_bg = ImageTk.PhotoImage(text_area_image)
        #text_box_image = text_bg_image.resize((610, 100))  # 画像をリサイズ
        #self.text_box_bg = ImageTk.PhotoImage(text_box_image)
        self.create_text_area()
        self.create_text_box()
        self.create_command_button()
        self.create_close_button()
                
        # ウィンドウ位置の更新
        self.update_position()

    '''
    def create_text_area(self):
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=10, bg=self.TEXT_BG_COLOR)  # 背景色を黄土色に変更
        self.text_area.place(x=30, y=30, width=640, height=600)

    def create_text_box(self):
        self.text_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=5, bg=self.TEXT_BG_COLOR)  # 背景色を黄土色に変更
        self.text_box.place(x=30, y=640, width=640, height=100)
    '''
    def create_text_area(self):
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=80, height=20, bg="khaki") 
        self.text_area_window = self.canvas.create_window(30, 30, window=self.text_area, anchor=tk.NW, width=640, height=600)
    
    def create_text_box(self):
        self.text_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=40, height=5, bg="khaki")
        self.text_box_window = self.canvas.create_window(30, 640, window=self.text_box, anchor=tk.NW, width=640, height=100)
    
    def create_command_button(self):
        self.command_button = tk.Button(self, text="Enter", command=self.send_message)
        self.command_button.place(x=600, y=750, width=70, height=30)

    def create_close_button(self):
        self.close_button = tk.Button(self, text="x", command=self.close_window)
        self.close_button.place(x=650, y=10, width=20, height=20)


    def update_position(self):
        # ウィンドウのサイズを背景画像に合わせて設定
        self.geometry(f"{self.bg_image.width()}x{self.bg_image.height()}+{self.parent.winfo_x() -self.point_x}+{self.parent.winfo_y() - self.point_y}")
        self.after(50, self.update_position)

    def send_message(self):
        message = self.text_box.get("1.0", tk.END).strip()
        if message:
            self.text_area.insert(tk.END, f"You: {message}\n")
            self.text_box.delete("1.0", tk.END)

    def close_window(self):
        self.destroy()


# 以下の部分はテスト用なので、実際の使用時には不要です
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("200x200+1000+1000")

    def open_chat_window():
        ChatWindow(root)

    open_button = tk.Button(root, text="Open Chat Window", command=open_chat_window)
    open_button.pack(expand=True)

    root.mainloop()
