from requests import get
from pprint import pprint
from json import dump, loads
from os import listdir, system
from csv import writer, QUOTE_MINIMAL

# system('mkdir -p commonallplayers')
# system('mkdir -p playercareerstats')

# # Get players

# # start = 1946
# start
# end = 2014

# for year in range(start,end+1):
#   season = str(year)+'-'+str(year+1)[-2:]
#   print 'Season: ' + season

#   url = 'http://stats.nba.com/stats/commonallplayers?LeagueID=00&Season='+season+'&IsOnlyCurrentSeason=0'
#   print 'Request URL: ' + url

#   print 'Getting response ...'
#   response = get(url)
#   print 'Got response ...'

#   if response.status_code == 200:
#     print 'Status code: ' + str(response.status_code)
#     response = response.json()
#     print 'Response: ' + str(response)
#     print 'Writing response ...'
#     with open('response/commonallplayers/commonallplayers_'+season+'.json','w') as f:
#       dump(response,f)
#     print 'Done writing response!'

#     # pprint(response.keys())
#     # [u'resource', u'resultSets', u'parameters']

# # Get career stats

# seasons = ['response/commonallplayers/'+file for file in listdir('response/commonallplayers')]

# person_ids = []

# for season in seasons:
#   with open(season) as f:
#     response = loads(f.read())
#     header = response['resultSets'][0]['headers']
#     rows = response['resultSets'][0]['rowSet']
#     person_ix = 0

#     for row in rows:
#       person_id = row[person_ix]
#       if person_id not in person_ids:
#         person_ids.append(person_id)

# for person_id in person_ids:
#   print 'Person ID: ' + str(person_id)

#   url = 'http://stats.nba.com/stats/playercareerstats?PerMode=Totals&PlayerID='+str(person_id)
#   print 'Request URL: ' + url

#   print 'Getting response ...'
#   response = get(url)
#   print 'Got response ...'

#   if response.status_code == 200:
#     print 'Status code: ' + str(response.status_code)
#     response = response.json()
#     print 'Response: ' + str(response)
#     print 'Writing response ...'
#     with open('response/playercareerstats/playercareerstats_'+str(person_id)+'.json','w') as f:
#       dump(response,f)
#     print 'Done writing response!'

# Parse career stats

# players = ['response/playercareerstats/'+file for file in listdir('response/playercareerstats')]

# for player in players:
#   player_id = player.split('_')[1].split('.')[0]
#   with open(player) as f:
#     response = loads(f.read())
#     header = response['resultSets'][0]['headers']
#     rows = response['resultSets'][0]['rowSet']
#     csv = 'parse/playercareerstats_'+player_id+'.csv'
#     with open(csv,'w') as c:
#       print 'CSV: ' + csv
#       w = writer(c, delimiter = ',', quotechar = '"', quoting = QUOTE_MINIMAL)
#       w.writerow(header)
#       print header
#       for row in rows:
#         w.writerow(row)
#         print row

# Copy career stats

# sql = '''

# \set table playercareerstats

# drop table if exists :table cascade
# ;

# create table :table
# ( player_id int,
#   season_id text,
#   league_id text,
#   team_id int,
#   team_abbreviation text,
#   player_age float,
#   gp int,
#   gs int,
#   min int,
#   fgm int,
#   fga int,
#   fg_pct float,
#   fg3m int,
#   fg3a int,
#   fg3_pct float,
#   ftm int,
#   fta int,
#   ft_pct float,
#   oreb int,
#   dreb int,
#   reb int,
#   ast int,
#   stl int,
#   blk int,
#   tov int,
#   pf int,
#   pts int
# )
# ;

# '''

# with open('database/instance.sql','w') as f:
#   f.write(sql)

# system('cat database/instance.sql | psql -U andrew -d dev')

# players = ['parse/'+file for file in listdir('parse/')]

# for player in players:
#   sql = '''
#     \set table playercareerstats

#     copy :table
#     from \'/Users/andrew/nba/'''+player+''''
#     delimiter ','
#     header
#     quote '"'
#     csv
#     ;
#   '''

#   with open('database/instance.sql','w') as f:
#     f.write(sql)

#   system('cat database/instance.sql | psql -U andrew -d dev')  
#   print sql

# Parse common players

# players = ['response/commonallplayers/'+file for file in listdir('response/commonallplayers')]

# for player in players:
#   player_id = player.split('_')[1].split('.')[0]
#   with open(player) as f:
#     response = loads(f.read())
#     header = response['resultSets'][0]['headers']
#     rows = response['resultSets'][0]['rowSet']
#     csv = 'parse//commonallplayers/commonallplayers_'+player_id+'.csv'
#     with open(csv,'w') as c:
#       print 'CSV: ' + csv
#       w = writer(c, delimiter = ',', quotechar = '"', quoting = QUOTE_MINIMAL)
#       w.writerow(header)
#       print header
#       for row in rows:
#         w.writerow(row)
#         print row

# Copy career stats

sql = '''

\set table commonallplayers

drop table if exists :table cascade
;

create table :table
( person_id int,
  display_last_comma_first text,
  rosterstatus int,
  from_year int,
  to_year int,
  playercode text,
  team_id int,
  team_city text,
  team_name text,
  team_abbreviation text,
  team_code text,
  games_played_flag text
)
;

'''

with open('database/instance.sql','w') as f:
  f.write(sql)

system('cat database/instance.sql | psql -U andrew -d dev')

players = ['parse/commonallplayers/'+file for file in listdir('parse/commonallplayers/')]

for player in players:
  sql = '''
    \set table commonallplayers

    copy :table
    from \'/Users/andrew/nba/'''+player+''''
    delimiter ','
    header
    quote '"'
    csv
    ;
  '''

  with open('database/instance.sql','w') as f:
    f.write(sql)

  system('cat database/instance.sql | psql -U andrew -d dev')  
  print sql