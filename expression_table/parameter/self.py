
class parameter: pass

from .init   import parameter_init;
from .str    import parameter_str;
from .eq     import parameter_eq;
from .hash   import parameter_hash;
from .dotout import parameter_dotout;

parameter.__init__ = parameter_init;
parameter.__str__  = parameter_str;
parameter.__eq__   = parameter_eq;
parameter.__hash__ = parameter_hash;

parameter.dotout = parameter_dotout;


