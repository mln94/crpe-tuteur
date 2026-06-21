import express from 'express';
import cors from 'cors';
import path from 'path';
import { fileURLToPath } from 'url';
import Anthropic from '@anthropic-ai/sdk';
import { config } from 'dotenv';

config();

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const isProd = process.env.NODE_ENV === 'production';

const app = express();
app.use(cors());
app.use(express.json({ limit: '200kb' }));

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

/* ── API ── */
app.post('/api/chat', async (req, res) => {
  const { messages, system } = req.body;

  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');

  try {
    const stream = client.messages.stream({
      model: 'claude-sonnet-4-6',
      max_tokens: 2000,
      system: [{ type: 'text', text: system, cache_control: { type: 'ephemeral' } }],
      messages,
    });

    stream.on('text', (text) => {
      res.write(`data: ${JSON.stringify({ text })}\n\n`);
    });

    await stream.finalMessage();
    res.write('data: [DONE]\n\n');
    res.end();
  } catch (err) {
    console.error('[API error]', err.message);
    res.write(`data: ${JSON.stringify({ error: err.message })}\n\n`);
    res.write('data: [DONE]\n\n');
    res.end();
  }
});

/* ── Static (dev local uniquement — sur Vercel ces fichiers sont servis directement depuis dist/) ── */
app.use(express.static(path.join(__dirname, 'landing')));

if (isProd) {
  app.use('/app', express.static(path.join(__dirname, 'dist/app')));
  app.get('/app/*', (_, res) =>
    res.sendFile(path.join(__dirname, 'dist/app/index.html'))
  );
}

app.get('/', (_, res) =>
  res.sendFile(path.join(__dirname, 'landing/index.html'))
);

export default app;
