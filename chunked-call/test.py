#!/usr/bin/env python2.7
# Charles Markello - cmarkell@ucsc.edu
import subprocess
import unittest

class TestChunkedCall(unittest.TestCase):

    def test_docker_call(self):
        out, err = check_docker_output(tool='quay.io/ucsc_cgl/chunked_call')
        self.assertTrue('usage: chunked_call [-h] [--chunk CHUNK] [--overlap OVERLAP]' in out)

def check_docker_output(tool):
    command = 'docker run ' + tool
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()
    return output

if __name__ == '__main__':
    unittest.main()
