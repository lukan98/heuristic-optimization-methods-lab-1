import parser
import sys
from models import *

players = parser.parse_instance(sys.argv[1])[:15]

squad = Squad()

squad.first_team = players[:11]
squad.substitutes = players[11:15]

for player in squad.first_team + squad.substitutes:
    print(player.name, player.position, player.club)

print(squad.get_substitute_count_for_position("GK"))
print(squad.get_starter_count_for_position("GK"))

print(squad.get_player_count_for_club("Arsenal"))