<?php

/////////////////////////////////////////////////////////////////////////////
// General information
/////////////////////////////////////////////////////////////////////////////

$app['basename'] = 'kibana_web';
$app['version'] = '1.0.0';
$app['release'] = '1';
$app['vendor'] = 'eGloo';
$app['packager'] = 'eGloo';
$app['license'] = 'GPLv3';
$app['license_core'] = 'LGPLv3';
$app['description'] = lang('kibana_web_app_description');

/////////////////////////////////////////////////////////////////////////////
// App name and categories
/////////////////////////////////////////////////////////////////////////////

$app['name'] = lang('kibana_web_app_name');
$app['category'] = lang('base_category_server');
$app['subcategory'] = 'Search';

/////////////////////////////////////////////////////////////////////////////
// Packaging
/////////////////////////////////////////////////////////////////////////////

$app['obsoletes'] = array(
    'app-kibana'
);

$app['core_obsoletes'] = array(
    'app-kibana-core'
);

$app['core_requires'] = array(
    'app-elasticsearch-core',
    'kibana',
    'java',
);

$app['requires'] = array(
    'app-elasticsearch',
);

$app['core_directory_manifest'] = array(
    '/var/clearos/kibana_web' => array(),
    '/var/clearos/kibana_web/backup' => array(),
);

$app['core_file_manifest'] = array(
    'kibana.php'=> array('target' => '/var/clearos/base/daemon/kibana.php')
);

$app['delete_dependency'] = array(
    'app-kibana-web-core',
    'kibana',
);
