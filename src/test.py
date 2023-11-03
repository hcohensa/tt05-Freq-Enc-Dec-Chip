
# import cocotb
# from cocotb.clock import Clock
# from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles



import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_my_design(dut):
    CONSTANT_CURRENT = 10

    clock = Clock(dut.clk, 1, units="ns")
    await clock.start()

    dut.rst_n <= 0
    await RisingEdge(dut.clk)
    dut.rst_n <= 1
    await RisingEdge(dut.clk)

    dut.ui_in <= CONSTANT_CURRENT
    dut.ena <= 1

    expected_output = 0
    pulse_count = 0

    for cycle in range(200):  # Adjust the number of cycles
        await RisingEdge(dut.clk)

        # Count the pulses received
        if int(dut.uo_out) != expected_output:
            expected_output = int(dut.uo_out)
            pulse_count += 1

        if pulse_count >= 3:  # Check for a specific number of pulses
            dut._log.info("Test passed: Expected pulses observed")
            break  # End the test upon receiving the expected number of pulses

    if pulse_count < 3:
        dut._log.error("Test failed: Expected pulses not observed")



#Runs indefinitely
# import cocotb
# from cocotb.clock import Clock
# from cocotb.triggers import RisingEdge

# @cocotb.test()
# async def test_my_design(dut):
#     CONSTANT_CURRENT = 10

#     clock = Clock(dut.clk, 1, units="ns")
#     await clock.start()
#     # cocotb.fork(clock.start())

#     dut.rst_n <= 0
#     await RisingEdge(dut.clk)
#     dut.rst_n <= 1
#     await RisingEdge(dut.clk)

#     dut.ui_in <= CONSTANT_CURRENT
#     dut.ena <= 1

#     expected_output = 0
#     pulse_count = 0

#     for cycle in range(200):  # Adjust the number of cycles
#         await RisingEdge(dut.clk)

#         # Count the pulses received
#         if int(dut.uo_out) != expected_output:
#             expected_output = int(dut.uo_out)
#             pulse_count += 1

#         if cycle == 150:  # Adjust the cycle count based on expected behavior
#             # Change the expected_output after 150 cycles
#             expected_output = 3  # Modify this value based on the expected behavior

#     if pulse_count >= 3:  # Adjust the expected number of pulses based on design
#         dut._log.info("Test passed: Expected behavior validated")
#     else:
#         dut._log.error("Test failed: Unexpected behavior")





##Same, but trying to cater it
# import cocotb
# from cocotb.clock import Clock
# from cocotb.triggers import RisingEdge, Timer

# @cocotb.test()
# async def test_my_design(dut):
#     CONSTANT_CURRENT = 10

#     # Initialize clock
#     clock = Clock(dut.clk, 1, units="ns")
#     cocotb.fork(clock.start())

#     dut.rst_n <= 0  # Active low reset
#     await RisingEdge(dut.clk)
#     dut.rst_n <= 1  # Take out of reset
#     await RisingEdge(dut.clk)

#     dut.ui_in <= CONSTANT_CURRENT
#     dut.ena <= 1  # Enable design

#     for _ in range(100):  # Simulate 100 clock cycles
#         await RisingEdge(dut.clk)

#     # Set expected output to the maximum value (255 for 8-bit output)
#     expected_output = 255
#     assert int(dut.uo_out) == expected_output, f"Expected {expected_output}, but got {int(dut.uo_out)}"





##Same
# import cocotb
# from cocotb.clock import Clock
# from cocotb.triggers import RisingEdge, FallingEdge, Timer

# @cocotb.test()
# async def test_my_design(dut):
#     # Constants
#     CONSTANT_CURRENT = 10

#     # Initialize clock
#     clock = Clock(dut.clk, 10, units="ns")  # Adjust based on your design's clock
#     cocotb.fork(clock.start())

#     # Reset
#     dut.rst_n <= 0
#     await RisingEdge(dut.clk)
#     dut.rst_n <= 1
#     await RisingEdge(dut.clk)

#     # Set inputs
#     dut.ui_in <= CONSTANT_CURRENT
#     dut.ena <= 1

#     # Simulate clock cycles
#     for _ in range(50):
#         await RisingEdge(dut.clk)

#     # Validate expected output
#     expected_output = 42  # Change this value based on the expected design behavior
#     assert int(dut.uo_out) == expected_output, f"Output Mismatch: Expected {expected_output}, Got {int(dut.uo_out)}"




##Same as prior test
# Import necessary Cocotb modules
# import cocotb
# from cocotb.clock import Clock
# from cocotb.triggers import RisingEdge, Timer

# # Import any other necessary modules or classes from your design

# @cocotb.test()
# async def test_design(dut):
#     # Set your arbitrary input value
#     input_value = 42  # An example input value

#     # Initialize the clock
#     clock = Clock(dut.clk, 10, units="ns")  # Assuming 10ns clock period
#     cocotb.fork(clock.start())

#     # Reset the DUT
#     dut.rst_n <= 0
#     await RisingEdge(dut.clk)
#     dut.rst_n <= 1
#     await RisingEdge(dut.clk)

#     # Apply the input value and enable the design
#     dut.ui_in <= input_value
#     dut.ena <= 1

#     # Wait for a certain number of clock cycles for processing
#     for _ in range(10):  # Adjust this value according to your design's latency
#         await RisingEdge(dut.clk)

#     # Get the output value from the decoder
#     output_value = dut.uo_out.value.integer

#     # Perform assertions to verify the expected output
#     # Assuming the decoder design simply passes through the input, check if output matches input
#     assert output_value == input_value, f"Expected: {input_value}, Got: {output_value}"




## Did not work - only docs passed
# @cocotb.test()
# async def test_design(dut):
#     CONSTANT_CURRENT = 10

#     cocotb.fork(Clock(dut.clk, 1, units="ns").start())

#     dut.rst_n <= 0
#     await ClockCycles(dut.clk, 10)
#     dut.rst_n <= 1

#     dut.ui_in <= CONSTANT_CURRENT
#     dut.ena <= 1

#     for _ in range(100):
#         await RisingEdge(dut.clk)

#     # Your additional assertions or checks go here
#     # Example: Check the uo_out signals after 100 clock cycles
#     for _ in range(8):  # Assuming uo_out is 8 bits
#         assert dut.uo_out.value.integer == expected_output  # Replace expected_output with the expected value
#         await RisingEdge(dut.clk)

#     # Add more checks or assertions if needed




## First Try - test failed
# segments = [63, 6, 91, 79, 102, 109, 125, 7, 127, 111]

# @cocotb.test()
# async def test_design(dut):
#     CONSTANT_CURRENT = 10  # Inject some current

#     dut._log.info("Starting simulation")

#     # Initialize clock
#     clock = Clock(dut.clk, 1, units="ns")
#     cocotb.fork(clock.start())

#     dut.rst_n <= 0  # Active low reset
#     await RisingEdge(dut.clk)
#     dut.rst_n <= 1  # Take out of reset

#     dut.ui_in <= CONSTANT_CURRENT
#     dut.ena <= 1  # Enable design

#     for _ in range(100):
#         await RisingEdge(dut.clk)

#     dut._log.info("Test done")





## Passed tests!
# import cocotb
# from cocotb.clock import Clock
# from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles



# @cocotb.test()
# async def test_my_design(dut):
#     dut._log.info("start")





# # In class demo
# segments = [ 63, 6, 91, 79, 102, 109, 125, 7, 127, 111 ]

# @cocotb.test()
# async def test_my_design(dut):
#     CONSTANT_CURRENT = 10 #inject some current

#     dut._log.info("starting simulation")

#     #initialize clock
#     clock = Clock(dut.clk, 1, units="ns")
#     cocotb.start_soon(clock.start())

#     dut.rst_n.value = 0 # active low reset

#     await ClockCycles(dut.clk, 10)
#     dut.rst_n.value = 1 # take out of reset

#     dut.ui_in.value = CONSTANT_CURRENT
#     dut.ena.value =1 # enable design

#     for _ in range(100):
#         await RisingEdge(dut.clk)

#     dut._log.info("done?")




#async def test_7seg(dut):
    
    # dut._log.info("start")
    # clock = Clock(dut.clk, 10, units="us")
    # cocotb.start_soon(clock.start())

    # # reset
    # dut._log.info("reset")
    # dut.rst_n.value = 0
    # # set the compare value
    # dut.ui_in.value = 1
    # await ClockCycles(dut.clk, 10)
    # dut.rst_n.value = 1

    # # the compare value is shifted 10 bits inside the design to allow slower counting
    # max_count = dut.ui_in.value << 10
    # dut._log.info(f"check all segments with MAX_COUNT set to {max_count}")
    # # check all segments and roll over
    # for i in range(15):
    #     dut._log.info("check segment {}".format(i))
    #     await ClockCycles(dut.clk, max_count)
    #     assert int(dut.segments.value) == segments[i % 10]

    #     # all bidirectionals are set to output
    #     assert dut.uio_oe == 0xFF

    # # reset
    # dut.rst_n.value = 0
    # # set a different compare value
    # dut.ui_in.value = 3
    # await ClockCycles(dut.clk, 10)
    # dut.rst_n.value = 1

    # max_count = dut.ui_in.value << 10
    # dut._log.info(f"check all segments with MAX_COUNT set to {max_count}")
    # # check all segments and roll over
    # for i in range(15):
    #     dut._log.info("check segment {}".format(i))
    #     await ClockCycles(dut.clk, max_count)
    #     assert int(dut.segments.value) == segments[i % 10]

