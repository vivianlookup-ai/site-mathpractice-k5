import { defineConfig } from "astro/config";
import cloudflare from "@astrojs/cloudflare";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// https://astro.build/config
export default defineConfig({
  site: "https://mathpracticek5.com",
  output: "static",
  adapter: cloudflare({
    imageService: true,
  }),
  vite: {
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src"),
      },
    },
  },
});
