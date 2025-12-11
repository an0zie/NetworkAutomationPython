## TOOLS ENVIRONMENT

## INTRODUCTION
IN THIS SECTION WE ARE GOING TO DESCRIBE THE SOFTWARE AND HARDWARE TOOLS NEEDED TO DEVELOP  THE NETWORK AUTOMATION PROJECT AS WELL AS SOME TESTING METHODS 
APPLIED TO ENSURE ITS RELIABILITY 

## Software Tools
**Python 3.12 and above** : The programming language that will be used for network automation as
it will be used to write automation scripts for generating the IOS configuration
**JUSTIFICATION FOR USING PYTHON** :Using python for automation project provides for a scable and scriptable methid to configure devices faster  with fewer errors 

**NetMiko Library and Paramiko Library**: These are  open-source python library(NetMiko)  and  SSHv2 protocol library (Paramiko)built for SSH-based communication with 
network devices such routers , switches , servers and fire wall

**Cisco Packet Tracer**:This is a Network simulation software made by Cisco that is used to design , configure and test routers, 
switches ,test , servers and PC virtually. It is also known as Packet Tracer
**JUSTIFICATION FOR USING CISCO PACKET TRACER**: Using Packet Tracer offers a  safe virtual environment to replicate real networking hardware  

**NotePad**:Basic text editor that is used for quick editing of configuration files, notes and test reults 

**Windows Command Prompt (CMD)** :This is the  Built in Windows terminal interface  that will be used to activate Python virtual environmentrun scripts and perform ping and  SSH tests

## Hardware Tools
**Cisco 2911 Router (Simulated)**:High Performative integrated services router with multiple Gigabit Ethernet interface that is configured with SSH ,
Domain Name and local admin credentails for automation testing

**Cisco 2960-24TT Switch (Simulated)**:A layer 2 (Data-Link Layer)managed switch that connects PC and the router in the simulated topology

**Cisco 3560-24PS Mulilayer Switch(Simulated)**:An enterprise grade Layer 3(Network Layer) Switch  that is capable of inter-VLAN routing and Advanced management used to connect all network devices and enable routing between VLAN and networks when needed

**Servers (Simulated)** : Packet Tracer Server Node .This is used for Centralised SSH or Telnet management and testing 

**Wiring(Simulated)**:Ethernet cablesand Console connections within Packet Tracer that is used to connect routers, switches  and PCs for proper communication For Example to connect routers in the core routers we will use COPPER CROSS-OVER cables and between routers 
and other network devices you use COPPER STRAIGHT-THROUGH cables 

**PCs  and Laptops (Simulated)** : End Devices used to access the network and also test SSH automation . For Example One PC runs the Python script , another acts as a target host  

## TESTING METHODS 
**Ping Test**: This is used to vertify connectivity between the PCs, Servers  and Routers as the sender network device sending out the (echo request ICMP (Internet Control Message Protocol) message) ping message should  recieve a reply message back from the reciever network device

**SSH Login Test**: Here you use Python (Netmiko) to connect to connect the router using SSH credentails and we are expecting Successful connection and command execution

**Error Handling Test**:Simulate incorrect credentailS or wrong IP Address and we expect script to detect and report failed connections


## SUMMARY
THE COMBINATION OF PYTHON(FOR AUTOMATION) PACKET TRACER (FOR SIMULATION AND CONFIGURATION) ENABLES EFFICIENT TESTING AND VALIDATIONOF NETWORKWORKFLOWS IN A CONTROLLED LAB ENVIRONMENT 






