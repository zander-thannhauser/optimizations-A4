
class liverange:
	instance_counter = 0;

from .str import liverange_str;
from .init import liverange_init;
from .dotout import liverange_dotout;

liverange.__init__ = liverange_init;
liverange.__str__ = liverange_str;

liverange.dotout = liverange_dotout;



