#Paul Lindberg
#Assignment #4 Pacman
#Friday 9AM

class Score:
    def __init__(self, settings, screen):
        self.value = 0
        self.settings = settings
        self.points = "{:,}".format(self.value)
        self.textsurface = settings.myfont.render(self.points, False, (255, 255, 255))
        self.screen = screen

    def blitme(self):
        self.points = "{:,}".format(self.value)
        self.textsurface = self.settings.myfont.render(self.points, False, (255, 255, 255))
        self.screen.blit(self.textsurface, (490, 220))
