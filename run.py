#!/usr/bin/env python
#
# Writes something at as many `snakemake.output` files as there are

def do_something(input_fns, out_fn):
  with open(out_fn, 'w') as sys.stdout:
    print("I've seen ", ' '.join(input_fns))
    
for out in snakemake.output:
  ## paths are omnibenchmark's responsability
  ## if not os.path.exists(os.path.dirname(out)):
  ##    os.makedirs(os.path.dirname(out))  
  with open(out, 'w') as sys.stdout:  
      do_something(input_fns = snakemake.input.values(),
                     out_fn  = out)
