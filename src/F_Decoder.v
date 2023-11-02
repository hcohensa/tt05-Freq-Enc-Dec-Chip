
module Frequency_Decoder(
    input wire [7:0] encoded_binary_code,  // 8-bit encoded frequency input
    output reg decoded_frequency_signal  // Decoded frequency signal
);
    always @* begin
        // Decoding 8-bit binary code back to frequency signal
        if (encoded_binary_code == 8'b11111111)  // Max frequency reached
            decoded_frequency_signal = 0;  // Reset frequency
        else
            decoded_frequency_signal = encoded_binary_code;  // Retrieve frequency from binary code
    end
endmodule