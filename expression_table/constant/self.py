
class constant: pass

from .init   import constant_init;
from .str    import constant_str;
from .eq     import constant_eq;
from .hash   import constant_hash;

from .dotout import constant_dotout;
#from .append_instructions import constant_append_instructions;

constant.__init__ = constant_init;
constant.__str__  = constant_str;
constant.__eq__   = constant_eq;
constant.__hash__ = constant_hash;

constant.dotout = constant_dotout;
#constant.append_instructions = constant_append_instructions;


