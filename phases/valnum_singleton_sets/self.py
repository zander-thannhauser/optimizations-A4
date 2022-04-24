
from phases.self import phase;

class valnum_singleton_sets_phase(phase): pass;

from .init import valnum_singleton_sets_phase_init;
from .str import valnum_singleton_sets_phase_str;
from .lt import valnum_singleton_sets_phase_lt;
from .eq import valnum_singleton_sets_phase_eq;

from .dotout import valnum_singleton_sets_phase_dotout;
from .process import valnum_singleton_sets_phase_process;

valnum_singleton_sets_phase.__init__ = valnum_singleton_sets_phase_init;
valnum_singleton_sets_phase.__str__ = valnum_singleton_sets_phase_str;
valnum_singleton_sets_phase.__lt__ = valnum_singleton_sets_phase_lt;
valnum_singleton_sets_phase.__eq__ = valnum_singleton_sets_phase_eq;

valnum_singleton_sets_phase.dotout = valnum_singleton_sets_phase_dotout;
valnum_singleton_sets_phase.process = valnum_singleton_sets_phase_process;


