from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
includes = [ 'jinja2' , 'jinja2.ext'] 
excludes = ['Tkinter']
additional_files = ['templates']
build_options = {'packages': [], 
                 'excludes':excludes,
                 'includes':includes,
                 'include_files': additional_files }

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('app.py', base=base, target_name = 'test')
]

setup(name='test',
      version = '0.1',
      description = '',
      options = {'build_exe': build_options},
      executables = executables)
