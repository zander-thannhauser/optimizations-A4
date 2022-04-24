
default: all


.PRECIOUS: dot/%.png

dot/%.png: dot/%.dot
	dot -Tpng < $< > $@

eog-%: dot/%.png
	eog $<

mpv-%: dot/%.png
	mpv $<

gimp-%: dot/%.png
	gimp $<


dot/all.mk:
	find $(@D) -name '*.dot' | sort -V | sed 's/^/alls += /;s/.dot$$/.png/' > $@

include dot/all.mk

all: $(alls)

gimp-all: $(alls)
	gimp $(alls)

eog-all: $(alls)
	eog $(alls)

mpv-all: $(alls)
	mpv $(alls) --no-save-position-on-quit


dot/critical.mk:
	find $(@D) -name '*-critical.dot' | sort -V | sed 's/^/critical += /;s/.dot$$/.png/' > $@

include dot/critical.mk

mpv-critical: $(critical)
	mpv $(critical)

eog-critical: $(critical)
	eog $(critical)

gimp-critical: $(critical)
	gimp $(critical)



dot/valnum_singleton_sets.mk:
	find $(@D) -name '*-valnum_singleton_sets.dot' | sort -V | sed 's/^/valnum_singleton_sets += /;s/.dot$$/.png/' > $@

include dot/valnum_singleton_sets.mk

mpv-valnum_singleton_sets: $(valnum_singleton_sets)
	mpv $(valnum_singleton_sets)

eog-valnum_singleton_sets: $(valnum_singleton_sets)
	eog $(valnum_singleton_sets)

gimp-valnum_singleton_sets: $(valnum_singleton_sets)
	gimp $(valnum_singleton_sets)



dot/union_valnum_sets.mk:
	find $(@D) -name '*-union_valnum_sets.dot' | sort -V | sed 's/^/union_valnum_sets += /;s/.dot$$/.png/' > $@

include dot/union_valnum_sets.mk

mpv-union_valnum_sets: $(union_valnum_sets)
	mpv $(union_valnum_sets)

eog-union_valnum_sets: $(union_valnum_sets)
	eog $(union_valnum_sets)

gimp-union_valnum_sets: $(union_valnum_sets)
	gimp $(union_valnum_sets)


dot/rename_valnums_to_liveids.mk:
	find $(@D) -name '*-rename_valnums_to_liveids.dot' | sort -V | sed 's/^/rename_valnums_to_liveids += /;s/.dot$$/.png/' > $@

include dot/rename_valnums_to_liveids.mk

mpv-rename_valnums_to_liveids: $(rename_valnums_to_liveids)
	mpv $(rename_valnums_to_liveids)

eog-rename_valnums_to_liveids: $(rename_valnums_to_liveids)
	eog $(rename_valnums_to_liveids)

gimp-rename_valnums_to_liveids: $(rename_valnums_to_liveids)
	gimp $(rename_valnums_to_liveids)



dot/liveinout.mk:
	find $(@D) -name '*-liveinout.dot' | sort -V | sed 's/^/liveinout += /;s/.dot$$/.png/' > $@

include dot/liveinout.mk

mpv-liveinout: $(liveinout)
	mpv $(liveinout)

eog-liveinout: $(liveinout)
	eog $(liveinout)

gimp-liveinout: $(liveinout)
	gimp $(liveinout)


dot/live_inheritance.mk:
	find $(@D) -name '*-live_inheritance.dot' | sort -V | sed 's/^/live_inheritance += /;s/.dot$$/.png/' > $@

include dot/live_inheritance.mk

mpv-live_inheritance: $(live_inheritance)
	mpv $(live_inheritance)

eog-live_inheritance: $(live_inheritance)
	eog $(live_inheritance)

gimp-live_inheritance: $(live_inheritance)
	gimp $(live_inheritance)


dot/live_instances.mk:
	find $(@D) -name '*-live_instances.dot' | sort -V | sed 's/^/live_instances += /;s/.dot$$/.png/' > $@

include dot/live_instances.mk

mpv-live_instances: $(live_instances)
	mpv $(live_instances)

eog-live_instances: $(live_instances)
	eog $(live_instances)

gimp-live_instances: $(live_instances)
	gimp $(live_instances)























