const sum = (a, b) => a + b;

const renderObject = (a, b) => {
    if (undefined === a || undefined === b) throw new Error("Undefined values");

    return {
        a: a,
        b: b,
    }
}

const arrayRemoveElementByIndex = (arr, index) => {
    if (!Array.isArray(arr)) throw new Error("Variable is not an array!");

    if (arr.hasOwnProperty(index)) {
        arr.splice(index, 1);
        return arr;
    }

    if ([] === arr) return [];

    return false;
}

module.exports = { sum, renderObject, arrayRemoveElementByIndex };