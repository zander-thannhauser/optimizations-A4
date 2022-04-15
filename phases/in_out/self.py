
from phases.self import phase;

class in_out_phase(phase): pass;

from .init import in_out_phase_init;
from .str import in_out_phase_str;
from .lt import in_out_phase_lt;
from .eq import in_out_phase_eq;

from .dotout import in_out_phase_dotout;
from .process import in_out_phase_process;

in_out_phase.__init__ = in_out_phase_init;
in_out_phase.__str__ = in_out_phase_str;
in_out_phase.__lt__ = in_out_phase_lt;
in_out_phase.__eq__ = in_out_phase_eq;

in_out_phase.dotout = in_out_phase_dotout;
in_out_phase.process = in_out_phase_process;


