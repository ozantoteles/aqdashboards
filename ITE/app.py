 
import dash
from dash.dependencies import Input, Output

from dash import html
from dash import dcc
import dash_admin_components as dac

from dash.exceptions import PreventUpdate

from apps.cards import cards_tab
from apps.social_cards import social_cards_tab
from apps.tab_cards import tab_cards_tab
from apps.basic_boxes_all import basic_boxes_tab_all
from apps.basic_boxes1 import basic_boxes_tab1
from apps.basic_boxes2 import basic_boxes_tab2
from apps.basic_boxes3 import basic_boxes_tab3
from apps.value_boxes import value_boxes_tab

from example_plots import plot_scatter1_temp, plot_scatter1_hum, plot_scatter1_pm1, plot_scatter1_pm2_5, plot_scatter1_pm10, plot_scatter1_voc, plot_scatter1_nox, plot_scatter1_co2, plot_scatter1_bat, plot_scatter2_bat, plot_scatter2_co2,  plot_scatter2_hum, plot_scatter2_nox, plot_scatter2_pm1, plot_scatter2_pm10, plot_scatter2_pm2_5, plot_scatter2_temp, plot_scatter2_voc, plot_scatter3_bat, plot_scatter3_co2,  plot_scatter3_hum, plot_scatter3_nox, plot_scatter3_pm1, plot_scatter3_pm10, plot_scatter3_pm2_5, plot_scatter3_temp, plot_scatter3_voc

from apps.tab_cards import text_1, text_2, text_3

import boto3
from boto3.dynamodb.conditions import Key
import json
from datetime import timedelta
import pandas as pd
import numpy as np
import json

# =============================================================================
# Boto and DynamoDB Table Connection
# =============================================================================

with open('cred.json', 'r') as login_file:
    login = json.load(login_file)

dynamodb = boto3.resource('dynamodb', aws_access_key_id=login["aws_access_key_id"],
                          aws_secret_access_key=login["aws_secret_access_key"], region_name=login["region_name"])
table = dynamodb.Table('CAirAirQualitySensorHistoryTable')

applianceID_20500023 = "F999926119979744638157"
applianceID_20800007 = "F999957025223178249265"
applianceID_20500025 = "F999998675609486879710"


# =============================================================================
# Functions
# =============================================================================


def prepareSingleDevData_cair(applianceID):
    import time
    nowMillis = int(round(time.time() * 1000))
    now = int(round(time.time()))
    h1Millis = 3600000
    h1 = 3600
    startTimeMillis = nowMillis - h1Millis * 48
    startTime = now - h1 * 48
    endTime = now
    endTimeMillis = nowMillis

    response = table.query(TableName='CAirAirQualitySensorHistoryTable',
                           KeyConditionExpression=Key('applianceId').eq(applianceID) & Key('timestamp').gte(startTime))

    data = response['Items']

    print("###############")
    print("cair devID: ", applianceID)
    print("startTime: ", startTime)
    print("endTime: ", endTime)
    #print(data[0])
    print("len(data): ", len(data))
    print("###############")

    parsed = []
    times = []
    errortimes = []
    for i in range(len(data)):
        try:
            ts = float(data[i]['timestamp'])  # ['N']
            time = pd.to_datetime(ts, unit='s') + timedelta(hours=3)
            payload = json.loads(data[i]['payload'])
            #print(payload)
            #print(len(payload))
            CAIRCO2LEVEL = payload[10]['val']
            CAIRPM2008_1_0_TSI_LEVEL = payload[12]['val']
            CAIRPM2008_2_5_TSI_LEVEL = payload[14]['val']
            CAIRPM2008_10_TSI_LEVEL = payload[16]['val']
            STT_BATTERY_LEVEL = payload[4]['val']
            CAIRRHTLEVEL_EXTERNAL_TEMP = payload[24]['val'] #####
            CAIRRHTLEVEL_EXTERNAL_HUM = payload[22]['val']
            CAIRTVOCLEVEL = payload[18]['val']
            #CAIRCOLEVEL = payload[18]['val']
            #CAIRNH3LEVEL = payload[26]['val']
            CAIRNO2LEVEL = payload[20]['val']
            parsed.append(
                [CAIRCO2LEVEL, 
                CAIRPM2008_1_0_TSI_LEVEL, 
                CAIRPM2008_2_5_TSI_LEVEL, 
                CAIRPM2008_10_TSI_LEVEL, 
                STT_BATTERY_LEVEL, 
                CAIRRHTLEVEL_EXTERNAL_TEMP, 
                CAIRRHTLEVEL_EXTERNAL_HUM, 
                CAIRTVOCLEVEL,  
                CAIRNO2LEVEL])
            times.append(time)
        except:
            time = pd.to_datetime(float(data[i]['-']['N']), unit='s') + timedelta(hours=3)
            errortimes.append(time)

    return errortimes, times, np.array(parsed)


# =============================================================================
# Dash App and Flask Server
# =============================================================================
app = dash.Dash(__name__)
app.title = 'Air Quality Demo Dashboard'
server = app.server

# =============================================================================
# Dash Admin Components
# =============================================================================
# Navbar
right_ui = dac.NavbarDropdown(
    badge_label="!",
    badge_color="danger",
    src="https://quantee.ai",
    header_text="2 Items",
    children=[
        dac.NavbarDropdownItem(
            children="CO2 level is unhealthy",
            date="today"
        ),
        dac.NavbarDropdownItem(
            children="Low Battery",
            date="yesterday"
        ),
    ]
)

navbar = dac.Navbar(color="white",
                    text="",
                    children=right_ui)

# Sidebar ???
subitems = [dac.SidebarMenuSubItem(id='tab_gallery_1',
                                   label='Gallery 1',
                                   icon='arrow-circle-right',
                                   badge_label='Soon',
                                   badge_color='success'),
            dac.SidebarMenuSubItem(id='tab_gallery_2',
                                   label='Gallery 2',
                                   icon='arrow-circle-right',
                                   badge_label='Soon',
                                   badge_color='success')
            ]

sidebar = dac.Sidebar(
    dac.SidebarMenu(
        [
            # dac.SidebarHeader(children="Cards"),
            # dac.SidebarMenuItem(id='tab_cards', label='Basic cards', icon='box'),
            # dac.SidebarMenuItem(id='tab_social_cards', label='Social cards', icon='id-card'),
            # dac.SidebarMenuItem(id='tab_tab_cards', label='Tab cards', icon='image'),
            dac.SidebarHeader(children="Device"),
            dac.SidebarMenuItem(id='tab_basic_boxes1', label='20500023', icon='box'),
            dac.SidebarMenuItem(id='tab_basic_boxes2', label='20800007', icon='box'),
            dac.SidebarMenuItem(id='tab_basic_boxes3', label="20500025", icon='box'),
            #dac.SidebarMenuItem(id='tab_basic_boxes_all', label="All", icon='suitcase'),
            #dac.SidebarHeader(children="Allergens"),
            #dac.SidebarMenuItem(label='Galleries', icon='cubes', children=subitems),
        ]
    ),
    title='AQ Dashboard',
    skin="dark",
    color="primary",
    brand_color="primary",
    url="https://www.arcelikglobal.com",
    src="https://www.marketbeat.com/logos/ar%C3%A7elik-anonim-sirketi-logo.png",
    elevation=3,
    opacity=0.8
)

# Body
body = dac.Body(
    dac.TabItems([
        # cards_tab,
        # social_cards_tab,
        # tab_cards_tab,
        basic_boxes_tab1,
        basic_boxes_tab2,
        basic_boxes_tab3,
        #basic_boxes_tab_all,
        # value_boxes_tab,
        #dac.TabItem(html.P('Gallery 1 (You can add Dash Bootstrap Components!)'),
        #            id='content_gallery_1'),
        #dac.TabItem(html.P('Gallery 2 (You can add Dash Bootstrap Components!)'),
        #            id='content_gallery_2'),
    ])
)

# Controlbar
controlbar = dac.Controlbar(
    [
        html.Br(),
        html.P("Slide to change graph in Basic Boxes"),
        dcc.Slider(
            id='controlbar-slider',
            min=10,
            max=50,
            step=1,
            value=20
        )
    ],
    title="Settings",
    skin="dark"
)

# Footer
footer = dac.Footer(
   html.A("Arçelik Global",
          href="https://www.arcelikglobal.com",
          target="_blank",
          ),
   right_text="2022"
)

# =============================================================================
# App Layout
# =============================================================================
app.layout = dac.Page([navbar, sidebar, body, controlbar, footer])
#app.layout = dac.Page([navbar, sidebar, body, controlbar])


# =============================================================================
# Callbacks
# =============================================================================
def activate(input_id,
             n_basic_boxes1, n_basic_boxes2, n_basic_boxes3):
    if input_id == 'tab_basic_boxes1' and n_basic_boxes1:
        return True, False, False
    elif input_id == 'tab_basic_boxes2' and n_basic_boxes2:
        return False, True, False
    elif input_id == 'tab_basic_boxes3' and n_basic_boxes3:
        return False, False, True
    else:
        return False, True, False # App init


@app.callback([Output('content_basic_boxes1', 'active'),
               Output('content_basic_boxes2', 'active'),
               Output('content_basic_boxes3', 'active')],
              [Input('tab_basic_boxes1', 'n_clicks'),
               Input('tab_basic_boxes2', 'n_clicks'),
               Input('tab_basic_boxes3', 'n_clicks')]
              )
def display_tab(n_basic_boxes1, n_basic_boxes2, n_basic_boxes3):
    ctx = dash.callback_context  # Callback context to recognize which input has been triggered

    # Get id of input which triggered callback  
    if not ctx.triggered:
        raise PreventUpdate
    else:
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]

    return activate(input_id,
                    n_basic_boxes1, n_basic_boxes2, n_basic_boxes3)


@app.callback([Output('tab_basic_boxes1', 'active'),
               Output('tab_basic_boxes2', 'active'),
               Output('tab_basic_boxes3', 'active')],
              [Input('tab_basic_boxes1', 'n_clicks'),
               Input('tab_basic_boxes2', 'n_clicks'),
               Input('tab_basic_boxes3', 'n_clicks')]
              )
def activate_tab(n_basic_boxes1, n_basic_boxes2, n_basic_boxes3):
    ctx = dash.callback_context  # Callback context to recognize which input has been triggered

    # Get id of input which triggered callback  
    if not ctx.triggered:
        raise PreventUpdate
    else:
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]

    return activate(input_id,
                    n_basic_boxes1, n_basic_boxes2, n_basic_boxes3)


# @app.callback(Output('tab_box_1', 'children'),
#               [Input('tab_box_1_menu', 'active_tab')]
#               )
# def display_tabbox1(active_tab):
#     # Depending on tab which triggered a callback, show/hide contents of app
#     if active_tab == 'tab_box_1_tab1':
#         return text_1
#     elif active_tab == 'tab_box_1_tab2':
#         return text_2
#     elif active_tab == 'tab_box_1_tab3':
#         return text_3
#
#
# @app.callback(Output('tab_box_2', 'children'),
#               [Input('tab_box_2_menu', 'active_tab')]
#               )
# def display_tabbox2(active_tab):
#     # Depending on tab which triggered a callback, show/hide contents of app
#     if active_tab == 'tab_box_2_tab1':
#         return text_1
#     elif active_tab == 'tab_box_2_tab2':
#         return text_2
#     elif active_tab == 'tab_box_2_tab3':
#         return text_3


# Update figure on slider change
@app.callback(
    Output('box1-graph0', 'figure'),
    Output('box1-graph1', 'figure'),
    Output('box1-graph2', 'figure'),
    Output('box1-graph3', 'figure'),
    Output('box1-graph4', 'figure'),
    Output('box1-graph5', 'figure'),
    Output('box1-graph6', 'figure'),
    Output('box1-graph7', 'figure'),
    Output('box1-graph8', 'figure'),
    [Input('controlbar-slider', 'value')])
def update_box_graph(value):
    errTime, time, data = prepareSingleDevData_cair(applianceID_20500023)
    return plot_scatter1_co2(time, data), plot_scatter1_temp(time, data), plot_scatter1_hum(time, data), plot_scatter1_pm1(time, data), plot_scatter1_pm2_5(time, data), plot_scatter1_pm10(time, data), plot_scatter1_voc(time, data), plot_scatter1_nox(time, data), plot_scatter1_bat(time, data)

@app.callback(
    Output('box2-graph0', 'figure'),
    Output('box2-graph1', 'figure'),
    Output('box2-graph2', 'figure'),
    Output('box2-graph3', 'figure'),
    Output('box2-graph4', 'figure'),
    Output('box2-graph5', 'figure'),
    Output('box2-graph6', 'figure'),
    Output('box2-graph7', 'figure'),
    Output('box2-graph8', 'figure'),
    [Input('controlbar-slider', 'value')])
def update_box_graph(value):
    errTime, time, data = prepareSingleDevData_cair(applianceID_20800007)
    return plot_scatter2_co2(time, data), plot_scatter2_temp(time, data), plot_scatter2_hum(time, data), plot_scatter2_pm1(time, data), plot_scatter2_pm2_5(time, data), plot_scatter2_pm10(time, data), plot_scatter2_voc(time, data), plot_scatter2_nox(time, data), plot_scatter2_bat(time, data)

@app.callback(
    Output('box3-graph0', 'figure'),
    Output('box3-graph1', 'figure'),
    Output('box3-graph2', 'figure'),
    Output('box3-graph3', 'figure'),
    Output('box3-graph4', 'figure'),
    Output('box3-graph5', 'figure'),
    Output('box3-graph6', 'figure'),
    Output('box3-graph7', 'figure'),
    Output('box3-graph8', 'figure'),
    [Input('controlbar-slider', 'value')])
def update_box_graph(value):
    errTime, time, data = prepareSingleDevData_cair(applianceID_20500025)
    return plot_scatter3_co2(time, data), plot_scatter3_temp(time, data), plot_scatter3_hum(time, data), plot_scatter3_pm1(time, data), plot_scatter3_pm2_5(time, data), plot_scatter3_pm10(time, data), plot_scatter3_voc(time, data), plot_scatter3_nox(time, data), plot_scatter3_bat(time, data)

# @app.callback(
#     Output('box-graph1', 'figure'),
#     [Input('controlbar-slider', 'value')])
# def update_box_graph(value):
#     errTime, time, data = prepareSingleDevData(applianceID_aio)
#     return plot_scatter_temp(time, data)



# =============================================================================
# Run app    
# =============================================================================
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=9094)
