#!/usr/bin/python3

import os

import argparse
from random import shuffle

from modules.classes import Card, Player, GameSet
from modules.cards import carros_esporte, carros_esporte_vals

parser = argparse.ArgumentParser()
parser.add_argument("--players", "-p", type=str, nargs='+', help="Name of the players", required=True)
args = parser.parse_args()

N = len(args.players)
INITSEQ = args.players

def main():

    
    turn = [i for i in range(N)]
    shuffle(INITSEQ)
    print('Super Trunfo')
    gset = GameSet(INITSEQ)
    gset.setPlayers(carros_esporte)
    init = len(gset.players[0].cards)
    while init:
        for t in turn:
            os.system('clear')
            gset.players[t].viewCards()
            value = gset.players[t].selectCard()
            gset.setTurn(t, value)
        turn_vals = [gset.turn[k] for k in gset.turn]
        print(turn_vals)
        maxVal, winnerIdx = (max(turn_vals), turn_vals.index(max(turn_vals)))
        init-=1
        print(init)



if __name__ == "__main__":
    main()
