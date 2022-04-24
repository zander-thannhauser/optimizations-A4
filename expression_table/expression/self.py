
class expression: pass

from .init import expression_init;
from .str  import expression_str;
from .eq   import expression_eq;
from .hash import expression_hash;

from .dotout import expression_dotout;
#from .append_instructions import expression_append_instructions;

expression.__init__ = expression_init;
expression.__str__  = expression_str;
expression.__eq__   = expression_eq;
expression.__hash__ = expression_hash;

expression.dotout = expression_dotout;
#expression.append_instructions = expression_append_instructions;



