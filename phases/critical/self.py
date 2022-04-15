
from phases.self import phase;

class critical_phase(phase): pass;

from .init import critical_phase_init;
from .str import critical_phase_str;
from .lt import critical_phase_lt;
from .eq import critical_phase_eq;

from .dotout import critical_phase_dotout;
from .process import critical_phase_process;

critical_phase.__init__ = critical_phase_init;
critical_phase.__str__ = critical_phase_str;
critical_phase.__lt__ = critical_phase_lt;
critical_phase.__eq__ = critical_phase_eq;

critical_phase.dotout = critical_phase_dotout;
critical_phase.process = critical_phase_process;


