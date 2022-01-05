import Encoder
import time

enc=Encoder.Encoder(15,14)
old_arch = 0

while(1):
    arch = enc.read()
    arch = arch/40
    if arch != old_arch:
        print("Aktueller Winkel: "+ str(arch))
        old_arch=arch
        time.sleep(0.01)
