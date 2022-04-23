
class phase:
	frame_counter         = 0;
	LOST_PARENT           = 1;
	
	# code-motion (A3):
	SYNTAX_LOOKUP         = 2;
	AVAILABLE             = 3;
	ANTICIPATION          = 4;
	EARLIEST              = 5;
	LATER                 = 6;
	INSERT_DELETE         = 7;
	
	# SSA redundancy-elimination (A2):
#	RESET_DOMINATORS      = 2;
#	DOMINATORS            = 3;
#	RESET_POST_DOMINATORS = 4;
#	POST_DOMINATORS       = 5;
#	RESET_IN_OUT          = 6;
#	IN_OUT                = 7;
#	INHEIRTANCE           = 8;
#	PHI                   = 9;
#	OPTIMIZE              = 10;
	
	# dead-code removal (A3?):
#	CRITICAL              = 11;
#	DEAD_CODE             = 12;
	
	# register-allocation (A4):
#	MAX_PHASE             = 13;

from .init import phase_init;

phase.__init__ = phase_init;


