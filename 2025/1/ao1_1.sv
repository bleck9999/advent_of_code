module ao1_1 (input wire CLOCK_50, input wire[3:0] KEY, input [9:0] SW,
				  output reg [6:0] HEX0, HEX1, HEX2, HEX3, HEX4, HEX5,
				  output [9:0] LEDR);
	
	assign resetn=KEY[2];
	assign clk=SW[0] ? CLOCK_50 : KEY[3];
	
	reg [7:0] cur_input;
	reg [14:0] input_address;
	//reg [7:0] working_addr;
	reg [15:0] ram_in, ram_out;
	reg [31:0] out;
	reg [6:0] rotations;
	reg wren;
	
	rom input_mem(
		.address(input_address),
	   .clock(clk),
		.q(cur_input)
	);
	
	/*ram working_memory (
		.address(working_addr),
		.clock(clk),
		.data(ram_in),
		.wren(wren),
		.q(ram_out)
	);*/
	
	sevenseg s0 (.data_in(out[3:0]), .hex_out(HEX0));
	sevenseg s1 (.data_in(out[7:4]), .hex_out(HEX1));
	sevenseg s2 (.data_in(out[11:8]), .hex_out(HEX2));
	sevenseg s3 (.data_in(out[15:12]), .hex_out(HEX3));
	sevenseg s4 (.data_in(out[19:16]), .hex_out(HEX4));
	sevenseg s5 (.data_in(out[23:20]), .hex_out(HEX5));
	
	reg [2:0] state, next_state;
	//assign LEDR[6:0] = cur_input;
	//assign LEDR[9:7] = state;
	assign LEDR = input_address[14:5];
	
	always_ff @(posedge clk, negedge resetn) begin
		if (!resetn) begin
			input_address <= 0;
			out <= 0;
			state <= 7;
			rotations <= 50;
			ram_out <= 0;
		end
		else begin
			unique case (state)
			0: begin
				input_address <= input_address + 1;
			end
			1, 2: begin
				//working_addr <= working_addr + 1;
				input_address <= input_address + 1;
			end
			3, 4: begin
				if (ram_out == 0) begin
					// terrifying hack to fix off by one
					input_address <= input_address - 1;
					
					if (rotations == 0)
						out <= out + 1;
				end else begin
					if (state == 3) begin
						if (rotations == 0)
							rotations <= 99;
						else
							rotations <= rotations - 1;
					end else if (state == 4) begin
						if (rotations == 99)
							rotations <= 0;
						else
							rotations <= rotations + 1;
					end
				end
			end
			6: begin
				out <= 'h17;
			end
			default: begin end
			endcase
			state <= next_state;
			if (wren) ram_out <= ram_in;
		end
	end
	
	reg [3:0] digit;
	
	always_comb begin
		//if (state >= 6) begin
		//	HEX5[6] = 0;
		//end else HEX5[6] = 1;

		wren = 0;
		digit = 0;
		ram_in = 0;
		//working_addr = 0;
		unique case (state)
			7: begin
				wren = 1;
				next_state = 0;
			end
			0: begin
				if (cur_input == "L")
					next_state = 1;
				else if (cur_input == "R")
					next_state = 2;
				else next_state = 6;
			end
			1, 2:	begin
				if (48 <= cur_input && cur_input <= 57) begin
					digit = cur_input ^ 48;
					wren = 1;
					ram_in = ram_out * 10 + digit;
					next_state = state;
				end else if (cur_input == 'h0a) begin
					wren = 0;
					next_state = state + 2;
				end else begin
					wren = 0;
					next_state = state;
				end
			end
			3, 4: begin
				if (ram_out == 0) begin
					wren = 0;
					next_state = 5;
				end else begin
					wren = 1;
					ram_in = ram_out - 1;
					next_state = state;
				end
			end
			5: begin
				if (cur_input != 0)
					next_state = 0;
				else
					next_state = state;
			end
			default: begin
				next_state = state;
			end
		endcase
	end
endmodule