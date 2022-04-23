
default:

dot/all.mk:
	find $(@D) -name '*.txt' | sort -V | sed 's/^/alls += /;s/.txt$$/.png/' > $@

dot/top_down_ranking.mk:
	find $(@D) -name '*-top_down_ranking.txt' | sort -V | sed 's/^/top_down_ranking += /;s/.txt$$/.png/' > $@

dot/bottom_up_ranking.mk:
	find $(@D) -name '*-bottom_up_ranking.txt' | sort -V | sed 's/^/bottom_up_ranking += /;s/.txt$$/.png/' > $@

dot/dominators.mk:
	find $(@D) -name '*-dominators.txt' | sort -V | sed 's/^/dominators += /;s/.txt$$/.png/' > $@

dot/postdominators.mk:
	find $(@D) -name '*-postdominators.txt' | sort -V | sed 's/^/postdominators += /;s/.txt$$/.png/' > $@

dot/phi.mk:
	find $(@D) -name '*-phi.txt' | sort -V | sed 's/^/phi += /;s/.txt$$/.png/' > $@

dot/optimize.mk:
	find $(@D) -name '*-optimize.txt' | sort -V | sed 's/^/optimize += /;s/.txt$$/.png/' > $@

dot/inheritance.mk:
	find $(@D) -name '*-inheritance.txt' | sort -V | sed 's/^/inheritance += /;s/.txt$$/.png/' > $@

include dot/all.mk
include dot/top_down_ranking.mk
include dot/bottom_up_ranking.mk
include dot/dominators.mk
include dot/postdominators.mk
include dot/phi.mk
include dot/optimize.mk
include dot/inheritance.mk

all: $(alls)

.PRECIOUS: dot/%.png

eog-%: dot/%.png
	eog $<

mpv-%: dot/%.png
	mpv $<

gimp-%: dot/%.png
	gimp $<

gimp-all: $(alls)
	gimp $(alls)

mpv-all: $(alls)
	mpv $(alls) # --no-save-position-on-quit

mpv-top_down_ranking: $(top_down_ranking)
	mpv $(top_down_ranking)

mpv-bottom_up_ranking: $(bottom_up_ranking)
	mpv $(bottom_up_ranking)

mpv-dominators: $(dominators)
	mpv $(dominators)

mpv-postdominators: $(postdominators)
	mpv $(postdominators)

mpv-inheritance: $(inheritance)
	mpv $(inheritance)

mpv-phi: $(phi)
	mpv $(phi)

mpv-optimize: $(optimize)
	mpv $(optimize)

gimp-optimize: $(optimize)
	gimp $(optimize)

gimp-%: dot/%.png
	gimp $<

dot/%.png: dot/%.txt
	dot -Tpng < $< > $@












