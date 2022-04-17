
class unknown: pass

from .init   import unknown_init;
from .str    import unknown_str;
from .hash   import unknown_hash;
from .dotout import unknown_dotout;

unknown.__init__ = unknown_init;
unknown.__str__  = unknown_str;
unknown.__hash__ = unknown_hash;
unknown.dotout = unknown_dotout;


