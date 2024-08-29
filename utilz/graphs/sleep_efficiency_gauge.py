import plotly.graph_objs as go

def plot_sleep_efficiency_gauge():
    sleep_efficiency = 85

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = sleep_efficiency,
        title = {'text': "Sleep Efficiency"},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 75], 'color': "gray"},
                {'range': [75, 100], 'color': "green"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 85}}))

    return fig