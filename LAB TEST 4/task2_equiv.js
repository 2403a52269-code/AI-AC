
// task2_equiv.js
// Equivalent JavaScript operations to the Python program.

function operations() {
    let data = { a: 1, b: 2, c: 3 };
    // add 'd' as sum of values
    const sum = Object.values(data).reduce((s, v) => s + v, 0);
    data["d"] = sum;
    // increment numeric values by 1
    for (const k of Object.keys(data)) {
        const v = data[k];
        if (Number.isInteger(v)) data[k] = v + 1;
    }
    // remove key 'b'
    delete data["b"];
    // sorted keys array
    const sorted_keys = Object.keys(data).slice().sort();
    // squares of values
    const squares = {};
    for (const k of Object.keys(data)) {
        squares[k] = data[k] * data[k];
    }
    return { data: data, sorted_keys: sorted_keys, squares: squares };
}

function canonicalize(obj) {
    if (Array.isArray(obj)) return obj.map(canonicalize);
    if (obj && typeof obj === 'object') {
        const keys = Object.keys(obj).sort();
        const out = {};
        for (const k of keys) out[k] = canonicalize(obj[k]);
        return out;
    }
    return obj;
}

const result = operations();
console.log(JSON.stringify(canonicalize(result)));
