
from debug import *;

first_time = True;

def print_block_asm(block, p):
	enter(f"print_asm(block.rpo = {block.rpo})");
	
	p.comment("block.rpo = %s:", block.rpo);
	
	global first_time;
	
	if block.label and (block.label != ".return" or first_time):
		p.printf("%s:", block.label, prefix = "");
		first_time = False;
	
	for inst in block.newest_instructions:
		inst.print(p);
	
	if block.newest_jump is not None:
		block.newest_jump.print(p);
	
	for i, child in enumerate(block.successors):
		
		dprint(f"children[{i}] = {child}");
		
		match (i, "printed-assembly" in child.phase_counters):
			
			# fallthrough child, assembly already printed
			case (0, 1):
				assert(child.label);
				if child.label == ".return":
					p.printf("ret");
				else:
					p.printf("jumpI -> %s", child.label);
			
			# not fallthrough, assembly already printed
			case (_, 1):
				# this block's jump will already go there
				pass;
			
			# any child with assembly that has yet to print:
			case (_, 0):
				child.phase_counters["printed-assembly"] = 1;
				print_block_asm(child, p);
			
			case conditions:
				dprint(f"conditions = {conditions}");
				assert(not "TODO");
	
	exit();

def print_asm(p, start, frame, parameters, **_):
	enter("print_asm()");
	
	p.printf(".frame %s, %s %s", frame["name"], frame["framesize"], \
		"".join(f", %vr{p.liverange.register}" for p in parameters[4:]), prefix = "");
	
	p.indent();
	print_block_asm(start, p);
	p.unindent();
	
	exit("return;");





















