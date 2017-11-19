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
    my_file.write('revision,author,date, time,number_of_lines,changed_path,comment\n')
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
    save_commits(commits, 'changes.csv')
    
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


    #count how many different authors have commit objects and groub by author
    log_in_per = data_frame[['author' ,'date']].groupby(['author'], as_index = False).count()
    #rename column names and print
    log_in_per = log_in_per.rename(columns = {'author': 'Author', 'date': 'Commit count'})
    #sort values
    log_in_per = log_in_per.sort_values(['Commit count'], ascending = [False])
    log_in_per
    
    
    
    #create a factor plot
    sns.factorplot('Author', 'Commit count', data = log_in_per, size = 4, aspect = 3)
    
    
    
    #create an axe for a plot
    fig, (axis1) = plt.subplots(1,1,figsize=(15,5))
    #display as a bar chart
    ax = sns.barplot('Author', 'Commit count', data = log_in_per, order = ['Thomas', 'Vincent', \
                                                                           'DCV', 'Jimmy','Freddie', 'Dave', \
                                                                           'ajon0002', 'murari.krishnan', \
                                                                           'Nicky', 'Alan'], ax = axis1)
    ax.set (xlabel = 'Author', ylabel = 'Commit count')
    plt.show

    
    
    #display overall percentage of commits by author
    commits = int(data_frame['date'].count())
    #add new column to the data frame, and calculate percentage
    log_in_per['Percentage'] = pd.Series.round(((log_in_per['Commit count']*100)/commits),2 )
    log_in_per
    
    
    #create and axis for the pie chart
    fig, (axis1) = plt.subplots(1,1,figsize=(15,10))
    #plot relevant data frame
    ax = log_in_per.plot.pie(y='Percentage', shadow = True, ax = axis1, labels = log_in_per['Percentage'])   
    #set a y label
    ax.set ( ylabel = 'Percentage of commit objects')
    #set a possition of the legend to the left top corner
    plt.legend(labels = log_in_per['Author'], bbox_to_anchor=(0.85,1.025), loc="upper left")
    plt.show


    '''Number of comments per author & average number of comments per commit per author'''

    
    #check how many comment lines each author has created
    number_of_lines = data_frame[['author' ,'number of lines']].groupby(['author'], as_index = False).sum()
    #rename columns
    number_of_lines= number_of_lines.rename(columns = {'author': 'Author', 'number of lines': 'Commented lines'})
    #sort values in descending order
    number_of_lines = number_of_lines.sort_values(['Commented lines'], ascending = [False])
    number_of_lines
    
    
    
    #merge two different data frames
    mergged_df = pd.merge( left = log_in_per, right = number_of_lines, left_on = 'Author', right_on = 'Author' )
    mergged_df
    
    
    
    #add new column to the dataframe
    mergged_df['Average number of comments per commit'] = pd.Series.round(mergged_df['Commented lines'] / mergged_df['Commit count'], 2)
    mergged_df
    
    
    #create a factor plot
    sns.factorplot('Author', 'Average number of comments per commit', data = mergged_df, size = 4, aspect = 3)
    
    
    '''The favourit part of the day to create a commit object'''
    
    #strip time into hours minutes and seconds
    data_frame['hours'], data_frame['minutes'], data_frame['seconds'] = data_frame['time'].str.split(':',2).str
    
    
    #add additional column in the dataframe, 0 first half of the day 1 second half of the day
    data_frame['day_time'] = data_frame['hours']
    
    #repalce first half of the day values to 0
    data_frame['day_time'] = data_frame['day_time'].replace(['00', '01', '02', '03', '04', \
              '05','06','07','08','09','10','11'], '0')
                
    #repalce second half of the day values to 1
    data_frame['day_time'] = data_frame['day_time'].replace(['12', '13', '14', '15', '16', \
          '17', '18','19','20','21','22','23', '24'], '1')
    
                

    
   
    
    #count how many commits done in the morning and in the evening
    count_daytime = data_frame[['day_time' ,'revision']].groupby(['day_time'], as_index = False).count()
    #Replace value 0 into str Morning
    count_daytime['day_time'] = count_daytime['day_time'].replace(['0'], 'Morning')
    #replace value 1 into str Evening
    count_daytime['day_time'] = count_daytime['day_time'].replace(['1'], 'Evening') 
    #connect two values for visualisation purpose
    count_daytime['visual'] = count_daytime[['day_time' ,'revision']].apply(lambda x : '{} = {}'.format(x[0],x[1]), axis=1)
    #display
    count_daytime
    
    
    
    
    #count how many comments made in the morning and howe many in the evening
    number_of_lines_time = data_frame[['day_time' ,'number of lines']].groupby(['day_time'], as_index = False).sum()
    #Replace value 0 into str Morning
    number_of_lines_time['day_time'] = number_of_lines_time['day_time'].replace(['0'], 'Morning')
    #replace value 1 into str Evening
    number_of_lines_time['day_time'] = number_of_lines_time['day_time'].replace(['1'], 'Evening')  
    #connect two values for visualisation purpose
    number_of_lines_time['visual'] = number_of_lines_time[['day_time' ,'number of lines']].apply(lambda x : '{} = {}'.format(x[0],x[1]), axis=1)
    #display
    number_of_lines_time 

    
    
    
    #create sub plots
    fig, (axis1,axis2) = plt.subplots(1,2,figsize=(15,6))
    
    #create sns barplot
    ax = sns.barplot(x='day_time', y='revision', data=count_daytime, ax=axis1, order=['Morning','Evening'])
    ax.set (xlabel = 'Period of the day', ylabel = 'Count of commits created')

    
    #total is the lenght of the commits
    total = len(data_frame['revision'])
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x()+p.get_width()/2.,
            height + 3,
            '{:1.2f}'.format(height/total),
            ha="center") 
    plt.show
    
    
    #create sns barplot
    ax = sns.barplot(x='day_time', y='number of lines', data=number_of_lines_time, ax=axis2, order=['Morning','Evening'])
    ax.set (xlabel = 'Period of the day', ylabel = 'Number of commented lines')
    
    #total is a sum of commented liens in a dataframe
    total = sum(number_of_lines_time['number of lines'])
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x()+p.get_width()/2.,
            height + 3,
            '{:1.2f}'.format(height/total),
            ha="center") 
    plt.show

    
    #create sub plots
    fig, (axis1,axis2) = plt.subplots(1,2,figsize=(15,6))
        
    ax = count_daytime.plot.pie(y='revision', shadow = True, ax = axis1, labels = count_daytime['visual'])   
    ax.set ( ylabel = 'Count of commits created')
    plt.show
    
    ax = number_of_lines_time.plot.pie(y='number of lines', shadow = True, ax = axis2, labels = number_of_lines_time['visual'])   
    ax.set ( ylabel = 'Number of commented lines')
    plt.show
    
    
    
    
    #add additional column to the data frame
    data_frame['day_time_str'] =  data_frame['day_time']
    #replace int 0 to str Morning
    data_frame['day_time_str'] = data_frame['day_time_str'].replace(['0'], 'Morning')
    #replace int 1 to str Evening
    data_frame['day_time_str'] = data_frame['day_time_str'].replace(['1'], 'Evening')
    
    
    #look for a size of each option grouped by author and str
    authors_time_commits = data_frame.groupby(['author' ,'day_time_str']).count()
    
    #with out hierachi
    authors_time_commits = data_frame.groupby(['author' ,'day_time_str']).count().unstack()
    authors_time_commits = authors_time_commits['revision']
    authors_time_commits
    

    #create an ax for the plot
    fig, (axis1) = plt.subplots(1,1,figsize=(17,5))
    plot = authors_time_commits.plot.bar(stacked=False, title="Amount of commit objects by author", ax = axis1)
    plot.set_xlabel("Author")
    plot.set_ylabel("Morning or Evening")


    
        
    authors_time_comments = data_frame.groupby(['author' ,'day_time_str']).sum()
    #with out hierachi
    authors_time_comments = data_frame.groupby(['author' ,'day_time_str']).sum().unstack()
    authors_time_comments
    
    #create an ax for the plot
    fig, (axis1) = plt.subplots(1,1,figsize=(17,5))
    plot = authors_time_comments.plot.bar(stacked=False, title="Amount of comments by author", ax = axis1)
    plot.set_xlabel("Author")
    plot.set_ylabel("Morning or Evening")
   


    #amount of comments in the morning and night
    #amlount of log ins in the morning and night
    #by author what time does he work
                

    '''doesn't work with 09 values'''
    
    '''
    data_frame['day_period'] = data_frame['hours']
    data_frame['day_period'].loc[data_frame['hours'] < 12] = 0
    data_frame['day_period'].loc[data_frame['hours'] >= 12] = 1
    
    
    #add additional cell in the dqata frame which will have first string value
    data_frame ['hour_first_index'] = data_frame['hours'].str[0]

    data_frame['day_period_first_index'] = data_frame ['hour_first_index']
    data_frame['day_period_first_index'].loc[data_frame['hour_first_index'] == 0] = 0

    del data_frame['hour_first_index']
    
    
    '''
    

    
    
    
    