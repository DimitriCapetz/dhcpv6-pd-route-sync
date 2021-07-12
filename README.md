# DHCPv6 Prefix Delegation Route Sync

This EOS SDK Agent is used to synchronize DHCPv6 Prefix Delegation routes installed on one EOS device to another peer device.

## Switch Setup

### Install
1. Copy `DHCPv6PDRouteSync-x.x.x-x.swix` to `/mnt/flash/` on the switch or to the `flash:` directory.
2. Copy and install the `.swix` file to the extensions directory from within EOS.  Below command output shows the copy and install process for the extension.
```
dime-a-tron-720xp#copy flash:DHCPv6PDRouteSync-0.1.0-1.swix extension:
Copy completed successfully.
dime-a-tron-720xp#show extensions
Name                                Version/Release      Status      Extension
----------------------------------- -------------------- ----------- ---------
DHCPv6PDRouteSync-0.1.0-1.swix      0.1.0/1              A, NI       1


A: available | NA: not available | I: installed | NI: not installed | F: forced
S: valid signature | NS: invalid signature
The extensions are stored on internal flash (flash:)
dime-a-tron-720xp#extension DHCPv6PDRouteSync-0.1.0-1.swix
Agents to be restarted:
Note: no agents to restart
dime-a-tron-720xp#show extensions
Name                                Version/Release      Status      Extension
----------------------------------- -------------------- ----------- ---------
DHCPv6PDRouteSync-0.1.0-1.swix      0.1.0/1              A, I        1


A: available | NA: not available | I: installed | NI: not installed | F: forced
S: valid signature | NS: invalid signature
The extensions are stored on internal flash (flash:)
```
3. In order for the extension to be installed on-boot, enter the following command:
```
dime-a-tron-720xp#copy installed-extensions boot-extensions
Copy completed successfully.
```

### DHCPv6 PD Route Sync Agent Configuration
1. In EOS config mode perform the following commands. The options shown here are required:
```
daemon DHCPv6PDRouteSync
   exec /usr/bin/DHCPv6PDRouteSync
   option pdmask value {mask_length}
   option peer value {peer_ip}
```
**`mask_length` **(REQUIRED)** Specify the mask length of prefix delegations assigned via the DHCPv6 Server as a two digit number*

**`peer_ip` **(REQUIRED)** Specify an IP to configure the peer device. NOTE: Default VRF for management is required today*

2. Optionally, configure a VRF value if Prefix Delegations occur in a non-default VRF:
```
daemon DHCPv6PDRouteSync
   option vrf value {vrf_name}
```
**`vrf_name` **(optional)** Specify a VRF where Prefix Delegations will occur. If none is specified, the default VRF will be used*

***To see what configurations have been created, enter `show daemon DHCPv6PDRouteSync`*

Example of a full `daemon DHCPv6PDRouteSync` config would look like with all parameters specified
```
daemon DHCPv6PDRouteSync
   exec /usr/bin/DHCPv6PDRouteSync
   option pdmask value 64
   option peer value 10.112.112.243
   option vrf value IPV6
   no shutdown
```


#### Sample outputs of `show daemon DHCPv6PDRouteSync`
```
dime-a-tron-720xp#show daemon DHCPv6PDRouteSync
Agent: DHCPv6PDRouteSync (running with PID 15208)
Uptime: 0:00:10 (Start time: Thu Jul 08 15:47:23 2021)
Configuration:
Option       Value
------------ --------------
pdmask       64
peer         10.112.112.243
vrf          IPV6

Status:
Data         Value
------------ --------------
pdmask       64
peer         10.112.112.243
vrf          IPV6
```

After a DHCPv6 PD route has been detected and sychronized to the peer device, it will show in the `show daemon DHCPv6PDRouteSync` output.

```
dime-a-tron-720xp#show daemon DHCPv6PDRouteSync
Agent: DHCPv6PDRouteSync (running with PID 30709)
Uptime: 0:00:53 (Start time: Mon Jul 12 11:03:24 2021)
Configuration:
Option       Value
------------ --------------
pdmask       64
peer         10.112.112.243
vrf          IPV6

Status:
Data                   Value
---------------------- ---------------------------------
2001:dead:1::/64       Next-hop fe80::20c:29ff:fe99:9df9
pdmask                 64
peer                   10.112.112.243
vrf                    IPV6
```