likod = "Ang likod ng manok o chicken back ay ang patag at mabutong bahagi sa itaas ng katawan \
 ng manok na nagdurugtong sa leeg hanggang sa pwetan nito. "
leeg = " Paborito itong iihaw bilang street food (kilala bilang adidas o helmet ang ulo, at leeg mismo) \
 o isahog sa mga sabaw at adobo dahil malasa ang laman at balat na nakabalot sa mga buto nito."
wings = "Ang wings o pakpak ay ang bahagi ng manok na nahahati \ " \
"sa tatlong seksyon na tinatawag na drumette, wingette (o flat), at wing tip"
ribs = "Ang ribs o tadyang ay ang kurbadong hanay ng mga buto \
sa gitnang bahagi ng katawan ng manok na bumubuo sa hawla ng dibdib nito. "
buto_buto = [likod,leeg,wings,ribs]
manok = ["breast", "paa", buto_buto]
adobo = [manok,"baboy","sitaw","palaka"]
ulam = {"pang bansa": adobo, "maasim":"sinigang", "bbq":"inihaw"}

print(ulam["pang bansa"][0][2][3])
