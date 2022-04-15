
class expression_table:
	valcounter = 0;

from .init import expression_table_init;

expression_table.__init__ = expression_table_init;

#from .mkvn   import expression_table_mkvn;
from .avrwvn import expression_table_avrwvn;
from .extovn import expression_table_extovn;
from .vntoex import expression_table_vntoex;
from .copy   import expression_table_copy;
from .vrtovn import expression_table_vrtovn;

#expression_table.mkvn   = expression_table_mkvn;
expression_table.avrwvn = expression_table_avrwvn;
expression_table.extovn = expression_table_extovn;
expression_table.vntoex = expression_table_vntoex;
expression_table.copy   = expression_table_copy;
expression_table.vrtovn = expression_table_vrtovn;


