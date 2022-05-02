
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

include dot/all-dots.mk

all_pngs = $(patsubst %.dot,%.png,$(all_dots))

$(info $(all_pngs))

all: $(all_pngs)

gimp-all: $(all_pngs)
	gimp $(all_pngs)

eog-all: $(all_pngs)
	eog $(all_pngs)

mpv-all: $(all_pngs)
	mpv $(all_pngs) --no-save-position-on-quit --pause

inout_pngs = $(filter %-inout.png,$(all_pngs))

gimp-inout: $(inout_pngs)
	gimp $(inout_pngs)

eog-inout: $(inout_pngs)
	eog $(inout_pngs)

mpv-inout: $(inout_pngs)
	mpv $(inout_pngs) --no-save-position-on-quit --pause

inheritance_pngs = $(filter %-inheritance.png,$(all_pngs))

gimp-inheritance: $(inheritance_pngs)
	gimp $(inheritance_pngs)

eog-inheritance: $(inheritance_pngs)
	eog $(inheritance_pngs)

mpv-inheritance: $(inheritance_pngs)
	mpv $(inheritance_pngs) --no-save-position-on-quit --pause

phi_pngs = $(filter %-phi.png,$(all_pngs))

gimp-phi: $(phi_pngs)
	gimp $(phi_pngs)

eog-phi: $(phi_pngs)
	eog $(phi_pngs)

mpv-phi: $(phi_pngs)
	mpv $(phi_pngs) --no-save-position-on-quit --pause














