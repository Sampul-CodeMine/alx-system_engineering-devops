# 0x07. Networking basics 1

## OSI Model

- What it is The `Open Systems Interconnection` model: ? (OSI model) is a conceptual model that 'provides a common basis for the coordination of [ISO] standards development for the purpose of systems interconnection. It comprises of 7 layers
  - `Physical Layers (Bit or Symbol)` - Transmission and reception of raw bit streams over a physical medium
  - `Data Link Layers (Frames)` - Transmission of data frames between two nodes connected by a physical layer
  - `Network Layers (Packets)` - Structuring and managing a multi-node network, including addressing, routing and traffic control
  - `Transport Layers (Segment or Datagram)` - Reliable transmission of data segments between points on a network, including segmentation, acknowledgement and multiplexing
  - `Session Layers (Data)` - Managing communication sessions, i.e., continuous exchange of information in the form of multiple back-and-forth transmissions between two nodes
  - `Presentation Layers (Data)` - Translation of data between a networking service and an application; including character encoding, data compression and encryption/decryption
  - `Application Layers (Data)` - High-level protocols such as for resource sharing or remote file access, e.g. HTTP, FTP.`

## What is LAN

`LAN (Local Area Networ)` is a computer network that interconnects computers within a limited area such as a residence, school, laboratory, university campus or office buildings.

## What is WAN

`WAN (Wide Area Network)`  is a telecommunications network that extends over a large geographic area. Wide area networks are often established with leased telecommunication circuits.

### Other Types of Area Networks

- WLAN: Wireless Local Area Network
- MAN: Metropolitan Area Network
- SAN: Storage Area Network, System Area Network, Server Area Network, or sometimes Small Area Network
- CAN: Campus Area Network, Controller Area Network, or sometimes Cluster Area Network
- PAN: Personal Area Network

## What is the Internet

The `Internet` is the global system of interconnected computer networks that uses the Internet protocol suite (TCP/IP) to communicate between networks and devices. It is a network of networks that consists of private, public, academic, business, and government networks of local to global scope, linked by a broad array of electronic, wireless, and optical networking technologies. The Internet carries a vast range of information resources and services, such as the interlinked hypertext documents and applications of the World Wide Web (WWW), electronic mail, telephony, and file sharing.
The origins of the `Internet` dates back to the development of packet switching and research commissioned by the United States Department of Defense in the late 1960s to enable time-sharing of computers.

## What is an IP address

`IP Address (Internet Protocol Address)` is a unique number or address given to every machine that is connected to the internet with which it can be communicated with and as well communicate with other interconnected machines.

### Two (2) types of IP address

- `IPV4`: `Internet Protocol version 4 (IPv4)` defines an IP address as a 32-bit number. IPv4 is the initial version used on the first generation of the Internet and is still in dominant use. It was designed to address up to ≈4.3 billion (10<sup>9</sup>) hosts. However, the explosive growth of the Internet has led to IPv4 address exhaustion, which entered its final stage in 2011, when the global IPv4 address allocation pool was exhausted.
- `IPV6`: Because of the growth of the Internet and the depletion of available IPv4 addresses, a new version of IP `IPv6`, was developed in the mid-1990s, which provides vastly larger addressing capabilities and more efficient routing of Internet traffic. IPv6 uses 128 bits for the IP address and was standardized in 1998. IPv6 deployment has been ongoing since the mid-2000s and is currently in growing deployment around the world, since Internet address registries (RIRs) began to urge all resource managers to plan rapid adoption and conversion. `IPv6` is not directly interoperable by design with IPv4. In essence, it establishes a parallel version of the Internet not directly accessible with IPv4 software. Thus, translation facilities must exist for internetworking or nodes must have duplicate networking software for both networks. Essentially all modern computer operating systems support both versions of the Internet Protocol. Network infrastructure, however, has been lagging in this development. Aside from the complex array of physical connections that make up its infrastructure, the Internet is facilitated by bi- or multi-lateral commercial contracts, e.g., peering agreements, and by technical specifications or protocols that describe the exchange of data over the network. Indeed, the Internet is defined by its interconnections and routing policies.

### Classes of IP Address

These IP addresses can further be broken down into classes. These classes are A, B, C, D, E and their possible ranges can be seen in Figure 2 below.

|Class |Start address |Finish address|
|---|---|---|
|A |0.0.0.0 |126.255.255.255|
|B |128.0.0.0 |191.255.255.255|
|C |192.0.0.0 |223.255.255.255|
|D |224.0.0.0 |239.255.255.255|
|E |240.0.0.0 |255.255.255.255|

## Private Network IP Addressing

Of the approximately four billion addresses defined in IPv4, about 18 million addresses in three ranges are reserved for use in private networks. Packets addressed in these ranges are not routable on the public Internet; they are ignored by all public routers. Therefore, private hosts cannot directly communicate with public networks, but require network address translation at a routing gateway for this purpose.

**Reserved private IPv4 network ranges**

|Name |CIDR block |-| Address range |Number of addresses |Obsolete classful description  |
|--- |---  |---|---   |---     |---       |
|24-bit |block  |10.0.0.0/8 |10.0.0.0 – 10.255.255.255 |16777216 |Single Class A.|
|20-bit |block |172.16.0.0/12 |172.16.0.0 – 172.31.255.255 |1048576 |Contiguous range of 16 Class B blocks.|
|16-bit |block |192.168.0.0/16 |192.168.0.0 – 192.168.255.255 |65536 |Contiguous range of 256 Class C blocks.|

## What is Localhost (127.0.0.1 / ::1)

In computer networking, localhost is a hostname that refers to the current computer used to access it. It is used to access the network services that are running on the host via the loopback network interface. Using the loopback interface bypasses any local network interface hardware. The local loopback mechanism may be used to run a network service on a host without requiring a physical network interface, or without making the service accessible from the networks the computer may be connected to. For example, a locally installed website may be accessed from a Web browser by the URL <http://localhost> to display its home page.
> `Localhost access: IPv4 - 127.0.0.1`
>
> `Localhost access: IPv6 - ::1`

## What is a subnet

A `Subnetwork` or `Subnet` is a logical subdivision of an `IP` network. The practice of dividing a network into two or more networks is called subnetting. Computers that belong to a subnet are addressed with an identical most-significant bit-group in their IP addresses. This results in the logical division of an IP address into two fields, the network number or routing prefix and the rest field or host identifier. The rest field is an identifier for a specific host or network interface.

## MAC Address (Media Access Control Address)

A `Media Access Control (MAC)` address is a string of characters that identifies a device on a network. It’s tied to a key connection device in your computer called the network interface card, or NIC. The NIC is essentially a computer circuit card that makes it possible for your computer to connect to a network. A NIC turns data into an electrical signal that can be transmitted over the network.

### Difference between IP Address and MAC Address

- The basic difference between an IP address and a MAC address is that an IP address represents software and a MAC address represents hardware.
- The MAC address identifies specific devices within the same local network and the IP address identifies those devices outside of the local network.

Once again, that’s hardware and software working together, IP addresses and MAC addresses working together. The MAC address is sometimes referred to as a networking hardware address, the burned-in address (BIA), or the physical address. MAC address do not change. They are hard-wired to the NIC. IP address change depending on the subnet, routing protocol etc that you are connected to.

## TCP/UDP

`Transmission Control Protocol / Internet Protocol (TCP/IP)` is a suite of protocols used by devices to communicate over the Internet and most local networks. TCP provides apps a way to deliver (and receive) an ordered and error-checked stream of information packets over the network.
`User Datagram Protocol (UDP)` is used by apps to deliver a faster stream of information by doing away with error-checking. When configuring some network hardware or software, you may need to know the difference.

_Note: These (UDP and TCP) are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)_

### Main difference between TCP and UDP

The main difference between `TCP (transmission control protocol)` and `UDP (user datagram protocol)` is that TCP is a connection-based protocol and UDP is connectionless. While TCP is more reliable because it performs error-checking, it transfers data more slowly. UDP is less reliable but works more quickly by skipping error-checking.

## What is a port

A port is a virtual point where network connections start and end. Ports are software-based and managed by a computer's operating system. Each port is associated with a specific process or service. Ports allow computers to easily differentiate between different kinds of traffic: emails go to a different port than webpages, for instance, even though both reach a computer over the same Internet connection.

### What is a port number?

Ports are standardized across all network-connected devices, with each port assigned a number. Most ports are reserved for certain protocols — for example, all Hypertext Transfer Protocol (HTTP) messages go to port 80. While IP addresses enable messages to go to and from specific devices, port numbers allow targeting of specific services or applications within those devices.

### Memorize SSH, HTTP and HTTPS port numbers

|Protocols | Port Numbers |
|---|---|
|echo|7|
|FTP (File Transfer Protocol)|20/21|
|SSH (Secure SHell)|22|
|Telnet|23|
|SMTP (Simple Mail Transfer Protocol)|25|
|DNS (Domain Name System)|53|
|DHCP (Dynamic Host Configuration Protocol)|67/68|
|POP (Post Office Protocol)|110|
|IMAP (Internet Message Access Protocol)|143|
|HTTP (HyperText Transfer Protocol)|80|
|HTTPS (HyperText Transfer Protocol over SSL)|443|
