
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

dot/anticipation.mk:
	find $(@D) -name '*-anticipation.txt' | sort -V | sed 's/^/anticipation += /;s/.txt$$/.png/' > $@

dot/available.mk:
	find $(@D) -name '*-available.txt' | sort -V | sed 's/^/available += /;s/.txt$$/.png/' > $@

dot/earliest.mk:
	find $(@D) -name '*-earliest.txt' | sort -V | sed 's/^/earliest += /;s/.txt$$/.png/' > $@

dot/later.mk:
	find $(@D) -name '*-later.txt' | sort -V | sed 's/^/later += /;s/.txt$$/.png/' > $@

include dot/all.mk
include dot/top_down_ranking.mk
include dot/bottom_up_ranking.mk
include dot/dominators.mk
include dot/postdominators.mk
include dot/phi.mk
include dot/optimize.mk
include dot/anticipation.mk
include dot/available.mk
include dot/earliest.mk
include dot/later.mk

all: $(alls)

.PRECIOUS: dot/%.png

eog-%: dot/%.png
	eog $<

mpv-%: dot/%.png
	mpv $<

gimp-all: $(alls)
	gimp $(alls)

mpv-top_down_ranking: $(top_down_ranking)
	mpv $(top_down_ranking)

mpv-bottom_up_ranking: $(bottom_up_ranking)
	mpv $(bottom_up_ranking)

mpv-all: $(alls)
	mpv $(alls)

mpv-dominators: $(dominators)
	mpv $(dominators)

mpv-postdominators: $(postdominators)
	mpv $(postdominators)

mpv-phi: $(phi)
	mpv $(phi)

mpv-optimize: $(optimize)
	mpv $(optimize)

gimp-optimize: $(optimize)
	gimp $(optimize)

mpv-available: $(available)
	mpv $(available)

gimp-available: $(available)
	gimp $(available)

eog-available: $(available)
	eog $(available)

mpv-anticipation: $(anticipation)
	mpv $(anticipation)

eog-anticipation: $(anticipation)
	eog $(anticipation)

gimp-anticipation: $(anticipation)
	gimp $(anticipation)

mpv-earliest: $(earliest)
	mpv $(earliest)

eog-earliest: $(earliest)
	eog $(earliest)

gimp-earliest: $(earliest)
	gimp $(earliest)

eog-later: $(later)
	eog $(later)

mpv-later: $(later)
	mpv $(later)

gimp-later: $(later)
	gimp $(later)

gimp-%: dot/%.png
	gimp $<

dot/%.png: dot/%.txt
	dot -Tpng < $< > $@












