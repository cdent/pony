
def builder(module):
    package = module.__name__.split('.', 1)[1]
    print package
    prefix = package.upper().replace('.', '_')
    for name in module.NAMES:
        print name
        fullname = '%s_%s' % (prefix, name)
        print fullname
        setattr(module, fullname, fullname)
    print dir(module)


