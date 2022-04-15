
from phases.self import phase;

class phi_phase(phase): pass;

from .init import phi_phase_init;
from .str import phi_phase_str;
from .lt import phi_phase_lt;
from .eq import phi_phase_eq;

from .dotout import phi_phase_dotout;
from .process import phi_phase_process;

phi_phase.__init__ = phi_phase_init;
phi_phase.__str__ = phi_phase_str;
phi_phase.__lt__ = phi_phase_lt;
phi_phase.__eq__ = phi_phase_eq;

phi_phase.dotout = phi_phase_dotout;
phi_phase.process = phi_phase_process;


