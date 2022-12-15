from dash import html
from dash import dcc
import dash_admin_components as dac

# from example_plots import plot_scatter_hum
# from example_plots import plot_scatter_temp

basic_boxes_tab_all = dac.TabItem(id='content_basic_boxes_all',

                              children=html.Div(
                                  [
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="Carbon dioxide",
                                          children=[
                                              dcc.Graph(
                                                  id='box-graph0',
                                                  config=dict(displayModeBar=False),
                                                  style={'width': '38vw'}
                                              )
                                          ]
                                      ),
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
                                      ),
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="PM1.0",
                                          children=[
                                              dcc.Graph(
                                                  id='box-graph3',
                                                  config=dict(displayModeBar=False),
                                                  style={'width': '38vw'}
                                              )
                                          ]
                                      ),
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="PM2.5",
                                          children=[
                                              dcc.Graph(
                                                  id='box-graph4',
                                                  # figure=plot_scatter_nem(),
                                                  config=dict(displayModeBar=False),
                                                  style={'width': '38vw'}
                                              )
                                          ]
                                      ),
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="PM10",
                                          children=[
                                              dcc.Graph(
                                                  id='box-graph5',
                                                  # figure=plot_scatter_nem(),
                                                  config=dict(displayModeBar=False),
                                                  style={'width': '38vw'}
                                              )
                                          ]
                                      ),
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="Volatile Organic Compounds",
                                          children=[
                                              dcc.Graph(
                                                  id='box-graph6',
                                                  config=dict(displayModeBar=False),
                                                  style={'width': '38vw'}
                                              )
                                          ]
                                      ),
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="Nitrogen Oxides",
                                          children=[
                                              dcc.Graph(
                                                  id='box-graph7',
                                                  # figure=plot_scatter_nem(),
                                                  config=dict(displayModeBar=False),
                                                  style={'width': '38vw'}
                                              )
                                          ]
                                      ),
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="Battery Charge",
                                          children=[
                                              dcc.Graph(
                                                  id='box-graph8',
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
