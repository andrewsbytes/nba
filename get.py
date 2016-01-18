from requests import get
from pprint import pprint
from json import dump, loads
from os import listdir, system

system('mkdir -p commonallplayers')
system('mkdir -p playercareerstats')

# Get players

# start = 1946
start
end = 2014

for year in range(start,end+1):
  season = str(year)+'-'+str(year+1)[-2:]
  print 'Season: ' + season

  url = 'http://stats.nba.com/stats/commonallplayers?LeagueID=00&Season='+season+'&IsOnlyCurrentSeason=0'
  print 'Request URL: ' + url

  print 'Getting response ...'
  response = get(url)
  print 'Got response ...'

  if response.status_code == 200:
    print 'Status code: ' + str(response.status_code)
    response = response.json()
    print 'Response: ' + str(response)
    print 'Writing response ...'
    with open('response/commonallplayers/commonallplayers_'+season+'.json','w') as f:
      dump(response,f)
    print 'Done writing response!'

    # pprint(response.keys())
    # [u'resource', u'resultSets', u'parameters']

# Get career stats

seasons = ['response/commonallplayers/'+file for file in listdir('response/commonallplayers')]

person_ids = []

for season in seasons:
  with open(season) as f:
    response = loads(f.read())
    header = response['resultSets'][0]['headers']
    rows = response['resultSets'][0]['rowSet']
    person_ix = 0

    for row in rows:
      person_id = row[person_ix]
      if person_id not in person_ids:
        person_ids.append(person_id)

for person_id in person_ids:
  print 'Person ID: ' + str(person_id)

  url = 'http://stats.nba.com/stats/playercareerstats?PerMode=Totals&PlayerID='+str(person_id)
  print 'Request URL: ' + url

  print 'Getting response ...'
  response = get(url)
  print 'Got response ...'

  if response.status_code == 200:
    print 'Status code: ' + str(response.status_code)
    response = response.json()
    print 'Response: ' + str(response)
    print 'Writing response ...'
    with open('response/playercareerstats/playercareerstats_'+str(person_id)+'.json','w') as f:
      dump(response,f)
    print 'Done writing response!'

# Parse career stats

# players = ['response/playercareerstats/'+file for file in listdir('response/playercareerstats')]

# for season in seasons[:1]:
#   with open(season) as f:
#     response = loads(f.read())
#     header = response['resultSets'][0]['headers']
#     rows = response['resultSets'][0]['rowSet']


