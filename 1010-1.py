import sqlite3
import pandas
from pprint import pprint

con = sqlite3.connect('sqmight.sqlite3')
cur = con.cursor()

cur.execute('SELECT SUM(price_each * quantity), order_id FROM order_products GROUP BY order_id')
df = pandas.DataFrame(cur.fetchall(),columns = ['SUM(price_each * quantity)','order_id'])
order = df['SUM(price_each * quantity)'].values
binned_orders = {}
def get_order_bins(order):
    if order<200:
        return 'Under $200'
    if order<=400:
        return '$200-$400'
    if order<=600:
        return '$400-$600'
    if order<=800:
        return '$600-$800'
    if order<=1000:
        return '$800-$1000'
    if order<=1500:
        return '$1000-$1500'
    if order>=1500:
        return 'Over $1500'
for o in order:
    which_bin = get_order_bins(o)
    if which_bin not in binned_orders:
        binned_orders[which_bin]=0
    binned_orders[which_bin]+=1
pprint(binned_orders)
print('most of the order value are under $200 (125 orders).')

from bokeh.io import show, output_file
from bokeh.plotting import figure


x_values = list(binned_orders.keys())
y_values = list(binned_orders.values())

fig = figure(x_range=x_values, \
 plot_height=250, \
 title="Order Value", \
 toolbar_location=None, tools="")

fig.vbar(x=x_values, top=y_values, width=0.9)

fig.xgrid.grid_line_color = None
fig.y_range.start = 0

output_file("bars.html") 
show(fig) 
