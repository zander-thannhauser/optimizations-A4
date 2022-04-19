
from phases.self import phase;

class reset_in_out_phase(phase): pass;

from .init import reset_in_out_phase_init;
from .str import reset_in_out_phase_str;
from .lt import reset_in_out_phase_lt;
from .eq import reset_in_out_phase_eq;

from .dotout import reset_in_out_phase_dotout;
from .process import reset_in_out_phase_process;

reset_in_out_phase.__init__ = reset_in_out_phase_init;
reset_in_out_phase.__str__ = reset_in_out_phase_str;
reset_in_out_phase.__lt__ = reset_in_out_phase_lt;
reset_in_out_phase.__eq__ = reset_in_out_phase_eq;

reset_in_out_phase.dotout = reset_in_out_phase_dotout;
reset_in_out_phase.process = reset_in_out_phase_process;


