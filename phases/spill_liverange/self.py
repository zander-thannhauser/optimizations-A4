
from phases.self import phase;

class spill_liverange_phase(phase): pass;

from .init import spill_liverange_phase_init;
from .str import spill_liverange_phase_str;
from .lt import spill_liverange_phase_lt;
from .eq import spill_liverange_phase_eq;

from .dotout import spill_liverange_phase_dotout;
from .process import spill_liverange_phase_process;

spill_liverange_phase.__init__ = spill_liverange_phase_init;
spill_liverange_phase.__str__ = spill_liverange_phase_str;
spill_liverange_phase.__lt__ = spill_liverange_phase_lt;
spill_liverange_phase.__eq__ = spill_liverange_phase_eq;

spill_liverange_phase.dotout = spill_liverange_phase_dotout;
spill_liverange_phase.process = spill_liverange_phase_process;


