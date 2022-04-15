
from phases.self import phase;

class post_dominators_phase(phase): pass;

from .init import post_dominators_phase_init;
from .str import post_dominators_phase_str;
from .lt import post_dominators_phase_lt;
from .eq import post_dominators_phase_eq;

from .dotout import post_dominators_phase_dotout;
from .process import post_dominators_phase_process;

post_dominators_phase.__init__ = post_dominators_phase_init;
post_dominators_phase.__str__ = post_dominators_phase_str;
post_dominators_phase.__lt__ = post_dominators_phase_lt;
post_dominators_phase.__eq__ = post_dominators_phase_eq;

post_dominators_phase.dotout = post_dominators_phase_dotout;
post_dominators_phase.process = post_dominators_phase_process;


