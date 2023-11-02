
module FrequencyDecoder (
    input wire pulse_input,
    input wire enable,
    input wire clk,
    output reg [7:0] data_output
);
    reg [7:0] counter = 8'b00000000; // Initialize the counter

    always @(posedge clk) begin
        if (enable) begin // Only count when enabled by the PLL
            counter <= counter + 1; // Increment the counter
        end
    end

    // Output the decoded data when a pulse is received
    always @(posedge clk) begin
        if (pulse_input) begin
            data_output <= counter;
        end
    end
endmodule