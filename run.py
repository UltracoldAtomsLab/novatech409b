import driver
import sys
import time

dev = driver.Novatech409B("/dev/tty.usbserial-FTDCTBEZ")
dev.set_freq(int(sys.argv[1]), float(sys.argv[2]))

# table mode
#dev.table_write(0, 1e7, 1000, 1e7, 1000)
#dev.table_write(1, 1e8, 1000, 1e8, 1000)
#dev.table_start()
#time.sleep(2)
#dev.table_next()
