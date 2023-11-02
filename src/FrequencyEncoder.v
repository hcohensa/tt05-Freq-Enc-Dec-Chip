
module FrequencyEncoder (
    input wire data_input,
    input wire enable,
    input wire clk,
    output reg pulse_output
);
    reg [7:0] counter = 8'b00000000; // Initialize the counter

    always @(posedge clk) begin
        if (enable) begin // Only count when enabled by the PLL
            counter <= counter + 1; // Increment the counter
        end
    end

    // Output a pulse when the count matches the data input
    always @(posedge clk) begin
        if (counter == data_input) begin
            pulse_output <= 1'b1;
        end else begin
            pulse_output <= 1'b0;
        end
    end
    
endmodule