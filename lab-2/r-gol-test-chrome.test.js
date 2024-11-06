const {Builder, By, Key, until} = require('selenium-webdriver');

describe('R-GOL', () => {
    let driver;

    beforeAll(async () => {
        driver = await new Builder().forBrowser('chrome').build();
    });

    afterAll(async () => {
        await driver.quit();
    });

    test('Should add product to favourite', async () => {
        await driver.manage().window().setRect({width: 768, height: 720})
        await driver.get('https://www.r-gol.com/');
        const homepageTitle = await driver.getTitle();
        expect(homepageTitle).toContain('R-GOL');

        const cookieBot = await driver.wait(
            until.elementLocated(By.id('CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')),
            4000
        );
        await cookieBot.click();

        const searchInput = await driver.wait(
            until.elementLocated(By.id('autocomplete-mobile')),
            2000
        );
        await searchInput.click();

        const searchModal = await driver.wait(
            until.elementLocated(By.css('div[itemtype="http://schema.org/ItemList"]')),
            1000
        );

        const isDisplayed = await searchModal.isDisplayed();
        expect(isDisplayed).toBe(true);

        const inputField = await driver.findElement(By.css('.luigi-ac-heromobile-input'));
        const inputValue = 'merkurial';
        await inputField.sendKeys(inputValue, Key.ENTER);

        await driver.wait(until.urlContains('phrase='), 10000);
        expect(await driver.getCurrentUrl()).toContain(inputValue);

        const heart = await driver.wait(
            until.elementLocated(By.css('.cupboard-heart')),
            2000
        );
        await heart.click();

        await driver.wait(
            until.elementLocated(By.id('__BVID__70')),
            5000
        );

        const modalHeading = await driver.findElement(By.id('__BVID__70___BV_modal_title_')).getText();
        expect(modalHeading).toBe('Dodaj do Schowka');

        const notSelectedSize = await driver.wait(
            until.elementLocated(By.css('div.not-set')),
            5000
        );

        const isDisplayedNotSelectedSize = await notSelectedSize.isDisplayed();
        expect(isDisplayedNotSelectedSize).toBe(true);

        const submitModalButton = await driver.findElement(By.css('footer.modal-footer button:nth-of-type(2)'));
        expect(await submitModalButton.getAttribute('disabled')).toBe("true");

        const enabledSizeElement = await driver.findElement(By.css('a.nav-link.cursor-pointer:not(.crossed)'));
        expect(await enabledSizeElement.getAttribute('class')).not.toContain('crossed');

        await enabledSizeElement.click();
        expect(await submitModalButton.getAttribute('disabled')).toBeNull();

        await submitModalButton.click();
    }, 15000);

    test('Should add product to cart', async () => {
        await driver.manage().window().setRect({width: 1280, height: 720})
        await driver.get('https://www.r-gol.com/korki-nike-zoom-mercurial-superfly-10-academy-fg-mg-limonkowy,p-193272');

        const cookieBot = await driver.wait(
            until.elementLocated(By.id('CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')),
            20000
        );
        await cookieBot.click();

        const productName = await driver.findElement(By.className('product-card__title')).getText();
        const searchedProductName = 'Korki Nike Zoom Mercurial Superfly 10 Academy FG/MG';
        expect(productName).toContain(searchedProductName);

        const productPriceElement = await driver.wait(
            until.elementLocated(By.className('product-card__current-price')),
            2000
        );
        const productPrice = await productPriceElement.getText();

        expect(productPrice).toContain('419,99 zł');

        const productSizeListItem = await driver.wait(
            until.elementLocated(By.css('li.product-attributes__attribute-value:not(:has(i))')),
            2000
        );

        const productSizeButton = await productSizeListItem.findElement(By.css('.cursor-pointer:not(.crossed)'));
        const productSize = await productSizeListItem.findElement(By.css('.cursor-pointer:not(.crossed) span')).getText();

        const addToCartButton = await driver.findElement(By.className('product-card__add-basket-btn'));
        expect(await addToCartButton.getAttribute('outerHTML')).toContain('Dodaj do koszyka');

        //await productSizeButton.click();
        await driver.executeScript("arguments[0].click();", productSizeButton);

        await driver.executeScript("arguments[0].click();", addToCartButton);

        await driver.wait(
            until.elementLocated(By.className('modal-content')),
            5000
        );

        expect(await driver.findElement(By.css('.modal-content h2')).getText()).toContain(searchedProductName);
        //expect(await driver.findElement(By.css('.modal-content h2')).getText()).toBe(searchedProductName);
        expect(await driver.findElement(By.css('.modal-content .product-card__current-price')).getText()).toBe(productPrice);

        await driver.findElement(By.css('.modal-content button.btn-primary')).click();

        await driver.wait(until.urlContains('basket'), 10000);
        expect(await driver.getCurrentUrl()).toContain('basket');

        await driver.wait(
            until.elementLocated(By.css('.summary-final__amount')),
            5000
        );

        const totalPriceInBasket = await driver.findElement(By.css('.summary-final__amount')).getText();
        expect(totalPriceInBasket).toBe(productPrice);

        expect(await driver.findElement(By.className('item-attr__value')).getText()).toBe(productSize);
    }, 10000);
});