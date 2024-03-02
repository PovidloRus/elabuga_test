import copy


class Log:
    move_type: int
    player: str
    card_id: int

    def __init__(self, move_type: int, player: str, card_id: int):
        self.move_type = move_type
        self.player = player
        self.card_id = card_id


class Deck:
    player: str
    deck: list[int]

    def __init__(self, player: str, deck: list[int]) -> None:
        self.player = player
        self.deck = deck


class KKI:
    def __init__(self, deck_1: Deck, deck_2: Deck, logs: list[Log]):
        self.deck_1 = deck_1
        self.deck_2 = deck_2
        self.logs = logs

    def modify_player_deck(self, log: Log) -> None:
        if log.player == self.deck_1.player:
            if log.move_type == 1:
                self.deck_1.deck.append(log.card_id)
            if log.move_type == -1:
                self.deck_1.deck.remove(log.card_id)
        if log.player == self.deck_2.player:
            if log.move_type == 1:
                self.deck_2.deck.append(log.card_id)
            if log.move_type == -1:
                self.deck_2.deck.remove(log.card_id)

    def calc_diversity(self):
        player_1_deck = copy.copy(self.deck_1.deck)
        player_2_deck = copy.copy(self.deck_2.deck)
        set_dec_1 = set(player_1_deck)
        set_dec_2 = set(player_2_deck)
        same_card = set_dec_1 & set_dec_2
        for i in same_card:
            player_1_deck.remove(i)
            player_2_deck.remove(i)

        return len(player_1_deck) + len(player_2_deck)

    def start(self):
        res = []
        for i in self.logs:
            self.modify_player_deck(i)
            res.append(str(self.calc_diversity()))
        return res


if __name__ == '__main__':
    count_card_player_1, count_card_player_2, count_modify = list(map(int, input().split()))

    deck_1 = Deck('A', list(map(int, input().split())))
    deck_2 = Deck('B', list(map(int, input().split())))
    logs = list()
    counter = 0
    while counter < count_modify:
        type_move, player, card_id = input().split()
        type_move = int(type_move)
        card_id = int(card_id)
        logs.append(Log(type_move, player, card_id))
        counter += 1

    a = KKI(deck_1, deck_2, logs)
    res = a.start()
    print(' '.join(res))
