
from phases.self import phase;

class template_phase(phase): pass;

from .init import template_phase_init;
from .str import template_phase_str;
from .lt import template_phase_lt;
from .eq import template_phase_eq;

from .dotout import template_phase_dotout;
from .process import template_phase_process;

template_phase.__init__ = template_phase_init;
template_phase.__str__ = template_phase_str;
template_phase.__lt__ = template_phase_lt;
template_phase.__eq__ = template_phase_eq;

template_phase.dotout = template_phase_dotout;
template_phase.process = template_phase_process;


