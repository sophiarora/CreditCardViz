import numpy as np
import pandas as pd


credit_card = pd.read_csv('creditcard_viz.csv', encoding = 'utf-8')
from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import row, widgetbox
from bokeh.models import Select, CategoricalColorMapper
from bokeh.application.handlers import FunctionHandler
from bokeh.palettes import Spectral5
from bokeh.plotting import curdoc, figure
from bokeh.application import Application
from sklearn.preprocessing import MinMaxScaler
#from bokeh.palettes import RdYlGn

#output_notebook()
df = credit_card.copy()
scale = MinMaxScaler()
#COLORS = Spectral5
#define color
df['color'] = np.where(df['Class'] == 0, 'grey', 'orange')
df['size'] = scale.fit_transform(df['Amount'].values.reshape(-1, 1)).ravel()*100
df['type'] = np.where(df['Class'] == 0, 'Normal', 'Fraud')
# data cleanup
del df['Time']
del df['Class']

columns = sorted(df.columns[0:28])


def create_figure():
    """function for interactive actions"""
    def update_frame():
        if transaction.value == 'both':
            return df
        elif transaction.value =='Normal':
            return df[df['type'] == 'Normal']
        else:
            return df[df['type'] == 'Fraud']

    df_plot = update_frame()
    xs = df_plot[x.value].values
    ys = df_plot[y.value].values
    plot_color = df_plot['color'].values
    plot_size = df_plot['size'].values
    x_title = x.value.title()
    y_title = y.value.title()
    tran_title = transaction.value.title()

    kw = dict()
    kw['title'] = "%s vs %s with %s transactions" % (x_title, y_title, tran_title)

    p = figure(plot_height=600, plot_width=800, tools='pan,box_zoom,reset', **kw, \
                  x_range = (min(df[x.value].values), max(df[x.value].values)),\
                  y_range = (min(df[y.value].values), max(df[y.value].values)))
    #added x range and y range so the plot range will not change when transaction type changes
    p.xaxis.axis_label = x_title
    p.yaxis.axis_label = y_title

    #color_mapper = CategoricalColorMapper(factors=["normal", "fraud"], palette=["pink", "yellow"])

    p.circle(x=xs, y=ys, color = plot_color, line_color="white", \
                alpha=0.6, hover_color='white', hover_alpha=0.5, size = plot_size)

    return p


def update(attr, old, new):
    layout.children[1] = create_figure()
    #push updates to notebook
    push_notebook()

    #define xs
x = Select(title='X-Axis', value='V1', options=columns)
x.on_change('value', update)

y = Select(title='Y-Axis', value='V2', options=columns)
y.on_change('value', update)

transaction = Select(title='Transaction Type', value='both', options=['Normal', 'Fraud', 'both'])
transaction.on_change('value', update)

controls = widgetbox([x, y, transaction], width=200)
layout = row(controls, create_figure())
curdoc().add_root(layout)
curdoc().title = "creditcard"
