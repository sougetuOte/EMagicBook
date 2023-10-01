
import tkinter as tk
from PIL import Image, ImageTk
from menu import SubMenu

class TransparentWindow:
    FRAME_OFFSET = -2
    BG_COLOR = "white"

    def __init__(self, main, image, position=(0,0), size=(0,0)):
        # Window作成
        self.main = main
        self.main.config(bg=self.BG_COLOR)

        # イメージをPhotoImageに変換 (透過部分は透過)　
        # 幅と高さを取得　毎度イメージを読み込むのは非効率
        self.photo_image = ImageTk.PhotoImage(image)
        self.original_image = image #元イメージの保持
        self.image_width = self.photo_image.width()
        self.image_height = self.photo_image.height()
        
        # ウィンドウの位置とサイズ
        self.window_position = position
        self.window_size = size

        # ウィンドウの作成
        self.main.geometry(str(self.window_size[0]) + "x" +
                           str(self.window_size[1]) + "+" +
                           str(self.window_position[0]) + "+" +
                           str(self.window_position[1]))
        
        # ウィンドウの枠を消す
        self.main.wm_overrideredirect(True)
        # 透過表示(くり抜き)色を指定
        self.main.wm_attributes("-transparentcolor",
                                self.BG_COLOR)
        # ウィンドウの最前面に表示
        self.main.wm_attributes("-topmost", True)
        
        # キャンバスの作成
        self.init_canvas(self.main, self.photo_image)
        
        # Mouse drag start position
        self.start_x = self.window_position[0]

        # メニューウィンドウの作成
        self.menu = None
        
        # チャットウィンドーの作成
        self.chat_window = None
        

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
            self.photo_image.width() / 2,
            self.photo_image.height() / 2,
            image=self.photo_image)   

        # Bind events
        # ドラッグの開始位置を記録
        self.canvas.bind("<ButtonPress-1>", self.start_drag)
        # クリックイベントの設定　投下してない部分をドラッグしたら移動 ただし横方向のみ
        self.canvas.bind("<B1-Motion>", self.drag)
        # クリックイベントの設定 透過していない部分を右クリック。
        self.canvas.bind("<Button-3>", self.click_canvas_event)
        

        
    def start_drag(self, event):
        self.start_x = event.x
        #self.start_y = event.y

    def drag(self, event):
        x = self.main.winfo_x() - self.start_x + event.x
        y = self.main.winfo_y() #- self.start_y + event.y
        self.main.geometry(f"+{x}+{y}")

    # 右クリックイベント
    def click_canvas_event(self, event):
        print("click:(x:" + str(event.x) + ",y=" + str(event.y) + ")")
        #メニューウィンドーの表示
        if self.menu is None:
            self.menu = SubMenu(self.main, self.chat_window)
        # menu表示
        self.menu.menu_window.post(event.x_root, event.y_root)  

if __name__ == "__main__":
    # Create main window
    main = tk.Tk()
    #main.overrideredirect(1)

    # Load the image
    image = Image.open("images/closedbook000.png")
    
    # サイズ調整　縦が200を超えたら、200に縮小、横は縦の比率で縮小
    MAX_IMAGE_HEIGHT = 200
    if image.height > MAX_IMAGE_HEIGHT:
        image = image.resize(
            (int(image.width * (MAX_IMAGE_HEIGHT / image.height)),
             MAX_IMAGE_HEIGHT),
            Image.HAMMING)
    
    # Create a transparent window with the given image
    window_position = (main.winfo_screenwidth() - image.width - 100 , main.winfo_screenheight() - image.height - 50) 
    TransparentWindow(main, image, position=window_position, size=(image.width, image.height))

    # Run the application
    main.mainloop()
