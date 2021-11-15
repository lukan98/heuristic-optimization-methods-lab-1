class Player:
    def __init__(self, identifier: int, position: str, name: str, club: str, points: float, price: float):
        self.identifier = identifier
        self.position = position
        self.name = name
        self.club = club
        self.points = points
        self.price = price


class Squad:
    first_team: [Player] = []
    substitutes: [Player] = []
    player_stack: [Player] = []

    def get_player_count_for_position(self, position: str) -> int:
        return self.get_substitute_count_for_position(position) + self.get_starter_count_for_position(position)

    def get_substitute_count_for_position(self, position: str) -> int:
        return sum(1 for substitute in self.substitutes if substitute.position == position)

    def get_starter_count_for_position(self, position: str) -> int:
        return sum(1 for starter in self.first_team if starter.position == position)

    def get_player_count_for_club(self, club: str) -> int:
        return sum(1 for player in self.first_team + self.substitutes if player.club == club)

    def add_to_first_team(self, player: Player):
        self.first_team.append(player)
        most_recently_added = player
        return

    def add_to_substitutes(self, player: Player):
        self.substitutes.append(player)
        most_recently_added = player
        return

    def pop_player(self) -> Player:
        popped_player = self.player_stack.pop()
        if self.substitutes.contains(popped_player):
            self.substitutes.remove(popped_player)
        else:
            self.first_team.remove(popped_player)

        return popped_player
