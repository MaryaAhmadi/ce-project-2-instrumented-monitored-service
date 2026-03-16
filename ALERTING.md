# Alerting

## Alert Strategy

CloudWatch alarms detect abnormal behavior.

Configured alarms:

HighCPU  
HighErrorRate  
LowOrders

## Thresholds

HighCPU → CPU > 70%  
HighErrorRate → ErrorCount > 5  
LowOrders → OrdersCreated < 1

## Notification System

Alerts are delivered through Amazon SNS.

SNS sends email notifications to operators.

## Response Procedure

1. Check the CloudWatch alarm
2. Inspect dashboard metrics
3. Investigate logs
4. Identify root cause
