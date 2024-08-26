from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec3



class MyGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.disableMouse()


        # load box model
        self.box = self.loader.loadModel("models/box")
        self.box.setScale(0.8)
        self.box.setPos(0, 10, 0)
        self.box.reparentTo(self.render)

        #camera mode
        self.is_first_person = False
        #self.setup_camera()

        #setup controls
        self.setup_controls()

        # # Start the task to update the camera position
        # self.taskMgr.add(self.update_camera, "update_camera")

    def setup_camera(self):
        pass

    def toggle_camera_view(self):
        self.is_first_person = not self.is_first_person



    #setting up control for movement
    def setup_controls(self):
        self.accept('a', self.move_left)
        self.accept('a-repeat', self.move_left)
        self.accept('d', self.move_right)
        self.accept('d-repeat', self.move_right)

        self.accept('w', self.move_up)
        self.accept('w-repeat', self.move_up)
        self.accept('s', self.move_down)
        self.accept('s-repeat', self.move_down)

        self.accept('q', self.scale_down)
        self.accept('q-repeat', self.scale_down)
        self.accept('e', self.scale_up)
        self.accept('e-repeat', self.scale_up)

        self.accept('c', self.toggle_camera_view)


        #defining methods for movements
    def move_left(self):
        self.box.setX(self.box.getX() - 1)

    def move_right(self):
        self.box.setX(self.box.getX() + 1)


    def move_up(self):
        current_pos = self.box.getPos()
        new_z = current_pos.z + 1
        self.box.setPos(current_pos.x, current_pos.y, new_z)

    def move_down(self):
        current_pos = self.box.getPos()
        new_z = current_pos.z - 1
        self.box.setPos(current_pos.x, current_pos.y, new_z)

    def scale_down(self):
        current_pos = self.box.getPos()
        new_y = current_pos.y + 1
        self.box.setPos(current_pos.x, new_y, current_pos.z)

    def scale_up(self):
        current_pos = self.box.getPos()
        new_y = current_pos.y - 1
        self.box.setPos(current_pos.x, new_y, current_pos.z)



game = MyGame()
game.run()