
from phases.self import phase;

class optimize_phase(phase): pass;

from .init import optimize_phase_init;
from .str import optimize_phase_str;
from .lt import optimize_phase_lt;
from .eq import optimize_phase_eq;

from .dotout import optimize_phase_dotout;
from .process import optimize_phase_process;
from .subdotout import optimize_phase_subdotout;

optimize_phase.__init__ = optimize_phase_init;
optimize_phase.__str__ = optimize_phase_str;
optimize_phase.__lt__ = optimize_phase_lt;
optimize_phase.__eq__ = optimize_phase_eq;

optimize_phase.dotout = optimize_phase_dotout;
optimize_phase.process = optimize_phase_process;
optimize_phase.subdotout = optimize_phase_subdotout;


