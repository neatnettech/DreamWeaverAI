import plotly.graph_objs as go

def plot_sleep_latency_chart():
    sleep_latency = {
        "Monday": 15,
        "Tuesday": 20,
        "Wednesday": 10,
        "Thursday": 25,
        "Friday": 30,
        "Saturday": 12,
        "Sunday": 18
    }

    days = list(sleep_latency.keys())
    latency_values = list(sleep_latency.values())

    fig = go.Figure(go.Bar(
        x=days,
        y=latency_values,
        marker=dict(color='purple'),
    ))

    fig.update_layout(
        title="Sleep Latency (Time to Fall Asleep)",
        xaxis_title="Days",
        yaxis_title="Minutes",
        yaxis=dict(range=[0, max(latency_values) + 5]),
    )

    return fig