#!/usr/bin/env python3

from game import Game
from bounced_ball import BouncedBallScene
from disp_stage import DisplayStage
from scene import Scene, Stage


def main():
    ''' Run program '''
    print('Starting Game')
    stage: Stage = DisplayStage()
    scene: Scene = BouncedBallScene(stage)
    game: Game = Game('Ball', scene, stage)
    game.run()


if __name__ == '__main__':
    main()
