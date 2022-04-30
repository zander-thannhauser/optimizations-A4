
from phases.self import phase;

class insert_delete_phase(phase): pass;

from .init import insert_delete_phase_init;
from .str import insert_delete_phase_str;
from .lt import insert_delete_phase_lt;
from .eq import insert_delete_phase_eq;

from .dotout import insert_delete_phase_dotout;
from .process import insert_delete_phase_process;

insert_delete_phase.__init__ = insert_delete_phase_init;
insert_delete_phase.__str__ = insert_delete_phase_str;
insert_delete_phase.__lt__ = insert_delete_phase_lt;
insert_delete_phase.__eq__ = insert_delete_phase_eq;

insert_delete_phase.dotout = insert_delete_phase_dotout;
insert_delete_phase.process = insert_delete_phase_process;


