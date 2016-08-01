#!/usr/bin/env python2.7
# Charles Markello
import subprocess
import tempfile
import unittest


class TestGLENN2VCF(unittest.TestCase):

    def test_docker_call(self):
        out, err = check_docker_output(tool='quay.io/ucsc_cgl/glenn2vcf')
        self.assertTrue('Program: glenn2vcf' in out)

def check_docker_output(tool):
    command = 'docker run ' + tool
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()
    return output

if __name__ == '__main__':
    unittest.main()
