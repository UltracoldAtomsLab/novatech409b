import driver
import sys

dev = driver.Novatech409B("/dev/tty.usb")
dev.set_freq(sys.argv[0], sys.argv[1])
