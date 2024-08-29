import plotly.express as px
from utilz.mock_sleep_data import get_last_night_sleep_phases

def plot_sleep_phases_chart():
    sleep_phases = get_last_night_sleep_phases()

    fig = px.pie(names=sleep_phases.keys(), values=sleep_phases.values(),
                 title="Time Spent in Each Sleep Phase", hole=0.3)
    fig.update_traces(textinfo='label+percent', insidetextorientation='radial')

    return fig