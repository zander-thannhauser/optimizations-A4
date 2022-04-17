
class unordered: pass

from .init       import unordered_init;
from .str        import unordered_str;
from .eq         import unordered_eq;
from .hash       import unordered_hash;
from .dotout     import unordered_dotout;

unordered.__init__ = unordered_init;
unordered.__str__  = unordered_str;
unordered.__eq__   = unordered_eq;
unordered.__hash__ = unordered_hash;

unordered.dotout = unordered_dotout;


