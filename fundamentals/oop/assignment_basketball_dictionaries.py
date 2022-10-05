
######class and constructor
class Players:
    def __init__(self, player_info):
        self.name = player_info['name']
        self.age = player_info['age']
        self.position = player_info['position']
        self.team = player_info['team']


######  add players
    @classmethod
    def add_players(cls, player_info):
        player_list = []
        for dict in player_info:
            player_list.append(cls(dict))
        return player_list


#### adds the data back in string 
    def __repr__(self):
        display = f"Player: {self.name}, age: {self.age} , pos: {self.position}, team: {self.team}"
        return display


kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}


###### add a few legends to the list
michael = {
        "name": "Michael Jordan", 
        "age":55, 
        "position": "Shooting Guard", 
        "team": "Chicago Bulls"
}
gary = {
        "name": "Gary Payton", 
        "age":54, "position": "Point Guard", 
        "team": "Seattle Sonics"
}


#####send players into the class constructor
player_jason = Players(jason)
player_kevin = Players(kevin)
player_kyrie = Players(kyrie)
player_michael = Players(michael)
player_gary = Players(gary)


###### print each player
print(player_jason)
print(player_kevin)
print(player_kyrie)
print(player_michael)
print(player_gary)


#nothing to see here!!!
players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]


######pull data from dictionary and append to new list
new_team = []
for player_dict in players:
    player = Players(player_dict)
    new_team.append(player)


print("---------test---------")
########added print out by line for ability to read
print(*new_team, sep = "\n")
