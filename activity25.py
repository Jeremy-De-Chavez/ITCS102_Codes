ribs = "Ang ribs o tadyang ay ang kurbadong hanay ng mga buto \
sa gitnang bahagi ng katawan ng manok na bumubuo sa hawla ng dibdib nito. "
buto_buto = ["lokod","leeg","wings",ribs]
manok = ["breast", "paa", buto_buto]
adobo = [manok,"baboy","sitaw","palaka"]
ulam = {"pang bansa": adobo, "maasim":"sinigang", "bbq":"inihaw"}

print(ulam["pang bansa"][0][2][3])