Name:		softflowd
Version:	0.9.9
Release:	1%{?dist}
Summary:	Flow-based network traffic analyser capable of Cisco NetFlow data export.

Group:		Applications/System
License:	BSD
URL:		https://code.google.com/p/%{name}/
Source0:	https://%{name}.google.com/files/%{name}-%{version}.tar.gz

BuildRequires:	libpcap-devel

%description
Softflowd is flow-based network traffic analyser capable of Cisco NetFlow data
export. Softflowd semi-statefully tracks traffic flows recorded by listening on
a network interface or by reading a packet capture file. These flows may be
reported via NetFlow to a collecting host or summarised within softflowd
itself.

Softflowd supports Netflow versions 1, 5 and 9 and is fully IPv6-capable - it
can track IPv6 flows and send export datagrams via IPv6. It also supports
export to multicast groups, allowing for redundant flow collectors. 

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%{_sbindir}/softflowctl
%{_sbindir}/softflowd
%{_mandir}/man8/softflowctl.8.gz
%{_mandir}/man8/softflowd.8.gz


%changelog
* Wed Jul 08 2015 Charles Simpson <csimpson@gmail.com>
- initial creation of RPM file for version 0.9.9

