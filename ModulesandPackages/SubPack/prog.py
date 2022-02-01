import sys
sys.path.append('/Users/kirubaha/Desktop/Python/ModulesandPackages/')
print(sys.path)

from sub import func2
from sub import func3


from MainPack import mod as Main
from MainPack.SubOfMain import mainsub

print('I am a program running from SubPack Folder')

func2()
func3()
Main.newfunc()
mainsub.main_sub_mod()