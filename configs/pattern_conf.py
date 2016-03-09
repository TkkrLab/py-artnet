# import all patterns availble for use.
from patterns.Patterns import *

pixelmatrix = "pixelmatrix"
ledboard = 'ledboard'
raspberrypi = "192.168.2.42"
michiel_laptop = "192.168.1.199"
localhost = "127.0.0.1"
broadcast = "10.42.255.255"
matrix = "10.42.4.36"
dest = ledboard
# dest = pixelmatrix
# dest = '10.42.4.213'

TARGETS = {
    # dest: RainPattern(color=(0xff, 0xff, 0xff), chance=0.5),
    # dest: FillTest(),
    # dest: Sven(),
    # dest: BarberpolePattern(),
    # dest: OldTron(),
    # dest: Tron(),
    # dest: Snake(speed=17),
    # dest: MixedLife(),
    # dest: RandomLife(),
    # dest: RedLife(),
    # dest: BlueLife(),
    # dest: GreenLife(),
    # dest: SuperPixelBros(),
    # dest: Pong(speed=5),
    # dest: Pong(bcolor=(0, 0, 255), speed=3, port="USB", plugged=0),
    # dest: Pong(speed=8),
    # dest: ScreenCapture(fullscreen=True),
    # dest: ScreenCapture(fullscreen=False),
    # dest: DisplayImage('../Pictures/nebulacrosseyed.jpg'),
    # dest: DisplayImage('images/sisters-sprites.png'),
    # dest: DisplayImage('images/horse-2-xxl.png'),
    # dest: DisplayImage('images/horse-xxl.png'),
    # dest: DisplayImage('images/hue_alpha.png'),
    # dest: DisplayImage('images/ringDepthMagicEye.jpg'),
    # dest: DisplayImage('images/tiger.jpg'),
    # dest: DisplayGif('/home/robert/1353.gif'),
    # dest: VideoPlay('/home/robert/Videos/bad-noshadow.mp4'),
    # dest: VideoPlay('/home/duality/Videos/bad.mkv'),
    # dest: Water(),
    # dest: AliasedWPlasma(),
    
    # dest: AliasedFire(),
    # dest: MiniFire(),
    # dest: Smolders(),
    # dest: FireOne(),
    # dest: FireTwo(),
    # dest: FireThree(),
    # dest: RectTest(),

    # dest: RainbowEffect(),
    # dest: ColorFade(),
    # dest: PlasmaFifth(),
    # dest: PlasmaFourth(),
    # dest: PlasmaFirst(),
    # dest: PlasmaSecond(),
    # dest: PlasmaThird(),
    # dest: RevolvingCircle(),
    dest: RainPattern(chance=0.7, color=(40, 60, 255)),
    # dest: GraphicsCircleTest(),
    # dest: GraphicsRectTest(),
    # dest: GraphicsLineTest(),
    # dest: GraphicsPixelTest(),
    # dest: GraphicsDotTest(),
    # dest: VUmeterThree(),
}
