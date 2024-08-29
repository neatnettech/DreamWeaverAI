import plotly.graph_objs as go
from utilz.mock_sleep_data import get_last_night_sleep_distribution

def plot_sleep_distribution_chart():
    sleep_distribution = get_last_night_sleep_distribution()

    time_labels = list(sleep_distribution.keys())
    sleep_states = list(sleep_distribution.values())

    colors = {"Awake": "red", "Light Sleep": "yellow", "Deep Sleep": "blue", "REM": "purple"}
    colors_mapped = [colors[state] for state in sleep_states]

    fig = go.Figure(go.Bar(
        x=time_labels,
        y=[1] * len(sleep_distribution),
        marker=dict(color=colors_mapped),
        text=sleep_states,
        hoverinfo="text",
    ))
    fig.update_layout(
        yaxis=dict(showticklabels=False),
        title="Sleep State Distribution Over Time"
    )

    return fig