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
        #frm = ttk.Frame(self, padding=10)
        self.title('Nao Sei')
        fig = figure.Figure()
        fig_canvas = backend_tkagg.FigureCanvasTkAgg(fig, self)
        calculator.TenPointPolyhedron.create(fig)
        fig_canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


if __name__ == '__main__':
    app = Window.windowmaker()
    app.mainloop()
