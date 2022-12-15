 
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

from example_plots import plot_scatter_temp, plot_scatter_hum, plot_scatter_pm1, plot_scatter_pm2_5, plot_scatter_pm10, \
    plot_scatter_voc, plot_scatter_nox, plot_scatter_co2, plot_scatter_bat

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

#applianceID_cansinhoca = "F999964903236707560225"
applianceID_aio = "F999914256286571835718" # davos
#applianceID_aio = "F999930444469872072597" #nly1
#applianceID_aio = "F999904805674944622288"
#applianceID_aio = "F999946606470865153433" # bahce
#applianceID_aio = "F999952074267397637271"
#applianceID_aio = "F999957849119247990869"


# =============================================================================
# Functions
# =============================================================================

def prepareSingleDevData(applianceID):
    import time
    nowMillis = int(round(time.time() * 1000))
    now = int(round(time.time()))
    h1Millis = 3600000
    h1 = 3600
    startTimeMillis = nowMillis - h1Millis * 24
    startTime = now - h1 * 24
    endTime = now
    endTimeMillis = nowMillis

    response = table.query(TableName='CAirAirQualitySensorHistoryTable',
                           KeyConditionExpression=Key('applianceId').eq(applianceID) & Key('timestamp').gte(startTime))

    data = response['Items']

    print("devID: ", applianceID)
    print("startTime: ", startTime)
    print("endTime: ", endTime)
    print(data[-1])
    print("len(data): ", len(data))

    parsed = []
    times = []
    errortimes = []
    for i in range(len(data)):
        try:
            # print("type(data[i]['timestamp']): ",type(data[i]['timestamp']))
            # print("data[i]['timestamp']: ",data[i]['timestamp'])
            # print("#####################")
            ts = float(data[i]['timestamp'])  # ['N']
            # tsj = json.loads(ts)
            time = pd.to_datetime(ts, unit='s') + timedelta(hours=3)
            # co2=float(data[i]['payload']['M']['data']['M']['functions']['L'][0]['M']['val']['N'])
            # CAIRCO2LEVEL=float(data[i]['payload']['M']['data']['M']['functions']['L'][0]['M']['val']['N'])
            # print("#####################")
            # print("data: ", data, type(data)) #list
            # print("data[i]: ", data[i], type(data[i])) #disct
            # print("data[i]['payload']: ", data[i]['payload'], type(data[i]['payload'])) #str
            # print("#####################")
            # print("data[i]['payload']['S']: ", data[i]['payload']['S'], type(data[i]['payload']['S']))
            # print("#####################")
            payload = json.loads(data[i]['payload'])
            CAIRCO2LEVEL = payload[10]['val']
            # pm2=float(data[i]['payload']['M']['data']['M']['functions']['L'][1]['M']['val']['N'])
            #CAIRPM2008_1_0_GRIMM_LEVEL = payload[1]['val']
            #CAIRPM2008_2_5_GRIMM_LEVEL = payload[2]['val']
            #CAIRPM2008_10_GRIMM_LEVEL = payload[3]['val']
            CAIRPM2008_1_0_TSI_LEVEL = payload[12]['val']
            CAIRPM2008_2_5_TSI_LEVEL = payload[14]['val']
            CAIRPM2008_10_TSI_LEVEL = payload[16]['val']
            STT_BATTERY_LEVEL = payload[4]['val']
            # CAIRPM2008_0_3_L_LEVEL=payload[7]['val']
            #CAIRPM2008_0_5_L_LEVEL = payload[8]['val']
            #CAIRPM2008_1_0_L_LEVEL = payload[9]['val']
            #CAIRPM2008_2_5_L_LEVEL = payload[10]['val']
            #CAIRPM2008_5_L_LEVEL = payload[11]['val']
            #CAIRPM2008_10_L_LEVEL = payload[12]['val']
            # temp=float(data[i]['payload']['M']['data']['M']['functions']['L'][2]['M']['val']['N'])
            #CAIRRHTLEVEL_TEMP = payload[13]['val']
            # humid=float(data[i]['payload']['M']['data']['M']['functions']['L'][3]['M']['val']['N'])
            #CAIRRHTLEVEL_HUM = payload[14]['val']
            CAIRRHTLEVEL_EXTERNAL_TEMP = payload[24]['val']
            CAIRRHTLEVEL_EXTERNAL_HUM = payload[22]['val']
            CAIRTVOCLEVEL = payload[18]['val']
            CAIRCOLEVEL = payload[18]['val']
            #CAIRNH3LEVEL = payload[19]['val']
            CAIRNO2LEVEL = payload[20]['val']
            # voc=float(data[i]['payload']['M']['data']['M']['functions']['L'][6]['M']['val']['N'])
            # co=float(data[i]['payload']['M']['data']['M']['functions']['L'][7]['M']['val']['N'])
            # nh3=float(data[i]['payload']['M']['data']['M']['functions']['L'][8]['M']['val']['N'])
            # no2=float(data[i]['payload']['M']['data']['M']['functions']['L'][9]['M']['val']['N'])

            # parsed.append([CAIRCO2LEVEL,CAIRPM2008_1_0_GRIMM_LEVEL,temp,humid,CAIRRHTLEVEL_EXTERNAL_TEMP,CAIRRHTLEVEL_EXTERNAL_HUM,voc,co,nh3,no2])
            parsed.append(
                [CAIRCO2LEVEL, CAIRPM2008_1_0_TSI_LEVEL, CAIRPM2008_2_5_TSI_LEVEL, CAIRPM2008_10_TSI_LEVEL, STT_BATTERY_LEVEL,
                 CAIRRHTLEVEL_EXTERNAL_TEMP, CAIRRHTLEVEL_EXTERNAL_HUM, CAIRTVOCLEVEL, CAIRCOLEVEL, CAIRNO2LEVEL])
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
                    text=applianceID_aio,
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
            dac.SidebarHeader(children="Air Quality"),
            dac.SidebarMenuItem(id='tab_basic_boxes1', label='Temperature and Humidity', icon='desktop'),
            dac.SidebarMenuItem(id='tab_basic_boxes2', label='Particulate Matter', icon='suitcase'),
            dac.SidebarMenuItem(id='tab_basic_boxes3', label="VOC\'s and NOx", icon='suitcase'),
            dac.SidebarMenuItem(id='tab_basic_boxes_all', label="All", icon='suitcase'),
            dac.SidebarHeader(children="Allergens"),
            dac.SidebarMenuItem(label='Galleries', icon='cubes', children=subitems),
        ]
    ),
    title='Air Quality Dashboard',
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
        basic_boxes_tab_all,
        # value_boxes_tab,
        dac.TabItem(html.P('Gallery 1 (You can add Dash Bootstrap Components!)'),
                    id='content_gallery_1'),
        dac.TabItem(html.P('Gallery 2 (You can add Dash Bootstrap Components!)'),
                    id='content_gallery_2'),
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
# app.layout = dac.Page([navbar, sidebar, body, controlbar, footer])
app.layout = dac.Page([navbar, sidebar, body, controlbar])


# =============================================================================
# Callbacks
# =============================================================================
def activate(input_id,
             n_basic_boxes1, n_basic_boxes2, n_basic_boxes3, n_basic_boxes_all,
             n_gallery_1, n_gallery_2):
    # Depending on tab which triggered a callback, show/hide contents of app
    # if input_id == 'tab_cards' and n_cards:
    #     return True, False, False, False, False, False, False
    # elif input_id == 'tab_social_cards' and n_social_cards:
    #     return False, True, False, False, False, False, False
    # elif input_id == 'tab_tab_cards' and n_tab_cards:
    #     return False, False, True, False, False, False, False
    if input_id == 'tab_basic_boxes1' and n_basic_boxes1:
        return True, False, False, False, False, False
    elif input_id == 'tab_basic_boxes2' and n_basic_boxes2:
        return False, True, False, False, False, False
    elif input_id == 'tab_basic_boxes3' and n_basic_boxes3:
        return False, False, True, False, False, False
    elif input_id == 'tab_basic_boxes_all' and n_basic_boxes_all:
        return False, False, False, True, False, False
    elif input_id == 'tab_gallery_1' and n_gallery_1:
        return False, False, False, False, True, False
    elif input_id == 'tab_gallery_2' and n_gallery_2:
        return False, False, False, False, False, True
    else:
        return False, False, False, True, False, False  # App init


@app.callback([Output('content_basic_boxes1', 'active'),
               Output('content_basic_boxes2', 'active'),
               Output('content_basic_boxes3', 'active'),
               Output('content_basic_boxes_all', 'active'),
               Output('content_gallery_1', 'active'),
               Output('content_gallery_2', 'active')],
              [Input('tab_basic_boxes1', 'n_clicks'),
               Input('tab_basic_boxes2', 'n_clicks'),
               Input('tab_basic_boxes3', 'n_clicks'),
               Input('tab_basic_boxes_all', 'n_clicks'),
               Input('tab_gallery_1', 'n_clicks'),
               Input('tab_gallery_2', 'n_clicks')]
              )
def display_tab(n_basic_boxes1, n_basic_boxes2, n_basic_boxes3, n_basic_boxes_all,
                n_gallery_1, n_gallery_2):
    ctx = dash.callback_context  # Callback context to recognize which input has been triggered

    # Get id of input which triggered callback  
    if not ctx.triggered:
        raise PreventUpdate
    else:
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]

    return activate(input_id,
                    n_basic_boxes1, n_basic_boxes2, n_basic_boxes3, n_basic_boxes_all,
                    n_gallery_1, n_gallery_2)


@app.callback([Output('tab_basic_boxes1', 'active'),
               Output('tab_basic_boxes2', 'active'),
               Output('tab_basic_boxes3', 'active'),
               Output('tab_basic_boxes_all', 'active'),
               Output('tab_gallery_1', 'active'),
               Output('tab_gallery_2', 'active')],
              [Input('tab_basic_boxes1', 'n_clicks'),
               Input('tab_basic_boxes2', 'n_clicks'),
               Input('tab_basic_boxes3', 'n_clicks'),
               Input('tab_basic_boxes_all', 'n_clicks'),
               Input('tab_gallery_1', 'n_clicks'),
               Input('tab_gallery_2', 'n_clicks')]
              )
def activate_tab(n_basic_boxes1, n_basic_boxes2, n_basic_boxes3, n_basic_boxes_all,
                 n_gallery_1, n_gallery_2):
    ctx = dash.callback_context  # Callback context to recognize which input has been triggered

    # Get id of input which triggered callback  
    if not ctx.triggered:
        raise PreventUpdate
    else:
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]

    return activate(input_id,
                    n_basic_boxes1, n_basic_boxes2, n_basic_boxes3, n_basic_boxes_all,
                    n_gallery_1, n_gallery_2)


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
    Output('box-graph0', 'figure'),
    Output('box-graph1', 'figure'),
    Output('box-graph2', 'figure'),
    Output('box-graph3', 'figure'),
    Output('box-graph4', 'figure'),
    Output('box-graph5', 'figure'),
    Output('box-graph6', 'figure'),
    Output('box-graph7', 'figure'),
    Output('box-graph8', 'figure'),
    [Input('controlbar-slider', 'value')])
def update_box_graph(value):
    errTime, time, data = prepareSingleDevData(applianceID_aio)
    return plot_scatter_co2(time, data), plot_scatter_temp(time, data), plot_scatter_hum(time, data), plot_scatter_pm1(time, data), plot_scatter_pm2_5(time, data), plot_scatter_pm10(time, data), plot_scatter_voc(time, data), plot_scatter_nox(time, data), plot_scatter_bat(time, data)

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
    app.run_server(debug=True, host='0.0.0.0', port=9090)
