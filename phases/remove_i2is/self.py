
from phases.self import phase;

class remove_i2is_phase(phase): pass;

from .init import remove_i2is_phase_init;
from .str import remove_i2is_phase_str;
from .lt import remove_i2is_phase_lt;
from .eq import remove_i2is_phase_eq;

from .dotout import remove_i2is_phase_dotout;
from .process import remove_i2is_phase_process;

remove_i2is_phase.__init__ = remove_i2is_phase_init;
remove_i2is_phase.__str__ = remove_i2is_phase_str;
remove_i2is_phase.__lt__ = remove_i2is_phase_lt;
remove_i2is_phase.__eq__ = remove_i2is_phase_eq;

remove_i2is_phase.dotout = remove_i2is_phase_dotout;
remove_i2is_phase.process = remove_i2is_phase_process;


