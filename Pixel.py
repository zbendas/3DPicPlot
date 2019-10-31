class Pixel:
    def __init__(self, data=()):
        if data == ():
            self.R = 0
            self.G = 0
            self.B = 0
            self.normal = False
            self.hex_string = "#000000"
        else:
            self.R = data[0]
            self.G = data[1]
            self.B = data[2]
            self.hex_string = self.hex()
            if (0 < self.R < 1) and (0 < self.G < 1) and (0 < self.B < 1):
                self.normal = True
            else:
                self.normal = False

    def __str__(self):
        return "{}(R:{}, G:{}, B:{})".format("N" if self.normal else "", self.R, self.G, self.B)

    def normalize(self):
        if self.normal:
            return False
        else:
            self.R /= 255
            self.G /= 255
            self.B /= 255
            self.normal = True
            return self

    def denormalize(self):
        if self.normal:
            self.R *= 255
            self.G *= 255
            self.B *= 255
            self.normal = False
            return self
        else:
            return False

    def array(self, mode="RGB"):
        if mode == "RGB":
            return [self.R, self.G, self.B]
        elif mode == "BGR":
            return [self.B, self.G, self.R]
        else:
            raise ValueError("Unsupported mode parameter value provided.")

    def hex(self):
        return "#{:06x}".format((self.R << 16) | (self.G << 8) | self.B)
