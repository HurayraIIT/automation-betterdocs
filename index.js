"use strict";

const {Builder, By, Key, until} = require('selenium-webdriver');
const config = require('./util/config.json');

async function example() {
    let driver = await new Builder().forBrowser('firefox').build();
    await driver.get(`${config.site_root}/docs`);
    await driver.findElement(By.name('s')).sendKeys('test');
    await driver.sleep(3000);
    
}

example();