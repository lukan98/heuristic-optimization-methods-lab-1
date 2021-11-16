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
    max_points = float("inf")
    clubs_filtered = set()
    first_team_positions_filtered = set()
    squad_positions_filtered = set()
    prioritized_positions = set()

    players_by_points_descending = sorted(players, key=lambda player: (player.points, -player.price), reverse=True)
    players_by_price_ascending = sorted(players, key=lambda player: (-player.price, player.points), reverse=True)

    iterations = 0

    while len(squad.first_team) + len(squad.substitutes) < 15:

        iterations += 1

        if len(squad.first_team) < 11:
            # check if its time to fill out defender, forward or goalkeeper quotas
            if 11 - len(
                    squad.first_team) <= first_team_goalkeepers + min_first_team_defenders + min_first_team_forwards:
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
                players_by_points = players_by_points_descending
            else:
                players_by_points = players_by_points_descending
                players_by_points = list(
                    filter(lambda player: player.position in prioritized_positions, players_by_points))

            # check if there are affordable players
            if any(player.price <= max_price
                   and player not in squad.first_team + squad.substitutes
                   and player.club not in clubs_filtered
                   and player.position not in first_team_positions_filtered
                   and player.position not in squad_positions_filtered
                   and player.points < max_points for player in players_by_points):
                selected_player = list(
                    filter(lambda player: player.price <= max_price
                                          and player not in squad.first_team + squad.substitutes
                                          and player.club not in clubs_filtered
                                          and player.position not in first_team_positions_filtered
                                          and player.position not in squad_positions_filtered
                                          and player.points < max_points,
                           players_by_points)
                )[0]

                squad.add_to_first_team(selected_player)

                max_price -= selected_player.price

                if squad.get_player_count_for_club(selected_player.club) == max_players_per_club:
                    clubs_filtered.add(selected_player.club)

                if selected_player.position == "GK" and squad.get_starter_count_for_position(
                        "GK") == first_team_goalkeepers:
                    first_team_positions_filtered.add("GK")

                if selected_player.position == "DEF" and squad.get_player_count_for_position("DEF") == max_defenders:
                    first_team_positions_filtered.add("DEF")
                    squad_positions_filtered.add("DEF")

                if selected_player.position == "MID" and squad.get_player_count_for_position("MID") == max_midfielders:
                    first_team_positions_filtered.add("MID")
                    squad_positions_filtered.add("MID")

                if selected_player.position == "FW" and squad.get_player_count_for_position("FW") == max_forwards:
                    first_team_positions_filtered.add("FW")
                    squad_positions_filtered.add("FW")
            # no affordable players
            else:
                last_selected_player = squad.pop_player()
                if last_selected_player.position in first_team_positions_filtered:
                    first_team_positions_filtered.remove(last_selected_player.position)

                if last_selected_player.position in squad_positions_filtered:
                    squad_positions_filtered.remove(last_selected_player.position)

                if last_selected_player.club in clubs_filtered:
                    clubs_filtered.remove(last_selected_player.club)

                max_price += last_selected_player.price
                max_points = last_selected_player.points


        # we're filling the substitutes
        else:
            if len(squad.substitutes) < 4:
                if 4 - len(squad.substitutes) == substitute_goalkeepers:
                    prioritized_positions.add("GK")
                elif "GK" in prioritized_positions:
                    prioritized_positions.remove("GK")

            if len(prioritized_positions) == 0:
                players_by_price = players_by_price_ascending
            else:
                players_by_price = players_by_price_ascending
                players_by_price = list(
                    filter(lambda player: player.position in prioritized_positions, players_by_price))

            if any(player.price <= max_price
                   and player not in squad.first_team + squad.substitutes
                   and player.club not in clubs_filtered
                   and player.position not in first_team_positions_filtered
                   and player.position not in squad_positions_filtered
                   and player.points < max_points for player in players_by_price):
                selected_player = list(
                    filter(lambda player: player.price <= max_price
                                          and player not in squad.first_team + squad.substitutes
                                          and player.club not in clubs_filtered
                                          and player.position not in squad_positions_filtered
                                          and player.points < max_points,
                           players_by_price)
                )[0]

                squad.add_to_substitutes(selected_player)

                max_price -= selected_player.price

                if squad.get_player_count_for_club(selected_player.club) == max_players_per_club:
                    clubs_filtered.add(selected_player.club)

                if selected_player.position == "GK" and squad.get_substitute_count_for_position(
                        "GK") == substitute_goalkeepers:
                    squad_positions_filtered.add("GK")

                if selected_player.position == "DEF" and squad.get_player_count_for_position("DEF") == max_defenders:
                    squad_positions_filtered.add("DEF")

                if selected_player.position == "MID" and squad.get_player_count_for_position("MID") == max_midfielders:
                    squad_positions_filtered.add("MID")

                if selected_player.position == "FW" and squad.get_player_count_for_position("FW") == max_forwards:
                    squad_positions_filtered.add("FW")

            # no affordable players
            else:
                last_selected_player = squad.pop_player()
                if last_selected_player.position in first_team_positions_filtered:
                    first_team_positions_filtered.remove(last_selected_player.position)

                if last_selected_player.position in squad_positions_filtered:
                    squad_positions_filtered.remove(last_selected_player.position)

                if last_selected_player.club in clubs_filtered:
                    clubs_filtered.remove(last_selected_player.club)

                max_price += last_selected_player.price
                max_points = last_selected_player.points

    print(iterations)

    return squad
