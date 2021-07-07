from math import sin
from kivy.app import App
from kivy.uix.widget import Widget
from kivy_garden.graph import Graph, MeshLinePlot
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.label import Label

#class GraphxtData(Widget):
#    pass

class GraphxtApp(App):
    def build(self):
#        lbl = Label(text ="Hello World!")
#        return lbl
        b = BoxLayout(orientation='vertical')
        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                  x_ticks_major=25, y_ticks_major=1,
                  y_grid_label=True, x_grid_label=True, padding=5,
                  x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
        plot = MeshLinePlot(color=[1, 0, 0, 1])
        plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        graph.add_plot(plot)
        b.add_widget (graph)
        return b
#        return GraphxtData()

if __name__ == '__main__':
    GraphxtApp().run()
