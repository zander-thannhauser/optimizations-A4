
from phases.self import phase;

class live_inheritance_phase(phase): pass;

from .init import live_inheritance_phase_init;
from .str import live_inheritance_phase_str;
from .lt import live_inheritance_phase_lt;
from .eq import live_inheritance_phase_eq;

from .dotout import live_inheritance_phase_dotout;
from .process import live_inheritance_phase_process;

live_inheritance_phase.__init__ = live_inheritance_phase_init;
live_inheritance_phase.__str__ = live_inheritance_phase_str;
live_inheritance_phase.__lt__ = live_inheritance_phase_lt;
live_inheritance_phase.__eq__ = live_inheritance_phase_eq;

live_inheritance_phase.dotout = live_inheritance_phase_dotout;
live_inheritance_phase.process = live_inheritance_phase_process;


