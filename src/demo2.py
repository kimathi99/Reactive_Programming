from reactivex import of, operators as op
# instead of create  use  of to  the source 
# This factory accepts an argument list, iterates 
# on each argument to emit them as items, and the completes

source = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
    op.map(lambda s: len(s)),
    op.filter(lambda i: i >= 5)
).subscribe(lambda value: print("Received {0}".format(value)))

# refactor  the code once 
# composed = source.pipe(
#     op.map(lambda s: len(s)),
#     op.filter(lambda i: i >= 5)
# # )
# composed.subscribe(lambda value: print("Received {0}".format(value)))
