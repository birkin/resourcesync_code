
# Resources

- code
    - https://github.com/resync
    - https://github.com/resync/resync
    - https://github.com/resync/resync-simulator -- wasn't going to pursue this, but I can't easily find public resource-sync endpoints  :()

- info
    - the specification: <http://www.openarchives.org/rs/1.1/resourcesync>
    - <https://hyku.samvera.org/2017/06/22/resourcesync.html>
        - note, the <https://github.com/dpla/ingestion3> code referenced gives a github 404 when the resourcesync link is clicked.


---

# rsync-simulator installation

Reason: Because there doesn't exist anywhere in the known galaxies a public resource-sync endpoint.

So, via trial and error and the instructions at <https://github.com/resync/resync-simulator>, this worked...

- create a python2 virtual-environment
- pip install the `requirements_resync_simulatr.txt` packages
- `$ git clone git://github.com/resync/resync-simulator.git ./resync-simulator`
- cd into the `resync-simulator` directory
- source the env2 virtual-environment
- `$ ./resync-simulator`
    - ignore error output
    - now <http://localhost:8888> loads up the default resync-simulator page
    - (aside: normal ways of exiting this terminal-session don't work -- i ended up closing the tab which halts the process)

---
