# 🧪 Black Box API Challenge – Report

This report documents the reverse-engineered behavior of each mysterious endpoint hosted at [https://blackbox-interface.vercel.app](https://blackbox-interface.vercel.app). Each section includes a different test input and a corresponding analysis.

---

## ✅ 1. POST `/data`

- **Input:** `"python3.11"`
- **Output:** `"InB5dGhvbi4xMSI="`
- **Decoded Result (Base64):** `"python3.11"`

### 📌 Inference:
Encodes the input string using **Base64 encoding**, including double quotes. Acts as a string encoder.

---

## ✅ 2. GET `/time`

- **Output:** `{ "result": 8132707 }`

### 📌 Inference:
Returns a **custom increasing number** — likely a tick counter or session-based increment. Does not match Unix timestamp formats.

---

##  3. POST `/fizzbuzz`

- **Inputs Tried:**
  - `[3, 5, 15]`
  - `["Fizz", "Buzz", "FizzBuzz"]`
  - `[]`

- **Outputs:** Always `{ "result": false }`

### 📌 Inference:
This endpoint may:
- Expect a very specific input format (e.g., array of integers).
- Require internal logic (like multiples of 3 and 5) to pass.
- Still return `false`, possibly as a red herring.

More testing required.

---

## ✅ 4. POST `/zap`

- **Input:** `"OpenAI GPT"`
- **Output:** `"\"OpenAI GPT\""`

### 📌 Inference:
Returns the **JSON-stringified** version of the input — essentially wrapping the input in quotes. Same behavior seen across multiple strings.

---

## ✅ 5. POST `/alpha`

- **Inputs Tried:**
  - `"ONLYCAPS"` → `false`
  - `"onlylower"` → `false`
  - `"Alpha42"` → `false`
  - `"XYZ"` → `false`

### 📌 Inference:
All inputs returned `false`, suggesting:
- The endpoint checks for a **very specific pattern**.
- Could require a specific keyword or internal validation logic.

---

## ✅ 6. POST `/glitch`

- **Input:** `"debug-mode"`
- **Output:** `"\"debug-mode\""`

### 📌 Inference:
Same behavior as `/zap`. The input is echoed with quotes. Possibly aliases or duplicates internally. Useful for verifying text wrapping behavior.

---

## 🔍 Summary Table

| Endpoint     | Behavior Summary                                                       |
|--------------|------------------------------------------------------------------------|
| `/data`      | Base64-encodes the input string with quotes                            |
| `/time`      | Returns a non-standard counter value                                   |
| `/fizzbuzz`  | Returns false for all arrays; exact logic unclear                      |
| `/zap`       | Wraps the input string in quotes (JSON stringify)                      |
| `/alpha`     | Returns false unless input meets unknown strict pattern                |
| `/glitch`    | Same as `/zap`, wraps input in quotes                                  |
