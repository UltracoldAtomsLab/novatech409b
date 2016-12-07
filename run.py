import driver
import sys
import time

dev = driver.Novatech409B("/dev/serial/by-id/usb-FTDI_US232R_FTDCTBEZ-if00-port0")

# static. frequency in MHz
#dev.set_freq(int(sys.argv[1]), float(sys.argv[2]))

# table mode. frequency in MHz
dev.table_init()
dev.table_write(0, 137.182, 1023, 56.6, 1023)
dev.table_write(1, 137.182, 1023, 55.4, 1023)
dev.table_start()
