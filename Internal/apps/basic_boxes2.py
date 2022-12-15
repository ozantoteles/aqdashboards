from dash import html
from dash import dcc
import dash_admin_components as dac

# from example_plots import plot_scatter
# from example_plots import plot_scatter_nem

basic_boxes_tab2 = dac.TabItem(id='content_basic_boxes2',

                              children=html.Div(
                                  [
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
                                      )
                                  ],
                                  className='row'
                              )
                              )
