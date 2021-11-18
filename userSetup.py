import os
import maya.cmds as cmds

# Cleans maya files from the vaccine.py virus
def clean():
    print("Scanning for malicious scripts and nodes...")

    scriptdir = cmds.internalVar(userAppDir=True) + 'scripts'

    virloc = os.path.join(scriptdir, "vaccine.py")

    if os.path.isfile(virloc):
        cmds.warning("Found vaccine.py in scriptlocation, removing ...")
        os.remove(virloc)

    virloc = os.path.join(scriptdir, "vaccine.pyc")

    if os.path.isfile(virloc):
        cmds.warning("Found vaccine.pyc` in scriptlocation, removing ...")
        os.remove(virloc)

    bannedNodes = ["vaccine_gene", "breed_gene"]

    for i in cmds.ls(type="script"):

        if i in bannedNodes:
            cmds.warning("Found malicious scriptnode '" + i + "', removing...")
            cmds.delete(i)


clean()
open_scene_job = cmds.scriptJob(e=["SceneOpened", lambda: clean()], protected=True)
