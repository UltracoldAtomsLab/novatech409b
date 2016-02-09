import driver
import sys

dev = driver.Novatech409B("/dev/tty.usbserial-FTXOSB6L")
dev.set_freq(int(sys.argv[1]), float(sys.argv[2]))
