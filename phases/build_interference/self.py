
from phases.self import phase;

class build_interference_phase(phase): pass;

from .init import build_interference_phase_init;
from .str import build_interference_phase_str;
from .lt import build_interference_phase_lt;
from .eq import build_interference_phase_eq;

from .dotout import build_interference_phase_dotout;
from .process import build_interference_phase_process;
from .subdotout import build_interference_phase_subdotout;

build_interference_phase.__init__ = build_interference_phase_init;
build_interference_phase.__str__ = build_interference_phase_str;
build_interference_phase.__lt__ = build_interference_phase_lt;
build_interference_phase.__eq__ = build_interference_phase_eq;

build_interference_phase.dotout = build_interference_phase_dotout;
build_interference_phase.process = build_interference_phase_process;
build_interference_phase.subdotout = build_interference_phase_subdotout;


