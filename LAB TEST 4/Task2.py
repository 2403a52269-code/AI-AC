import json
import subprocess
import shutil
from pathlib import Path

# Convert a Python dictionary manipulation program into equivalent JavaScript,
# run both, and compare outputs to verify correctness.


def python_operations():
    # original Python dictionary manipulations
    data = {"a": 1, "b": 2, "c": 3}
    # add 'd' as sum of values
    data["d"] = sum(data.values())
    # increment each numeric value by 1
    for k, v in list(data.items()):
        if isinstance(v, int):
            data[k] = v + 1
    # remove key 'b'
    data.pop("b", None)
    # sorted keys list
    sorted_keys = sorted(data.keys())
    # squares of values
    squares = {k: data[k] * data[k] for k in data}

    final = {
        "data": data,
        "sorted_keys": sorted_keys,
        "squares": squares
    }
    return final

def canonicalize(obj):
    # recursively sort dict keys so JSON output is deterministic and comparable
    if isinstance(obj, dict):
        return {k: canonicalize(obj[k]) for k in sorted(obj.keys())}
    if isinstance(obj, list):
        return [canonicalize(x) for x in obj]
    return obj

def json_out(obj):
    return json.dumps(canonicalize(obj), separators=(',', ':'), ensure_ascii=False)

JS_CODE = r'''
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
'''

def write_js(path: Path):
    path.write_text(JS_CODE, encoding="utf-8")
    return path

def run_node(js_path: Path):
    node = shutil.which("node")
    if not node:
        raise FileNotFoundError("Node.js not found in PATH")
    completed = subprocess.run([node, str(js_path)], capture_output=True, text=True, check=True)
    return completed.stdout.strip()

def main():
    py_result = python_operations()
    py_json = json_out(py_result)

    js_path = Path(__file__).with_name("task2_equiv.js")
    write_js(js_path)

    try:
        js_stdout = run_node(js_path)
    except FileNotFoundError:
        print("Node.js not found. Wrote JavaScript to:", js_path)
        print("Python output:")
        print(py_json)
        return
    except subprocess.CalledProcessError as e:
        print("Error running Node.js:", e.stderr)
        return

    # Node printed canonical JSON using JSON.stringify on sorted object keys
    js_json = js_stdout

    print("Python JSON:")
    print(py_json)
    print("JavaScript JSON:")
    print(js_json)

    if py_json == js_json:
        print("OK: Outputs match")
    else:
        print("MISMATCH: Outputs differ")

if __name__ == "__main__":
    main()