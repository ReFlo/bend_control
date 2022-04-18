from pigpio_encoder.rotary import Rotary

def rotary_callback(counter):
    print("Counter value: ", counter/50)

my_rotary = Rotary(clk_gpio=15, dt_gpio=18, sw_gpio=14)
my_rotary.setup_rotary(rotary_callback=rotary_callback, max=16000, debounce=10)
my_rotary.watch()