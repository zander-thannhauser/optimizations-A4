
from phases.self import phase;

class anticipation_phase(phase): pass;

from .init import anticipation_phase_init;
from .str import anticipation_phase_str;
from .lt import anticipation_phase_lt;
from .eq import anticipation_phase_eq;

from .dotout import anticipation_phase_dotout;
from .process import anticipation_phase_process;
from .subdotout import anticipation_phase_subdotout;

anticipation_phase.__init__ = anticipation_phase_init;
anticipation_phase.__str__ = anticipation_phase_str;
anticipation_phase.__lt__ = anticipation_phase_lt;
anticipation_phase.__eq__ = anticipation_phase_eq;

anticipation_phase.dotout = anticipation_phase_dotout;
anticipation_phase.process = anticipation_phase_process;
anticipation_phase.subdotout = anticipation_phase_subdotout;

