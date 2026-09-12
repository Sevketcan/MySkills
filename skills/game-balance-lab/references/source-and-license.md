# Sources and licenses

The workflow was informed by these public skills:

1. **game-balance** and **systems-economy-design** by David Smereski
   - Repository: https://github.com/DSmereski/agent-skills
   - Reviewed commit: `7eb549e65c1bd6bba546c0250f8a8641459e5292`
   - License: MIT
   - Ideas retained: measurable target bands, simulations before feel checks, controlled knob sweeps, and explicit source/sink/feedback-loop audits.
2. **godot-monte-carlo-balancer** by thedivergentai contributors
   - Repository: https://github.com/thedivergentai/GD-Agentic-Skills
   - Reviewed commit: `4c4d0ff5c4597938cc9257d99d9e35f7692c9c06`
   - License: LGPL-3.0
   - High-level inspiration: seeded Monte Carlo matrices, player-policy modeling, confidence-aware verdicts, career simulations, calibration, and reproducible snapshots. Godot/Rust-specific code and fixed target bands were not copied.

The runner and Codex-native instructions in this package are original adaptations. They avoid engine-specific assumptions and universal “healthy” thresholds.

## MIT notice for adapted Smereski material

Copyright (c) 2026 David Smereski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
