
from phases.self import phase;

class live_in_out_phase(phase): pass;

from .init import live_in_out_phase_init;
from .str import live_in_out_phase_str;
from .lt import live_in_out_phase_lt;
from .eq import live_in_out_phase_eq;

from .dotout import live_in_out_phase_dotout;
from .process import live_in_out_phase_process;

live_in_out_phase.__init__ = live_in_out_phase_init;
live_in_out_phase.__str__ = live_in_out_phase_str;
live_in_out_phase.__lt__ = live_in_out_phase_lt;
live_in_out_phase.__eq__ = live_in_out_phase_eq;

live_in_out_phase.dotout = live_in_out_phase_dotout;
live_in_out_phase.process = live_in_out_phase_process;


