# pylint: disable=C0111
import sys
import pygame

class Game:
    ''' Handles game loop '''
    def __init__(self, title, scene, stage):
        self.scene = scene
        self.title = title
        self.stage = stage

    def exit_game(self):
        ''' Exits the program '''
        if self.scene is not None:
            self.scene.unload_resources()
        pygame.quit()
        print('Thank You')
        sys.exit()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit_game()
            self.scene.process(event)

    def game_loop(self):
        ''' main game loop '''
        clock = pygame.time.Clock()

        while self.scene is not None:
            time_step = clock.tick(60)
            self.scene.load_if_needed()
            self.stage.clear()
            self.process_events()
            self.scene.update(time_step)
            self.scene.render()
            self.stage.swap()
            self.scene = self.scene.go_to_next_scene()

    def run(self):
        ''' Run program '''
        print('Starting')
        pygame.init()
        pygame.display.set_caption(self.title)
        self.stage.init()
        self.game_loop()
        self.exit_game()
