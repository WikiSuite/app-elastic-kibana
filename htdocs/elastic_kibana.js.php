<?php

/**
 * MariaDB ajax helpers.
 *
 * @category   apps
 * @package    elastic-kibana
 * @subpackage javascript
 * @author     eGloo <team@egloo.ca>
 * @copyright  2017 Marc Laporte
 * @license    http://www.gnu.org/copyleft/gpl.html GNU General Public License version 3 or later
 * @link       https://www.egloo.ca
 */

///////////////////////////////////////////////////////////////////////////////
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.  
//
///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////
// B O O T S T R A P
///////////////////////////////////////////////////////////////////////////////

$bootstrap = getenv('CLEAROS_BOOTSTRAP') ? getenv('CLEAROS_BOOTSTRAP') : '/usr/clearos/framework/shared';
require_once $bootstrap . '/bootstrap.php';

///////////////////////////////////////////////////////////////////////////////
// T R A N S L A T I O N S
///////////////////////////////////////////////////////////////////////////////

clearos_load_language('kibana');

///////////////////////////////////////////////////////////////////////////////
// J A V A S C R I P T
///////////////////////////////////////////////////////////////////////////////

header('Content-Type:application/x-javascript');
?>

///////////////////////////////////////////////////////////////////////////
// M A I N
///////////////////////////////////////////////////////////////////////////

$(document).ready(function() {
    $('#kibana_not_running').hide();
    $('#kibana_running').hide();

    clearosGetKibanaStatus();
});


// Functions
//----------

function clearosGetKibanaStatus() {
    $.ajax({
        url: '/app/elastic_kibana/server/status',
        method: 'GET',
        dataType: 'json',
        success : function(payload) {
            handleKibanaForm(payload);
            window.setTimeout(clearosGetKibanaStatus, 1000);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            window.setTimeout(clearosGetKibanaStatus, 1000);
        }
    });
}

function handleKibanaForm(payload) {
    if (payload.status == 'running') {
        $('#kibana_running').show();
        $('#kibana_not_running').hide();
    } else {
        $('#kibana_running').hide();
        $('#kibana_not_running').show();
    }
}

// vim: syntax=javascript
