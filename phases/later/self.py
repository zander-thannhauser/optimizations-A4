
from phases.self import phase;

class later_phase(phase): pass;

from .init import later_phase_init;
from .str import later_phase_str;
from .lt import later_phase_lt;
from .eq import later_phase_eq;

from .dotout import later_phase_dotout;
from .process import later_phase_process;

later_phase.__init__ = later_phase_init;
later_phase.__str__ = later_phase_str;
later_phase.__lt__ = later_phase_lt;
later_phase.__eq__ = later_phase_eq;

later_phase.dotout = later_phase_dotout;
later_phase.process = later_phase_process;


