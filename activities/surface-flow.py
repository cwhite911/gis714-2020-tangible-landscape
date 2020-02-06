#!/usr/bin/env python3

"""
Instructions

- Functions intended to run for each scan
  need to be named run_xxxxx

- Do not modify the parameters of the run_xxx function
  unless you know what you are doing
  see optional parameters:
  https://github.com/tangible-landscape/grass-tangible-landscape/wiki/Running-analyses-and-developing-workflows#python-workflows

- All gs.run_command/read_command/write_command/parse_command
  need to be passed env parameter (..., env=env)
"""

import grass.script as gs


def run_slope(scanned_elev, env, **kwargs):
    gs.run_command('r.slope.aspect', elevation=scanned_elev, slope='slope', dx='dx', dy='dy', env=env)


def run_contours(scanned_elev, env, **kwargs):
    interval = 5
    gs.run_command('r.contour', input=scanned_elev, output='contours', step=interval, flags='t', env=env)

def run_water_flow(scanned_elev, env, **kwargs):
    gs.run_command('r.sim.water', dx='dx', dy='dy', elevation=scanned_elev, rain_value=200, infil_value=0, man_value=0.05, depth='depth', discharge='discharge', niterations=1, output_step=120, env=env)





# this part is for testing without TL
def main():
    import os

    # we want to run this repetetively without deleted the created files
    os.environ['GRASS_OVERWRITE'] = '1'

    elevation = 'elev_lid792_1m'
    elev_resampled = 'elev_resampled'
    # resampling to have similar resolution as with TL
    gs.run_command('g.region', raster=elevation, res=4, flags='a')
    gs.run_command('r.resamp.stats', input=elevation, output=elev_resampled)

    run_slope(scanned_elev=elev_resampled, env=None)
    run_contours(scanned_elev=elev_resampled, env=None)
    run_water_flow(scanned_elev=elev_resampled, env=None)




if __name__ == '__main__':
    main()
