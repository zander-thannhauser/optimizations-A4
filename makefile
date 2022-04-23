
default:

dot/all.mk:
	find $(@D) -name '*.txt' | sort -V | sed 's/^/alls += /;s/.txt$$/.png/' > $@

dot/anticipation.mk:
	find $(@D) -name '*-anticipation.txt' | sort -V | sed 's/^/anticipation += /;s/.txt$$/.png/' > $@

dot/available.mk:
	find $(@D) -name '*-available.txt' | sort -V | sed 's/^/available += /;s/.txt$$/.png/' > $@

dot/earliest.mk:
	find $(@D) -name '*-earliest.txt' | sort -V | sed 's/^/earliest += /;s/.txt$$/.png/' > $@

dot/dominators.mk:
	find $(@D) -name '*-dominators.txt' | sort -V | sed 's/^/dominators += /;s/.txt$$/.png/' > $@

dot/postdominators.mk:
	find $(@D) -name '*-postdominators.txt' | sort -V | sed 's/^/postdominators += /;s/.txt$$/.png/' > $@

dot/inout.mk:
	find $(@D) -name '*-inout.txt' | sort -V | sed 's/^/inout += /;s/.txt$$/.png/' > $@

dot/inheritance.mk:
	find $(@D) -name '*-inheritance.txt' | sort -V | sed 's/^/inheritance += /;s/.txt$$/.png/' > $@

include dot/all.mk
include dot/anticipation.mk
include dot/available.mk
include dot/earliest.mk
include dot/dominators.mk
include dot/postdominators.mk
include dot/inout.mk
include dot/inheritance.mk

all: $(alls)

.PRECIOUS: dot/%.png

dot/%.png: dot/%.txt
	dot -Tpng < $< > $@

eog-%: dot/%.png
	eog $<

mpv-%: dot/%.png
	mpv $<

gimp-%: dot/%.png
	gimp $<

gimp-all: $(alls)
	gimp $(alls)

eog-all: $(alls)
	eog $(alls)

mpv-all: $(alls)
	mpv $(alls) --no-save-position-on-quit

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

mpv-dominators: $(dominators)
	mpv $(dominators)

eog-dominators: $(dominators)
	eog $(dominators)

gimp-dominators: $(dominators)
	gimp $(dominators)

mpv-postdominators: $(postdominators)
	mpv $(postdominators)

eog-postdominators: $(postdominators)
	eog $(postdominators)

gimp-postdominators: $(postdominators)
	gimp $(postdominators)

mpv-inout: $(inout)
	mpv $(inout)

eog-inout: $(inout)
	eog $(inout)

gimp-inout: $(inout)
	gimp $(inout)

mpv-inheritance: $(inheritance)
	mpv $(inheritance)

eog-inheritance: $(inheritance)
	eog $(inheritance)

gimp-inheritance: $(inheritance)
	gimp $(inheritance)












