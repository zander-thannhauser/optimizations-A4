
default:

dot/all.mk:
	find $(@D) -name '*.txt' | sort -V | sed 's/^/alls += /;s/.txt$$/.png/' > $@

dot/anticipation.mk:
	find $(@D) -name '*-anticipation.txt' | sort -V | sed 's/^/anticipation += /;s/.txt$$/.png/' > $@

dot/available.mk:
	find $(@D) -name '*-available.txt' | sort -V | sed 's/^/available += /;s/.txt$$/.png/' > $@

dot/earliest.mk:
	find $(@D) -name '*-earliest.txt' | sort -V | sed 's/^/earliest += /;s/.txt$$/.png/' > $@

include dot/all.mk
include dot/anticipation.mk
include dot/available.mk
include dot/earliest.mk

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












