"use strict";

const {Builder, By, Key, until} = require('selenium-webdriver');
const config = require('./config.json');

async function example() {
    let driver = await new Builder().forBrowser('firefox').build();
    await driver.get(`${config.site_root}/docs`);
    
}

example();