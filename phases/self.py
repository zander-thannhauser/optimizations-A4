
class phase:
	frame_counter         =  0;
	
	# SSA redundancy elmination (A2):
	LOST_PARENT           =  1;
	RESET_DOMINATORS      =  2;
	DOMINATORS            =  3;
	RESET_POST_DOMINATORS =  4;
	POST_DOMINATORS       =  5;
	RESET_IN_OUT          =  6;
	IN_OUT                =  7;
	INHEIRTANCE           =  8;
	PHI                   =  9;
	OPTIMIZE              = 10;
	
	# dead-code elmination (A3?):
	SUPERFICAL_CRITICAL   = 11;
	CRITICAL              = 12;
	DEAD_CODE             = 13;
	
	# register-allocation (A4):
	VALNUM_SINGLETON_SETS     = 14;
	UNION_VALNUM_SETS         = 15;
	RENAME_VALNUMS_TO_LIVEIDS = 16;
	# while changed:
	LIVE_IN_OUT               = 17;
	LIVE_INHERITANCE          = 18;
	LIVE_INSTANCES            = 19;
	BUILD_INTERFERENCE        = 20;
	

from .init import phase_init;

phase.__init__ = phase_init;























