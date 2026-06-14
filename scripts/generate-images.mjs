#!/usr/bin/env node

/**
 * Image generator for Ditto deck using Google Imagen (gemini model)
 * Usage: node scripts/generate-images.mjs "your prompt here" output-filename.jpg
 * Or: node scripts/generate-images.mjs --all  (generates all missing deck images)
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const IMAGES_DIR = path.join(ROOT, 'pm-workspace/specs/ideas/activation-and-audience/images');

// Load API key
const envPath = path.join(ROOT, '.env');
const envContent = fs.readFileSync(envPath, 'utf-8');
const API_KEY = envContent.match(/GOOGLE_API_KEY=['"]*([^'"\n]+)/)?.[1];
if (!API_KEY) { console.error('No GOOGLE_API_KEY found in .env'); process.exit(1); }

// Style prefix applied to all prompts
const STYLE = `35mm analog film photograph, warm golden hour light, shallow depth of field, slight film grain, candid and unposed, warm earth tones with amber and soft blue, European setting, nostalgic and hopeful mood, not clinical or staged`;

// Predefined prompts for missing deck images
const DECK_IMAGES = {
  'gen-hospital-warmth.jpg': `${STYLE}. Two middle-aged people sitting together in a sun-drenched hospital waiting area, holding hands, morning light streaming through large windows. Warm and tender, not sad or clinical. Plants visible. Soft focus background.`,
  'gen-care-circle-garden.jpg': `${STYLE}. Three generations of a family gathered around a garden table in late afternoon golden light — an elderly woman, her adult daughter, and a teenage grandchild. Candid moment, someone is reaching across the table. Dappled light through trees. European terrace setting.`,
};

async function generateImage(prompt, filename) {
  const outputPath = path.join(IMAGES_DIR, filename);

  console.log(`\nGenerating: ${filename}`);
  console.log(`Prompt: ${prompt.substring(0, 120)}...`);

  const response = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-fast-generate-001:predict?key=${API_KEY}`,
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        instances: [{ prompt }],
        parameters: {
          sampleCount: 1,
          aspectRatio: '16:9',
          outputOptions: { mimeType: 'image/jpeg' },
        },
      }),
    }
  );

  if (!response.ok) {
    const err = await response.text();
    console.error(`Error ${response.status}: ${err}`);
    return false;
  }

  const data = await response.json();

  if (!data.predictions?.[0]?.bytesBase64Encoded) {
    console.error('No image data in response:', JSON.stringify(data).substring(0, 300));
    return false;
  }

  const imageBuffer = Buffer.from(data.predictions[0].bytesBase64Encoded, 'base64');
  fs.writeFileSync(outputPath, imageBuffer);
  console.log(`Saved: ${outputPath} (${(imageBuffer.length / 1024).toFixed(0)}KB)`);
  return true;
}

async function main() {
  const args = process.argv.slice(2);

  if (args[0] === '--all') {
    console.log('Generating all missing deck images...');
    for (const [filename, prompt] of Object.entries(DECK_IMAGES)) {
      const outputPath = path.join(IMAGES_DIR, filename);
      if (fs.existsSync(outputPath)) {
        console.log(`Skipping ${filename} (already exists)`);
        continue;
      }
      await generateImage(prompt, filename);
    }
    console.log('\nDone.');
  } else if (args.length >= 2) {
    const prompt = `${STYLE}. ${args[0]}`;
    const filename = args[1];
    await generateImage(prompt, filename);
  } else {
    console.log(`
Usage:
  node scripts/generate-images.mjs "prompt description" output-filename.jpg
  node scripts/generate-images.mjs --all

Style prefix (auto-applied):
  ${STYLE}

Predefined deck images:
${Object.entries(DECK_IMAGES).map(([f, p]) => `  ${f}: ${p.substring(STYLE.length + 2, STYLE.length + 80)}...`).join('\n')}
    `);
  }
}

main().catch(console.error);
