import os
import argparse
import glob

parser = argparse.ArgumentParser(description="Output directory list into \
    markdown urls.")
parser.add_argument("pathname")
parser.add_argument("outfile", nargs="?")
args = parser.parse_args()

md_glob = args.pathname + "/" + "*.md"

files =  [f for f in glob.glob(md_glob)]
entries = []

for f in files:
  pathname, f = os.path.split(f)
  x = "[[{0}]]  ".format(f.replace(".md", ""))
  entries.append(x)

if args.outfile is None:
  parser.print_help()
  print("\n".join(entries))
else:
  outpath = os.path.join(args.pathname, args.outfile)
  print("Appending to file ==> {0}".format(outpath))
  
  with open(outpath, "a") as o:
    o.write("\n".join(entries))
    o.close()

print("\n".join(entries))
print("Processed: {0} files.").format(len(entries))
