from icalendar import Calendar
from PyRSS2Gen import RSSItem, RSS2
import re,urllib,feedparser

ICAL_URL = 'http://www.pogdesign.co.uk/cat/download_ics/dd1cc774b062db1df0a594402f3ac10b'

url = urllib.urlopen(ICAL_URL)

cal = Calendar.from_string(url.read())
events = cal.walk('VEVENT')

p = re.compile('(.*) Episodes, TV Shows')

series = []
for event in events:
    serie = event.get('CATEGORIES')
    serie = p.match(serie).groups()[0].strip()
    series.append(serie)

series = list(set(series))
print series

# generate the rss urls
hit_list = []
for name in series:
    feed = 'http://ezrss.it/search/index.php?show_name=%s&mode=rss'%name
    hit_list.append(feed)

print hit_list

# get the feeds and join them in one big list
feeds = [feedparser.parse(rss_url) for rss_url in hit_list]
print "Found",len(feeds),"feeds."

entries = feedparser.FeedParserDict()
for feed in feeds:
    entries.update(feed)


items = [RSSItem(**item) for item in entries['items']]
feeds = RSS2(title="My series feed",description="This feed is an aggregation of various feeds",link="",items = items)
f = open('feed.xml','w')
f.write(feeds.to_xml())
f.close()


# this section is for sorting the entries
#decorated = [(entry["date_parsed"], entry) for entry in entries]
#decorated.sort()
#decorated.reverse()
#sorted = [entry for (date,entry) in decorated]

