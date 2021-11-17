import parser
import sys
import greedy_algorithm

players = parser.parse_instance(sys.argv[1])

squad = greedy_algorithm.run(players)

for player in squad.first_team + squad.substitutes:
    print(player.identifier, player.position, player.club, player.name, player.price, player.points)

file = open("greedy_solution.txt", "w")
first_team = list(map(lambda x: str(x.identifier), squad.first_team))
subs = list(map(lambda x: str(x.identifier), squad.substitutes))
file.write(",".join(first_team))
file.write("\n")
file.write(",".join(subs))
file.close()
