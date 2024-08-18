Issue Summary
Duration: August 16, 2024, 10:00 AM - 12:00 PM GMT+2 (2 hours)
Impact: The primary web application experienced a complete outage, affecting 100% of users. Users were unable to access the website, resulting in an estimated 10,000 failed page loads.
Root Cause: Misconfigured PHP-FPM settings, specifically the pm.max_children parameter, causing all available workers to be exhausted, leading to 504 gateway timeouts.
Timeline
10:00 AM - Monitoring alert detected an increase in 504 errors.
10:05 AM - Engineer confirmed the issue after receiving customer complaints about inaccessible services.
10:10 AM - Initial investigation focused on network connectivity and load balancer configuration.
10:20 AM - Misleading debugging path assumed a DNS issue due to recent changes, which was ruled out after verification.
10:30 AM - Escalation to backend team to investigate server-side configurations.
11:00 AM - PHP-FPM configuration identified as the root cause.
11:15 AM - PHP-FPM settings adjusted, increasing the pm.max_children value.
11:30 AM - Services gradually restored, monitoring confirmed normal operation.
12:00 PM - Full service restoration confirmed, post-incident analysis began.
Root Cause and Resolution
Root Cause: The issue stemmed from the PHP-FPM configuration on the application server. The pm.max_children setting was too low, which caused all worker processes to be consumed during peak traffic. This led to the server being unable to handle incoming requests, resulting in 504 gateway timeouts for all users.
Resolution: The PHP-FPM pm.max_children parameter was increased to allow for more concurrent processes, which accommodated the peak traffic load. Additionally, a short-term load reduction strategy was implemented by temporarily disabling some non-essential services.
Corrective and Preventative Measures
Improvements:
Load Testing: Implement more rigorous load testing to determine appropriate server configurations under various traffic conditions.
Monitoring: Enhance monitoring to include alerts for resource exhaustion in PHP-FPM and similar services.
Incident Response: Improve incident response documentation to reduce time spent on misleading debugging paths.
Tasks:
Patch PHP-FPM Configuration: Increase pm.max_children and test under simulated peak load.
Enhance Monitoring: Add specific monitoring for PHP-FPM worker usage and memory consumption.
Update Incident Playbook: Document this incident and the correct diagnostic steps for similar issues.
Schedule Load Testing: Conduct regular load tests to validate server configurations against expected traffic volumes.
