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
                                      ),
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="PM1.0 [ug/m3 TSI]",
                                          children=[
                                              dcc.Graph(
                                                  id='box3-graph3',
                                                  config=dict(displayModeBar=False),
                                                  #style={'width': '38vw'}
                                              )
                                          ]
                                      ),
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="PM2.5 [ug/m3 TSI]",
                                          children=[
                                              dcc.Graph(
                                                  id='box3-graph4',
                                                  # figure=plot_scatter_nem(),
                                                  config=dict(displayModeBar=False),
                                                  #style={'width': '38vw'}
                                              )
                                          ]
                                      ),
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="PM10 [ug/m3 TSI]",
                                          children=[
                                              dcc.Graph(
                                                  id='box3-graph5',
                                                  # figure=plot_scatter_nem(),
                                                  config=dict(displayModeBar=False),
                                                  #style={'width': '38vw'}
                                              )
                                          ]
                                      ),
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="Volatile Organic Compounds [Index/500]",
                                          children=[
                                              dcc.Graph(
                                                  id='box3-graph6',
                                                  config=dict(displayModeBar=False),
                                                  #style={'width': '38vw'}
                                              )
                                          ]
                                      ),
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="Nitrogen Oxides [ppb]",
                                          children=[
                                              dcc.Graph(
                                                  id='box3-graph7',
                                                  # figure=plot_scatter_nem(),
                                                  config=dict(displayModeBar=False),
                                                  #style={'width': '38vw'}
                                              )
                                          ]
                                      ),
                                      dac.SimpleBox(
                                          style={'height': "600px"},
                                          title="Battery Charge [%]",
                                          children=[
                                              dcc.Graph(
                                                  id='box3-graph8',
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
