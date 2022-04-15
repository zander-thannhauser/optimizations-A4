
from phases.self import phase;

class dead_code_phase(phase): pass;

from .init import dead_code_phase_init;
from .str import dead_code_phase_str;
from .lt import dead_code_phase_lt;
from .eq import dead_code_phase_eq;

from .dotout import dead_code_phase_dotout;
from .process import dead_code_phase_process;

dead_code_phase.__init__ = dead_code_phase_init;
dead_code_phase.__str__ = dead_code_phase_str;
dead_code_phase.__lt__ = dead_code_phase_lt;
dead_code_phase.__eq__ = dead_code_phase_eq;

dead_code_phase.dotout = dead_code_phase_dotout;
dead_code_phase.process = dead_code_phase_process;


