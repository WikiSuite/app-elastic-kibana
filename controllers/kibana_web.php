<?php

/**
 * Kibana controller.
 *
 * @category   apps
 * @package    kibana-web
 * @subpackage controllers
 * @author     eGloo <team@egloo.ca>
 * @copyright  2016 eGloo
 * @license    http://www.gnu.org/copyleft/gpl.html GNU General Public License version 3 or later
 * @link       https://www.egloo.ca/netify/community
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
// C L A S S
///////////////////////////////////////////////////////////////////////////////

/**
 * Kibana controller.
 *
 * @category   apps
 * @package    kibana-web
 * @subpackage controllers
 * @author     eGloo <team@egloo.ca>
 * @copyright  2016 eGloo
 * @license    http://www.gnu.org/copyleft/gpl.html GNU General Public License version 3 or later
 * @link       https://www.egloo.ca/netify/community
 */

class Kibana_Web extends ClearOS_Controller
{
    /**
     * Kibana default controller.
     *
     * @return view
     */

    function index()
    {
        // Load dependencies
        //------------------

        $this->lang->load('kibana_web');

        // Load views
        //-----------

        $views = array('kibana_web/server', 'kibana_web/settings');

        $this->page->view_forms($views, lang('kibana_web_app_name'));
    }
}
