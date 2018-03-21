# Desired input & output directories
in_dir = "/home/ryanmars/Projects/local/share/templates/html/"
out_dir = "/home/ryanmars/Projects/output/html/"

# I/O file names (Change the "format" variable for other subjects)
in_fname = "bet_slices.html"
out_fname = "sub{:03d}_bet_slices.html".format(2)
in_f = open(in_dir+in_fname, "r")
out_f = open(out_dir+out_fname, "w")

# Read template
in_text = in_f.read()

# Fill in the "format" options to generalize to other subjects;
# Write output file
out_f.write(in_text.format(2,2))

in_f.close()
out_f.close()
