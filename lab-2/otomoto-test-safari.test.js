const {Builder, By, until} = require('selenium-webdriver');

describe('Otomoto', () => {
    let driver;

    beforeAll(async () => {
        driver = await new Builder().forBrowser('safari').build();

        await driver.manage().setTimeouts({implicit: 20000});
    });

    afterAll(async () => {
        await driver.quit();
    });

    test('Should open car list by selected brand on homepage', async () => {
        await driver.get('https://www.otomoto.pl/');
        expect(await driver.getTitle()).toContain('OTOMOTO');

        const acceptPolicyButton = await driver.wait(
            until.elementLocated(By.id('onetrust-accept-btn-handler')),
            2000
        );
        expect(await acceptPolicyButton.getText()).toBe('Akceptuję');
        await acceptPolicyButton.click();

        const submitFormButton = await driver.findElement(By.css('.e1wnr56l4.ep2wx1j0.ooa-1ktp2qo'));
        const submitFormTextButton = await submitFormButton.getText();

        const input = await driver.wait(
            until.elementLocated(By.css('.ooa-4ehujk')),
            4000
        );
        await driver.executeScript("arguments[0].click();", input);

        const brandSelectElements = await driver.findElements(By.css('.ooa-164w2lr'));
        expect(brandSelectElements.length).toBeGreaterThan(1);

        const secondBrandElement = brandSelectElements[1];
        const brandWithNumbers = await secondBrandElement.getText();
        const brand = brandWithNumbers.replace(/\s*\(.*?\)\s*/g, '').trim();

        await secondBrandElement.click();
        expect(await input.getAttribute('value')).toContain(brandWithNumbers);

        await driver.wait(async () => {
            const text = await submitFormButton.getText();
            return submitFormTextButton !== text;
        }, 1000);
        expect(await submitFormButton.getText()).not.toBe(submitFormTextButton);

        await submitFormButton.click();

        await driver.wait(async () => {
            const readyState = await driver.executeScript('return document.readyState');
            return readyState === 'complete';
        });

        const firstCarItem = await driver.wait(until.elementLocated(By.css('h1.epwfahw9.ooa-1ed90th.er34gjf0 > a')), 10000);
        const firstCarItemHeader = await firstCarItem.getText();
        expect(firstCarItemHeader).toContain(brand);

        expect(await driver.getCurrentUrl()).toContain(brand.toLowerCase());
        expect(await driver.findElement(By.css('h4.e17gkxda1.ooa-1l0bag1.er34gjf0')).getText()).toContain(brand);
    }, 10000);
});
