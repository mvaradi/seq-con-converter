import re


def rgb_to_hex(color):
    """
    This function converts RGB color to HEX, or returns the input if it is already HEX
    RGB input should be in the format of: rgb(100, 100, 100)
    HEX input should be in the format of: #d3d3d3 or #D3D3D3
    :param color: RGB or HEX color
    :return: HEX color
    """
    if re.match("rgb", color):
        values = color.replace("rgb(", "").replace(")", "").split(",")
        return "#%02x%02x%02x" % (int(values[0]), int(values[1]), int(values[2]))
    elif re.match("#", color):
        return color
    else:
        raise ValueError("Only RGB or HEX input allowed")