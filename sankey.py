import plotly.graph_objects as go


def make_sankey_plot(data, y, color=None):
    #
    # Creates the id number for each node
    id = 0
    nodes_id = {}
    for year in list(data.keys()):
        for cluster in range(len(data[year].keys())):
            key = str(year) + "." + str(cluster)
            nodes_id[key] = id
            id += 1

    #
    # years range
    starting_year = min([int(key) for key in data.keys()])
    ending_year = max([int(key) for key in data.keys()])

    #
    # Compute the link weights
    links = {}

    for year_curr in list(data.keys())[:-1]:
        #
        year_nxt = str(int(year_curr) + 1)
        for cluster_curr in range(len(data[year_curr].keys())):
            for word_curr in data[year_curr][str(cluster_curr)]:
                for cluster_nxt in range(len(data[year_nxt])):
                    for word_nxt in data[year_nxt][str(cluster_nxt)]:
                        if word_curr == word_nxt:
                            key_curr = str(year_curr) + "." + str(cluster_curr)
                            key_nxt = str(year_nxt) + "." + str(cluster_nxt)
                            key = (key_curr, key_nxt)

                            if key not in links.keys():
                                links[key] = 0
                            links[key] += 1

    #
    # Creates the variables for the sankey diagram
    source = [nodes_id[key[0]] for key in links.keys()]
    target = [nodes_id[key[1]] for key in links.keys()]
    value = list(links.values())

    label = [
        "<br>".join([t.replace("_", " ") for t in data[year][str(cluster)][:6]])
        for year in list(data.keys())
        for cluster in range(len(data[year].keys()))
    ]

    x = [
        0.025 + 0.95 * (int(year) - starting_year) / (ending_year - starting_year)
        for year in list(data.keys())
        for _ in range(len(data[year].keys()))
    ]

    for year in list(data.keys()):
        for cluster in range(len(data[year].keys())):
            key = str(year) + "." + str(cluster)
            nodes_id[key] = id
            id += 1

    fig = go.Figure(
        data=[
            go.Sankey(
                arrangement="fixed",
                node=dict(
                    pad=10,
                    thickness=10,
                    line=dict(color="black", width=0.3),
                    label=label,
                    x=x,
                    y=y,
                    color=color,
                ),
                link=dict(
                    source=source,
                    target=target,
                    value=value,
                ),
                textfont={"size": 9, "color": "black"},
            )
        ]
    )

    for x_coor, year in enumerate(data.keys()):
        if year == "2016":
            text = "2014-2016"
        else:
            text = str(year)

        fig.add_annotation(
            x=0.02 + 0.96 * x_coor / (len(data.keys()) - 1),
            y=1.05,
            xref="paper",
            yref="paper",
            text=text,
            showarrow=False,
            font=dict(
                # family="Courier New, monospace",
                size=11,
                # color="black"
            ),
            align="center",
        )

    return fig
