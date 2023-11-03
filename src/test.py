
# import cocotb
# from cocotb.clock import Clock
# from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles


import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_my_design(dut):
    CONSTANT_CURRENT = 10

    # Initialize clock
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    # Reset the design
    dut.rst_n.setimmediatevalue(0)
    await RisingEdge(dut.clk)
    dut.rst_n.setimmediatevalue(1)
    await RisingEdge(dut.clk)

    # Set the constant current and enable the design
    dut.ui_in.setimmediatevalue(CONSTANT_CURRENT)
    dut.ena.setimmediatevalue(1)

    # Define expected output and pulse count
    expected_output = 0
    pulse_count = 0

    # Run for a specific number of cycles
    for cycle in range(200):  # Adjust the number of cycles
        await RisingEdge(dut.clk)

        # Detect pulses and update the count
        if int(dut.uo_out.value) != expected_output:
            expected_output = int(dut.uo_out.value)
            pulse_count += 1

        # Change the expected output after a certain number of cycles
        if cycle == 150:  # Adjust the cycle count based on expected behavior
            expected_output = 3  # Modify this value based on the expected behavior

    # Validate the test based on the expected pulse count
    if pulse_count >= 3:  # Adjust the expected number of pulses based on design
        dut._log.info("Test passed: Expected behavior validated")
    else:
        dut._log.error("Test failed: Unexpected behavior")




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

