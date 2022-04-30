
from phases.self import phase;

class syntax_lookup_phase(phase): pass;

from .init import syntax_lookup_phase_init;
from .str import syntax_lookup_phase_str;
from .lt import syntax_lookup_phase_lt;
from .eq import syntax_lookup_phase_eq;

from .dotout import syntax_lookup_phase_dotout;
from .process import syntax_lookup_phase_process;

syntax_lookup_phase.__init__ = syntax_lookup_phase_init;
syntax_lookup_phase.__str__ = syntax_lookup_phase_str;
syntax_lookup_phase.__lt__ = syntax_lookup_phase_lt;
syntax_lookup_phase.__eq__ = syntax_lookup_phase_eq;

syntax_lookup_phase.dotout = syntax_lookup_phase_dotout;
syntax_lookup_phase.process = syntax_lookup_phase_process;


