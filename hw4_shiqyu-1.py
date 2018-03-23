
####Side-loading Twitter Credentials
import json
from twython import Twython
with open('twitter-creds.json') as cred_file:
    creds = json.load(cred_file)
twitter = Twython(creds['consumer_key'], creds['consumer_secret'],
                  creds['access_token'], creds['access_token_secret'])



###Retrieve data from the Twitter API
who = "maroon5"
num_follower = 100
results = twitter.get_followers_list(screen_name = who,count = num_follower)

name = []
for i in results['users']:
    name.append(i['screen_name'])
comma_separated_string = ",".join(name)
output= twitter.lookup_user(screen_name = comma_separated_string)

followernum = []
for user in output:
    followernum.append(user['followers_count'])

combine=[[x,y]for x,y in zip(name,followernum)]
###Store the data in persistent format
import csv
with open('follower_count.csv','w') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(combine)

    
###Load the stored data from the file
with open('follower_count.csv','r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    followerlist = []
    for row in readCSV:
        if row:
            follower = row[1]
            followerlist.append(int(follower))

###and present a visualization      
nofollow = []
follow_20 = []
follow_50 = []
follow_100 = []
follow_500 = []
follow_g500 = []
for i in followerlist:
    if i==0:
        nofollow.append(i)        
    elif i<20:
        follow_20.append(i)
    elif i<50:
        follow_50.append(i)
    elif i<100:
        follow_100.append(i)
    elif i<500:
        follow_500.append(i)
    elif i>=500:
        follow_g500.append(i)
count = [len(nofollow),len(follow_20),
         len(follow_50),len(follow_100),
         len(follow_500),len(follow_g500)]


from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

output_file("Maroon5_followers_follower.html")

follow_range = ['0', '<=20',
                '<=50', '<=100',
                '<=500', '>500']
print(count)
source = ColumnDataSource(data=dict(follow_range=follow_range, count=count))

p = figure(x_range=follow_range, plot_height=350, toolbar_location=None, title="How many followers do Maroon 5's followers have?")
p.vbar(x='follow_range', top='count', width=0.9, source=source, legend="follow_range",
       line_color='white', fill_color=factor_cmap('follow_range', palette=Spectral6, factors=follow_range))

p.xgrid.grid_line_color = None
p.y_range.start = 0
p.y_range.end = 80
p.legend.orientation = "horizontal"
p.legend.location = "top_center"

show(p)
    

