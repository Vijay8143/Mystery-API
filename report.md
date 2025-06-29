# 🧪 Black Box API Challenge – Report

This report documents the reverse-engineered behavior of each mysterious endpoint hosted at [https://blackbox-interface.vercel.app](https://blackbox-interface.vercel.app). Each section includes a different test input and a corresponding analysis.

---

## ✅ 1. POST `/data`

- **Input:** `"python3.11"`
- **Output:** `"cHl0aG9uMy4xMQ=="`
- **Decoded Result (Base64):** `"python3.11"`

### 📌 Inference:
Encodes the input string using **Base64 encoding**. No additional wrapping or formatting is applied. It’s a straightforward string encoder.

---

## ✅ 2. GET `/time`

- **Output:** `{ "result": 8132707 }`

### 📌 Inference:
Returns a **countdown in seconds** to a preset future timestamp (approximately 95 days from server start). The number **decreases** over time — unlike Unix timestamps, which increase.

---

## ✅ 3.POST `/fizzbuzz`

- **Inputs Tried:**
  - `[1, 2, 3]`
  - `["Fizz", "Buzz"]`
  - `[{}]`
  - `[]`
  - `[true, false]`
  - `[ "__proto__", "constructor" ]`

- **Output:** Always
  ```json
  { "result": false }
  ```

### 📌 Inference:
Always returns `false`, even for valid JSON arrays. Input structure (length, type, or content) has no effect — likely designed as a **red herring** or placeholder logic.

---

## ✅ 4. POST `/zap`

- **Input:** `"Z@p-123!"`
- **Output:** `"Z@p-!"`

### 📌 Inference:
Removes all **numeric digits** from the input string. Symbols, letters, and punctuation are preserved.

---

## ✅ 5. POST `/alpha`

- **Inputs Tried:**
  - `"Gadget007"` → `true`
  - `"4ward"` → `false`
  - `"@mention"` → `false`
  - `"banana"` → `true`
  - `"99balloons"` → `false`

### 📌 Inference:
- Returns `true` **only if the first character is a letter** (A–Z or a–z)
- Returns `false` for digits, symbols, or special characters at the beginning
- Case-insensitive logic — both uppercase and lowercase letters pass

---

## ✅ 6. POST `/glitch`

- **Input (odd-length):** `"glitchy"`
- **Output:** `"yhctilg"`

- **Input (even-length):** `"shuffle"`
- **Output:** `"hesuflf"` *(example; result varies)*

### 📌 Inference:
- If the input string has an **odd number of characters**, it is **reversed**
- If the input string has an **even number of characters**, it is **shuffled randomly**
- The behavior is deterministic based on character count, not content

---

## 🔍 Summary Table

| Endpoint     | Behavior Summary                                                       |
|--------------|------------------------------------------------------------------------|
| `/data`      | Base64-encodes the input string                                        |
| `/time`      | Returns a countdown (seconds) to a future timestamp                    |
| `/fizzbuzz`  | Returns `false` for every input array(hypothesis)           |
| `/zap`       | Removes all numeric digits from input                                  |
| `/alpha`     | `true` if first char is a letter; `false` otherwise                    |
| `/glitch`    | Reverses if odd-length; shuffles if even-length                        |

