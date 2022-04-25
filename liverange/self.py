
class liverange:
	instance_counter = 0;

from .lt        import liverange_lt;
from .eq        import liverange_eq;
from .str       import liverange_str;
from .init      import liverange_init;
from .hash      import liverange_hash;
from .dotout    import liverange_dotout;
#from .newdotout import liverange_newdotout;

liverange.__lt__ = liverange_lt;
liverange.__eq__ = liverange_eq;
liverange.__str__ = liverange_str;
liverange.__init__ = liverange_init;
liverange.__hash__ = liverange_hash;

liverange.dotout = liverange_dotout;
#liverange.newdotout = liverange_newdotout;



