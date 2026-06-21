import app from './app.js';

const isProd = process.env.NODE_ENV === 'production';
const PORT = process.env.PORT || 3001;

app.listen(PORT, () => {
  console.log(`CRPE Tuteur API  →  http://localhost:${PORT}`);
  if (isProd) console.log(`CRPE App         →  http://localhost:${PORT}/app`);
});
