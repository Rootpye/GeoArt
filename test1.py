import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, OptionMenu, StringVar, Scale, HORIZONTAL

class MathArtApp:
    def __init__(self, root):
        self.root = root
        self.root.title("수학적 예술 생성기")

        # 언어 설정
        self.language = StringVar(root)
        self.language.set("한국어")
        self.language.trace("w", self.update_language)

        self.lang_label = Label(root, text="언어 선택:")
        self.lang_label.pack()

        self.lang_menu = OptionMenu(root, self.language, "한국어", "English", "Español", "简体中文")
        self.lang_menu.pack()

        # 곡선 선택
        self.curve_label = Label(root, text="곡선 선택:")
        self.curve_label.pack()

        self.curve_type = StringVar(root)
        self.curve_type.set("리사주 곡선")

        # 새로운 도형 옵션 추가
        self.option_menu = OptionMenu(root, self.curve_type,
                                      "리사주 곡선", "극좌표 꽃", "페르마 나선",
                                      "로지스틱 곡선", "리만 곡선", "클로소이드 곡선",
                                      "아르키메데스 나선", "리사주 나비", "카디오이드", "수레바퀴 곡선")
        self.option_menu.pack()

        # 슬라이더
        self.freq_label = Label(root, text="주파수")
        self.freq_label.pack()

        self.freq_slider = Scale(root, from_=1, to=20, orient=HORIZONTAL)
        self.freq_slider.set(5)
        self.freq_slider.pack()

        self.phase_label = Label(root, text="위상")
        self.phase_label.pack()

        self.phase_slider = Scale(root, from_=0, to=2 * np.pi, resolution=0.1, orient=HORIZONTAL)
        self.phase_slider.set(0)
        self.phase_slider.pack()

        # 생성 버튼
        self.plot_button = Button(root, text="예술 생성", command=self.generate_art)
        self.plot_button.pack()

    def update_language(self, *args):
        lang = self.language.get()
        if lang == "한국어":
            self.root.title("수학적 예술 생성기")
            self.lang_label.config(text="언어 선택:")
            self.curve_label.config(text="곡선 선택:")
            self.freq_label.config(text="주파수")
            self.phase_label.config(text="위상")
            self.plot_button.config(text="예술 생성")
            self.curve_type.set("리사주 곡선")
            self.option_menu["menu"].delete(0, "end")
            for option in ["리사주 곡선", "극좌표 꽃", "페르마 나선", "로지스틱 곡선",
                           "리만 곡선", "클로소이드 곡선", "아르키메데스 나선",
                           "리사주 나비", "카디오이드", "수레바퀴 곡선"]:
                self.option_menu["menu"].add_command(label=option, command=lambda value=option: self.curve_type.set(value))
        else:
            self.update_language_english_spanish_chinese()

    def generate_art(self):
        curve = self.curve_type.get()
        freq = self.freq_slider.get()
        phase = self.phase_slider.get()

        if curve == "리사주 곡선":
            self.plot_lissajous(freq, phase)
        elif curve == "극좌표 꽃":
            self.plot_polar_rose(freq)
        elif curve == "페르마 나선":
            self.plot_fermat_spiral()
        elif curve == "로지스틱 곡선":
            self.plot_logistic_curve()
        elif curve == "리만 곡선":
            self.plot_riemann_curve()
        elif curve == "클로소이드 곡선":
            self.plot_clothoid_curve()
        elif curve == "아르키메데스 나선":
            self.plot_archimedean_spiral()
        elif curve == "리사주 나비":
            self.plot_lissajous_butterfly()
        elif curve == "카디오이드":
            self.plot_cardioid()
        elif curve == "수레바퀴 곡선":
            self.plot_trochoid()

    def plot_archimedean_spiral(self):
        theta = np.linspace(0, 4 * np.pi, 1000)
        r = theta
        plt.figure(figsize=(6, 6))
        plt.polar(theta, r, color='orange')
        plt.title("아르키메데스 나선")
        plt.show()

    def plot_lissajous_butterfly(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        x = np.sin(2 * t) * np.exp(np.cos(t))
        y = np.cos(2 * t) * np.exp(np.sin(t))
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color='purple')
        plt.title("리사주 나비")
        plt.axis("equal")
        plt.show()

    def plot_cardioid(self):
        theta = np.linspace(0, 2 * np.pi, 1000)
        r = 1 + np.cos(theta)
        plt.figure(figsize=(6, 6))
        plt.polar(theta, r, color='red')
        plt.title("카디오이드")
        plt.show()

    def plot_trochoid(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        R, r, d = 5, 1, 3
        x = (R - r) * np.cos(t) + d * np.cos((R - r) / r * t)
        y = (R - r) * np.sin(t) - d * np.sin((R - r) / r * t)
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color='blue')
        plt.title("수레바퀴 곡선")
        plt.axis("equal")
        plt.show()

root = Tk()
app = MathArtApp(root)
root.mainloop()
