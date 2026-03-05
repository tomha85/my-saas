const express = require('express');
const router = express.Router();

// Define the GET /version endpoint
router.get('/version', (req, res) => {
    res.json({ version: '0.0.1' });
});

module.exports = router;