from .resource import IOResource
import serial
import attr

@attr.s
class SerialPort(IOResource):
    target = attr.ib()
    port = attr.ib(validator=attr.validators.instance_of(str))
    speed = attr.ib(default=115200, validator=attr.validators.instance_of(int))

    def __attrs_post_init__(self):
        self.serial = serial.Serial(self.port, self.speed)
        self.target.resources.append(self)

    def read(self, size: int=1024):
        """
        Reads 'size' bytes from the serialport

        Keyword Arguments:
        size -- amount of bytes to read, defaults to 1024
        """
        return self.serial.read(size)

    def write(self, data: bytes):
        """
        Writes 'data' to the serialport

        Arguments:
        data -- data to write, must be bytes
        """
        self.serial.write(data)

    def __del__(self):
        if self.serial:
            self.serial.close()
