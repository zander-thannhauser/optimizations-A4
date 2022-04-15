
class instruction:
	counter = 0;

from .init   import instruction_init;
from .str    import instruction_str;
from .eq     import instruction_eq;
from .hash   import instruction_hash;

from .dotout    import instruction_dotout;
from .newdotout import instruction_newdotout;

instruction.__init__ = instruction_init;
instruction.__str__  = instruction_str;
instruction.__eq__   = instruction_eq;
instruction.__hash__ = instruction_hash;

instruction.dotout = instruction_dotout;
instruction.newdotout = instruction_newdotout;


