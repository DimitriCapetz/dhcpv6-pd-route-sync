Summary: DHCPv6PDRouteSync
Name: DHCPv6PDRouteSync
Version: 0.1.2
Release: 1
License: Arista Networks
Group: EOS/Extension
Source0: %{name}-%{version}-%{release}.tar
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.tar
BuildArch: noarch

%description
This EOS SDK script will monitor DHCPv6 Routes and Install them to peer.

%prep
%setup -q -n source

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
# mkdir -p $RPM_BUILD_ROOT/usr/lib/SysdbMountProfiles
# cp DHCPv6PDRouteSync.mp $RPM_BUILD_ROOT/usr/lib/SysdbMountProfiles/DHCPv6PDRouteSync
cp DHCPv6PDRouteSync $RPM_BUILD_ROOT/usr/bin/

%files
%defattr(-,root,root,-)
/usr/bin/DHCPv6PDRouteSync
# /usr/lib/SysdbMountProfiles/DHCPv6PDRouteSync
%attr(0755,root,root) /usr/bin/DHCPv6PDRouteSync
