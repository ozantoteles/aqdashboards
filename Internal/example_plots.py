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


def plot_scatter_temp(time, data):
    sicaklik = go.Scatter(
        y=list(data[:, 5]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 5], [-40, 0, 15, 35, 40, 50], ["rgb(0,0,255)", "rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,0,0)", "black"]),
            # color = [np.linspace(0,500,len(data[:,15]))], #set color equal to a variable
            # color=data[:,15],
            # colorscale='Viridis',
            # color=[[0,"black"],[0.14,"rgb(0,0,255)"],[0.2,"rgb(0,255,10)"],[0.3,"rgb(255,255,0)"],[0.4,"rgb(255,120,0)"],[1.0,"rgb(255,0,0)"]],
            # color=["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)"],
            #showscale=True
        )
    )

    return dict(data=[sicaklik])

def plot_scatter_hum(time, data):
    nem = go.Scatter(
        y=list(data[:, 6]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 6], [0, 20, 40, 60, 80, 100],
                             ["rgb(255,0,0)", "rgb(0,255,10)", "rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,0,0)", "black"]),
            # color = [np.linspace(0,500,len(data[:,15]))], #set color equal to a variable
            # color=data[:,15],
            # colorscale='Viridis',
            # color=[[0,"black"],[0.14,"rgb(0,0,255)"],[0.2,"rgb(0,255,10)"],[0.3,"rgb(255,255,0)"],[0.4,"rgb(255,120,0)"],[1.0,"rgb(255,0,0)"]],
            # color=["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)"],
            # showscale=True
        )
    )
    return dict(data=[nem])

def plot_scatter_pm1(time, data):
    nem = go.Scatter(
        y=list(data[:, 1]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 1], [0, 27, 55, 155, 255, 300], ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)", "black"]),
            # color = [np.linspace(0,500,len(data[:,15]))], #set color equal to a variable
            # color=data[:,15],
            # colorscale='Viridis',
            # color=[[0,"black"],[0.14,"rgb(0,0,255)"],[0.2,"rgb(0,255,10)"],[0.3,"rgb(255,255,0)"],[0.4,"rgb(255,120,0)"],[1.0,"rgb(255,0,0)"]],
            # color=["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)"],
            # showscale=True
        )
    )
    return dict(data=[nem])

def plot_scatter_pm2_5(time, data):
    nem = go.Scatter(
        y=list(data[:, 2]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 2], [0, 27, 55, 155, 255, 300], ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)", "black"]),
            # color = [np.linspace(0,500,len(data[:,15]))], #set color equal to a variable
            # color=data[:,15],
            # colorscale='Viridis',
            # color=[[0,"black"],[0.14,"rgb(0,0,255)"],[0.2,"rgb(0,255,10)"],[0.3,"rgb(255,255,0)"],[0.4,"rgb(255,120,0)"],[1.0,"rgb(255,0,0)"]],
            # color=["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)"],
            # showscale=True
        )
    )
    return dict(data=[nem])


def plot_scatter_pm10(time, data):
    nem = go.Scatter(
        y=list(data[:, 3]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 3], [0, 27, 55, 155, 255, 300], ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)", "black"]),
            # color = [np.linspace(0,500,len(data[:,15]))], #set color equal to a variable
            # color=data[:,15],
            # colorscale='Viridis',
            # color=[[0,"black"],[0.14,"rgb(0,0,255)"],[0.2,"rgb(0,255,10)"],[0.3,"rgb(255,255,0)"],[0.4,"rgb(255,120,0)"],[1.0,"rgb(255,0,0)"]],
            # color=["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)"],
            # showscale=True
        )
    )
    return dict(data=[nem])


def plot_scatter_voc(time, data):
    nem = go.Scatter(
        y=list(data[:, 7]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 7], [0, 150, 200, 300, 400, 500],
                             ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)",
                              "black"]),
            # color = [np.linspace(0,500,len(data[:,15]))], #set color equal to a variable
            # color=data[:,15],
            # colorscale='Viridis',
            # color=[[0,"black"],[0.14,"rgb(0,0,255)"],[0.2,"rgb(0,255,10)"],[0.3,"rgb(255,255,0)"],[0.4,"rgb(255,120,0)"],[1.0,"rgb(255,0,0)"]],
            # color=["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)"],
            # showscale=True
        )
    )
    return dict(data=[nem])


def plot_scatter_nox(time, data):
    nem = go.Scatter(
        y=list(data[:, 9]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 9], [0, 200, 250, 300, 400, 500],
                             ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)",
                              "black"]),
            # color = [np.linspace(0,500,len(data[:,15]))], #set color equal to a variable
            # color=data[:,15],
            # colorscale='Viridis',
            # color=[[0,"black"],[0.14,"rgb(0,0,255)"],[0.2,"rgb(0,255,10)"],[0.3,"rgb(255,255,0)"],[0.4,"rgb(255,120,0)"],[1.0,"rgb(255,0,0)"]],
            # color=["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)"],
            # showscale=True
        )
    )
    return dict(data=[nem])


def plot_scatter_co2(time, data):
    nem = go.Scatter(
        y=list(data[:, 0]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 0], [0, 700, 1000, 1500, 2000, 5000],
                             ["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)",
                              "black"]),
            # color = [np.linspace(0,500,len(data[:,15]))], #set color equal to a variable
            # color=data[:,15],
            # colorscale='Viridis',
            # color=[[0,"black"],[0.14,"rgb(0,0,255)"],[0.2,"rgb(0,255,10)"],[0.3,"rgb(255,255,0)"],[0.4,"rgb(255,120,0)"],[1.0,"rgb(255,0,0)"]],
            # color=["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)"],
            # showscale=True
        )
    )
    return dict(data=[nem])

def plot_scatter_bat(time, data):
    nem = go.Scatter(
        y=list(data[:, 4]),

        x=list(time),
        mode='markers',
        # mode='lines',
        marker=dict(
            size=5,
            color=get_colors(data[:, 4], [0, 20, 40, 60, 80, 100],
                             ["rgb(255,0,0)", "rgb(255,120,0)", "rgb(255,255,0)", "rgb(0,255,10)", "rgb(0,0,255)", "black"]),
            # color = [np.linspace(0,500,len(data[:,15]))], #set color equal to a variable
            # color=data[:,15],
            # colorscale='Viridis',
            # color=[[0,"black"],[0.14,"rgb(0,0,255)"],[0.2,"rgb(0,255,10)"],[0.3,"rgb(255,255,0)"],[0.4,"rgb(255,120,0)"],[1.0,"rgb(255,0,0)"]],
            # color=["rgb(0,0,255)", "rgb(0,255,10)", "rgb(255,255,0)", "rgb(255,120,0)", "rgb(255,0,0)"],
            # showscale=True
        )
    )
    return dict(data=[nem])

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
