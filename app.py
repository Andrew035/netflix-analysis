import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("netflix_titles.csv")
df.dropna(subset=["type", "release_year", "country", "listed_in"], inplace=True)
df["country"] = df["country"].str.split(", ").str[0]  # Use first listed country
df["listed_in"] = df["listed_in"].str.split(", ").str[0]  # Use first genre

# Init Dash app
app = dash.Dash(__name__)
app.title = "Netflix Data Dashboard"

# App layout
app.layout = html.Div(
    [
        html.H1("🎬 Netflix Data Dashboard", style={"textAlign": "center"}),
        html.Div(
            [
                html.Label("Select Content Type:"),
                dcc.Dropdown(
                    id="type-dropdown",
                    options=[{"label": t, "value": t} for t in df["type"].unique()],
                    value="Movie",
                    clearable=False,
                ),
            ],
            style={"width": "30%", "margin": "auto"},
        ),
        dcc.Graph(id="content-over-time"),
        dcc.Graph(id="top-countries"),
        dcc.Graph(id="genre-distribution"),
    ]
)


# Callbacks
@app.callback(
    [
        Output("content-over-time", "figure"),
        Output("top-countries", "figure"),
        Output("genre-distribution", "figure"),
    ],
    [Input("type-dropdown", "value")],
)
def update_graphs(selected_type):
    filtered_df = df[df["type"] == selected_type]

    # Content over time
    content_by_year = (
        filtered_df.groupby("release_year").size().reset_index(name="count")
    )
    fig1 = px.line(
        content_by_year,
        x="release_year",
        y="count",
        title=f"{selected_type}s Released Over Time",
    )

    # Top 10 countries
    top_countries = filtered_df["country"].value_counts().nlargest(10).reset_index()
    top_countries.columns = ["country", "count"]
    fig2 = px.bar(
        top_countries,
        x="country",
        y="count",
        title=f"Top 10 Countries Producing {selected_type}s",
    )

    # Genre distribution
    top_genres = filtered_df["listed_in"].value_counts().nlargest(8).reset_index()
    top_genres.columns = ["genre", "count"]
    fig3 = px.pie(
        top_genres,
        names="genre",
        values="count",
        title=f"Genre Breakdown of {selected_type}s",
    )

    return fig1, fig2, fig3


# Run app
if __name__ == "__main__":
    app.run(debug=True)
