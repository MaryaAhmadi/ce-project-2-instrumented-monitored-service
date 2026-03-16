# Incident Reports

## Incident 1 – Error Spike

Description:

Multiple requests were sent to the /error endpoint.

Detection:

CloudWatch alarm HighErrorRate triggered.

Investigation:

Dashboard showed spike in ErrorCount.

Logs confirmed repeated HTTP 500 responses.

Root Cause:

Simulated error endpoint.

Lesson Learned:

Monitoring successfully detected the failure.
