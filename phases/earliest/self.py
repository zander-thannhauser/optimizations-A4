
from phases.self import phase;

class earliest_phase(phase): pass;

from .init import earliest_phase_init;
from .str import earliest_phase_str;
from .lt import earliest_phase_lt;
from .eq import earliest_phase_eq;

from .dotout import earliest_phase_dotout;
from .process import earliest_phase_process;

earliest_phase.__init__ = earliest_phase_init;
earliest_phase.__str__ = earliest_phase_str;
earliest_phase.__lt__ = earliest_phase_lt;
earliest_phase.__eq__ = earliest_phase_eq;

earliest_phase.dotout = earliest_phase_dotout;
earliest_phase.process = earliest_phase_process;


