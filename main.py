import click
import qrcode
import qrcode.constants
from drawers.base import CustomStyledPilImage
from drawers.eyedrawers import CircleEyeDrawer, BarsEyeDrawer
from drawers.moduledrawers import GappedCircleModuleDrawer
from qrcode.image.styles.moduledrawers.pil import SquareModuleDrawer, GappedSquareModuleDrawer, RoundedModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer

@click.command()

@click.argument('content')
@click.argument('name')

@click.option('--style', '-s')

def main(content, name, style):
    match style:
        case "pixel":
            module_drawer   = GappedSquareModuleDrawer(size_ratio = .75)
            eye_drawer      = SquareModuleDrawer()
        case "circle":
            module_drawer   = GappedCircleModuleDrawer(size_ratio = .75)
            eye_drawer      = CircleEyeDrawer()
        case "rounded":
            module_drawer   = RoundedModuleDrawer()
            eye_drawer      = RoundedModuleDrawer()
        case "v-bars":
            module_drawer   = VerticalBarsDrawer(horizontal_shrink = .75)
            eye_drawer      = BarsEyeDrawer()
        case "h-bars":
            module_drawer   = HorizontalBarsDrawer(vertical_shrink = .75)
            eye_drawer      = BarsEyeDrawer()
        case _:
            module_drawer   = SquareModuleDrawer()
            eye_drawer      = SquareModuleDrawer()

    qr = qrcode.QRCode(
        version             = None,
        error_correction    = qrcode.constants.ERROR_CORRECT_H,
        box_size            = 100,
        border              = 5
    )

    qr.add_data(content)
    qr.make(fit = True)
    img = qr.make_image(
        image_factory   = CustomStyledPilImage,
        module_drawer   = module_drawer,
        eye_drawer      = eye_drawer,
        fill_color      = "black", 
        back_color      = "white"
    )
    img.save("{}.png".format(name))

if __name__ == "__main__":
    main()