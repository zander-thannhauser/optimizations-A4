
class instruction:
	counter = 0;

from .init   import instruction_init;
from .str    import instruction_str;
from .eq     import instruction_eq;
from .hash   import instruction_hash;
from .lt     import instruction_lt;

from .dotout    import instruction_dotout;
from .newdotout import instruction_newdotout;
from .newerdotout import instruction_newerdotout;

instruction.__init__ = instruction_init;
instruction.__str__  = instruction_str;
instruction.__eq__   = instruction_eq;
instruction.__hash__ = instruction_hash;
instruction.__lt__   = instruction_lt;

instruction.dotout = instruction_dotout;
instruction.newdotout = instruction_newdotout;
instruction.newerdotout = instruction_newerdotout;


