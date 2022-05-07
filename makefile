
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

all: $(all_pngs)

gimp-all: $(all_pngs)
	gimp $(all_pngs)

eog-all: $(all_pngs)
	eog $(all_pngs)

mpv-all: $(all_pngs)
	mpv $(all_pngs) --no-save-position-on-quit --pause

lost_parent_pngs = $(filter %-lost_parent_phase.png,$(all_pngs))

gimp-lost_parent: $(lost_parent_pngs)
	gimp $(lost_parent_pngs)

eog-lost_parent: $(lost_parent_pngs)
	eog $(lost_parent_pngs)

mpv-lost_parent: $(lost_parent_pngs)
	mpv $(lost_parent_pngs) --no-save-position-on-quit --pause

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


optimize_pngs = $(filter %-optimize.png,$(all_pngs))

gimp-optimize: $(optimize_pngs)
	gimp $(optimize_pngs)

eog-optimize: $(optimize_pngs)
	eog $(optimize_pngs)

mpv-optimize: $(optimize_pngs)
	mpv $(optimize_pngs) --no-save-position-on-quit --pause



suboptimize_pngs = $(filter %-suboptimize.png,$(all_pngs))

gimp-suboptimize: $(suboptimize_pngs)
	gimp $(suboptimize_pngs)

eog-suboptimize: $(suboptimize_pngs)
	eog $(suboptimize_pngs)

mpv-suboptimize: $(suboptimize_pngs)
	mpv $(suboptimize_pngs) --no-save-position-on-quit --pause














