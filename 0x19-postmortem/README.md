POSTMORTEM REPORT: WEB APPLICATION OUTAGE
ISSUE SUMMARY
Duration of Outage: January,15 2024, from 14:00 to 17:00 EAT(3 hours)

Impact: The main web application was inaccessible, resulting in 100% downtime for all users. Approximately 15,000 active users were affected during this period. Users experienced an HTTP 500 Internal Server Error when attempting to access the site.

Root Cause: The outage was caused by a misconfiguration in the load balancer settings during a routine deployment, which led to the application servers being unable to handle incoming traffic properly.

TIMELINE

13:45 EAT: Deployment of a new version of the web application begins.
14:00 EAT: Monitoring alerts triggered due to an increase in HTTP 500 errors.
14:20 EAT: Application logs reviewed; no significant errors found.
15:00 EAT: identify irregularities in load balancer configuration.
15:15 EAT: Misleading path: Focus on potential DNS issues, but no anomalies detected.
15:30 EAT: Load balancer settings reviewed and corrected.
15:45 EAT: Load balancer restarted, and traffic routing begins to normalize.
16:00 EAT: Monitoring shows reduction in errors, site partially accessible.
16:30 EAT: Full accessibility restored for all users.
17:00 EAT: Post-recovery monitoring confirms stability.

ROOT CAUSE AND RESOLUTION

Root Cause: During the deployment process, the configuration changes inadvertently removed the backend server pool from the load balancer, causing it to route traffic to non-existent endpoints and resulting in HTTP 500 errors for all incoming requests.

Resolution: I identified the misconfiguration by reviewing the load balancer settings and comparing them to the previous stable configuration. Once the incorrect settings were identified, they were reverted to the correct configuration. 

CORRECTIVE AND PREVENTATIVE MEASURES
Improvements/Fixes:

Implement a pre-deployment configuration validation step to catch potential misconfigurations before they are applied.
Enhance monitoring and alerting specifically for load balancer configurations to detect similar issues more rapidly.
Conduct a review and update of deployment procedures to include a checklist for verifying load balancer settings.

Tasks:


Review and update the current load balancer configuration templates.
Implement automated checks to validate configuration changes before deployment.
Add Monitoring on Load Balancer Health:

Set up detailed monitoring for load balancer settings and health status.
Create alerts for any anomalies or configuration changes that deviate from the norm.
Review Deployment Procedures:

Develop a comprehensive deployment checklist.
Ensure all deployment steps are documented and include verification of key configurations.

Schedule training sessions focused on load balancer configuration and management.
Conduct regular drills to simulate and resolve load balancer-related issues.
By addressing these areas, we aim to prevent similar outages in the future and ensure a more resilient and stable deployment process

image url.

https://docs.google.com/document/d/1MhVw_D4hRiihvZCkY3LM1Jv755vymesoqoRmiwSWjdw/edit?usp=sharing
