import os
import errno
import psutil
import logging
import importlib


def mkdir_p(path):
    """ Equivalent of mkdir -p """
    """ source: http://bit.ly/1dyli3d """
    try:
        os.makedirs(path)
    except OSError as exc:   # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def memory_usage():
    """ return the memory usage in MB """
    """ source: http://bit.ly/1dspz7I """
    process = psutil.Process(os.getpid())
    try:
        mem = process.get_memory_info()[0] / float(2 ** 20)
    except:
        mem = process.memory_info()[0] / float(2 ** 20)
    return mem


def wc_l(fname):
    """ return number of lines in a file """

    lineCount = 0
    try:
        with open(fname, 'r') as f:
            for line in f:
                lineCount = lineCount + 1
    except:
        print('Could not open file ', fname)
        pass
    return lineCount


def git_version():
    """ returns git revision """
    """ source: http://bit.ly/1Ctm1ho """

    from subprocess import Popen, PIPE
    gitproc = Popen(['git', 'rev-parse', 'HEAD'], stdout=PIPE)
    (stdout, _) = gitproc.communicate()
    return stdout.strip()


def str_to_object(module_name, class_name, args=None):
    """ get class from string """
    """ source: http://bit.ly/1MWvAJ2 """

    try:
        module_ = importlib.import_module(module_name)
        try:
            if args:
                class_ = getattr(module_, class_name)(args)
        except AttributeError:
            logging.error('Class does not exist')
    except ImportError:
        logging.error('Module does not exist')
    return class_ or None
