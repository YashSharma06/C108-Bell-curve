import csv
import pandas as pd
import plotly.figure_factory as ff

cd = pd.read_csv("height-weight.csv")

fig = ff.create_distplot([cd["Height(Inches)"].tolist()],["Range"], show_hist = False)

fig.show()


