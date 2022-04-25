
from phases.self import phase;

class allocate_register_phase(phase): pass;

from .init import allocate_register_phase_init;
from .str import allocate_register_phase_str;
from .lt import allocate_register_phase_lt;
from .eq import allocate_register_phase_eq;

from .dotout import allocate_register_phase_dotout;
from .process import allocate_register_phase_process;

allocate_register_phase.__init__ = allocate_register_phase_init;
allocate_register_phase.__str__ = allocate_register_phase_str;
allocate_register_phase.__lt__ = allocate_register_phase_lt;
allocate_register_phase.__eq__ = allocate_register_phase_eq;

allocate_register_phase.dotout = allocate_register_phase_dotout;
allocate_register_phase.process = allocate_register_phase_process;


