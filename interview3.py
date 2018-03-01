'''Compare print with concatenation and with format string.'''

applicant = input("Enter the applicant's name: ")
interviewer = input("Enter the interviewer's name: ")
time = input("Enter the appointment time: ")
print('{0} will interview {1} at {2}. And {1} and {0} are happy.'.format(interviewer, applicant, time))
