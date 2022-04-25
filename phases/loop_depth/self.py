
from phases.self import phase;

class loop_depth_phase(phase): pass;

from .init import loop_depth_phase_init;
from .str import loop_depth_phase_str;
from .lt import loop_depth_phase_lt;
from .eq import loop_depth_phase_eq;

from .dotout import loop_depth_phase_dotout;
from .process import loop_depth_phase_process;

loop_depth_phase.__init__ = loop_depth_phase_init;
loop_depth_phase.__str__ = loop_depth_phase_str;
loop_depth_phase.__lt__ = loop_depth_phase_lt;
loop_depth_phase.__eq__ = loop_depth_phase_eq;

loop_depth_phase.dotout = loop_depth_phase_dotout;
loop_depth_phase.process = loop_depth_phase_process;


