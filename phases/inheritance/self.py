
from phases.self import phase;

class inheritance_phase(phase): pass;

from .init import inheritance_phase_init;
from .str import inheritance_phase_str;
from .lt import inheritance_phase_lt;
from .eq import inheritance_phase_eq;

from .dotout import inheritance_phase_dotout;
from .process import inheritance_phase_process;

inheritance_phase.__init__ = inheritance_phase_init;
inheritance_phase.__str__ = inheritance_phase_str;
inheritance_phase.__lt__ = inheritance_phase_lt;
inheritance_phase.__eq__ = inheritance_phase_eq;

inheritance_phase.dotout = inheritance_phase_dotout;
inheritance_phase.process = inheritance_phase_process;


