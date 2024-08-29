import plotly.graph_objs as go
import numpy as np
from utilz.mock_sleep_data import get_mock_sleep_data

def plot_sleep_consistency_chart():
    current_data, _ = get_mock_sleep_data()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    sleep_hours = list(current_data.values())
    avg_sleep = np.mean(sleep_hours)
    deviations = [round(hour - avg_sleep, 2) for hour in sleep_hours]

    fig = go.Figure(go.Bar(
        x=days,
        y=deviations,
        marker=dict(color='orange'),
    ))

    fig.update_layout(
        title="Sleep Duration Consistency (Deviation from Average)",
        xaxis_title="Days",
        yaxis_title="Deviation (Hours)",
        yaxis=dict(range=[min(deviations) - 1, max(deviations) + 1]),
    )

    return fig