

# Project 2 - Instrumented & Monitored Cloud Service

**Cloud Engineering Bootcamp – Week 6 
**Activity Type:** Individual 
**Estimated Time:** 3 days 
 


## Overview

This project demonstrates how to build an observable cloud service using AWS.

The system includes structured logging, custom metrics, monitoring dashboards, alerting, and incident response simulation.

The goal is to build a production-ready system that is observable and maintainabl

I'm continuing a **Cloud Observability project** I was working on in another chat.

---

## 🎯 Lab Objective

Goal:

The goal of this lab was to analyze and improve the performance and observability of a cloud-based web service deployed on AWS.
The objective was to instrument the application with logging and metrics, monitor system behavior using CloudWatch dashboards, and evaluate how the system behaves under different conditions such as error spikes and latency spikes.

This lab demonstrates how observability tools help engineers understand system performance and diagnose issues quickly.

---


## Architecture

Components used:

- Flask API
- EC2 Instance
- CloudWatch Logs
- CloudWatch Metrics
- CloudWatch Dashboard
- CloudWatch Alarms
- SNS Email Notifications

Architecture Flow:

Client → Flask API → CloudWatch Logs + Metrics → Dashboard + Alarms

---
## 🔧 Optimizations Implemented

Several improvements were implemented to enhance monitoring and operational visibility:

Structured Logging
Implemented JSON structured logging using structlog to make logs machine-readable and easier to analyze.

Correlation IDs
Each request was assigned a unique correlation ID to trace the request lifecycle across logs and metrics.

Custom Application Metrics
The application publishes the following metrics to CloudWatch:

RequestCount
ErrorCount
OrdersCreated
OrderValue
Monitoring Dashboard
A CloudWatch dashboard was created to visualize key system signals.
Automated Alerting

CloudWatch alarms were configured to detect abnormal behavior and send notifications via Amazon SNS.

---

## ⚡ Performance Comparison

The system was tested under different scenarios to observe behavior and validate monitoring capabilities.

Test scenarios included:

Normal API requests
- Error spike simulation
- Latency spike simulation
- Real measured values (my run):
- Metric	Normal Load	Error Simulation	Latency Simulation

| Metric          | Normal Load     | Error Simulation | Latency Simulation |
| --------------- | --------------- | ---------------- | ------------------ |
| RequestCount    | ~5 requests/min | ~30 requests/min | ~20 requests/min   |
| ErrorCount      | 0               | >10 errors/min   | 0                  |
| Latency         | ~20 ms          | ~25 ms           | ~3000 ms           |
| CPU Utilization | ~5%             | ~10%             | ~12%               |


These results demonstrate how observability metrics reveal system behavior under different conditions.

---

## Application Endpoints

| Endpoint | Description |
|--------|-------------|
| / | Basic API response |
| /health | Health check endpoint |
| /order | Simulates order creation |
| /error | Simulates application error |
| /slow | Simulates slow response |

---


## Structured Logging

Logs are written in JSON format and include:

- correlation_id
- timestamp
- request path
- status code
- latency
- log level


### Custom Metrics

## Metrics sent to CloudWatch:
- RequestCount
- ErrorCount
- OrdersCreated
- OrderValue

## Namespace:

Project2/ObservableService
---

## Monitoring Dashboard
The CloudWatch dashboard visualizes key metrics including:
Request Rate
Error Rate
Orders Created
Order Value
CPU Utilization
---

## Alerting System
CloudWatch alarms trigger notifications when abnormal behavior occurs.

## Configured alarms:

    Alarm	  |   Condition
HighCPU	CPU   |  > 70%
HighErrorRate  |	 ErrorCount > 5
LowOrders	  | OrdersCreated < 1

Alerts are delivered via SNS email notifications.
---

## Failure Simulation
Two simulated failures were tested.


## Error Spike

Multiple requests were sent to /error, causing HTTP 500 responses.
CloudWatch detected the spike and triggered an alarm.

## Latency Spike
Requests were sent to /slow, generating high latency responses.
Logs confirmed increased response times.

---

## 🛠️ Key Lessons Learned

Key insights gained from this lab:

- Observability is essential for understanding system behavior in production.
- Metrics provide a high-level view of system health.
- Logs provide detailed information required for root cause analysis.
- Dashboards help visualize trends and detect anomalies quickly.
- Automated alerts significantly reduce incident response time.

This lab demonstrates how combining logs, metrics, and alerts creates a reliable monitoring strategy.

---

## 📊 How to Reproduce

To reproduce this experiment:

- Deploy the Flask API to an EC2 instance.
- Configure CloudWatch logging using the CloudWatch agent.
- Configure custom metrics using the AWS SDK (boto3).
- Create a CloudWatch dashboard with key metrics.
- Configure CloudWatch alarms and SNS notifications.
- Simulate system behavior:

Error spike simulation:
curl http://EC2-IP:5001/error

Latency simulation:
curl http://EC2-IP:5001/slow

Observe the dashboard and alerts.

---

## 🔧 Tools & Versions Used

| Tool       | Purpose                |
| ---------- | ---------------------- |
| Python     | Application runtime    |
| Flask      | Web API framework      |
| structlog  | Structured logging     |
| boto3      | AWS SDK for metrics    |
| AWS EC2    | Application hosting    |
| CloudWatch | Logging and monitoring |
| SNS        | Alert notifications    |

Environment:
Ubuntu 24.04
Python 3.10+
EC2 instance type: t2.micro

---

## 📁 Repository Structure 

observable-cloud-service/
│
├── README.md
├── ARCHITECTURE.md
├── INSTRUMENTATION.md
├── MONITORING.md
├── ALERTING.md
├── INCIDENTS.md
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│
├── config/
│   ├── dashboard.json
│   ├── alarms.json
│   ├── cloudwatch-agent-config.json
│
├── docs/
│   ├── runbook.md
│   ├── dashboard-guide.md
│   ├── deployment.md
│
└─screenshots/
  ├── 01-structured-logging-json.png
  ├── 02-application-endpoints-logs.png
  ├── 03-request-latency-logging.png
  ├── 04-custom-metrics-logging.png
  ├── 06-cloudwatch-metric-send-test.png
  ├── 08-ssh-ec2-login.png
  ├── 09-ec2-python-venv-installation.png
  ├── 10-project-copied-to-ec2.png
  ├── 11-ec2-api-running.png
  ├── 12-ec2-health-endpoint.png
  ├── 13-application-log-file-on-ec2.png
  ├── 14-ec2-iam-role-attached.png
  ├── 15-iam-role-verification.png
  ├── 16-cloudwatch-log-group.png
  ├── 17-cloudwatch-log-stream-events.png
  ├── 18-cloudwatch-custom-metrics.png
  ├── 19-custom-metric-order-value.png
  ├── 20-cloudwatch-dashboard-overview.png
  ├── 21-dashboard-business-metrics.png
  ├── 22-sns-topic-created.png
  ├── 23-sns-email-subscription-confirmed.png
  ├── 24-cloudwatch-alarm-highcpu.png
  ├── 25-cloudwatch-alarm-higherror.png
  ├── 26-cloudwatch-alarm-loworders.png
  ├── 27-alarm-insufficient-data.png
  ├── 28-alarm-triggered-error-rate.png
  ├── 29-alert-email-error-rate.png
  ├── 30-dashboard-error-spike.png
  ├── 31-dashboard-request-spike.png
  ├── 32-cloudwatch-error-logs.png
  ├── 33-slow-endpoint-latency-logs.png
  ├── 34-cpu-utilization-during-slow.png
  └── api-running-&-health-endpoint.png

---

## Conclusion

This project demonstrates the importance of observability in modern cloud systems.
By combining logging, metrics, dashboards, and alerting, engineers can quickly detect and diagnose system issues.

---

🚀 Next Steps / Extra Mile Ideas

Possible improvements for future work:

1-Implement latency metrics for more detailed performance monitoring
2-Add distributed tracing using AWS X-Ray or OpenTelemetry
3-Implement auto-remediation using AWS Lambda triggered by alarms
4-Introduce load testing using tools such as Locust or k6
5-Add cost monitoring and FinOps dashboards

---


Thank you for reviewing!

Submitted by: Maryam Ahmadi 
Date: 16.03.2026

