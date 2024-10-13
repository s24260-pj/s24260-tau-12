const {sum, renderObject, arrayRemoveElementByIndex} = require('./functions');

test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);
});

test('adds true + false to equal true|1', () => {
    expect(sum(true, false)).toBeTruthy();
});

test('adds undefined + 5 to equal NaN', () => {
    expect(sum(undefined, 5)).toBeNaN();
});

test('adds "test " + 2 to equal "test 2"', () => {
    expect(sum("test ", 2)).toBe("test 2");
});

test('render object {a: 1, b: 2}', () => {
    const data = {a: 1, b: 2};
    expect(renderObject(1, 2)).toEqual(data);
});

test('throws error on undefined values', () => {
    expect(() => renderObject(undefined, undefined)).toThrow(new Error("Undefined values"));
});

test('throws error when trying to remove key from non-array', () => {
    const data = { test: 'test' }
    expect(() => arrayRemoveElementByIndex(data, 1)).toThrow(new Error("Variable is not an array!"));
});

test('slice array by index', () => {
    const data = ['12', 'test', '243'];
    expect(arrayRemoveElementByIndex(data, 1)).toEqual(['12', '243']);
});

test('slice array by index undefined', () => {
    const data = ['12', 'test', '243'];
    expect(arrayRemoveElementByIndex(data, undefined)).toBeFalsy();
});

test('slice empty array by index', () => {
    expect(arrayRemoveElementByIndex([], 0)).toBeFalsy();
});
