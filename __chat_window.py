import tkinter as tk
from tkinter import scrolledtext,  Label
from PIL import Image, ImageTk

class ChatWindow(tk.Toplevel):
    BG_COLOR = "white"
    FRAME_OFFSET = -2

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.width = 520
        self.height = 600
        self.update_idletasks()
        self.x = self.parent.winfo_x() - self.width - 10
        self.y = self.parent.winfo_y() - self.height + self.parent.winfo_height()

        self.configure(bg=self.BG_COLOR)
        self.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        # ウィンドウの枠を消す
        self.parent.wm_attributes("-transparentcolor", self.BG_COLOR)
        self.wm_overrideredirect(True)
        self.attributes("-topmost", True)
       

        # 背景画像の設定
        image = Image.open("images/bubble.png")
        image.putalpha(30)  # 透過度を設定        
        self.background_image = ImageTk.PhotoImage(image)

        # キャンバスの作成
        self.init_canvas(self.parent, self.background_image)

        bg_label = tk.Label(self, image=self.background_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        # オブジェクトの作成
#        self.create_text_area()
        self.create_text_box()
        self.create_command_button()
        self.create_close_button()

        self.update_position()

    def init_canvas(self, frame, image):
        # キャンバスの作成
        self.canvas = tk.Canvas(
            frame,
            width=image.width(),
            height=image.height(),
            bg=self.BG_COLOR
        )
        # 枠を消すためにマイナス値を指定
        self.canvas.place(x=self.FRAME_OFFSET,
                          y=self.FRAME_OFFSET)
        
        # PIL.Image から PhotoImage 生成
        #self.photo_image = ImageTk.PhotoImage(image=image)
        # canvasに画像を表示
        self.canvas.create_image(
            image.width() / 2,
            image.height() / 2,
            image=image)   

        
    #def create_text_area(self):
     # テキストエリアの作成
        self.text_area_frame = tk.Frame(self.canvas, bg=self.BG_COLOR)
        self.text_area = scrolledtext.ScrolledText(self.text_area_frame, wrap=tk.WORD, width=50, height=10, bg=self.BG_COLOR)
        self.text_area.pack(padx=5, pady=5, fill="both", expand=True)

        # テキストエリアをキャンバスに配置
        self.canvas.create_window(
            image.width() / 2,
            image.height() / 2,
            window=self.text_area_frame,
            anchor=tk.CENTER
        )

        
    def create_text_box(self):
        # 半透明の背景画像をラベルに設定
        bg_image = Image.open("images/text_box01.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self, image=bg_photo)
        bg_label.place(x=30, y=440, width=440, height=100)

        self.text_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=5, bg=self.BG_COLOR)
        self.text_box.place(x=30, y=440, width=440, height=100)
        
    def create_command_button(self):
        self.command_button = tk.Button(self, text="Enter", command=self.send_message)
        self.command_button.place(x=410, y=530, width=80, height=50)
        
    def create_close_button(self):
        self.close_button = tk.Button(self, text="x", command=self.close_window)
        self.close_button.place(x=480, y=0, width=20, height=20)
        
    def send_message(self):
        message = self.text_box.get("1.0", tk.END).strip()
        if message:
            self.text_area.insert(tk.END, f"You: {message}\n")
            self.text_box.delete("1.0", tk.END)
            
    def close_window(self):
        self.destroy()
        
    def update_position(self, initial=False):
       self.x = self.parent.winfo_x() - self.width - 10
       self.y = self.parent.winfo_y() - self.height + self.parent.winfo_height()
       self.geometry(f"+{self.x}+{self.y}")
       self.after(10, self.update_position)
