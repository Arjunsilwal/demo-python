from panda3d.core import loadPrcFile, KeyboardButton
import sys


loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase

class MyGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        #Only disables the default camera mouse control
        self.disableMouse()

        #panda objectw
        panda = self.loader.loadModel("models/panda")
        panda.setPos(0, 10, 0)
        panda.setScale(0.2, 0.1, 0.2)
        panda.reparentTo(self.render)

        forward_speed = 1
        backward_speed = 1
        forward_button = KeyboardButton.ascii_key('w')

        # Exit on pressing the escape button.
        self.accept('escape', sys.exit)

        def move_task(self, task):
            speed = 0.0

            #check if the player is holding w or s
            is_down = base.mouseWatcherNode.is_button_down

            if is_down(forward_button):
                speed += forward_speed

            # Move the player
            y_delta = speed * globalClock.get_dt()
            self.player.set_y(self.player, y_delta)


game = MyGame()
game.run()