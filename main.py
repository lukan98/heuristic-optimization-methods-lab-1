import parser
import sys
import algorithms
from models import *

players = parser.parse_instance(sys.argv[1])

players = sorted(players, key=lambda player: (-player.price, player.points), reverse=True)

squad = algorithms.run_greedy_algorithm(players)

for player in squad.first_team:
    print(player.position, player.club, player.name, player.price, player.points)