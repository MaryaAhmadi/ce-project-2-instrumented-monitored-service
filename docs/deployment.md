# Deployment Guide

## Overview

This document describes how to deploy the Observable Cloud Service on AWS EC2.

---

## Step 1 – Launch EC2 Instance

Create an EC2 instance with the following configuration:

Instance Type: t2.micro  
Operating System: Ubuntu 24.04  
Security Group: allow inbound port 5001

---

## Step 2 – Connect to EC2

Use SSH to connect:
ssh ubuntu@EC2_PUBLIC_IP

---

## Step 3 – Install Python Environment
sudo apt update
sudo apt install python3-venv -y

Create virtual environment:
python3 -m venv venv
source venv/bin/activate

---

## Step 4 – Install Dependencies
pip install flask structlog boto3

---

## Step 5 – Copy Application Code

Upload the application code to the EC2 instance.

Example:
scp -r app ubuntu@EC2_PUBLIC_IP:~/

---

## Step 6 – Run Application
python app.py

The API will run on:
http://EC2_PUBLIC_IP:5001

---

## Step 7 – Configure CloudWatch Agent

Install CloudWatch agent and apply configuration:
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl

Logs will be sent to:
/aws/observable-service/app

---

## Step 8 – Verify Deployment

Test the API:
curl http://EC2_PUBLIC_IP:5001/health

Expected response:
healthy

