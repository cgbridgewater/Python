class Players:
    player_objects = []
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']
    


    @classmethod
    def add_players(cls, data):
        player_objects = []
        for dict in data:
            player_objects.append(cls(dict))
        return player_objects
    
    
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




player_jason = Players(jason)
player_kevin = Players(kevin)
player_kyrie = Players(kyrie)
player_michael = Players(michael)
player_gary = Players(gary)
print(player_jason)
print(player_kevin)
print(player_kyrie)
print(player_michael)
print(player_gary)
