import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from panda3d.core import *

#disable default camera controller
base.disableMouse()

#create an event listener object
eventListener = DirectObject()

#load panda model
panda = loader.loadModel("models/panda")
panda.setScale(0.2, 0.1, 0.2)
assert not panda.isEmpty(), "can not find panda file"
panda.reparentTo(render)

#setup camera
camera.setPos(0, -10, 3)
camera.lookAt(panda)

#variables
wheelRot = 0
#constants
speed = 1
sensitivity = 1

def movePanda(amount):
    panda.setH(panda, wheelRot)
    panda.setY(panda, amount)


def turnWheels(amount):
    global wheelRot
    wheelRot += amount

#setup event handlers
eventListener.accept("w", movePanda, [speed])
eventListener.accept("w-repeat", movePanda, [speed])

eventListener.accept("s", movePanda, [-speed])
eventListener.accept("s-repeat", movePanda, [-speed])

eventListener.accept("a", turnWheels, [sensitivity])
eventListener.accept("a-repeat", turnWheels, [sensitivity])

eventListener.accept("d", turnWheels, [-sensitivity])
eventListener.accept("d-repeat", turnWheels, [-sensitivity])


run()