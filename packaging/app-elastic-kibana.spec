
Name: app-elastic-kibana
Epoch: 1
Version: 1.2.1
Release: 1%{dist}
Summary: Kibana
License: GPLv3
Group: ClearOS/Apps
Packager: eGloo
Vendor: WikiSuite
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
Requires: app-elasticsearch-core >= 1:1.2.1
Requires: app-kibana-plugin-core
Requires: clearos-framework >= 7.3.0
Requires: kibana >= 5.4.0
Requires: java
Requires: mod_authnz_external-webconfig
Requires: mod_authz_unixgroup-webconfig
Obsoletes: app-kibana-core

%description core
Kibana is an open source data visualization plugin for Elasticsearch. It provides visualization capabilities on top of the content indexed on an Elasticsearch system.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/elastic_kibana
cp -r * %{buildroot}/usr/clearos/apps/elastic_kibana/

install -d -m 0755 %{buildroot}/var/clearos/elastic_kibana
install -d -m 0755 %{buildroot}/var/clearos/elastic_kibana/backup
install -D -m 0644 packaging/kibana.conf %{buildroot}/usr/clearos/sandbox/etc/httpd/conf.d/kibana.conf
install -D -m 0644 packaging/kibana.php %{buildroot}/var/clearos/base/daemon/kibana.php

%post
logger -p local6.notice -t installer 'app-elastic-kibana - installing'

%post core
logger -p local6.notice -t installer 'app-elastic-kibana-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/elastic_kibana/deploy/install ] && /usr/clearos/apps/elastic_kibana/deploy/install
fi

[ -x /usr/clearos/apps/elastic_kibana/deploy/upgrade ] && /usr/clearos/apps/elastic_kibana/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-elastic-kibana - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-elastic-kibana-core - uninstalling'
    [ -x /usr/clearos/apps/elastic_kibana/deploy/uninstall ] && /usr/clearos/apps/elastic_kibana/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/elastic_kibana/controllers
/usr/clearos/apps/elastic_kibana/htdocs
/usr/clearos/apps/elastic_kibana/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/elastic_kibana/packaging
%exclude /usr/clearos/apps/elastic_kibana/unify.json
%dir /usr/clearos/apps/elastic_kibana
%dir /var/clearos/elastic_kibana
%dir /var/clearos/elastic_kibana/backup
/usr/clearos/apps/elastic_kibana/deploy
/usr/clearos/apps/elastic_kibana/language
/usr/clearos/apps/elastic_kibana/libraries
/usr/clearos/sandbox/etc/httpd/conf.d/kibana.conf
/var/clearos/base/daemon/kibana.php
