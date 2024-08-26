from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")
#make a folder name config and create file name with .prc extension
from direct.showbase.ShowBase import ShowBase

#another way for config file
#from panda3d.core import loadPrcFileData
#loadPrcFileData('', 'fullscreen true')

class MyGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)


game = MyGame()
game.run()