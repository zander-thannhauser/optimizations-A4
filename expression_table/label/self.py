
class label: pass

from .init   import label_init;
from .str    import label_str;
from .eq     import label_eq;
from .hash   import label_hash;

from .dotout import label_dotout;

label.__init__ = label_init;
label.__str__  = label_str;
label.__eq__   = label_eq;
label.__hash__ = label_hash;

label.dotout = label_dotout;


