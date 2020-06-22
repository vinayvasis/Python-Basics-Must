"""
In this section we will learn about generator expressions which is a high performance,
 memory efficient generalization of list comprehensions and generators.

For example we will try to sum the squares of all numbers from 1 to 9.

################################>>> sum([x*x for x in range(1,10)])
The example actually first creates a list of the square values in memory and then it iterates over it and finally after
 sum it frees the memory. You can understand the memory usage in case of a big list.

We can save memory usage by using a generator expression.

###################################sum(x*x for x in range(1,10))

The syntax of generator expression says that always needs to be directly inside a set of parentheses and cannot have a
comma on either side. Which basically means both the examples below are valid generator expression usage example.

############################>>> sum(x*x for x in range(1,10))
############################285
###########################>>> g = (x*x for x in range(1,10))
###########################>>> g
###########################<generator object <genexpr> at 0x7fc559516b90>
We can have chaining of generators or generator expressions.
In the following example we will read the file */var/log/cron* and will find if any particular job (in the example we
are searching for anacron) is running successfully or not.
We can do the same using a shell command tail -f /var/log/cron |grep anacron

###########################>>> jobtext = 'anacron'
###########################>>> all_lines = (line for line in open('/var/log/cron', 'r') )
############################>>> job = ( line for line in all_lines if line.find(jobtext) != -1)
##############################>>> text = next(job)
############################>>> text
############################"May  6 12:17:15 dhcp193-104 anacron[23052]: Job `cron.daily' terminated\n"
##########################>>> text = next(job)
#########################>>> text
############################'May  6 12:17:15 dhcp193-104 anacron[23052]: Normal exit (1 job run)\n'
###########################>>> text = next(job)
#############################>>> text
############################'May  6 13:01:01 dhcp193-104 run-parts(/etc/cron.hourly)[25907]: starting 0anacron\n'
"""
