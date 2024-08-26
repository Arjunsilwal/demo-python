from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode, CollisionHandlerQueue, CollisionRay, CollisionSphere
from panda3d.core import BitMask32, Point3
from direct.task import Task

class MyGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)


        self.cam.setPos(0, -10, 0)
        #self.disableMouse()
        # Load three objects (models)
        self.object1 = self.loader.loadModel("models/panda")
        self.object1.setScale(0.2)
        self.object1.setPos(-5, 10, 0)
        self.object1.reparentTo(self.render)

        self.object2 = self.loader.loadModel("models/panda")
        self.object2.setScale(0.2)
        self.object2.setPos(0, 10, 0)
        self.object2.reparentTo(self.render)

        self.object3 = self.loader.loadModel("models/panda")
        self.object3.setScale(0.2)
        self.object3.setPos(5, 10, 0)
        self.object3.reparentTo(self.render)

        # Set up collision detection for mouse picking
        self.picker = CollisionTraverser()
        self.pq = CollisionHandlerQueue()

        self.pickerNode = CollisionNode('mouseRay')
        self.pickerNP = self.camera.attachNewNode(self.pickerNode)
        self.pickerNode.setFromCollideMask(BitMask32.bit(1))
        self.pickerRay = CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)

        self.picker.addCollider(self.pickerNP, self.pq)

        # Add collision spheres to the objects
        self.add_collision_node(self.object1)
        self.add_collision_node(self.object2)
        self.add_collision_node(self.object3)

        # Initially, no object is selected
        self.selected_object = None

        # Setup controls
        self.accept('mouse1', self.on_mouse_click)
        self.accept('w', self.move_selected, [Point3(0, 1, 0)])  # Move forward
        self.accept('s', self.move_selected, [Point3(0, -1, 0)]) # Move backward
        self.accept('a', self.move_selected, [Point3(-1, 0, 0)]) # Move left
        self.accept('d', self.move_selected, [Point3(1, 0, 0)])  # Move right

        # Update the picker each frame
        self.taskMgr.add(self.update_picker, "update_picker")

    def add_collision_node(self, obj):
        bounds = obj.getTightBounds()
        center = (bounds[0] + bounds[1]) / 2
        radius = (bounds[1] - bounds[0]).length() / 2
        collision_sphere = CollisionSphere(center, radius)
        cnode = CollisionNode('cnode')
        cnode.addSolid(collision_sphere)
        cnode.setIntoCollideMask(BitMask32.bit(1))
        cnodepath = obj.attachNewNode(cnode)
        cnodepath.show()  # Show the collision bounds (optional for debugging)

    def update_picker(self, task):
        # Update the picker ray based on the mouse position
        if self.mouseWatcherNode.hasMouse():
            mpos = self.mouseWatcherNode.getMouse()
            self.pickerRay.setFromLens(self.camNode, mpos.getX(), mpos.getY())
        return Task.cont

    def on_mouse_click(self):
        # Check if the mouse is over an object
        self.picker.traverse(self.render)
        if self.pq.getNumEntries() > 0:
            self.pq.sortEntries()
            picked_obj = self.pq.getEntry(0).getIntoNodePath().getParent()
            self.selected_object = picked_obj

    def move_selected(self, move_vec):
        if self.selected_object:
            self.selected_object.setPos(self.selected_object.getPos() + move_vec)

game = MyGame()
game.run()