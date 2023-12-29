Description:

Distributed_web_infrastructure:

Why Adding Additional Elements:
Each additional element, such as redundancy, load balancers, or databases, is added to enhance performance, reliability, and scalability. Redundancy ensures continuity, load balancers distribute traffic, and databases ensure data persistence and availability.

Load Balancer Distribution Algorithm:
The distribution algorithm determines how the load balancer distributes incoming requests among multiple servers. Common algorithms include Round Robin, Least Connections, and IP Hash. For example, Round Robin evenly distributes requests among servers in a rotation.

Active-Active vs. Active-Passive Setup:
Active-Active: Both nodes are active and handle traffic simultaneously. They share the load, providing redundancy and load balancing. This setup enhances performance but requires synchronization and coordination.

Active-Passive: One node is active while the other is on standby. The standby node takes over if the active node fails. This setup ensures high availability but may underutilize resources in normal conditions.

Database Primary-Replica (Master-Slave) Cluster:
In a Primary-Replica cluster, the Primary (or Master) node handles write operations and replicates data to one or more Replica (or Slave) nodes. The Replica nodes handle read operations, providing scalability and fault tolerance. Data synchronization ensures consistency across nodes.

Primary vs. Replica Node:
Primary Node: Handles write operations, updates data, and replicates changes to Replica nodes. It serves as the authoritative source for data updates.

Replica Node: Receives replicated data from the Primary node and serves read requests. It provides fault tolerance, load balancing, and read scalability without directly handling write operations.

Issues with the Infrastructure:
SPOF:
Single Points of Failure (SPOF) exist where a component failure can disrupt the entire system, compromising availability and reliability. Redundancy and failover mechanisms are essential to mitigate these risks.

Security Issues:
Lack of a firewall exposes the infrastructure to unauthorized access, potential breaches, and attacks. Absence of HTTPS encryption jeopardizes data integrity and confidentiality, making sensitive information vulnerable to interception.

No Monitoring:
Without monitoring tools and practices, it's challenging to detect and address performance issues, anomalies, or failures promptly. Monitoring is crucial for maintaining optimal system health, identifying potential issues, and ensuring efficient resource utilization.
