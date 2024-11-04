from __future__ import annotations
from enum import Enum
import numpy as np


class Suit(Enum):
    __SUITS__ = "♠♡♣♢"

    Spade   = 1
    Heart   = 2
    Club    = 3
    Diamond = 4

    def __str__(self):
        return Suit.__SUITS__[self.value-1]


class Rank(Enum):
    __RANKS__ = "JQKA"

    Two = 2 
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10

    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

    def __str__(self):
        if self.value < 11:
            return str(self.value)
        return Rank.__RANKS__[self.value-11]


class Card:
    def __init__(self, rank: Rank | int, suit: Suit):
        self.rank = rank
        self.suit = suit

    @staticmethod
    def to_int(card: Card) -> int:
        return card.rank.value + card.suit.value * 100

    @staticmethod
    def from_int(card: int) -> Card:
        suit = Suit(card//100)
        rank = Rank(card % 100)
        return Card(suit, rank)

    @staticmethod
    def from_tuple(card: tuple[int, int]) -> Card:
        return Card(
            Rank(card[0]),
            Suit(card[0])
        )

    def __str__(self) -> str:
        return f"[{self.rank}{self.suit}]"


class Decks:
    def __init__(min_rank: int = 2):
        self.deck = (
            Card(r, s) 
            for r in range(min_rank, 14+1)
            for s in range(1, 4+1)
        )
        self.cur_deck = [c for c in self.deck]

    def shuffle(self):
        self.cur_deck = np.shuffle(self.cur_deck)



if __name__ == "__main__":
    c = Card(Rank.Jack, Suit.Club)
    print(c)
