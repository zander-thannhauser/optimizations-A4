
class phase:
	frame_counter         =  0;
	LOST_PARENT           =  1;
	RESET_IN_OUT          =  2;
	IN_OUT                =  3;
	INHEIRTANCE           =  4;
	PHI                   =  5;
	OPTIMIZE              =  6;
	RESET_POST_DOMINATORS =  7;
	POST_DOMINATORS       =  8;
	
	# dead-code removal (A3?):
#	CRITICAL              = 11;
#	DEAD_CODE             = 12;
	
	# register-allocation (A4):
#	MAX_PHASE             = 13;

from .init import phase_init;

phase.__init__ = phase_init;


