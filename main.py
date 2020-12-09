"""
Experiments with resource-sync.

Usage...
- can be called manually by cd-ing to the `resourcesync_code` directory (with virtual-environment activated) and running:
  $ python3 ./main.py
"""
from resync import CapabilityList, ResourceList, ResourceDump, dump

def test_features():
  # Read Capability List and show supported capabilities
  cl = CapabilityList()
  capability_url = 'http://localhost:8888/capabilitylist.xml'
  cl.read(capability_url)
  print( "\nAbout to show all capabilities..." )
  for resource in cl:
      print(f"supports {resource.capability} (at {resource.uri})")
  # Read Resource List and print it
  rl = ResourceList()
  resource_url = 'http://localhost:8888/resourcelist.xml'  # this url is one of the capabilities
  rl.read(resource_url)

  # for resource in rl:
  #   print(resource)

  # Attempting to download resources, but getting an error related to one resource
  #
  # So going to try creating a smaller subset of the Resource List and get only that to see if it works
  sub_rl = ResourceList()
  for i, r in enumerate(rl):
    sub_rl.add(r)
    if i > 3:
      break
  print('Sub list:')
  for r in sub_rl:
    print(r)

  # Getting a "No file path defined error when trying to dump, so trying to check/explore that first"
  for r in sub_rl.resources:
    print(f'Path = {r.path}')

  # Do any of them have a path defined?
  paths = [r.path for r in rl.resources]
  print(f'Unique paths: {set(paths)}')

  # d = dump.Dump(resources=sub_rl)
  # d.write(basename='/dump_test/sub_test_')

if __name__ == '__main__':
    test_features()
