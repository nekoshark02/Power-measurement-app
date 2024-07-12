################ ライブラリの導入 ####################
import sys
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.animation as animation
import numpy as np

class GUIApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # タイトル表示
        self.master.title("電力測定グラフ")
        self.master.geometry()
        # matplot配置用フレーム
        frame = tk.Frame(self.master)
        # matplotlibの描画領域の作成
        fig = Figure()
        self.ax = fig.add_subplot(1, 1, 1)
        self.fig_canvas = FigureCanvasTkAgg(fig, frame)
        self.toolbar = NavigationToolbar2Tk(self.fig_canvas, frame)
        self.fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        # フレームをウィンドウに配置
        frame.pack()
    
    def PowerGraph(self):
        # 要素の空の配列をいったん置く
        x = []
        y = []
        
        
        
    def Quit(self):
        self.quit()
        self.destroy()
        

def main():
    root = tk.Tk()
    app = GUIApplication(master=root)
    app.mainloop()
    
if __name__ == "__main__":
    main()
