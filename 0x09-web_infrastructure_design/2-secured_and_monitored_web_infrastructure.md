Description:

2-secured_and_monitored_web_infrastructure


Why Adding Additional Elements:


Additional elements like redundancy, load balancers, or databases are added to enhance performance, reliability, and scalability. They provide failover protection, distribute traffic, and manage data, respectively.

Purpose of Firewalls:
Firewalls act as a barrier between a trusted internal network and untrusted external networks, filtering incoming and outgoing traffic based on predefined security rules. They help prevent unauthorized access, malicious attacks, and data breaches.

Traffic over HTTPS:
HTTPS encrypts data transmitted between the server and client, ensuring confidentiality, integrity, and authentication. It protects sensitive information from eavesdropping, tampering, and impersonation, enhancing security for online transactions and communications.

Purpose of Monitoring:
Monitoring is used to oversee system performance, health, and behavior. It detects issues, anomalies, or failures, allowing for proactive management, timely interventions, and optimal resource utilization. It aids in maintaining system reliability, availability, and performance.

Data Collection in Monitoring:
Monitoring tools collect data by continuously monitoring system metrics, events, logs, and performance indicators. They use agents, probes, APIs, or direct integrations to gather information, store it in a centralized repository, and present it through dashboards, alerts, or reports.

Monitoring Web Server QPS:
To monitor web server Queries Per Second (QPS), you can use monitoring tools that capture request rates, analyze server logs, or measure network traffic. Configure metrics collection for HTTP requests or server performance to track QPS trends, identify patterns, and assess server load.

Issues with the Infrastructure:
Terminating SSL at Load Balancer:
Terminating SSL at the load balancer exposes decrypted traffic within the internal network, increasing the risk of unauthorized access, interception, or data exposure. It also places additional processing burden on the load balancer, potentially affecting performance and scalability.

Single MySQL Server for Writes:
Having a single MySQL server accepting writes creates a Single Point of Failure (SPOF) for write operations. If the server fails or becomes unavailable, write operations are disrupted, compromising data integrity, availability, and system functionality.

Uniform Servers with Same Components:
Deploying servers with identical components (database, web server, and application server) may lead to resource bottlenecks, performance issues, or system-wide failures. It lacks component specialization, limiting scalability, resilience, and optimization opportunities tailored to specific workload requirements.
