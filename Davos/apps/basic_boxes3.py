from dash import html
from dash import dcc
import dash_admin_components as dac


basic_boxes_tab3 = dac.TabItem(id='content_basic_boxes3',

                              children=html.Div(
                                  [
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="Carbon dioxide [ppm]",
                                          children=[
                                              dcc.Graph(
                                                  id='box3-graph0',
                                                  config=dict(displayModeBar=False),
                                                  #style={'width': '38vw'}
                                              )
                                          ]
                                      ),
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="Temperature [C]",
                                          children=[
                                              dcc.Graph(
                                                  id='box3-graph1',
                                                  config=dict(displayModeBar=False),
                                                  #style={'width': '38vw'}
                                              )
                                          ]
                                      ),
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="Relative Humidity [%]",
                                          children=[
                                              dcc.Graph(
                                                  id='box3-graph2',
                                                  # figure=plot_scatter_nem(),
                                                  config=dict(displayModeBar=False),
                                                  #style={'width': '38vw'}
                                              )
                                          ]
                                      )
                                  ],
                                  className='row'
                              )
                              )
