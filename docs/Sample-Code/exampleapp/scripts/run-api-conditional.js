// scripts/run-api-conditional.js
// Run the API based on the BACKEND_LOCAL_PORT defined in the .env file
// 2025-07-08 | CR

const path = require('path');
const fs = require('fs');
const { execSync } = require('child_process');
const dotenv = require('dotenv');

// Function to load .env file
function loadEnv(appPath) {
  const envPath = path.resolve(appPath, '.env');
  if (fs.existsSync(envPath)) {
    const envConfig = dotenv.parse(fs.readFileSync(envPath));
    return envConfig;
  }
  return {};
}

// Read 
const turboCommand = process.env.TURBO_COMMAND || 'pnpx turbo watch dev';

// Define paths to your apps
const uiAppPath = path.resolve(__dirname, '../apps/ui');
const fastapiAppPath = path.resolve(__dirname, '../apps/api-fastapi');
const flaskAppPath = path.resolve(__dirname, '../apps/api-flask');
const chaliceAppPath = path.resolve(__dirname, '../apps/api-chalice');
const mcpAppPath = path.resolve(__dirname, '../apps/mcp-server');


// Load .env variables for each app
const uiEnv = loadEnv(uiAppPath);
const fastapiEnv = loadEnv(fastapiAppPath);
const flaskEnv = loadEnv(flaskAppPath);
const chaliceEnv = loadEnv(chaliceAppPath);
const mcpEnv = loadEnv(mcpAppPath);

const uiPort = uiEnv.BACKEND_LOCAL_PORT;
const fastapiPort = fastapiEnv.BACKEND_LOCAL_PORT;
const flaskPort = flaskEnv.BACKEND_LOCAL_PORT;
const chalicePort = chaliceEnv.BACKEND_LOCAL_PORT;
const mcpPort = mcpEnv.BACKEND_LOCAL_PORT;

let apiToRun = null;

if (!uiPort) {
  console.error("❌ Error: BACKEND_LOCAL_PORT is not defined in apps/ui/.env");
  process.exit(1);
}

console.log(`🔍 UI's BACKEND_LOCAL_PORT: ${uiPort}`);
console.log(`🔍 FastAPI's BACKEND_LOCAL_PORT: ${fastapiPort}`);
console.log(`🔍 Flask's BACKEND_LOCAL_PORT: ${flaskPort}`);
console.log(`🔍 Chalice's BACKEND_LOCAL_PORT: ${chalicePort}`);
console.log(`🔍 MCP's BACKEND_LOCAL_PORT: ${mcpPort}`);

if (uiPort === fastapiPort) {
  apiToRun = 'api-fastapi';
} else if (uiPort === flaskPort) {
  apiToRun = 'api-flask';
} else if (uiPort === chalicePort) {
  apiToRun = 'api-chalice';
} else {
  console.error(`⚠️ No API found with matching BACKEND_LOCAL_PORT for UI (${uiPort}).`);
  process.exit(1);
}

// Run the apps/ui and the apps/api-[conditional]
const command = `${turboCommand} --filter=./apps/ui --filter=./apps/mcp-server --filter=./apps/${apiToRun}`;

console.log(`🚀 Running Turborepo command: ${command}`);

try {
  execSync(command, { stdio: 'inherit' });
} catch (error) {
  console.error(`❌ Turborepo command failed: ${error.message}`);
  process.exit(error.status || 1);
}
