
class phase:
	frame_counter         = 0;
	LOST_PARENT           = 1;
	RESET_DOMINATORS      = 2;
	DOMINATORS            = 3;
	RESET_POST_DOMINATORS = 4;
	POST_DOMINATORS       = 5;
	IN_OUT                = 6;
	INHEIRTANCE           = 7;
	PHI                   = 8;
	OPTIMIZE              = 9;
	CRITICAL              = 10;
	DEAD_CODE             = 11;

from .init import phase_init;

phase.__init__ = phase_init;


