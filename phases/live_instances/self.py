
from phases.self import phase;

class live_instances_phase(phase): pass;

from .init import live_instances_phase_init;
from .str import live_instances_phase_str;
from .lt import live_instances_phase_lt;
from .eq import live_instances_phase_eq;

from .dotout import live_instances_phase_dotout;
from .process import live_instances_phase_process;

live_instances_phase.__init__ = live_instances_phase_init;
live_instances_phase.__str__ = live_instances_phase_str;
live_instances_phase.__lt__ = live_instances_phase_lt;
live_instances_phase.__eq__ = live_instances_phase_eq;

live_instances_phase.dotout = live_instances_phase_dotout;
live_instances_phase.process = live_instances_phase_process;


