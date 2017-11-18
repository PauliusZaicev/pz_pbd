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
        
    #create instance which return commits as a dictionary
    def to_dic(self):
        return {'revision': self.revision, 'author': self.author, 'date': self.date, 'time': self.time, 'number of lines': self.number_of_lines , 'changed path': self.change_path, 'comment': self.comment}
    
    #return instance variable
    #return number of lines as a string, and join comments (because we can have multiple lines comments)
    def __repr__ (self):
        return self.revision+ ',' + self.author + ',' + self.date + \
    ',' + self.time + ',' + str(self.number_of_lines) + ',' + ' '.join(self.change_path) + ',' + ' '.join(self.comment) + '\n'



import pandas as pd
#create function which returns dataframe of commits
def to_df(data):
    commits = []
    for commit in data:
        commits.append(commit.to_dic())
    return pd.DataFrame(commits)

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
            # build in function look s for empty line index and return that index (use build in index function)
            change_file_end_index = data.index ('', index + 1)
            #chnaged path line starts from the third line
            commit.change_path = data[index +3 : change_file_end_index]
            #get comments
            commit.comment = data [change_file_end_index + 1:
                change_file_end_index + 1 + commit.number_of_lines]
            # add details to the list of commits.
            commits.append(commit)
            #find for a next 72 hifins
            #look for next index in the file which starts with 72 hifins
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
    #assigne all lines to data variable
    data = read_file(changes_file)
    #get commits from get _commits function and inert data variabel
    commits = get_commits(data)
    #make commits as a data frame 
    data_frame = to_df(commits)
    
    #going to test latter
    #save_commits(commits, 'changes.csv')
    
    # print the number of lines read
    print(len(data))
    #print lenght of commits, from thiscommits variable will start forming my data set
    print(len(commits))
    #display 0 index from the in commit list
    print(commits[0])
    #print author from the 0 index in commit list
    print(commits[0].author)
    #print author from the 420 index in commit list
    print(commits[420].author)
    #print revision from the 0 index in commit list
    print(commits[0].revision)
    #print comment from the 23 index in commit list
    print (commits[23].comment)
    #print change paths from the 40 index in commit list
    print (commits[40].change_path)
    #print author in index 9 from the data frame
    print (data_frame['author'][9])

    
    #import required libraries
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    #Seaborn is a Python visualization library based on matplotlib. 
    #It provides a high-level interface for drawing attractive statistical graphics.
    import seaborn as sns
    plt.style.use('fivethirtyeight')
    import warnings
    warnings.filterwarnings('ignore')
    
    #display information about data set
    data_frame.info()

    #display data frame
    data_frame.head()
    
    #print unique authors
    data_frame['author'].unique()
    

    #replace author /OU=Domain Control Validated/CN=svn.company.net into DCV
    #this creates new series of values, so we need to assign this new column to the correct column
    data_frame['author'] = data_frame['author'].replace(['/OU=Domain Control Validated/CN=svn.company.net'], 'DCV')
    
    #print unique authors
    data_frame['author'].unique()


    #count how many different authors have logged in
    log_in_per = data_frame[['author' ,'date']].groupby(['author'], as_index = False).count()
    log_in_per = log_in_per.rename(columns = {'author': 'Author', 'date': 'Log in count'})
    print log_in_per
    
    
    
    #create plot
    sns.factorplot('author', 'date', data = data_frame, size = 4, aspect = 3)
    
    #create tree axes for plots
    fig, (axis1) = plt.subplots(1,1,figsize=(15,5))
    
    sns.barplot(x = 'author', y = 'date', data = log_in_per, order = ['Thomas', 'Vincent', '/OU=Domain Control Validated/CN=svn.company.net', 'Jimmy','Freddie', 'Dave', 'ajon0002', 'murari.krishnan', 'Nicky', 'Alan'], ax = axis1)
    '''

