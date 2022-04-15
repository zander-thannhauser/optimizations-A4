
from phases.self import phase;

class lost_parent_phase(phase): pass;

from .init import lost_parent_phase_init;
from .str import lost_parent_phase_str;
from .lt import lost_parent_phase_lt;
from .eq import lost_parent_phase_eq;

from .dotout import lost_parent_phase_dotout;
from .process import lost_parent_phase_process;

lost_parent_phase.__init__ = lost_parent_phase_init;
lost_parent_phase.__str__ = lost_parent_phase_str;
lost_parent_phase.__lt__ = lost_parent_phase_lt;
lost_parent_phase.__eq__ = lost_parent_phase_eq;

lost_parent_phase.dotout = lost_parent_phase_dotout;
lost_parent_phase.process = lost_parent_phase_process;


