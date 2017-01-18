
Name: app-kibana-web
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
Obsoletes: app-kibana

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
Obsoletes: app-kibana-core

%description core
Kibana is an open source data visualization plugin for Elasticsearch. It provides visualization capabilities on top of the content indexed on an Elasticsearch system.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/kibana_web
cp -r * %{buildroot}/usr/clearos/apps/kibana_web/

install -d -m 0755 %{buildroot}/var/clearos/kibana_web
install -d -m 0755 %{buildroot}/var/clearos/kibana_web/backup
install -D -m 0644 packaging/kibana.php %{buildroot}/var/clearos/base/daemon/kibana.php

%post
logger -p local6.notice -t installer 'app-kibana-web - installing'

%post core
logger -p local6.notice -t installer 'app-kibana-web-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/kibana_web/deploy/install ] && /usr/clearos/apps/kibana_web/deploy/install
fi

[ -x /usr/clearos/apps/kibana_web/deploy/upgrade ] && /usr/clearos/apps/kibana_web/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-kibana-web - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-kibana-web-core - uninstalling'
    [ -x /usr/clearos/apps/kibana_web/deploy/uninstall ] && /usr/clearos/apps/kibana_web/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/kibana_web/controllers
/usr/clearos/apps/kibana_web/htdocs
/usr/clearos/apps/kibana_web/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/kibana_web/packaging
%dir /usr/clearos/apps/kibana_web
%dir /var/clearos/kibana_web
%dir /var/clearos/kibana_web/backup
/usr/clearos/apps/kibana_web/deploy
/usr/clearos/apps/kibana_web/language
/var/clearos/base/daemon/kibana.php
