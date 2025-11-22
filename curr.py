server.js
const express = require('express');
const fetch = require('node-fetch');
const sqlite3 = require('sqlite3').verbose();
const app = express();
const PORT = process.env.PORT || 3000;
const API_BASE = 'https://api.exchangerate.host/convert';

const db = new sqlite3.Database('./exchange.db', (err) => {
  if (err) console.error(err.message);
  else console.log('SQLite DB connected.');
});

db.serialize(() => {
  db.run(`
    CREATE TABLE IF NOT EXISTS conversions (
      id INTEGER PRIMARY KEY,
      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
      from_currency TEXT,
      to_currency TEXT,
      amount REAL,
      result REAL,
      rate REAL
    )
  `);
});

app.get('/convert', async (req, res) => {
  const { from, to, amount } = req.query;

  if (!from || !to || !amount || isNaN(amount)) {
    return res.status(400).json({ error: "Missing or invalid 'from', 'to', or 'amount'" });
  }

  try {
    const response = await fetch(`${API_BASE}?from=${from}&to=${to}&amount=${amount}`);
    const data = await response.json();

    if (!data.success) {
      return res.status(502).json({ error: "Failed to fetch from external API", details: data });
    }

    const { result, info } = data;
    const rate = info?.quote ?? (result / parseFloat(amount));

    db.run(
      `INSERT INTO conversions (from_currency, to_currency, amount, result, rate)
       VALUES (?, ?, ?, ?, ?)`,
      [from, to, amount, result, rate],
      function(err) {
        if (err) console.error("DB Insert Error:", err.message);
      }
    );

    res.json({ success: true, from, to, amount, rate, result });

  } catch (err) {
    console.error("Fetch Error:", err);
    res.status(500).json({ error: "Internal server error" });
  }
});

app.listen(PORT, () => console.log(`Server running: http://localhost:${PORT}`));
