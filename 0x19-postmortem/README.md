#0x19. Postmortem

<img src="./bg.jpg" style="width: 566px; height:350px; text-align:center;" alt="Programming Error">

In my early days as an employee in a financial institution, and new to the Information Communication Technology field as a new recruit, we were given a task to upgrade all workstations’ web browser from Internet Explorer 9 as at that time on all Microsoft Windows 7 Operating system to Internet Explorer 11 because the organization was trying to upgrade their financial application to a newer version which will not work well with Internet Explorer 9.
A deadline was given to perform this task by the Application Solutions Department. Unknown to us, complete documentation for the safe rollout of this upgrade was not given/communicated to us because the application needed a newer version of Java RE preferably Java RE 7 update 60.
On the day that was set for a general simulation of the new financial application, we had issues generally as applets from the application were not loading because of the Java RE installed and configured for all users’ workstation.
We had to brainstorm and updated the Java RE software to Java RE 7update60. Nonetheless, the agenda for the day was defeated because we had to start looking for a way to update all the Java runtime environment to a later version, as well as updating the job card earlier submitted to my department on upgrading and updating systems’ web browsers and java RE for the successful rollout of this software.
A postmortem is a tool widely used in the Information Technology industry. After any outage, problem, or an encounter which could be caused by the following:
- Bugs
- Traffic spikes
- Security issues
- Hardware failures
- Natural disasters
- Human errors (improper documentation of miscommunication)

	The team(s) in charge of the system will write a summary that has 2 main goals:
- To provide the rest of the company’s employees or stakeholders involved with easy access to information detailing the cause of the outage and ways to remedy these issues. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
- To ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

---

Dukeson Ehigboria
