
Name: app-kibana
Epoch: 1
Version: 1.0.0
Release: 1%{dist}
Summary: Kibana
License: GPLv3
Group: ClearOS/Apps
Packager: eGloo
Vendor: eGloo
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
Requires: %{name}-core = 1:%{version}-%{release}
Requires: app-base
Requires: app-elasticsearch

%description
Kibana is an open source data visualization plugin for Elasticsearch. It provides visualization capabilities on top of the content indexed on an Elasticsearch system.

%package core
Summary: Kibana - Core
License: LGPLv3
Group: ClearOS/Libraries
Requires: app-base-core
Requires: app-elasticsearch-core
Requires: kibana
Requires: java

%description core
Kibana is an open source data visualization plugin for Elasticsearch. It provides visualization capabilities on top of the content indexed on an Elasticsearch system.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/kibana
cp -r * %{buildroot}/usr/clearos/apps/kibana/

install -d -m 0755 %{buildroot}/var/clearos/kibana
install -d -m 0755 %{buildroot}/var/clearos/kibana/backup
install -D -m 0644 packaging/kibana.php %{buildroot}/var/clearos/base/daemon/kibana.php

%post
logger -p local6.notice -t installer 'app-kibana - installing'

%post core
logger -p local6.notice -t installer 'app-kibana-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/kibana/deploy/install ] && /usr/clearos/apps/kibana/deploy/install
fi

[ -x /usr/clearos/apps/kibana/deploy/upgrade ] && /usr/clearos/apps/kibana/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-kibana - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-kibana-core - uninstalling'
    [ -x /usr/clearos/apps/kibana/deploy/uninstall ] && /usr/clearos/apps/kibana/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/kibana/controllers
/usr/clearos/apps/kibana/htdocs
/usr/clearos/apps/kibana/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/kibana/packaging
%dir /usr/clearos/apps/kibana
%dir /var/clearos/kibana
%dir /var/clearos/kibana/backup
/usr/clearos/apps/kibana/deploy
/usr/clearos/apps/kibana/language
/usr/clearos/apps/kibana/libraries
/var/clearos/base/daemon/kibana.php
