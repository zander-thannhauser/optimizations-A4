
from phases.self import phase;

class rename_valnums_to_liveids_phase(phase): pass;

from .init import rename_valnums_to_liveids_phase_init;
from .str import rename_valnums_to_liveids_phase_str;
from .lt import rename_valnums_to_liveids_phase_lt;
from .eq import rename_valnums_to_liveids_phase_eq;

from .dotout import rename_valnums_to_liveids_phase_dotout;
from .process import rename_valnums_to_liveids_phase_process;

rename_valnums_to_liveids_phase.__init__ = rename_valnums_to_liveids_phase_init;
rename_valnums_to_liveids_phase.__str__ = rename_valnums_to_liveids_phase_str;
rename_valnums_to_liveids_phase.__lt__ = rename_valnums_to_liveids_phase_lt;
rename_valnums_to_liveids_phase.__eq__ = rename_valnums_to_liveids_phase_eq;

rename_valnums_to_liveids_phase.dotout = rename_valnums_to_liveids_phase_dotout;
rename_valnums_to_liveids_phase.process = rename_valnums_to_liveids_phase_process;


