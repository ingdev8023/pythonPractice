from pathlib import Path
p = Path('C:/Users/artej/Documents/MrRobot')
subdir = [x for x in p.iterdir() if x.is_dir()]
print(subdir)

