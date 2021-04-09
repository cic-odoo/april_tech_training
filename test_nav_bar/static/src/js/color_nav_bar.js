odoo.define('theme_test.test_customer', function (require) {
"use strict";

    var ajax = require('web.ajax');

    // Check for Production URL
    if (window.location.hostname != 'test-customer-odoo.odoo.com') {
        ajax.loadCSS('/test_nav_bar/static/src/css/nav_bar.css');
    }
});
