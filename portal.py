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
        self.title('Poliedro')
        content = ttk.Frame(self, padding=10)
        content.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        frm_figure = ttk.Frame(content, borderwidth=5)
        frm_figure.grid(column=0, row=0, rowspan=10)
        fig = figure.Figure()
        self.fig_canvas = backend_tkagg.FigureCanvasTkAgg(fig, frm_figure)
        self.fig_canvas.get_tk_widget().grid(column=0, row=0)
        self.polyhedron = calculator.TenPointPolyhedron.create(fig)

        ttk.Label(content, text="Transladar em x:").grid(column=1, row=0)
        self.translate_x_value = ttk.Entry(content)
        self.translate_x_value.grid(column=1, row=1, sticky=(tkinter.N))

        ttk.Label(content, text="Transladar em y:").grid(column=2, row=0)
        self.translate_y_value = ttk.Entry(content)
        self.translate_y_value.grid(column=2, row=1,sticky=(tkinter.N))

        ttk.Label(content, text="Transladar em z:").grid(column=3, row=0)
        self.translate_z_value = ttk.Entry(content)
        self.translate_z_value.grid(column=3, row=1,sticky=(tkinter.N))
        ttk.Button(content, text="Transladar", command=self.translate).grid(column=1, row=1, columnspan=3, sticky=(tkinter.S, tkinter.W, tkinter.E))

        ttk.Label(content, text="Redimensionar em x:").grid(column=1, row=2)
        self.scale_x_value = ttk.Entry(content)
        self.scale_x_value.grid(column=1, row=3, sticky=(tkinter.N))

        ttk.Label(content, text="Redimensionar em y:").grid(column=2, row=2)
        self.scale_y_value = ttk.Entry(content)
        self.scale_y_value.grid(column=2, row=3, sticky=(tkinter.N))

        ttk.Label(content, text="Redimensionar em z:").grid(column=3, row=2)
        self.scale_z_value = ttk.Entry(content)
        self.scale_z_value.grid(column=3, row=3, sticky=(tkinter.N))
        ttk.Button(content, text="Redimensionar", command=self.scale).grid(column=1, row=3, columnspan=3, sticky=(tkinter.S, tkinter.W, tkinter.E))

        ttk.Label(content, text="Eixo que deseja rotacionar:").grid(column=1, row=4)
        self.rotate_axis = ttk.Entry(content)
        self.rotate_axis.grid(column=1, row=5, sticky=(tkinter.N))

        ttk.Label(content, text="Ângulo que deseja rotacionar:").grid(column=3, row=4)
        self.rotate_angle = ttk.Entry(content)
        self.rotate_angle.grid(column=3, row=5, sticky=(tkinter.N))
        ttk.Button(content, text="Rotacionar", command=self.rotate).grid(column=1, row=5, columnspan=3, sticky=(tkinter.S, tkinter.W, tkinter.E))

        #ttk.Button(content, text="Reset", command=self.reset).grid(column=1, row=6, sticky=(tkinter.S, tkinter.W, tkinter.E))
        ttk.Button(content, text="Sair", command=self.destroy).grid(column=3, row=6, sticky=(tkinter.S, tkinter.W, tkinter.E))


        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


    def translate(self):
        try:
            x = int(self.translate_x_value.get())
        except ValueError:
            x = 0
        try:
            y = int(self.translate_y_value.get())
        except ValueError:
            y = 0
        try:
            z = int(self.translate_z_value.get())
        except ValueError:
            z = 0
        self.polyhedron.translate(x, y, z)
        self.fig_canvas.draw()

    def scale(self):
        try:
            x = int(self.scale_x_value.get())
        except ValueError:
            x = 1
        try:
            y = int(self.scale_y_value.get())
        except ValueError:
            y = 1
        try:
            z = int(self.scale_z_value.get())
        except ValueError:
            z = 1
        self.polyhedron.scale(x, y, z)
        self.fig_canvas.draw()

    def rotate(self):
        self.polyhedron.rotate(int(self.rotate_angle.get()), self.rotate_axis.get())
        self.fig_canvas.draw()

    #def reset(self):


if __name__ == '__main__':
    app = Window.windowmaker()
    app.mainloop()
