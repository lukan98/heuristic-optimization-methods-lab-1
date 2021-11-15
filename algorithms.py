from models import *

budget = 100.0

max_goalkeepers = 2
max_defenders = 5
max_midfielders = 5
max_forwards = 3

max_players_per_club = 3

first_team_goalkeepers = 1
min_first_team_defenders = 3
min_first_team_forwards = 1

substitute_goalkeepers = 1

def run_greedy_algorithm(players: [Player]) -> Squad:
    squad = Squad()
    max_price = budget
    clubs_filtered = set()
    first_team_positions_filtered = set()
    squad_positions_filtered = set()
    prioritized_positions = set()

    # build first team
    players_by_points = sorted(players, key=lambda player: (player.points, -player.price), reverse=True)

    while len(squad.first_team) < 11:
        # check if its time to fill out defender, forward or goalkeeper quotas
        if 11 - len(squad.first_team) <= first_team_goalkeepers + min_first_team_defenders + min_first_team_forwards:
            if squad.get_starter_count_for_position("GK") < first_team_goalkeepers:
                prioritized_positions.add("GK")
            elif "GK" in prioritized_positions:
                prioritized_positions.remove("GK")

            if squad.get_starter_count_for_position("DEF") < min_first_team_defenders:
                prioritized_positions.add("DEF")
            elif "DEF" in prioritized_positions:
                prioritized_positions.remove("DEF")

            if squad.get_starter_count_for_position("FW") < min_first_team_forwards:
                prioritized_positions.add("FW")
            elif "FW" in prioritized_positions:
                prioritized_positions.remove("FW")

        if len(prioritized_positions) == 0:
            players_by_points = sorted(players, key=lambda player: (player.points, -player.price), reverse=True)
        else:
            players_by_points = sorted(players, key=lambda player: (player.points, -player.price), reverse=True)
            players_by_points = list(filter(lambda player: player.position in prioritized_positions, players_by_points))

        # check if there are affordable players
        if any(player.price < max_price for player in players_by_points):
            selected_player = list(
                filter(lambda player: player.price <= max_price
                                      and player not in squad.first_team
                                      and player.club not in clubs_filtered
                                      and player.position not in first_team_positions_filtered
                                      and player.position not in squad_positions_filtered,
                       players_by_points)
            )[0]

            # check club filter
            # if selected_player.club in clubs_filtered:
            #     #todo
            #     return squad
            # else:
                # if selected_player.position in first_team_positions_filtered or selected_player.position in squad_positions_filtered:
                #     #todo
                #     return squad
                # else:
            squad.add_to_first_team(selected_player)

            max_price -= selected_player.price

            if squad.get_player_count_for_club(selected_player.club) == max_players_per_club:
                clubs_filtered.add(selected_player.club)

            if selected_player.position == "GK" and squad.get_starter_count_for_position(
                    "GK") == first_team_goalkeepers:
                first_team_positions_filtered.add("GK")

            if selected_player.position == "DEF" and squad.get_player_count_for_position("DEF") == max_defenders:
                first_team_positions_filtered.add("DEF")

            if selected_player.position == "MID" and squad.get_player_count_for_position("MID") == max_midfielders:
                first_team_positions_filtered.add("MID")

            if selected_player.position == "FW" and squad.get_player_count_for_position("FW") == max_forwards:
                first_team_positions_filtered.add("FW")

    return squad