# Maya vaccine virus removal tool

This userSetup.py file will remove the vaccine virus scriptnodes when you open a maya file. It will also remove the
vaccine.py in your scripts' folder if present.

Tested in Maya 2019.2 but should work in other versions as well.

### Vaccine Virus
In 2021 some users reported getting a strange chineese message when saving their maya scene. 

`Warning: 你的文件贼健康~我就说一声没有别的意思`

The tool wil run at startup but also when a scene is opened. Thus helping to remove the malicious code and prevent the virus from spreading.

I've created this tool to clean, and keep maya scenes clean in a shared studio setting.

Alternatively you can use the autodesk security tool.

### Installation

Put the userSetup.py in a scripts folder where maya looks. IE: `C:\Users\<user>\Documents\maya\2019\script`

If you already have a userSetup.py you can safely copy the contents of this tool to your own userSetup.py
