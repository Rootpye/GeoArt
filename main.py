import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, OptionMenu, StringVar, Scale, HORIZONTAL

class MathArtApp:
    def __init__(self, root):
        self.root = root
        self.root.title("수학적 예술 생성기")
        
        self.label = Label(root, text="곡선 선택:")
        self.label.pack()
        
        # 옵션 설정
        self.curve_type = StringVar(root)
        self.curve_type.set("리사주 곡선")  # 기본값
        
        self.option_menu = OptionMenu(root, self.curve_type, "리사주 곡선", "극좌표 꽃", "페르마 나선")
        self.option_menu.pack()

        # 슬라이더 추가
        self.freq_slider = Scale(root, from_=1, to=20, orient=HORIZONTAL, label="주파수")
        self.freq_slider.set(5)
        self.freq_slider.pack()

        self.phase_slider = Scale(root, from_=0, to=2*np.pi, resolution=0.1, orient=HORIZONTAL, label="위상")
        self.phase_slider.set(0)
        self.phase_slider.pack()
        
        # 생성 버튼
        self.plot_button = Button(root, text="예술 생성", command=self.generate_art)
        self.plot_button.pack()

    def generate_art(self):
        curve = self.curve_type.get()
        freq = self.freq_slider.get()
        phase = self.phase_slider.get()

        # 곡선 타입에 따라 다른 수학적 도형을 생성
        if curve == "리사주 곡선":
            self.plot_lissajous(freq, phase)
        elif curve == "극좌표 꽃":
            self.plot_polar_rose(freq)
        elif curve == "페르마 나선":
            self.plot_fermat_spiral()

    def plot_lissajous(self, freq, phase):
        t = np.linspace(0, 2 * np.pi, 1000)
        x = np.sin(freq * t + phase)
        y = np.sin((freq + 1) * t)
        
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color='blue')
        plt.title("리사주 곡선")
        plt.axis("equal")
        plt.show()

    def plot_polar_rose(self, freq):
        theta = np.linspace(0, 2 * np.pi, 1000)
        r = np.cos(freq * theta)
        
        plt.figure(figsize=(6, 6))
        plt.polar(theta, r, color='purple')
        plt.title("극좌표 꽃")
        plt.show()

    def plot_fermat_spiral(self):
        theta = np.linspace(0, 4 * np.pi, 1000)
        r = np.sqrt(theta)
        
        plt.figure(figsize=(6, 6))
        plt.polar(theta, r, color='green')
        plt.title("페르마 나선")
        plt.show()

root = Tk()
app = MathArtApp(root)
root.mainloop()
