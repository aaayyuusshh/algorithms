'''
Maximum Non-Overlapping Meetings (Activity Selection Problem)

You are given a list of meetings, each with a (start time, end time). 
The goal is to schedule the maximum number of meetings in a single room, 
such that no two meetings overlap. A meeting can start as soon as another meeting ends.

Input:
A list of meetings, where each meeting is represented as a tuple (start_time, end_time).

Output:
The maximum number of non-overlapping meetings that can be scheduled.

Example: If you have the meetings [(1, 4), (2, 3), (3, 5), (7, 8)], 
one possible optimal solution is to select the meetings (2, 3), (3, 5), and (7, 8), which gives a total of 3 meetings.
'''

def max_non_overlapping_meetings(meetings):
    # sort meetings by end times
    # select meeting with the earliest end time that doesn't overlap with the previous meeting you just did
    # key idea: selecting meeting with the earliest possible end time gives us the max possible opportunities to hit other meetings
    # if start time of current meeting(ith iteration) doesn't overlap with previous meeting's end time:
        # then we can hit the meeting in the current iteration

    sortedMeetings = sorted(meetings, key=lambda x: x[1])
    maximumMeetings = 0
    previousEnd = 0

    for meeting in sortedMeetings:
        currentStartTime, currentEndTime = meeting
        if(currentStartTime >= previousEnd):
            maximumMeetings += 1
            previousEnd = currentEndTime

    return maximumMeetings

if __name__ == "__main__":
    meetings = [(1, 4), (2, 3), (3, 5), (7, 8)]
    result = max_non_overlapping_meetings(meetings)
    print("maximum number of non-overlapping meetings:", result)
    
    '''
    1--------4(select)
      2----3
           3-----5(select)
                      7---8(select)
    '''
