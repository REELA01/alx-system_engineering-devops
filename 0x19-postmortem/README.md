## Issue Summary:

Duration: The outage occurred from 10:00 AM to 11:30 AM (UTC) on April 15th, 2024.
Impact: During the outage, SSH access to critical server infrastructure was unavailable, affecting all users attempting to authenticate via public key authentication. Approximately 80% of the users were affected, leading to disruption in deployment and administrative tasks.
## Timeline:

* 10:00 AM: The issue was detected when the operations team received alerts indicating SSH authentication failures.
* 10:05 AM: Engineers noticed multiple SSH connection attempts resulting in password denied errors.
* 10:10 AM: Initial investigation focused on server logs and SSH configuration files to identify any misconfigurations or unauthorized access attempts.
* 10:30 AM: Misleading investigation paths included examining network connectivity and firewall settings, which did not reveal any anomalies.
* 10:45 AM: The incident was escalated to the infrastructure team for further analysis and resolution.
* 11:30 AM: After extensive troubleshooting, the incident was resolved by reverting changes made to the SSH server configuration.
## Root Cause and Resolution:

Root Cause: The issue was caused by an unintended change in the SSH server configuration, specifically the removal of the authorized_keys file containing public keys for authentication.
Resolution: The issue was fixed by restoring the authorized_keys file from a backup and restarting the SSH service to apply the changes. Additionally, access controls were tightened to prevent unauthorized modifications to the SSH configuration.
## Corrective and Preventative Measures:

## Improvements/Fixes:

* Strengthen monitoring and alerting systems to promptly detect changes in critical configuration files, such as SSH server configurations.
* Implement version control for configuration files to track and revert changes effectively.
## Tasks:

* Implement automated backups of critical configuration files to facilitate quick restoration in case of similar incidents.
* Conduct regular audits of system configurations to ensure compliance with security best practices.
* Provide additional training to team members on the importance of reviewing and testing configuration changes before deployment.
## Conclusion:

The SSH password denied (public key) error outage highlighted the criticality of maintaining proper configuration management and monitoring systems. By implementing corrective measures and proactive steps to prevent similar incidents, the organization can mitigate the impact of configuration-related issues and ensure the reliability of its infrastructure.
