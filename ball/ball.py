#!/usr/bin/env python3

from game import Game
from bounced_ball import BouncedBallScene
from disp_stage import DisplayStage


def main():
    ''' Run program '''
    print('Starting Game')
    stage = DisplayStage()
    scene = BouncedBallScene(stage)
    game = Game('Ball', scene, stage)
    game.run()


if __name__ == '__main__':
    main()
