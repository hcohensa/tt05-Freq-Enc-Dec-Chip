
module PLL (
    input wire clk_in,
    output wire pll_clk_out
);
    reg [7:0] counter = 8'b00000000; // Initialize the counter

    always @(posedge clk_in) begin
        counter <= counter + 1; // Increment counter with each clock cycle
    end

    // Output a square wave with a 50% duty cycle
    assign pll_clk_out = (counter == 8'd0) ? 1'b1 : 1'b0;
endmodule