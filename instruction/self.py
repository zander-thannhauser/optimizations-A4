
class instruction:
	counter = 0;

from .init   import instruction_init;
from .str    import instruction_str;
from .eq     import instruction_eq;
from .hash   import instruction_hash;
from .lt     import instruction_lt;

from .print        import instruction_print;
from .dotout       import instruction_dotout;
from .newdotout    import instruction_newdotout;
from .newerdotout  import instruction_newerdotout;
from .newestdotout import instruction_newestdotout;

instruction.__init__ = instruction_init;
instruction.__str__  = instruction_str;
instruction.__eq__   = instruction_eq;
instruction.__hash__ = instruction_hash;
instruction.__lt__   = instruction_lt;

instruction.print = instruction_print;
instruction.dotout = instruction_dotout;
instruction.newdotout = instruction_newdotout;
instruction.newerdotout = instruction_newerdotout;
instruction.newestdotout = instruction_newestdotout;


