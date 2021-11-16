import parser
import sys
import greedy_algorithm
from models import *

players = parser.parse_instance(sys.argv[1])

players = sorted(players, key=lambda player: (-player.price, player.points), reverse=True)

squad = greedy_algorithm.run(players)

for player in squad.first_team + squad.substitutes:
    print(player.identifier, player.position, player.club, player.name, player.price, player.points)