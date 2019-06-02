import yaml

# Read the data of the format .yaml type
with open(path) as f: 
    data = yaml.load(f)
f.close()

# Find data type of the file
print(type(data))

# In which city, and at which venue the match was played and where was it played ?
city = (data['info']['city'])
venue = (data['info']['venue'])
print('Match was played in ' ,city,venue)
# Which are all the teams that played in the tournament ? How many teams participated in total?
teams = (data['info']['teams'])
print(teams[0],'&',teams[1],'played in the tournament')
print(len(teams),' teams participated in total')

# Which team won the toss and what was the decision of toss winner ?
print(data['info']['toss']['winner'], 'won the toss')
print(data['info']['toss']['decision'],'was the decision')
# Find the first bowler and first batsman who played the first ball of the first inning
print(data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman'])
print(data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler'])
# How many deliveries were delivered in first inning ?
print(len(data['innings'][0]['1st innings']['deliveries']))

# How many deliveries were delivered in second inning ?
print(len(data['innings'][1]['2nd innings']['deliveries']))

# Which team won and how ?
print(data['info']['outcome']['winner'])
print(data['info']['outcome']['by']['runs'])
