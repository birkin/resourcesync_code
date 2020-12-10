"""
Experiments with resource-sync.

Usage...
- can be called manually by cd-ing to the `resourcesync_code` directory (with virtual-environment activated) and running:
  $ python3 ./main.py
"""
from resync import CapabilityList, ResourceList, ResourceDump, dump

def test_features():
  # Not sure if there's a capabilities list, or where it is if so...
  # cl = CapabilityList()
  # capability_url = 'https://pod.stanford.edu/organizations/'
  # cl.read(capability_url)
  # print( "\nAbout to show all capabilities..." )
  # for resource in cl:
  #     print(f"supports {resource.capability} (at {resource.uri})")

  # Read Resource List and print it
  rl = ResourceList()
  resource_url = 'https://pod.stanford.edu/organizations/normalized_resourcelist/marcxml'
  rl.read(resource_url)

  for resource in rl:
    print(resource)
  # Attempting to download resources, but getting an error related to one resource
  # d = dump.Dump(resources=rl)
  # d.write(basename='./dump_test/test.xml')

if __name__ == '__main__':
    test_features()
