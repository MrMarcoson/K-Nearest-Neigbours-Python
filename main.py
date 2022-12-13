import math
import os

import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.colors import ListedColormap

listed_colors = ['magenta', 'cyan', 'green', 'yellow', 'red', 'blue']
colors = ListedColormap(listed_colors)


class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)


def map_class_to_color(value):
    return listed_colors[value - 1]


def onclick(event, window, ax, x1, x2, y, c, metric, vote, neighbours):
    if len(ax.collections) > 1:
        ax.collections[2].remove()
        ax.collections[1].remove()

    click_x, click_y = event.xdata, event.ydata

    closest = []
    for record_x1, record_x2, record_y, record_c in zip(x1, x2, y, c):
        if metric:
            dist = math.sqrt(pow(click_x - record_x1, 2) + pow(click_y - record_x2, 2))
        else:
            dist = abs(click_x - record_x1) + abs(click_y - record_x2)

        closest.append({"dist": dist, "x1": record_x1, "x2": record_x2, "y": record_y, "c": record_c})

    #Posortowanie i wybranie k sąsiadów (dodaje kazdego z taka sama odlegloscia)
    closest = sorted(closest, key=lambda record: record["dist"])

    v = []
    if neighbours > len(closest):
        v = closest
    else:
        v = closest[:neighbours]

    classes = {}
    for record in v:
        if vote:
            if record["y"] not in classes.keys():
                classes[record["y"]] = 1
            else:
                classes[record["y"]] += 1

        else:
            if record["y"] not in classes.keys():
                classes[record["y"]] = 1 / pow(record["dist"], 2)
            else:
                classes[record["y"]] += 1 / pow(record["dist"], 2)

    winner = max(classes, key=lambda k: classes[k])

    x1 = [record["x1"] for record in v]
    x2 = [record["x2"] for record in v]
    y = [record["y"] for record in v]
    dist = [record["dist"] for record in v]

    ax.scatter(x1, x2, c="black", marker='v')
    ax.scatter(click_x, click_y, c=map_class_to_color(winner), marker='s')
    ax.figure.canvas.draw_idle()
    window["-CLASS-"].update(value=winner)
    window["-TABLE-"].update(values = [[x1, x2, y, dist] for x1, x2, y, dist in zip(x1, x2, y, dist)])


def create_gui():
    sg.theme('Black')
    k = [x for x in range(1, 21)]

    layout = [[sg.Text('Algorytm k-sąsiadów')],
              [sg.Text('Marek Kasprowicz')],
              [sg.Text('')],
              [sg.Text('Liczba sąsiadów'), sg.Combo(k, key='-NEIGHBOURS-', default_value=1, change_submits=True)],
              [sg.Text('Rodzaj metryki'), sg.Radio("Euklidesowa", "METRIC", key="-METRIC-", default=True, change_submits=True), sg.Radio("Miejska", "METRIC", default=False, change_submits=True)],
              [sg.Text('Rodzaj głosowania'), sg.Radio("Prosty", "VOTE", key="-VOTE-", default=True, change_submits=True), sg.Radio("Ważony", "VOTE", default=False, change_submits=True)],
              [sg.Input(), sg.FileBrowse(key="-IN-")],
              [sg.Button('Submit')],
              [sg.Canvas(key="-TOOLBAR-")],
              [sg.Canvas(key="-CANVAS-")],
              [sg.Text('Klasa zaznaczenia: '), sg.Input(text_color="black", key="-CLASS-", disabled=True)],
              [sg.Table(headings=["x1", 'x2', "y", "dist"], values=[], key="-TABLE-", col_widths = [20, 20, 10, 30], auto_size_columns = False)]]

    window = sg.Window('Algorytm k-najbliższych sąsiadów', layout, finalize=True)

    fig, ax = get_figure_template()
    draw_figure_w_toolbar(window["-CANVAS-"].TKCanvas, fig, window["-TOOLBAR-"].TKCanvas)

    while True:
        event, values = window.read()
        metric, vote, neighbours, data = get_input(values)

        if event == sg.WIN_CLOSED:
            break

        elif event == "Submit":
            clear_figure(ax)
            plt.cla()

            metric, vote, neighbours, data = get_input(values)
            if data is None:
                continue

            x1, x2, y, c = get_figure(ax, data)
            fig.canvas.mpl_connect('button_press_event', lambda point: onclick(point, window, ax, x1, x2, y, c, metric, vote, neighbours))
            draw_figure_w_toolbar(window["-CANVAS-"].TKCanvas, fig, window["-TOOLBAR-"].TKCanvas)

        elif event == "Cancel":
            clear_figure(ax)
            plt.cla()
            draw_figure_w_toolbar(window["-CANVAS-"].TKCanvas, fig, window["-TOOLBAR-"].TKCanvas)

    window.close()


def get_input(values):
    metric = values["-METRIC-"]
    vote = values["-VOTE-"]
    neighbours = int(values["-NEIGHBOURS-"])
    data = get_data(values["-IN-"])

    return metric, vote, neighbours, data


def get_data(input):
    if os.path.isfile(input) is False:
        return None

    file = open(input, "r")
    data = []

    for line in file:
        text = line.split(",")
        record = {
            "x1": float(text[0]),
            "x2": float(text[1]),
            "y": int(text[2]),
        }

        data.append(record)

    return data


def normalize_data(values):
    normalized = []
    min_value = min(values)
    max_value = max(values)

    for record in values:
        normalized.append(round(2 * (record - min_value) / (max_value - min_value) - 1, 3))

    return normalized


def get_figure(ax, values):
    if len(values) == 0:
        return plt.figure()

    x1 = [record["x1"] for record in values]
    x2 = [record["x2"] for record in values]
    y = [record["y"] for record in values]
    c = [map_class_to_color(record["y"]) for record in values]

    x1 = normalize_data(x1)
    x2 = normalize_data(x2)

    classes = list(np.unique(np.array(y)))
    scatter = ax.scatter(x1, x2, c=c)
    plt.xlabel("X1")
    plt.ylabel("X2")
    #Kolory się zepsuły podczas rysowania sąsiadów, nie mogę włączyć legendy przez to
    #plt.legend(handles=scatter.legend_elements()[0], labels=classes, loc="upper left", title="Y")

    return x1, x2, y, c


def get_figure_template():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.xlabel("x1")
    plt.ylabel("x2")
    return fig, ax


def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()

    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()

    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()

    figure_canvas_agg.get_tk_widget().pack(side = "right", fill = "both", expand = 1)


def clear_figure(ax):
    if len(ax.collections) > 0:
        ax.collections.clear()


if __name__ == '__main__':
    create_gui()

