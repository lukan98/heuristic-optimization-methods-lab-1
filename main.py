import parser
import sys
import greedy_algorithm
import local_search_algorithm

players = parser.parse_instance(sys.argv[1])

squad = greedy_algorithm.run(players)

for player in squad.first_team + squad.substitutes:
    print(player.identifier, player.position, player.club, player.name, player.price, player.points)
print("Points: ", sum(map(lambda x: x.points, squad.first_team)), ", price: ", sum(map(lambda x: x.price, squad.first_team + squad.substitutes)))

file = open("greedy_solution.txt", "w")
first_team = list(map(lambda x: str(x.identifier), squad.first_team))
subs = list(map(lambda x: str(x.identifier), squad.substitutes))
file.write(",".join(first_team))
file.write("\n")
file.write(",".join(subs))
file.close()

while local_search_algorithm.optimise(squad, 100.0, players):
    print("------------")
    for player in squad.first_team + squad.substitutes:
        print(player.identifier, player.position, player.club, player.name, player.price, player.points)
    print("Points: ", sum(map(lambda x: x.points, squad.first_team)), ", price: ", sum(map(lambda x: x.price, squad.first_team + squad.substitutes)))


file = open("local_optimised.txt", "w")
first_team = list(map(lambda x: str(x.identifier), squad.first_team))
subs = list(map(lambda x: str(x.identifier), squad.substitutes))
file.write(",".join(first_team))
file.write("\n")
file.write(",".join(subs))
file.close()