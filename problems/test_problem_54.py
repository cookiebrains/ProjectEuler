from unittest import TestCase

from problems.problem_54 import Hand


class TestHand(TestCase):
    def test_is_straight_true(self):
        h = Hand('3C 4D 5C 6C 7C')
        self.assertTrue(h.is_straight())

    def test_is_straight_false(self):
        h = Hand('TC TC 9C 8C 7D')
        self.assertFalse(h.is_straight())

    def test_is_flush_false(self):
        h = Hand('9C 6S 7C 8H 5C')
        self.assertFalse(h.is_flush())

    def test_is_flush_true(self):
        h = Hand('9C 6C 7C 8C 5C')
        self.assertTrue(h.is_flush())

    def test_beats(self):
        h1 = Hand('')
        h2 = Hand('')
        # self.assertTrue(h1.beats(h2))

    def test_has_pair_two_true(self):
        h = Hand('9C 9C 4C 5C 6C')
        self.assertTrue(h.has_pair())

    def test_has_pair_three_true(self):
        h = Hand('9C 9C 9C 5C 6C')
        self.assertTrue(h.has_pair())

    def test_has_pair_false(self):
        h = Hand('4C 5C 6C 7C 8C')
        self.assertFalse(h.has_pair())

    def test_is_full_house_true(self):
        h = Hand('4C 4D 4H JC JD')
        self.assertTrue(h.is_full_house())

    def test_is_full_house_false(self):
        h = Hand('4C 4H 4S JC QD')
        self.assertFalse(h.is_full_house())

    def test_has_two_pairs_true(self):
        h = Hand('4C 4H 5S 5C QD')
        self.assertTrue(h.has_two_pairs())

    def test_has_two_pairs_true_with_full_house(self):
        h = Hand('4C 4H 5S 5C 5D')
        self.assertTrue(h.has_two_pairs())

    def test_has_two_pairs_true_with_full_house(self):
        h = Hand('4C 4H 5S 6C 7D')
        self.assertFalse(h.has_two_pairs())

    def test_has_highest_unique_card_true(self):
        h1 = Hand('9C 9C 5C 8C 7D')
        h2 = Hand('9C 9C 5C 8C 6D')
        self.assertTrue(h1.has_highest_unique_card(h2))

    def test_has_highest_unique_card_false(self):
        h1 = Hand('9C 9C 5C 8C 6D')
        h2 = Hand('9C 9C 5C 8C 7D')
        self.assertFalse(h1.has_highest_unique_card(h2))

    def test_get_group_value_one_pair(self):
        h1 = Hand('9C 9C 5C 8C 6D')
        self.assertEquals(h1.get_group_value(0), 9)

    def test_get_group_value_two_pair(self):
        h1 = Hand('9C 9C 5C 5D 6D')
        self.assertEquals(h1.get_group_value(1), 5)

    def test_get_group_value_full_house_first(self):
        h1 = Hand('9C 9D 9H 5D 5C')
        self.assertEquals(h1.get_group_value(0), 9)

    def test_get_group_value_full_house_second(self):
        h1 = Hand('9C 9D 9H 5D 5C')
        self.assertEquals(h1.get_group_value(1), 5)

    def test_tie_high_card_hand_one_wins(self):
        h1 = Hand('TC QC 9C 8C 7D')
        h2 = Hand('9C 2C 5C 8C 7D')
        self.assertTrue(h1.beats(h2))

    def test_tie_high_card_hand_one_loses(self):
        h1 = Hand('TC QC 9C 8C 7D')
        h2 = Hand('9C 2C 5C 8C KD')
        self.assertFalse(h1.beats(h2))

    def test_tie_one_pair_diff_pair_card_true(self):
        h1 = Hand('TC TC 9C 8C 7D')
        h2 = Hand('9C 9C 5C 8C 7D')
        self.assertTrue(h1.beats(h2))

    def test_tie_one_pair_diff_pair_card_false(self):
        h1 = Hand('6C 6C 9C 8C 7D')
        h2 = Hand('TC TC 5C 8C 7D')
        self.assertFalse(h1.beats(h2))

    def test_tie_one_pair_same_pair_card_true(self):
        h1 = Hand('TC TD 9C 8C 7D')
        h2 = Hand('TH TS 5C 8C 7D')
        self.assertTrue(h1.beats(h2))

    def test_tie_one_pair_same_pair_card_false(self):
        h1 = Hand('TC TD 9C 8C 7D')
        h2 = Hand('TH TS QC 8C 7D')
        self.assertFalse(h1.beats(h2))

    def test_tie_two_pairs_same_first_pair_value_true(self):
        h1 = Hand('TC TD 9C 9C 7D')
        h2 = Hand('TH TS 8C 8C 7D')
        self.assertTrue(h1.beats(h2))

    def test_tie_two_pairs_same_first_and_second_pair_value_true(self):
        h1 = Hand('TC TD 9C 9C 8D')
        h2 = Hand('TH TS 9C 9C 7D')
        self.assertTrue(h1.beats(h2))

    def test_tie_two_pairs_first_pair_value_diff_true(self):
        h1 = Hand('AC AD 9C 9C 8D')
        h2 = Hand('TH TS 9C 9C 7D')
        self.assertTrue(h1.beats(h2))

    def test_tie_two_pairs_same_first_pair_value_false(self):
        h1 = Hand('TC TD 8C 8C 7D')
        h2 = Hand('TH TS 9C 9C 7D')
        self.assertFalse(h1.beats(h2))

    def test_tie_two_pairs_same_first_and_second_pair_value_false(self):
        h2 = Hand('TC TD 9C 9C 8D')
        h1 = Hand('TH TS 9C 9C 7D')
        self.assertFalse(h1.beats(h2))

    def test_tie_two_pairs_first_pair_value_diff_false(self):
        h2 = Hand('AC AD 9C 9C 8D')
        h1 = Hand('TH TS 9C 9C 7D')
        self.assertFalse(h1.beats(h2))

    def test_pair_beats_nothing_true(self):
        h1 = Hand('KS 9D KH 8D AH')
        h2 = Hand('8S KC 5H 9H AD')
        self.assertTrue(h1.beats(h2))
















