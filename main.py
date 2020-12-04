"""
Experiments with resource-sync.

Usage...
- can be called manually by cd-ing to the `resourcesync_code` directory (with virtual-environment activated) and running:
  $ python3 ./main.py
"""
from resync import CapabilityList

def get_capabilities():
  # Read Capability List and show supported capabilities
  cl = CapabilityList()
  test_url = 'http://localhost:8888/capabilitylist.xml'
  cl.read(test_url)
  for resource in cl:
      print(f"supports {resource.capability} (at {resource.uri})")
  


if __name__ == '__main__':
    get_capabilities()
