from dash import html
from dash import dcc
import dash_admin_components as dac

# from example_plots import plot_scatter_hum
# from example_plots import plot_scatter_temp

basic_boxes_tab1 = dac.TabItem(id='content_basic_boxes1',

                              children=html.Div(
                                  [
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="Temperature",
                                          children=[
                                              dcc.Graph(
                                                  id='box-graph1',
                                                  config=dict(displayModeBar=False),
                                                  style={'width': '38vw'}
                                              )
                                          ]
                                      ),
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="Relative Humidity",
                                          children=[
                                              dcc.Graph(
                                                  id='box-graph2',
                                                  # figure=plot_scatter_nem(),
                                                  config=dict(displayModeBar=False),
                                                  style={'width': '38vw'}
                                              )
                                          ]
                                      )
                                  ],
                                  className='row'
                              )
                              )
