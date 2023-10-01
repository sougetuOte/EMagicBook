import tkinter as tk
from PIL import Image, ImageTk

class ChatWindow(tk.Toplevel):
    BG_COLOR="gray"
    FRAME_OFFSET = 0
    size_width = 520
    size_height = 620
    point_x = -450
    point_y = -500
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
         # 背景画像の設定
        image = Image.open("images/bubble.png")  # 画像のパスを指定
        self.bg_image = ImageTk.PhotoImage(image)
        #self.config.configure(bg=self.BG_COLOR)
        # ウィンドウの枠を消す
        self.wm_overrideredirect(True)
        # 透過表示(くり抜き)色を指定
        self.wm_attributes("-transparentcolor", self.BG_COLOR)
        # ウィンドウの作成
        self.geometry(str(self.size_width) + "x" +
                           str(self.size_height) + "+" +
                           str(self.bg_image.width()) + "+" +
                           str(self.bg_image.height()))
        
        # キャンバスの作成
        self.canvas = tk.Canvas(self, width=self.bg_image.width(), height=self.bg_image.height(), bg=self.BG_COLOR ,bd=0, highlightthickness=0)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        self.canvas.pack()  # キャンバスをウィンドウに配置
                
        # 枠を消すために0を指定
        self.canvas.place(x=self.FRAME_OFFSET, y=self.FRAME_OFFSET) 
        
#        print(self.size_width, self.size_height)

        # ウィンドウ位置の更新
        self.update_position()

    def update_position(self):
        # ウィンドウのサイズを背景画像に合わせて設定
        self.geometry(f"{self.bg_image.width()}x{self.bg_image.height()}+{self.parent.winfo_x() + self.point_x}+{self.parent.winfo_y() + self.point_y}")
        self.after(100, self.update_position)

# 以下の部分はテスト用なので、実際の使用時には不要です
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("200x200+1000+1000")

    def open_chat_window():
        ChatWindow(root)

    open_button = tk.Button(root, text="Open Chat Window", command=open_chat_window)
    open_button.pack(expand=True)

    root.mainloop()
