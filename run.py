import driver
import sys
import time

dev = driver.Novatech409B("/dev/tty.usbserial-FTDCTBEZ")
dev.set_freq(int(sys.argv[1]), float(sys.argv[2]))

# table mode. frequency in MHz
#dev.table_write(0, 130, 1000, 130, 1000)
#dev.table_write(1, 142, 1000, 142, 1000)
#dev.table_start()
