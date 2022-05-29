from tkinter import ttk
import tkinter
import matplotlib

matplotlib.use('TkAgg')

from matplotlib import figure
from matplotlib.backends import backend_tkagg

import calculator


class Window(tkinter.Tk):
    @classmethod
    def windowmaker(cls):
        return cls()

    def __init__(self):
        super().__init__()
        frm = ttk.Frame(self, padding=10)
        frm.grid()
        self.title('Nao Sei')
        fig = figure.Figure()
        fig_canvas = backend_tkagg.FigureCanvasTkAgg(fig, frm)
        self.polyhedron = calculator.TenPointPolyhedron.create(fig)
        fig_canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        ttk.Button(self, text="Transladar", command=self.translate)
        self.rotate()

    def translate(self):
        self.polyhedron.translate(1, 2, 3)

    def scale(self):
        self.polyhedron.scale(1, 1, 0.001)

    def rotate(self):
        self.polyhedron.rotate(45, 'x')


if __name__ == '__main__':
    app = Window.windowmaker()
    app.mainloop()
