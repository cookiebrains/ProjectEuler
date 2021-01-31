from itertools import groupby


class Card:
    def __init__(self, name):
        self.name = name
        self.__init_number_value()
        self.__init_suit()

    def __init_suit(self):
        two_values = list(self.name)
        self.suit = two_values[1]

    def __init_number_value(self):
        two_values = list(self.name)
        self.number_value = face_card_dict[two_values[0]]

    def __repr__(self):
        return self.name


class Hand:
    def __init__(self, hand_string):
        card_strings = hand_string.split()
        self.cards = list(map(lambda card_string: Card(card_string), card_strings))
        self.rank = -1

    def __repr__(self):
        s = f'rank: {self.rank} cards: {self.cards}'
        return s

    def get_values(self):
        return list(map(lambda card: card.number_value, self.cards))

    def get_suites(self):
        return list(map(lambda card: card.suit, self.cards))

    def beats(self, other, flush_skip=False):
        self.rank = self.get_rank(flush_skip)
        other.rank = other.get_rank(flush_skip)
        if self.rank == other.rank:
            return self.beats_tie(other)
        return self.rank < other.rank

    def beats_tie(self, other):
        rank = self.rank

        # High card
        if rank == 9:
            return self.has_highest_unique_card(other)
        # One pair
        elif rank == 8:
            # First check pair val, if tie check high card (excluding pair val)
            # Filter to group of 2, ex: [10, 10], get first to know what the high card in group is
            self_value = list(filter(lambda group: len(group) == 2, self.get_value_groups()))[0][0]
            other_value = list(filter(lambda group: len(group) == 2, other.get_value_groups()))[0][0]
            if self_value != other_value:
                return self_value > other_value
            return self.has_highest_unique_card(other)
        # Two pairs
        elif rank == 7:
            return self.has_highest_unique_card(other)
        # Three of a kind
        elif rank == 6:
            return self.has_highest_unique_card(other)
        # Straight
        elif rank == 5:
            return self.has_highest_unique_card(other)
        # Flush
        elif rank == 4:
            # Get next lowest rank for each, will use same tie logic as others (it won't be a straight, but could be 3 of a kind, 2 pair, pair)
            return self.beats(other, flush_skip=True)
        # Full house
        elif rank == 3:
            return self.has_highest_unique_card(other)
        # Four of a kind
        elif rank == 2:
            return self.has_highest_unique_card(other)
        # Straight flush
        elif rank == 1:
            return self.has_highest_unique_card(other)

    def get_rank(self, flush_skip=False):
        if self.is_straight_flush():
            return 1
        if self.has_four_of_a_kind():
            return 2
        if self.is_full_house():
            return 3
        if self.is_flush() and not flush_skip:
            return 4
        if self.is_straight():
            return 5
        if self.has_three_of_a_kind():
            return 6
        if self.has_two_pairs():
            return 7
        if self.has_pair():
            return 8
        return 9

    # Get group value where groups are sorted largest to smallest
    def get_group_value(self, group_number):
        sorted_groups = sorted(self.get_value_groups(), key=len, reverse=True)
        return sorted_groups[group_number][0]

    def has_highest_unique_card(self, other):
        # If highest of each is same, have to travel to next and repeat. Get unique values to do this.
        unique_values_self = sorted(list(set(self.get_values())), reverse=True)
        unique_values_other = sorted(list(set(other.get_values())), reverse=True)
        for i in range(0, len(unique_values_self) + 1):
            try:
                if unique_values_self[i] == unique_values_other[i]:
                    continue
            except:
                print('i is ', i)
            return unique_values_self[i] > unique_values_other[i]

        raise ValueError('There was no high card!')

    def is_flush(self):
        return self.get_suites().count(self.cards[0].suit) == 5

    def is_straight(self):
        values_list = self.get_values()
        sorted_values = sorted(values_list)
        for i in range(1, 5):
            if sorted_values[i] != sorted_values[i - 1] + 1:
                return False
        return True

    # Example hand 4, 4, 5, 6, 7 gives groups [[4, 4], [5], [6], [7]]
    def get_value_groups(self):
        # This totally didn't work... writing our own...
        # return [list(v) for k, v in groupby(self.get_values())]

        groups = {}
        for card in self.cards:
            num = card.number_value
            if num not in groups.keys():
                groups[num] = [num]
            else:
                groups[num].append(num)
        return list(groups.values())

    def get_largest_group(self):
        return max(map(lambda group: len(group), self.get_value_groups()))

    def has_pair(self):
        return self.get_largest_group() >= 2

    def has_two_pairs(self):
        group_numbers = list(map(lambda group: len(group), self.get_value_groups()))
        two_groups = group_numbers.count(2)
        three_groups = group_numbers.count(3)
        return two_groups + three_groups >= 2

    def has_three_of_a_kind(self):
        return self.get_largest_group() >= 3

    def has_four_of_a_kind(self):
        return self.get_largest_group() >= 4

    def is_straight_flush(self):
        return self.is_flush() and self.is_straight()

    def is_full_house(self):
        group_numbers = map(lambda group: len(group), self.get_value_groups())
        return 3 in group_numbers and 2 in group_numbers


face_card_dict = {'J': 11,
                  'Q': 12,
                  'K': 13,
                  'A': 14,
                  '1': 1,
                  '2': 2,
                  '3': 3,
                  '4': 4,
                  '5': 5,
                  '6': 6,
                  '7': 7,
                  '8': 8,
                  '9': 9,
                  'T': 10}


# def pair_values(value_list):
#     pairs = []
#     for num in value_list:
#         if value_list.count(num) == 2 and num not in pairs:
#             pairs.append(num)
#     return pairs


# def is_two_pairs(hand):
#     if len(pair_values(hand)) == 2:
#         return True
#     else:
#         return False
#
#
# def is_one_pair(hand):
#     if len(pair_values(hand)) == 1:
#         return True
#     else:
#         return False


# def is_hand_a_better(a, b):
#     max_a = max(get_values_list(a))
#     max_b = max(get_values_list(b))
#     if max_a > max_b:
#         return True
#     else:
#         return False


def get_solution():
    lines = []
    with open('input_files/p054_poker.txt', 'r') as file:
        for line in file:
            lines.append(line)

    player_1_wins = 0

    for line in lines:
        h1 = Hand(line[0:14])
        h2 = Hand(line[-15:])
        if h1.beats(h2):
            player_1_wins += 1

    return player_1_wins


def run():
    print(get_solution())
