
class expression_table:
	valcounter = 0;

from .init import expression_table_init;

expression_table.__init__ = expression_table_init;

from .extovn import expression_table_extovn;
from .vntoex import expression_table_vntoex;

expression_table.extovn = expression_table_extovn;
expression_table.vntoex = expression_table_vntoex;


