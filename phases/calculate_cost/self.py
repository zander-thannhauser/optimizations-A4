
from phases.self import phase;

class calculate_cost_phase(phase): pass;

from .init import calculate_cost_phase_init;
from .str import calculate_cost_phase_str;
from .lt import calculate_cost_phase_lt;
from .eq import calculate_cost_phase_eq;

from .dotout import calculate_cost_phase_dotout;
from .process import calculate_cost_phase_process;

calculate_cost_phase.__init__ = calculate_cost_phase_init;
calculate_cost_phase.__str__ = calculate_cost_phase_str;
calculate_cost_phase.__lt__ = calculate_cost_phase_lt;
calculate_cost_phase.__eq__ = calculate_cost_phase_eq;

calculate_cost_phase.dotout = calculate_cost_phase_dotout;
calculate_cost_phase.process = calculate_cost_phase_process;


