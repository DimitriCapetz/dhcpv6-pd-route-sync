# DHCPv6 Prefix Delegation Route Sync

This EOS SDK Agent is used to add a kernel static route for specified destination hosts with a specific MTU value. When a route update occurs on the switch for any of the routes, this agent will evaluate the route for the configured destinations and update any kernel static routes.

By Default, this agent will add in routes with a MTU of 1500.

## Switch Setup

### Install
1. Copy `RouteUpdate-x.x.x-x.swix` to `/mnt/flash/` on the switch or to the `flash:` directory.
2. Copy and install the `.swix` file to the extensions directory from within EOS.  Below command output shows the copy and install process for the extension.
```
leaf2#copy flash:RouteUpdate-0.1.0-1.swix extension:
Copy completed successfully.
leaf2#sh extensions
Name                          Version/Release      Status      Extension
----------------------------- -------------------- ----------- ---------
RouteUpdate-0.1.0-1.swix      0.1.0/1              A, NI       1


A: available | NA: not available | I: installed | NI: not installed | F: forced
S: valid signature | NS: invalid signature
The extensions are stored on internal flash (flash:)
leaf2#extension RouteUpdate-0.1.0-1.swix
Agents to be restarted:
Note: no agents to restart
leaf2#sh extensions
Name                          Version/Release      Status      Extension
----------------------------- -------------------- ----------- ---------
RouteUpdate-0.1.0-1.swix      0.1.0/1              A, I        1


A: available | NA: not available | I: installed | NI: not installed | F: forced
S: valid signature | NS: invalid signature
The extensions are stored on internal flash (flash:)
```
3. In order for the extension to be installed on-boot, enter the following command:
```
leaf2#copy installed-extensions boot-extensions
Copy completed successfully.
```

### Route Update Agent Configuration
1. In EOS config mode perform the following commands for basic functionality (see step #4 for further customization):
```
config
daemon RouteUpdate
exec /usr/bin/RouteUpdate
no shutdown
```

2. By default, the agent has the following default values:
- MTU = 1500

To modify the default behavior, use the following commands to override the defaults:
```
config
daemon RouteUpdate
option mtu value {mtu_value}
```
**`mtu_value` **(optional)** Specify a specific L3 MTU value for any traffic to the configured destinations*

3. In order for this agent to create a static kernel route for specific destinations, the following commands will need to be taken:
```
config
daemon RouteUpdate
option {device_name} value {ip_of_device}
```
**`device_name` needs to be a unique identifier for each remote switch/device*

**`ip_of_device` needs to be a valid IPv4 address for the destination address for the static kernel route to be created*

***To see what unique peer identifiers have been created, enter `show daemon RouteUpdate`*

Example of a full `daemon RouteUpdate` config would look like with all parameters specified
```
daemon RouteUpdate
   exec /usr/bin/RouteUpdate
   option host1 value 172.16.116.201
   option host2 value 172.16.116.202
   option mtu value 1450
   no shutdown
!
```


#### Sample output of `show daemon RouteUpdate`
```
leaf2#show daemon RouteUpdate
Agent: RouteUpdate (running with PID 27823)
Uptime: 0:11:26 (Start time: Tue Jun 22 20:12:42 2021)
Configuration:
Option       Value
------------ --------------
host1        172.16.116.201
host2        172.16.116.202

Status:
Data        Value
----------- -------------------------------------------------
MTU         1500
host1       172.16.116.0/24 network via 172.16.200.5 next-hop
host2       172.16.116.0/24 network via 172.16.200.5 next-hop
```
