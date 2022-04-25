
from phases.self import phase;

class liveids_to_register_phase(phase): pass;

from .init import liveids_to_register_phase_init;
from .str import liveids_to_register_phase_str;
from .lt import liveids_to_register_phase_lt;
from .eq import liveids_to_register_phase_eq;

from .dotout import liveids_to_register_phase_dotout;
from .process import liveids_to_register_phase_process;

liveids_to_register_phase.__init__ = liveids_to_register_phase_init;
liveids_to_register_phase.__str__ = liveids_to_register_phase_str;
liveids_to_register_phase.__lt__ = liveids_to_register_phase_lt;
liveids_to_register_phase.__eq__ = liveids_to_register_phase_eq;

liveids_to_register_phase.dotout = liveids_to_register_phase_dotout;
liveids_to_register_phase.process = liveids_to_register_phase_process;


