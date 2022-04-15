
from block.self import block;

from instruction.self import instruction;

from debug import *;

def read_block(t):
	
	enter("read_block()");
	
	block_label = ""
	
	if (t.token[0] == '.'):
		block_label = t.token;
		dprint(f"block_label == {block_label}");
		assert(next(t) == ":");
		t.next();
	
	instructions = [];
	jump = None;
	children = ["(fallthrough)"]; # indicates we also want fallthrough
	return_register = None;
	
	while t.token and (t.token[0] != '.'):
		operation = t.token; ins = []; out = None; const = None; label = None;
		
		# dprint(f"operation == {operation}");
		t.next();
		
		match (operation):
			
			# those who take one in and zero out:
			case "iwrite" | "swrite" | "iread":
				ins.append(t.token); t.next();
			
			# those who take one in and one out:
			case "i2i" | "i2f" | "f2i" | "load" | "fload" \
					| "testeq" | "testne" \
					| "testgt" | "testge" \
					| "testne" \
					| "testlt" | "testle" :
				ins.append(t.token); t.next();
				assert(t.token == "=>"); t.next();
				out = t.token; t.next();
			
			# those who take two in and one out:
			case "add" | "sub" | "mult" | "mod" | "comp" \
					| "fadd" | "fmult" | "or":
				ins.append(t.token); t.next();
				assert(t.token == ","); t.next();
				ins.append(t.token); t.next();
				assert(t.token == "=>"); t.next();
				out = t.token; t.next();
			
			# loadI
			case "loadI":
				const = int(t.token); t.next();
				assert(t.token == "=>"); t.next();
				out = t.token; t.next();
				dprint(out);
				# assert(not "CHECK");
			
			# store:
			case "store":
				ins.append(t.token); t.next();
				assert(t.token == "=>"); t.next();
				ins.append(t.token); t.next();
			
			# calls:
			case "call":
				func_label = t.token
				t.next();
				while t.token == ",":
					t.next();
					ins.append(t.token);
					t.next();
				# dprint(f"ins = {ins}");
				appendme = instruction(operation, ins, out = out, label = func_label);
			
			case "icall":
				assert(not "TODO");
#				func_label = t.token
#				t.next();
#				while t.token == ",":
#					t.next();
#					ins.append(t.token);
#					t.next();
#				dprint(f"ins = {ins}");
#				assert(t.token == "=>"); t.next();
#				out = t.token; t.next();
#				dprint(f"out = {out}");
#				instructions.append(instruction(operation, ins, out, func_label));
			
			# nop:
			case "nop":
				operation = None;
			
			# branching:
			case "cbr" | "cbrne":
				ins.append(t.token); t.next();
				assert(t.token == "->"); t.next();
				branch_label = t.token; t.next();
				jump = instruction(operation, ins, out, label = branch_label);
				children.append(branch_label);
				break;
			
			case "jumpI":
				assert(t.token == "->"); t.next();
				branch_label = t.token; t.next();
				children = [branch_label];
				operation = None;
				break;
			
			case "iret":
				assert(not "TODO");
#				ins.append(t.token); t.next();
#				jump = instruction(operation, ins, out, ".return");
#				children = [".return"];
#				break;
			
			case "ret":
				children = [".return"];
				break;
			
			case _:
				dprint(f"operation = {operation}");
				assert(not "TODO");
		
		if operation:
			appendme = instruction(operation, ins, out, \
				const = const, label = label);
			dprint(f"appendme: {str(appendme)}");
			instructions.append(appendme);
	
	retval = block(block_label, instructions, children, jump);
	exit(f"return {retval}");
	return retval;
















