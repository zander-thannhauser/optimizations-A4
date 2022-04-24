
from phases.self import phase;

class superfical_critical_phase(phase): pass;

from .init import superfical_critical_phase_init;
from .str import superfical_critical_phase_str;
from .lt import superfical_critical_phase_lt;
from .eq import superfical_critical_phase_eq;

from .dotout import superfical_critical_phase_dotout;
from .process import superfical_critical_phase_process;

superfical_critical_phase.__init__ = superfical_critical_phase_init;
superfical_critical_phase.__str__ = superfical_critical_phase_str;
superfical_critical_phase.__lt__ = superfical_critical_phase_lt;
superfical_critical_phase.__eq__ = superfical_critical_phase_eq;

superfical_critical_phase.dotout = superfical_critical_phase_dotout;
superfical_critical_phase.process = superfical_critical_phase_process;


