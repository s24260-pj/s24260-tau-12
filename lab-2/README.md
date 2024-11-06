# Test Automation Project

This project contains automated Selenium tests using Jest for three websites: **Morele**, **R-Gol**, and **Otomoto**. The tests are configured to run on multiple browsers (Chrome, Firefox, and Safari), and cover key user scenarios on each website.

## Project Structure

The test files are organized by website and browser, with individual `.test.js` files:
- **Morele**: `morele-test-chrome.test.js`, `morele-test-firefox.test.js`, `morele-test-safari.test.js`
- **R-Gol**: `r-gol-test-chrome.test.js`, `r-gol-test-firefox.test.js`, `r-gol-test-safari.test.js`
- **Otomoto**: `otomoto-test-chrome.test.js`, `otomoto-test-firefox.test.js`, `otomoto-test-safari.test.js`

Each file tests a specific user scenario on a designated website and browser, as described below.

## Test Scenarios

### Morele.net

**Goal:** Test product interaction, from viewing details to adding items to the cart.

#### Scenario: Add Product to Cart and Verify Price

1. Open the product page on Morele.net.
2. Accept cookies.
3. Retrieve product information (e.g., name, price, description).
4. Verify the retrieved information is not empty.
5. Check that the "Add to Cart" button has the text "Do koszyka".
6. Add the product to the cart.
7. Navigate to the cart.
8. Add the first product from the "Related Products" section.
9. Verify that the product price in the cart matches the price shown on the product page.

### R-Gol

**Goal:** Test search and wishlist functionalities on R-Gol.

#### Scenario 1: Search and Add Product to Wishlist

1. Open the R-Gol homepage.
2. Accept cookies.
3. Open the search modal.
4. Enter "merkurial" into the search bar.
5. Navigate to the search results page.
6. Click the heart icon for the first item on the list.
7. Confirm that the wishlist modal appears.
8. Add the product to the wishlist.

#### Scenario 2: Add Product to Cart and Verify Details

1. Open the product page.
2. Accept cookies.
3. Retrieve product information (e.g., name, price, available sizes).
4. Select a shoe size.
5. Add the product to the cart.
6. Navigate to the cart.
7. Verify that the product price in the cart matches the price on the product page.
8. Confirm that the product name in the cart matches the product page.

### Otomoto

**Goal:** Test car search functionality from selecting a car make to viewing details.

#### Scenario: Search for a Car and Verify Details

1. Open the Otomoto homepage.
2. Accept cookies.
3. Select the first car make from the list.
4. Submit the search form.
5. Ensure navigation to the results page for the selected make.
6. Verify that the chosen make is displayed on the results page.
7. Open the details page of the first listing.
8. Click the phone number button to reveal contact information.

## Setting Up the Environment

1. Ensure you have Node.js and npm installed.
2. Install the necessary dependencies:
   ```bash
   npm install

## Videos
https://github.com/user-attachments/assets/31d4b275-cb5c-44d1-a319-ac07ef968d35
https://github.com/user-attachments/assets/85c0bfb8-aa44-486a-b21f-0e14efe51933
https://github.com/user-attachments/assets/7c640ae9-cdda-4afd-82d6-046f163290fd
