
from phases.self import phase;

class reset_post_dominators_phase(phase): pass;

from .init import reset_post_dominators_phase_init;
from .str import reset_post_dominators_phase_str;
from .lt import reset_post_dominators_phase_lt;
from .eq import reset_post_dominators_phase_eq;

from .dotout import reset_post_dominators_phase_dotout;
from .process import reset_post_dominators_phase_process;

reset_post_dominators_phase.__init__ = reset_post_dominators_phase_init;
reset_post_dominators_phase.__str__ = reset_post_dominators_phase_str;
reset_post_dominators_phase.__lt__ = reset_post_dominators_phase_lt;
reset_post_dominators_phase.__eq__ = reset_post_dominators_phase_eq;

reset_post_dominators_phase.dotout = reset_post_dominators_phase_dotout;
reset_post_dominators_phase.process = reset_post_dominators_phase_process;


