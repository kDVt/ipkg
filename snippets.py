# 
# Extract (in this example) a control file's contents from a .deb
#

import unix_ar as ar
import tarfile as tar

filename = 'example.deb'
control = tar.open(fileobj=ar.open(filename).open('control.tar.gz')).extractfile(
    './control').read()
