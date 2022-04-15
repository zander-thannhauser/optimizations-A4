
class block: pass

from .init import block_init;
#from .lt import block_lt;
from .eq import block_eq;
from .str import block_str;
from .hash import block_hash;

block.__init__ = block_init;
#block.__lt__ = block_lt;
block.__eq__ = block_eq;
block.__str__ = block_str;
block.__hash__ = block_hash;


