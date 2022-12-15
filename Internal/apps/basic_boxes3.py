from dash import html
from dash import dcc
import dash_admin_components as dac

# from example_plots import plot_scatter
# from example_plots import plot_scatter_nem

basic_boxes_tab3 = dac.TabItem(id='content_basic_boxes3',

                              children=html.Div(
                                  [
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
                                      )
                                  ],
                                  className='row'
                              )
                              )
