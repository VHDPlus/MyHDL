from myhdl import *

# Define the Blinky module.
@block
def blinky(clk_i, led_o):

    cnt = Signal(intbv(0, 0, 12000000)) # Counter from 0 to 11999999.
    tgl = Signal(bool(0)) # Toggle flag drives the LED.

    # Sequential block triggered on every rising edge of the clock.
    @always_seq(clk_i.posedge, reset=None)
    def toggle_led():
        if cnt == cnt.max-1: # When the counter reaches its max value...
            tgl.next = ~tgl  # Toggle the flag...
            led_o.next = tgl # Output the flag to the LED...
            cnt.next = 0     # Reset the counter.
        else: # Counter hasn't reached max so just keep incrementing.
            cnt.next = cnt + 1

    # Return a reference to the Blinky logic.
    return toggle_led

# Define the connections to Blinky.
clk_i = Signal(bool(0))
led_o = Signal(bool(0))

# Create an instantiation of Blinky.
top = blinky(clk_i, led_o)

# Output VHDL code for Blinky.
top.convert(hdl='VHDL')
