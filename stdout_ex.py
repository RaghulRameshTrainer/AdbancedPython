import sys

write_out=sys.stdout

data=['Python','Spark','Hadoop','Machine Learning','Cloud']

for tech in data:
    write_out.write(tech+'\n')