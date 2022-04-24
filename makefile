
default: all


.PRECIOUS: dot/%.png

dot/%.png: dot/%.txt
	dot -Tpng < $< > $@

eog-%: dot/%.png
	eog $<

mpv-%: dot/%.png
	mpv $<

gimp-%: dot/%.png
	gimp $<


dot/all.mk:
	find $(@D) -name '*.txt' | sort -V | sed 's/^/alls += /;s/.txt$$/.png/' > $@

include dot/all.mk

all: $(alls)

gimp-all: $(alls)
	gimp $(alls)

eog-all: $(alls)
	eog $(alls)

mpv-all: $(alls)
	mpv $(alls) --no-save-position-on-quit


dot/critical.mk:
	find $(@D) -name '*-critical.txt' | sort -V | sed 's/^/critical += /;s/.txt$$/.png/' > $@

include dot/critical.mk

mpv-critical: $(critical)
	mpv $(critical)

eog-critical: $(critical)
	eog $(critical)

gimp-critical: $(critical)
	gimp $(critical)



dot/valnum_singleton_sets.mk:
	find $(@D) -name '*-valnum_singleton_sets.txt' | sort -V | sed 's/^/valnum_singleton_sets += /;s/.txt$$/.png/' > $@

include dot/valnum_singleton_sets.mk

mpv-valnum_singleton_sets: $(valnum_singleton_sets)
	mpv $(valnum_singleton_sets)

eog-valnum_singleton_sets: $(valnum_singleton_sets)
	eog $(valnum_singleton_sets)

gimp-valnum_singleton_sets: $(valnum_singleton_sets)
	gimp $(valnum_singleton_sets)



dot/union_valnum_sets.mk:
	find $(@D) -name '*-union_valnum_sets.txt' | sort -V | sed 's/^/union_valnum_sets += /;s/.txt$$/.png/' > $@

include dot/union_valnum_sets.mk

mpv-union_valnum_sets: $(union_valnum_sets)
	mpv $(union_valnum_sets)

eog-union_valnum_sets: $(union_valnum_sets)
	eog $(union_valnum_sets)

gimp-union_valnum_sets: $(union_valnum_sets)
	gimp $(union_valnum_sets)


dot/rename_valnums_to_liveids.mk:
	find $(@D) -name '*-rename_valnums_to_liveids.txt' | sort -V | sed 's/^/rename_valnums_to_liveids += /;s/.txt$$/.png/' > $@

include dot/rename_valnums_to_liveids.mk

mpv-rename_valnums_to_liveids: $(rename_valnums_to_liveids)
	mpv $(rename_valnums_to_liveids)

eog-rename_valnums_to_liveids: $(rename_valnums_to_liveids)
	eog $(rename_valnums_to_liveids)

gimp-rename_valnums_to_liveids: $(rename_valnums_to_liveids)
	gimp $(rename_valnums_to_liveids)



dot/liveinout.mk:
	find $(@D) -name '*-liveinout.txt' | sort -V | sed 's/^/liveinout += /;s/.txt$$/.png/' > $@

include dot/liveinout.mk

mpv-liveinout: $(liveinout)
	mpv $(liveinout)

eog-liveinout: $(liveinout)
	eog $(liveinout)

gimp-liveinout: $(liveinout)
	gimp $(liveinout)























