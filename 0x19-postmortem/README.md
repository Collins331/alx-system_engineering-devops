# Linc Softwares services Outage

The following is the incident report for the Linc Software website outage that occurred on February 15, 2024 extending to February 16, 2024. We understand this service issue has impacted our valued developers and users, and we apologize to everyone who was affected.

## Issue Summary
From 9:30 PM to 3:16 AM EAT, requests to our website ```lincsoftwares.tech``` resulted in 500 error response messages. Most of our services were not available to our users. At its peak, the issue affected 100% of traffic to website. Users could continue to access certain services that run on separate infrastructures. The root cause of this outage was an invalid configuration change that exposed a bug in a widely used internal library.
## Timeline
> (all times in East Africa Time(EAT))
- [x] 09:30 PM: Configuration push begins
- [x] 09:50 PM: Outage begins
- [x] 09:51 PM: Pagers alerted teams
- [x] 11:23 PM: Failed configuration change rollback
- [x] 02:24 AM: Successful configuration change rollback
- [x] 02:30 AM: Server restarts begin
- [x] 03:16 AM: 100% of traffic back online

## Root Cause

At 09:30 PM EAT, a configuration change was inadvertently released to our production environment without first being released to the testing enviroment. The change specified an invalid address for the authentication servers in production. This exposed a bug in the authentication libraries which caused them to block permanently while attempting to resolve the invalid address to physical services. In addition, the internal monitoring systems permanently blocked on this call to the authentication library. The combination of the bug and configuration error quickly caused all of the serving threads to be consumed. Traffic was permanently queued waiting for a serving thread to become available. The servers began repeatedly hanging and restarting as they attempted to recover and at 09:50 PM EAT, the service outage began.

## Resolution and recovery
At 09:51 PM EAT, the monitoring systems alerted our engineers who investigated and quickly escalated the issue. By 10:40 PM, the incident response team identified that the monitoring system was exacerbating the problem caused by this bug.

At 11:23 PM, we attempted to rollback the problematic configuration change. This rollback failed due to complexity in the configuration system which caused our security checks to reject the rollback. These problems were addressed and we successfully rolled back at 02:24 PM.

Some jobs started to slowly recover, and we determined that the overall recovery would be faster by a restart of all of the website infrastructure servers globally. To help with the recovery, we turned off some of our monitoring systems which were triggering the bug. As a result, we decided to restart servers gradually (at 02:30 AM), to avoid possible cascading failures from a wide scale restart. By 03:02 AM, 50% of traffic was restored and 100% of traffic was routed to the website infrastructure at 03:16 AM.

## Corrective and Preventative Measures

In the last two days, we’ve conducted an internal review and analysis of the outage. The following are actions we are taking to address the underlying causes of the issue and to help prevent recurrence and improve response times:
- [x] Disable the current configuration release mechanism until safer measures are implemented.
- [x] Change rollback process to be quicker and more robust.
- [x] Fix the underlying authentication libraries and monitoring to correctly timeout/interrupt on errors.
- [x] Programmatically enforce staged rollouts of all configuration changes.
- [x] Improve process for auditing all high-risk configuration options.
- [x] Add a faster rollback mechanism and improve the traffic ramp-up process, so any future problems of this type can be corrected quickly.
- [x] Develop better mechanism for quickly delivering status notifications during incidents.

Linc Sofwares is committed to continually and quickly improving our technology and operational processes to prevent outages. We appreciate your patience and again apologize for the impact to you, your users, and your organization. We thank you for your business and continued support



Sincerely,

The Linc Software Infrastructure Team

Posted by Collins Ochineg