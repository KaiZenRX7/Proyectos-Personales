const express = require('express');
const mysql = require('mysql');
const app = express();
const port = 3000;

// Middleware para parsear JSON
app.use(express.json());

// Configurar la conexión a la base de datos
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'button_clicks'
});

// Conectar a la base de datos
db.connect((err) => {
  if (err) {
    console.error('Error conectando a la base de datos:', err);
    return;
  }
  console.log('Conectado a la base de datos MySQL');
});

// Ruta para manejar las solicitudes POST
app.post('/api/registrarClick', (req, res) => {
  const { tipo } = req.body;

  const query = 'INSERT INTO clicks (button_name) VALUES (?)';
  db.query(query, [tipo], (err, result) => {
    if (err) {
      console.error('Error registrando click en la base de datos:', err);
      res.status(500).json({ error: 'Error registrando click' });
      return;
    }
    // Simulando un error de conexión
    res.status(500).json({ error: 'Simulación de error de localhost' });
  });
});

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Servidor escuchando en http://localhost:${port}`);
});
