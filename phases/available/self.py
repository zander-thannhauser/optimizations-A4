
from phases.self import phase;

class available_phase(phase): pass;

from .init import available_phase_init;
from .str import available_phase_str;
from .lt import available_phase_lt;
from .eq import available_phase_eq;

from .dotout import available_phase_dotout;
from .process import available_phase_process;
from .subdotout import available_phase_subdotout;

available_phase.__init__ = available_phase_init;
available_phase.__str__ = available_phase_str;
available_phase.__lt__ = available_phase_lt;
available_phase.__eq__ = available_phase_eq;

available_phase.dotout = available_phase_dotout;
available_phase.process = available_phase_process;
available_phase.subdotout = available_phase_subdotout;


