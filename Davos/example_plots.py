import numpy as np
import pandas as pd

import plotly.graph_objs as go


#def get_colors(values, lims, colors=["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)", "black"]):
def get_colors(values, lims, colors=["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)", "black"]):
    resultingColors = [colors[0] if lims[0] < value < lims[1] else
                       colors[1] if lims[1] < value < lims[2] else
                       colors[2] if lims[2] < value < lims[3] else
                       colors[3] if lims[3] < value < lims[4] else
                       colors[4] if lims[4] < value < lims[5] else
                       colors[5] for value in values]
    #print(resultingColors)
    return resultingColors


def plot_pie():
    labels = ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
    values = [4500, 2500, 1053, 500]
    colors = ['#FEBFB3', '#E1396C', '#96D38C', '#D0F9B1']

    trace = go.Pie(labels=labels, values=values,
                   hoverinfo='label+percent', textinfo='value',
                   textfont=dict(size=20),
                   marker=dict(colors=colors,
                               line=dict(color='#000000', width=2)))

    return dict(data=[trace])


def plot_scatter1_temp(time, data):
    temp = go.Scatter(
        y=list(data[:, 5]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 5].astype(float), [-40, 0, 15, 35, 40, 50], ["rgb(0,0,255)", "rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,0,0)", "black"]),

        )
    )

    return dict(data=[temp])

def plot_scatter1_hum(time, data):
    hum = go.Scatter(
        y=list(data[:, 6]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 6].astype(float), [0, 20, 40, 60, 80, 100],
                             ["rgb(255,0,0)", "rgb(0,255,10)", "rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,0,0)", "black"]),

        )
    )
    return dict(data=[hum])

def plot_scatter1_pm1(time, data):
    pm1 = go.Scatter(
        y=list(data[:, 1]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 1].astype(float), [0, 27, 55, 155, 255, 300], ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)", "black"]),

        )
    )
    return dict(data=[pm1])

def plot_scatter1_pm2_5(time, data):
    pm2_5 = go.Scatter(
        y=list(data[:, 2]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 2].astype(float), [0, 27, 55, 155, 255, 300], ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)", "black"]),

        )
    )
    return dict(data=[pm2_5])


def plot_scatter1_pm10(time, data):
    pm10 = go.Scatter(
        y=list(data[:, 3]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 3].astype(float), [0, 27, 55, 155, 255, 300], ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)", "black"]),

        )
    )
    return dict(data=[pm10])


def plot_scatter1_voc(time, data):
    voc = go.Scatter(
        y=list(data[:, 7]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 7].astype(float), [0, 150, 200, 300, 400, 500],
                             ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)",
                              "black"]),

        )
    )
    return dict(data=[voc])


def plot_scatter1_nox(time, data):
    nox = go.Scatter(
        y=list(data[:, 8]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 8].astype(float), [0, 200, 250, 300, 400, 500],
                             ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)",
                              "black"]),

        )
    )
    return dict(data=[nox])


def plot_scatter1_co2(time, data):
    #print(type(data[:, 0][0]))
    #print("float(data[:, 0]) -> ", data[:, 0].astype(float))
    co2 = go.Scatter(
        y=list(data[:, 0]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 0].astype(float), [0, 700, 1000, 1500, 2000, 5000],
                             ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)",
                              "black"]),

        )
    )
    return dict(data=[co2])
    

def plot_scatter1_bat(time, data):
    bat = go.Scatter(
        y=list(data[:, 4]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 4].astype(float), [0, 20, 40, 60, 80, 100],
                             ["rgb(255,0,0)", "rgb(255,120,0)", "rgb(255,255,0)", "rgb(0,255,10)", "rgb(0,0,255)", "black"]),

        )
    )
    return dict(data=[bat])
    
def plot_scatter2_temp(time, data):
    temp = go.Scatter(
        y=list(data[:, 5]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 5], [-40, 0, 15, 35, 40, 50], ["rgb(0,0,255)", "rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,0,0)", "black"]),

        )
    )

    return dict(data=[temp])

def plot_scatter2_hum(time, data):
    hum = go.Scatter(
        y=list(data[:, 6]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 6], [0, 20, 40, 60, 80, 100],
                             ["rgb(255,0,0)", "rgb(0,255,10)", "rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,0,0)", "black"]),

        )
    )
    return dict(data=[hum])

def plot_scatter2_pm1(time, data):
    pm1 = go.Scatter(
        y=list(data[:, 1]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 1], [0, 27, 55, 155, 255, 300], ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)", "black"]),

        )
    )
    return dict(data=[pm1])

def plot_scatter2_pm2_5(time, data):
    pm2_5 = go.Scatter(
        y=list(data[:, 2]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 2], [0, 27, 55, 155, 255, 300], ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)", "black"]),

        )
    )
    return dict(data=[pm2_5])


def plot_scatter2_pm10(time, data):
    pm10 = go.Scatter(
        y=list(data[:, 3]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 3], [0, 27, 55, 155, 255, 300], ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)", "black"]),

        )
    )
    return dict(data=[pm10])


def plot_scatter2_voc(time, data):
    voc = go.Scatter(
        y=list(data[:, 7]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 7], [0, 150, 200, 300, 400, 500],
                             ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)",
                              "black"]),

        )
    )
    return dict(data=[voc])


def plot_scatter2_nox(time, data):
    nox = go.Scatter(
        y=list(data[:, 8]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 8], [0, 200, 250, 300, 400, 500],
                             ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)",
                              "black"]),

        )
    )
    return dict(data=[nox])


def plot_scatter2_co2(time, data):
    co2 = go.Scatter(
        y=list(data[:, 0]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 0].astype(float), [0, 700, 1000, 1500, 2000, 5000],
                             ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)",
                              "black"]),

        )
    )
    return dict(data=[co2])
    
def plot_scatter2_hcho(time, data):
    hcho = go.Scatter(
        y=list(data[:, 9]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 9], [0, 700, 1000, 1500, 2000, 5000],
                             ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)",
                              "black"]),

        )
    )
    return dict(data=[hcho])

def plot_scatter2_bat(time, data):
    bat = go.Scatter(
        y=list(data[:, 4]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 4], [0, 20, 40, 60, 80, 100],
                             ["rgb(255,0,0)", "rgb(255,120,0)", "rgb(255,255,0)", "rgb(0,255,10)", "rgb(0,0,255)", "black"]),

        )
    )
    return dict(data=[bat])

def plot_scatter3_co2(time, data):
    co2 = go.Scatter(
        y=list(data[:, 0]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 0].astype(float), [0, 700, 1000, 1500, 2000, 5000],
                             ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)",
                              "black"]),

        )
    )
    return dict(data=[co2])

def plot_scatter3_temp(time, data):
    temp = go.Scatter(
        y=list(data[:, 1]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 1].astype(float), [-40, 0, 15, 35, 40, 50], ["rgb(0,0,255)", "rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,0,0)", "black"]),

        )
    )

    return dict(data=[temp])

def plot_scatter3_hum(time, data):
    hum = go.Scatter(
        y=list(data[:, 2]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 2].astype(float), [0, 20, 40, 60, 80, 100],
                             ["rgb(255,0,0)", "rgb(0,255,10)", "rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,0,0)", "black"]),

        )
    )
    return dict(data=[hum])

def plot_surface():
    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

    data = [
        go.Surface(
            z=z_data.values,
            contours=go.surface.Contours(
                z=go.surface.contours.Z(
                    show=True,
                    usecolormap=True,
                    highlightcolor="#42f462",
                    project=dict(z=True)
                )
            )
        )
    ]
    layout = go.Layout(
        title='Mt Bruno Elevation',
        scene=dict(camera=dict(eye=dict(x=1.87, y=0.88, z=-0.64))),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(
            l=35,
            r=20,
            b=35,
            t=45
        )
    )
    return go.Figure(data=data, layout=layout)
