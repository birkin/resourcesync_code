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
  uris = [r.uri for r in rl]
  print('---------------------------')
  print(uris[4])
  print('---------------------------')

  chosen_r = [k for k in rl.resources.keys()][4]
  print(chosen_r)
  rl_for_dump = ResourceList()
  rl_for_dump.add(rl.resources[chosen_r])
  for r in rl_for_dump:
    print(r)
  d = dump.Dump(resources=rl_for_dump)
  d.write(basename='/dump_test/dart_test_')

if __name__ == '__main__':
    test_features()
