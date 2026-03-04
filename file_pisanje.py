from pathlib import Path
fajl = Path("volim.txt")
text1 = input("Koji programski jezik volite na prvom mestu? ")
text2 = input("Koji programski jezik volite na drugom mestu? ")
text3 = input("Koji programski jezik volite na trećem mestu? ")

fajl.write_text("Ja volim najpre " + text1 + "\n zatim " + text2 + "\n na kraju " + text3)