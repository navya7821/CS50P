# ATTENDANCE TRACKER
#### Video Demo: <URL HERE>
#### Description:
Attendance Tracker is a program that can be implemented to keep track of attendance. It is very convenient to use and requires minimal input. It displays weekly data and semester-wise data upon being prompted for the same. It is also equipped with visualization to represent the contribution of every week to the semester attendance.

Unlike current attendance apps, ATTENDANCE TRACKER does not run based on a calendar or fixed timetable. It is operated based on weekly entries and hence it needs to be used with an honor system to ensure that the data is recorded truthfully. It also supports a flexible number of working days per week.

It works by marking the classes as 'PRESENT' or 'ABSENT' instead of following a rigid timetable, thereby avoiding the hassle of marking classes as 'Canceled' and enhancing user experience. The most important feature is that it allows maintaining data from multiple semesters simultaneously.

The design is based on a total of six core functions and one main function:

- `day_structure` is responsible for implementing the iterative collection of subject and present/absent data.
- `data_collection` creates a folder for each semester and stores the weekly data into their respective files.
- `data_retrieval` allows us to access weekly data by specifying the semester number and the week number. It returns a list of dictionaries where each dictionary corresponds to each day’s entry.
- This list is passed into the `attendance` function which returns the summary for each subject, the total number of classes conducted, and the number of classes attended for that week.
- This data is passed to the `percentage` function which calculates the percentage per subject and the overall weekly attendance percentage.
- Data for the whole semester can be accessed by prompting with the keyword `Semester` followed by the semester number. This triggers `plot_weekly_attendance_pie` which returns a pie chart representing each week’s contribution to the semester attendance.

This project is ideal for students who prefer a manual, flexible, and organized way to track their attendance patterns over time.
