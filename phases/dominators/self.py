
from phases.self import phase;

class dominators_phase(phase): pass;

from .init import dominators_phase_init;
from .str import dominators_phase_str;
from .lt import dominators_phase_lt;
from .eq import dominators_phase_eq;

from .dotout import dominators_phase_dotout;
from .process import dominators_phase_process;

dominators_phase.__init__ = dominators_phase_init;
dominators_phase.__str__ = dominators_phase_str;
dominators_phase.__lt__ = dominators_phase_lt;
dominators_phase.__eq__ = dominators_phase_eq;

dominators_phase.dotout = dominators_phase_dotout;
dominators_phase.process = dominators_phase_process;


