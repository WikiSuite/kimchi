Name:		kimchi
Version:	2.3.1
Release:	0%{?dist}
Summary:	Kimchi server application
BuildRoot:	%{_topdir}/BUILD/%{name}-%{version}-%{release}
BuildArch:	noarch
Group:		System Environment/Base
License:	LGPL/ASL2
Source0:	%{name}-%{version}.tar.gz
Requires:	wok >= 2.1.0
Requires:	ginger-base
Requires:	qemu-kvm
Requires:	gettext
Requires:	libvirt
Requires:	libvirt-python
Requires:	libvirt-daemon-config-network
Requires:	python-websockify
Requires:	python-configobj
Requires:	novnc
Requires:	python-pillow
Requires:	pyparted
Requires:	python-psutil >= 0.6.0
Requires:	python-jsonschema >= 1.3.0
Requires:	python-ethtool
Requires:	sos
Requires:	python-ipaddr
Requires:	python-lxml
Requires:	nfs-utils
Requires:	iscsi-initiator-utils
Requires:	python-libguestfs
Requires:	libguestfs-tools
Requires:	python-magic
Requires:	python-paramiko
BuildRequires:	gettext-devel
BuildRequires:	libxslt
BuildRequires:	python-lxml

%global with_systemd 1

%description
Web application to manage KVM/Qemu virtual machines


%prep
%setup -q


%build
./autogen.sh --system
%configure
make


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root)
%{python_sitelib}/wok/plugins/kimchi/
%{_datadir}/kimchi/doc/
%{_prefix}/share/locale/*/LC_MESSAGES/kimchi.mo
%{_datadir}/wok/plugins/kimchi/
%{_sysconfdir}/wok/plugins.d/kimchi.conf
%{_sysconfdir}/kimchi/
%{_sharedstatedir}/kimchi/
%{_sysconfdir}/systemd/system/wokd.service.d/kimchi.conf


%changelog
* Thu Jun 18 2015 Lucio Correia <luciojhc@linux.vnet.ibm.com> 2.0
- Run kimchi as a plugin

* Thu Feb 26 2015 Frédéric Bonnard <frediz@linux.vnet.ibm.com> 1.4.0
- Add man page for kimchid

* Tue Feb 11 2014 Crístian Viana <vianac@linux.vnet.ibm.com> 1.1.0
- Add help pages and XSLT dependency

* Tue Jul 16 2013 Adam Litke <agl@us.ibm.com> 0.1.0-1
- Adapted for autotools build

* Thu Apr 04 2013 Aline Manera <alinefm@br.ibm.com> 0.0-1
- First build
