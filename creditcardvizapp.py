import numpy as np
import pandas as pd


credit_card = pd.read_csv('https://github.com/sophiarora/CreditCardViz/raw/master/creditcard_viz.csv', encoding = 'utf-8')
from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import row, widgetbox
from bokeh.models import Select, ColumnDataSource
from bokeh.plotting import curdoc, figure
from sklearn.preprocessing import MinMaxScaler
#color palette import uncomment if want to use palettes:
#from bokeh.palettes import Spectral5
##following two lines are for notebook handler uncomment if want
#to use handbook handler to view in a jupyter notebook:
#from bokeh.application.handlers import FunctionHandler
#from bokeh.application import Application

#line for notebook handler:
#output_notebook()
df = credit_card.copy()
scale = MinMaxScaler()



#define color
df['color'] = np.where(df['Class'] == 0, 'grey', 'orange')
df['size'] = scale.fit_transform(df['Amount'].values.reshape(-1, 1)).ravel()*100
df['type'] = np.where(df['Class'] == 0, 'Normal', 'Fraud')
# data cleanup
del df['Time']
del df['Class']

columns = sorted(df.columns[0:28])


def create_figure():
    """function create figure"""
    def update_frame():
        """function to update frame to plot for fraud/normal/both types
        """
        if transaction.value == 'both':
            return df
        elif transaction.value =='Normal':
            return df[df['type'] == 'Normal']
        else:
            return df[df['type'] == 'Fraud']

    df_plot = update_frame()
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

    datasource = ColumnDataSource(df_plot[[x.value, y.value, 'color', 'type', 'size']])

    p.circle(x.value, y.value, color = 'color', line_color="white", \
            alpha=0.6, hover_color='white', hover_alpha=0.5, size = 'size', \
            legend = 'type', source = datasource)

    return p


def update(attr, old, new):
    layout.children[1] = create_figure()
    #push updates to notebook
    push_notebook()

#define each interaction
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
