const {Builder, By, until} = require('selenium-webdriver');

describe('Morele', () => {
    let driver;

    beforeAll(async () => {
        driver = await new Builder().forBrowser('chrome').build();
    });

    afterAll(async () => {
        await driver.quit();
    });

    test('Should add recommended product in cart', async () => {
        await driver.get('https://www.morele.net/lego-creator-expert-ford-mustang-10265-6331112/');
        const saveButton = await driver.wait(
            until.elementLocated(By.css('.btn--save-all')),
            1500
        );
        await saveButton.click();

        const productPrice = await driver.findElement(By.id('product_price_brutto')).getText();
        expect(productPrice).not.toBeNull();
        const productName = await driver.findElement(By.className('prod-name')).getText();
        expect(productName).not.toBeNull();

        const addToCartButton = await driver.findElement(By.className('btn-add-to-basket'));
        expect(await addToCartButton.getText()).toBe('Do koszyka');

        await driver.executeScript("arguments[0].click();", addToCartButton);
        await driver.wait(until.urlContains('koszyk'), 10000);
        expect(await driver.getCurrentUrl()).toContain('koszyk');

        await driver.wait(
            until.elementLocated(By.css('.product-title > a')),
            1500
        );
        expect(await driver.findElement(By.css('.product-title > a')).getText()).toBe(productName);
        expect(await driver.findElement(By.className('subtotal-price')).getText()).toBe(productPrice);

        const productCard = await driver.wait(
            until.elementLocated(By.css('.basket-similar-smp-products__content a.productData')),
            2000
        );

        const newProductPrice = await productCard.findElement(By.css('.ps-price')).getText();
        expect(newProductPrice).not.toBeNull();

        const addToCartNewProductButton = await productCard.findElement(By.css('button[type="button"]'));

        await driver.executeScript("arguments[0].click();", addToCartNewProductButton);

        const productPriceInt = parseInt(productPrice.replace(/\s*zł/g, '').replace(',', ''));
        const newProductPriceInt = parseInt(newProductPrice.replace(/\s*zł/g, '').replace(',', ''));

        const totalPriceCalculate = productPriceInt + newProductPriceInt;

        const initialPrice = '799,00 zł';

        await driver.wait(async () => {
            const currentPriceTextElement = await driver.findElement(By.css('.summary-box-price b'));
            const currentText = await currentPriceTextElement.getText();

            return currentText !== initialPrice;
        }, 5000);

        const totalPriceElement = await driver.findElement(By.css('.summary-box-price b'));
        const totalPriceText = await totalPriceElement.getText();
        const totalPriceInt = parseInt(totalPriceText.replace(/\s/g, '').replace(',', '.').replace(' zł', ''), 10);

        expect(totalPriceInt).toBe(totalPriceCalculate);
    }, 20000);
});