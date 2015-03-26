# import all patterns availble for use.
from patterns.Patterns import *

pixelMatrix = "pixelmatrix"
raspberrypi = "192.168.2.42"
michiel_laptop = "192.168.1.199"
local_host = "127.0.0.1"
broadcast = "10.42.255.255"

dest = pixelMatrix

TARGETS = {
    # dest: BarberpolePattern(),
    # dest: OldTron(),
    # dest: Tron(),
    dest: Snake(speed=17),
    # # MixedLife() doesn't work atm but will be fixed
    # dest: MixedLife(),
    # dest: RandomLife(),
    # dest: BlueLife(),
    # dest: BlueLife(),
    # dest: SuperPixelBros(),
    # dest: Pong(speed=5),
    # dest: Pong(speed=3),
    # dest: Pong(speed=8),
    # dest: Snake(),
    # dest: BlueLife(),
    # # needs images. wip still.
    # dest: DisplayPng(),
    # dest: PlasmaFirst(),
    # dest: PlasmaSecond(),
    # dest: PlasmaSecond(),
    # dest: PlasmaThird(),
    # dest: RainPattern(chance=0.2),
    # dest: GraphicsCircleTest(),
    # dest: GraphicsRectTest(),
    # dest: GraphicsLineTest(),
    # dest: GraphicsPixelTest(),
    # dest: GraphicsDotTest(),
}
