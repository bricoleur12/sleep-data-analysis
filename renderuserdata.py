import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/example'
db = SQLAlchemy(app)

class SleepData(db.Model):
    __tablename__ = 'sleep_data'
    User_ID
    cycle_id
    Date
    Day_of_Week
    RHR	
    HRV
    Recovery
    Sleep_Score
    Sleep_Onset
    Wake_Onset
    Hours_in_Bed
    Hours_of_Sleep
    Sleep_Need
    Sleep_Efficiency_Percentage
    Wake_Periods
    Sleep_Disturbances
    Latency_Minimum	
    Cycles
    REM_Sleep_hours
    Deep_Sleep hours
    Light_Sleep_hours
    Awake_hours	
    Missing_Data_hours
    Sleep_Debt_hours
    Sleep_Consistency
    Respiratory_Rate
    Last_Nap_End_Time
    Nap_Time_in_Bed
    Total Cycle Nap Time hours	Nap Disturbances	Nap REM	Nap SWS	Nap Light	Nap Wake	Nap Missing Data	Total Cycle Sleep Time hours	timezone_offset	REM Percentage	Deep Sleep Percentage	Restorative Sleep hours	Restorative Sleep Percentage
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
db.create_all()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

renderuserdata = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

renderuserdata.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    renderuserdata.run_server(dev_tools_hot_reload=False)
