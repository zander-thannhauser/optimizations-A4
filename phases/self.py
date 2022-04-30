
class phase:
	frame_counter             =  0;
	
	# check for unreachable:
	LOST_PARENT               =  1;
	
	# code-motion (A3):
	SYNTAX_LOOKUP             =  2;
	AVAILABLE                 =  3;
	ANTICIPATION              =  4;
	EARLIEST                  =  5;
	LATER                     =  6;
	INSERT_DELETE             =  7;
	
	# SSA redundancy elmination (A2):
	RESET_DOMINATORS          =  8;
	DOMINATORS                =  9;
	RESET_POST_DOMINATORS     = 10;
	POST_DOMINATORS           = 11;
	RESET_IN_OUT              = 12;
	IN_OUT                    = 13;
	INHEIRTANCE               = 14;
	PHI                       = 15;
	OPTIMIZE                  = 16;
	
	# dead-code elmination (A3?):
	SUPERFICAL_CRITICAL       = 17;
	CRITICAL                  = 18;
	DEAD_CODE                 = 19;
	
	LOOP_DEPTH                = 20;
	
	# register-allocation (A4):
	VALNUM_SINGLETON_SETS     = 21;
	UNION_VALNUM_SETS         = 22;
	RENAME_VALNUMS_TO_LIVEIDS = 23;
	# do:
	LIVE_IN_OUT               = 24;
	LIVE_INHERITANCE          = 25;
	LIVE_INSTANCES            = 26;
	BUILD_INTERFERENCE        = 27;
	CALCULATE_COST            = 28;
	ALLOCATE_REGISTER         = 29;
	SPILL_LIVERANGE           = 30;
	# while (spill);
	LIVEIDS_TO_REGISTER       = 31;
	REMOVE_I2IS               = 32;

from .init import phase_init;

phase.__init__ = phase_init;























