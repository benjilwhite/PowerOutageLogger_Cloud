# A Cloud Enabled Power Outage Logger

This project is an extension/modification of [JChristensen's](https://github.com/JChristensen) original [PowerOutageMonitor_HW](https://github.com/JChristensen/PowerOutageMonitor_HW) and [PowerOutageMonitor_SW](https://github.com/JChristensen/PowerOutageMonitor_SW). This code enables the arduino-based board to send power outage data via a serial connection to a Raspberry Pi once the power comes back on. Once the Raspberry Pi re-establishes an internet connection after a power outage, it sends the outage data to a REST API in AWS, where it can be stored in DynamoDB and sent to the user in an email message.

## How it Works

The [PowerOutageMonitor](https://github.com/JChristensen/PowerOutageMonitor_SW) code works almost entirely the same as the original, except for a few lines of code in the `void setup()` function which send data of the previous outage to the Raspberry Pi via an FTDI adapter plugged into the board. Once the Raspberry Pi receives the data and has a stable internet connection, it sends the data to a REST API via an HTTP POST request in AWS API Gateway.

An AWS Lambda function can be configured to write the `downTime`, `upTime`, and `maxTemp` to a DynamoDB table that can be viewed in the AWS Console. Lambda can also send the user an email notification via AWS Simple Notification Service.
