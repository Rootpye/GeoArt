import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, OptionMenu, StringVar, Scale, HORIZONTAL

class MathArtApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mathematical Art Generator")
        
        self.label = Label(root, text="Select Curve:")
        self.label.pack()
        
        # Setting options
        self.curve_type = StringVar(root)
        self.curve_type.set("Lissajous Curve")  # Default
        
        self.option_menu = OptionMenu(root, self.curve_type, 
                                      "Lissajous Curve", "Polar Rose", 
                                      "Fermat Spiral", "Cycloid", 
                                      "Heart Curve", "Lemniscate",
                                      "Hypotrochoid", "Epitrochoid",
                                      "Astroid", "Deltoid", "Limacon",
                                      "Bernoulli Lemniscate", "Cassini Oval", 
                                      "Eylenberg Curve", "Fibonacci Spiral",
                                      "Hyperbolic Spiral")
        self.option_menu.pack()

        # Add sliders
        self.freq_slider = Scale(root, from_=1, to=20, orient=HORIZONTAL, label="Frequency")
        self.freq_slider.set(5)
        self.freq_slider.pack()

        self.phase_slider = Scale(root, from_=0, to=2*np.pi, resolution=0.1, orient=HORIZONTAL, label="Phase")
        self.phase_slider.set(0)
        self.phase_slider.pack()
        
        # Generate button
        self.plot_button = Button(root, text="Generate Art", command=self.generate_art)
        self.plot_button.pack()

    def generate_art(self):
        curve = self.curve_type.get()
        freq = self.freq_slider.get()
        phase = self.phase_slider.get()

        # Generate different mathematical shapes based on curve type
        if curve == "Lissajous Curve":
            self.plot_lissajous(freq, phase)
        elif curve == "Polar Rose":
            self.plot_polar_rose(freq)
        elif curve == "Fermat Spiral":
            self.plot_fermat_spiral()
        elif curve == "Cycloid":
            self.plot_cycloid(freq)
        elif curve == "Heart Curve":
            self.plot_heart_curve()
        elif curve == "Lemniscate":
            self.plot_lemniscate()
        elif curve == "Hypotrochoid":
            self.plot_hypotrochoid()
        elif curve == "Epitrochoid":
            self.plot_epitrochoid()
        elif curve == "Astroid":
            self.plot_astroid()
        elif curve == "Deltoid":
            self.plot_deltoid()
        elif curve == "Limacon":
            self.plot_limacon()
        elif curve == "Bernoulli Lemniscate":
            self.plot_bernoulli_lemniscate()
        elif curve == "Cassini Oval":
            self.plot_cassini_oval()
        elif curve == "Eylenberg Curve":
            self.plot_eylenberg_curve()
        elif curve == "Fibonacci Spiral":
            self.plot_fibonacci_spiral()
        elif curve == "Hyperbolic Spiral":
            self.plot_hyperbolic_spiral()

    def plot_lissajous(self, freq, phase):
        t = np.linspace(0, 2 * np.pi, 1000)
        x = np.sin(freq * t + phase)
        y = np.sin((freq + 1) * t)
        
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color='blue')
        plt.title("Lissajous Curve")
        plt.axis("equal")
        plt.show()

    def plot_polar_rose(self, freq):
        theta = np.linspace(0, 2 * np.pi, 1000)
        r = np.cos(freq * theta)
        
        plt.figure(figsize=(6, 6))
        plt.polar(theta, r, color='purple')
        plt.title("Polar Rose")
        plt.show()

    def plot_fermat_spiral(self):
        theta = np.linspace(0, 4 * np.pi, 1000)
        r = np.sqrt(theta)
        
        plt.figure(figsize=(6, 6))
        plt.polar(theta, r, color='green')
        plt.title("Fermat Spiral")
        plt.show()

    def plot_cycloid(self, freq):
        t = np.linspace(0, 4 * np.pi, 1000)
        x = t - np.sin(freq * t)
        y = 1 - np.cos(freq * t)
        
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color='orange')
        plt.title("Cycloid")
        plt.axis("equal")
        plt.show()

    def plot_heart_curve(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        x = 16 * np.sin(t)**3
        y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
        
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color='red')
        plt.title("Heart Curve")
        plt.axis("equal")
        plt.show()

    def plot_lemniscate(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        x = np.sqrt(2) * np.cos(t) / (np.sin(t)**2 + 1)
        y = np.sqrt(2) * np.cos(t) * np.sin(t) / (np.sin(t)**2 + 1)
        
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color='magenta')
        plt.title("Lemniscate")
        plt.axis("equal")
        plt.show()
    def plot_hypotrochoid(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        R, r, d = 5, 3, 5  # radii and distance for hypotrochoid
        x = (R - r) * np.cos(t) + d * np.cos((R - r) / r * t)
        y = (R - r) * np.sin(t) - d * np.sin((R - r) / r * t)
        
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color='purple')
        plt.title("Hypotrochoid")
        plt.axis("equal")
        plt.show()

    def plot_epitrochoid(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        R, r, d = 5, 3, 5  # radii and distance for epitrochoid
        x = (R + r) * np.cos(t) - d * np.cos((R + r) / r * t)
        y = (R + r) * np.sin(t) - d * np.sin((R + r) / r * t)
        
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color='blue')
        plt.title("Epitrochoid")
        plt.axis("equal")
        plt.show()

    def plot_astroid(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        a = 1  # constant for astroid
        x = a * np.cos(t)**3
        y = a * np.sin(t)**3
        
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color='cyan')
        plt.title("Astroid")
        plt.axis("equal")
        plt.show()

    def plot_deltoid(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        a = 1  # constant for deltoid
        x = 2 * a * np.cos(t) + a * np.cos(2 * t)
        y = 2 * a * np.sin(t) - a * np.sin(2 * t)
        
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color='orange')
        plt.title("Deltoid")
        plt.axis("equal")
        plt.show()

    def plot_limacon(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        a, b = 1, 0.5  # constants for limacon
        r = a + b * np.cos(t)
        x = r * np.cos(t)
        y = r * np.sin(t)
        
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color='green')
        plt.title("Limacon")
        plt.axis("equal")
        plt.show()

    def plot_bernoulli_lemniscate(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        a = 1
        r = a * np.sqrt(np.cos(2 * t))
        x = r * np.cos(t)
        y = r * np.sin(t)
        
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color='cyan')
        plt.title("Bernoulli Lemniscate")
        plt.axis("equal")
        plt.show()

    def plot_cassini_oval(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        a, b = 1, 1.5
        r = np.sqrt(a**2 * np.cos(2*t) + np.sqrt(a**4 - b**4))
        x = r * np.cos(t)
        y = r * np.sin(t)
        
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color='brown')
        plt.title("Cassini Oval")
        plt.axis("equal")
        plt.show()

    def plot_eylenberg_curve(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        x = np.cos(t) * (3 * np.cos(t) - np.cos(3 * t))
        y = np.sin(t) * (3 * np.cos(t) - np.cos(3 * t))
        
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, color='orange')
        plt.title("Eylenberg Curve")
        plt.axis("equal")
        plt.show()

    def plot_fibonacci_spiral(self):
        theta = np.linspace(0, 4 * np.pi, 1000)
        a = 0.1
        r = a * np.exp(0.306 * theta)
        
        plt.figure(figsize=(6, 6))
        plt.polar(theta, r, color='gold')
        plt.title("Fibonacci Spiral")
        plt.show()

    def plot_hyperbolic_spiral(self):
        theta = np.linspace(0.1, 4 * np.pi, 1000)
        r = 1 / theta
        
        plt.figure(figsize=(6, 6))
        plt.polar(theta, r, color='lime')
        plt.title("Hyperbolic Spiral")
        plt.show()

root = Tk()
app = MathArtApp(root)
root.mainloop()
