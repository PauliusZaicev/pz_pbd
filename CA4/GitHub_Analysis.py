#set a directory
import os
os.chdir('D://DBS//5.Programming_for_big_data//github//pz_pbd//CA4')



def read_file(changes_file):
    # use strip to strip out spaces and trim the line
    #strip each line in the inserted file, and return then for loop checked all file
    return [line.strip() for line in open(changes_file, 'r')]


#create commit class
class Commit (object):
    
    #create commit instance variables
    def __init__ (self, revision, author, date, time, number_of_lines, change_path = '', comment = ''):
        self.revision = revision
        self.author = author
        self.date = date
        self.time = time
        self.number_of_lines = number_of_lines
        self.change_path = change_path
        self.comment = comment
        
    #return instance variable
    #return number of lines as a string, and join comments (because we can have multiple lines comments)
    def __repr__ (self):
        return self.revision+ ',' + self.author + ',' + self.date + \
    ',' + self.time + ',' + str(self.number_of_lines) + ',' + ' '.join(self.comment) + '\n'


#get commits function will help us to break inforamtion from each commit       
def get_commits(data):
    #each commit is separated by 72 hifins
    sep = 72*'-'
    #create a list to store each commit
    commits = []
    #first index starts in the line 0
    index = 0
    #while our index is less than data lenght
    while index < len(data):
        try:
            # find each line of the commit
            #and split by the separator |
            #index + 1 because line starts one line lower than index line
            details = data[index + 1].split('|')
            #call class commit and add details to the variable commit as per class
            commit = Commit(details[0].strip(),
                details[1].strip(),
                details[2].strip().split(' ')[0],
                details[2].strip().split(' ')[1],
                #get number of lines and return as int
                int(details[3].strip().split(' ')[0]))
            #set file end index
            # in my oppinion look for empty line and for this lines index adds one
            
            #ask darren to explain, but how each commit is treated seperatelly
            change_file_end_index = data.index ('', index + 1)
            #chnaged path line starts from the third line
            commit.changed_path = data[index +3 : change_file_end_index]
            #get comments
            #
            commit.comment = data [change_file_end_index + 1:
                change_file_end_index + 1 + commit.number_of_lines]
            # add details to the list of commits.
            commits.append(commit)
            #find for a next 72 hifins
            
            #ask to explain
            index = data.index(sep, index + 1)
        except IndexError:
            #then index equal to len of data program stops
            index = len(data)
    #return all commits
    return commits

#save as csv
def save_commits(commits, any_file):
    #open file as write
    my_file = open (any_file, 'w')
    #set column names
    my_file.write('revision,author,date, time,number_of_lines,comment\n')
    #for commit in commits write each line as a string
    for commit in commits:
       my_file.write(str(commit)) 
    #close files
    my_file.close()


if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    commits = get_commits(data)
    
    #save_commits(commits, 'changes.csv')
    
    # print the number of lines read
    print(len(data))
    #print(commits)
    print(len(commits))
    print(commits[0])
    print(commits[0].author)
    print(commits[420].author)
    print(commits[0].revision)
    print (commits[23].comment)
    print (commits[40].changed_path)


'''

#import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Seaborn is a Python visualization library based on matplotlib. 
#It provides a high-level interface for drawing attractive statistical graphics.
import seaborn as sns
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')



commits = get_commits(data)

#import pandas
import pandas as pd

#make commits as a data frame
data_frame = pd.DataFrame(commits)

#dispaly data frame
print data_frame



#display information about data set
data_frame.info()

#display head of the data set
data_frame.head()

#print unique authors
data_frame['author'].unique()

#count how many different outhors have ogged in
log_in_per = data_frame[['author' ,'date']].groupby(['author'], as_index = False).count()
print log_in_per
#create plot
sns.factorplot('author', 'date', data = data_frame, size = 4, aspect = 3)

#create tree axes for plots
fig, (axis1) = plt.subplots(1,1,figsize=(15,5))

sns.barplot(x = 'author', y = 'date', data = log_in_per, order = ['Thomas', 'Vincent', '/OU=Domain Control Validated/CN=svn.company.net', 'Jimmy','Freddie', 'Dave', 'ajon0002', 'murari.krishnan', 'Nicky', 'Alan'], ax = axis1)
'''

    
'''
if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    commits = get_commits(data)

    # print the number of lines read
    print(len(data))
    #print(commits)
    print(len(commits))
    print(commits[0])
    print(commits[0].author)
    print(commits[420].author)
    print(commits[0].revision)
    save_commits(commits, 'changes.csv')'''