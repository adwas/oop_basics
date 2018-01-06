#!/usr/bin/env python3
''' Common class for game scenes '''


class Scene:
    ''' Simple Scene '''

    def __init__(self, stage, next_scene=None):
        ''' Initialises scene and points to next scene.
            By default next scene is the same scene.
        '''
        if next_scene is None:
            next_scene = self
        self.next_scene = next_scene
        self.stage = stage
        self.loaded = False

    def load_if_needed(self):
        ''' Loads required resources only once '''
        if self.loaded is not True:
            self.load_resources()
            self.loaded = True

    def load_resources(self):
        ''' Loads required resources like images sounds etc'''
        pass

    def unload_resources(self):
        ''' Free alocated resources for scene '''
        pass

    def go_to_next_scene(self):
        ''' Unloads data from current scene before go to next scene'''
        if self != self.next_scene:
            self.unload_resources()
        return self.next_scene

    def process(self, event):
        ''' Process event '''
        pass

    def update(self, time_step):
        ''' Updates state for every game clock tick'''
        pass

    def render(self):
        ''' Renders state on pygame? surface '''
        pass

    def reset(self):
        ''' Resets to initial state '''
        pass


class Stage:
    ''' Physical layer on with scene is happen like display screen or sense hat lcd matrix '''

    def __init__(self, width, height, refresh_rate=12):
        self.width = width
        self.height = height
        self.refresh_rate = refresh_rate
        self.surface = None  # raw surface it can be anythig screen opengl surface, led matrix


    def init(self):
        ''' Initialise surface '''

    def clear(self):
        ''' Clears everything before rerendering '''
        pass

    def swap(self):
        ''' swlap buffers '''
        pass
