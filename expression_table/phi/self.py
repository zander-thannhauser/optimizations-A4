
class phi: pass;

from .init   import phi_init;
from .hash   import phi_hash;
from .eq     import phi_eq;
from .str    import phi_str;

from .dotout import phi_dotout;

phi.__init__ = phi_init;
phi.__hash__ = phi_hash;
phi.__eq__   = phi_eq;
phi.__str__  = phi_str;

phi.dotout = phi_dotout;


