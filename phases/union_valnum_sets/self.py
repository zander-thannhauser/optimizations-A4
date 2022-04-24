
from phases.self import phase;

class union_valnum_sets_phase(phase): pass;

from .init import union_valnum_sets_phase_init;
from .str import union_valnum_sets_phase_str;
from .lt import union_valnum_sets_phase_lt;
from .eq import union_valnum_sets_phase_eq;

from .dotout import union_valnum_sets_phase_dotout;
from .process import union_valnum_sets_phase_process;

union_valnum_sets_phase.__init__ = union_valnum_sets_phase_init;
union_valnum_sets_phase.__str__ = union_valnum_sets_phase_str;
union_valnum_sets_phase.__lt__ = union_valnum_sets_phase_lt;
union_valnum_sets_phase.__eq__ = union_valnum_sets_phase_eq;

union_valnum_sets_phase.dotout = union_valnum_sets_phase_dotout;
union_valnum_sets_phase.process = union_valnum_sets_phase_process;


