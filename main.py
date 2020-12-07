"""
Experiments with resource-sync.

Usage...
- can be called manually by cd-ing to the `resourcesync_code` directory (with virtual-environment activated) and running:
  $ python3 ./main.py
"""
from resync import CapabilityList, ResourceList

def test_features():
  # Read Capability List and show supported capabilities
  cl = CapabilityList()
  capability_url = 'http://localhost:8888/capabilitylist.xml'
  cl.read(capability_url)
  for resource in cl:
      print(f"supports {resource.capability} (at {resource.uri})")
  rl = ResourceList()
  resource_url = 'http://localhost:8888/resourcelist.xml'
  rl.read(resource_url)
  for resource in rl:
    print(resource)


if __name__ == '__main__':
    test_features()
