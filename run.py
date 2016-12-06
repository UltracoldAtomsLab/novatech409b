import driver
import sys
import time

dev = driver.Novatech409B("/dev/serial/by-id/usb-FTDI_US232R_FTDCTBEZ-if00-port0")

# static. frequency in MHz
#dev.set_freq(int(sys.argv[1]), float(sys.argv[2]))

# table mode. frequency in MHz
dev.table_write(0, 130, 1000, 130, 1000)
dev.table_write(1, 145, 1000, 145, 1000)
#dev.table_write(2, 130, 1000, 130, 1000)
dev.table_start()
