
class multiplicity: pass

from .init         import multiplicity_init;
from .str          import multiplicity_str;
from .eq           import multiplicity_eq;
from .hash         import multiplicity_hash;
from .dotout       import multiplicity_dotout;
from .union        import multiplicity_union;
from .difference   import multiplicity_difference;
from .intersection import multiplicity_intersection;

multiplicity.__init__ = multiplicity_init;
multiplicity.__str__  = multiplicity_str;
multiplicity.__eq__   = multiplicity_eq;
multiplicity.__hash__ = multiplicity_hash;

multiplicity.union = multiplicity_union;
multiplicity.dotout = multiplicity_dotout;
multiplicity.difference = multiplicity_difference;
multiplicity.intersection = multiplicity_intersection;


