import os
from contextlib import contextmanager
from pathlib import Path
import subprocess
import time
import pprint


@contextmanager
def set_directory(path):
    origin = Path().absolute()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(origin)


def run_cmd(cmd):
    start = time.monotonic()
    result = subprocess.check_output(' '.join(cmd), shell=True, stderr=subprocess.STDOUT)
    end = time.monotonic()
    return end - start, result.decode().strip()


ALOHA_DIR = '/home/userpp/omnetpp-5.6.2/samples/aloha/'
PY_ALOHA_DIR = '/home/userpp/pysamples/pyaloha/'

ALOHA_EXECUTABLE = 'aloha'
PY_ALOHA_EXECUTABLE = 'pyaloha'

NUM_HOSTS = 15
SIM_TIME_LIMIT = '90min'


def get_cmdline(*, ia_mean, slotted, py):
    executable = PY_ALOHA_EXECUTABLE if py else ALOHA_EXECUTABLE
    base_dir = PY_ALOHA_DIR if py else ALOHA_DIR
    cmd = [
        f'./{executable}',
        '-u', 'Cmdenv',
        '-f', os.path.join(base_dir, 'omnetpp.ini'),
        '-c', 'marcos',
        fr'--Aloha.host[*].iaTime=exponential\({ia_mean}s\)',
        f'--Aloha.slotTime={slotted * 100}ms',
        f'--sim-time-limit={SIM_TIME_LIMIT}',
        '> /dev/null 2>&1',
        '&&',
        'grep channelUtilization results/marcos-#0.sca | cut -d " " -f4',
    ]
    print(' '.join(cmd))
    return cmd


def main():
    slotted = [True, False]
    ia_mean = [
        0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1,
        1.5, 2, 2.5, 3,
        4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
    ]
    results = []

    for s in slotted:
        print('Slotted:', s)
        for m in ia_mean:
            print('iaMean', m)
            with set_directory(ALOHA_DIR):
                print('C++:   ', end=' ')
                cmd = get_cmdline(py=False, ia_mean=m, slotted=s)
                elapsed, result = run_cmd(cmd)

            print(result, '{}s'.format(elapsed))
            results.append(['c++', m, s, result, elapsed])

            with set_directory(PY_ALOHA_DIR):
                print('Python:', end=' ')
                cmd = get_cmdline(py=True, ia_mean=m, slotted=s)
                elapsed, result = run_cmd(cmd)

            print(result, '{}s'.format(elapsed))
            results.append(['python', m, s, result, elapsed])

    pprint.pprint(results, indent=2)


if __name__ == '__main__':
    main()
