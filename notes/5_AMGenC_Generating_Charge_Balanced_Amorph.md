---
title: "AMGenC: Generating Charge Balanced Amorphous Materials"
source: "https://arxiv.org/pdf/2604.27613v1"
captured_by: "sandipde"
date: 2026-10-09
issue: 5
---

# AMGenC: Generating Charge Balanced Amorphous Materials

- **Captured by:** @sandipde
- **Source:** https://arxiv.org/pdf/2604.27613v1

## Abstract
Amorphous (disordered) materials are solids that have shown great potential in various domains, including energy storage, thermal management, and advanced materials. Unlike crystalline materials that can be described by unit cells containing a few to hundreds of atoms, amorphous materials require larger simulation cells with at least hundreds to thousands of atoms. To advance the design of amorphous materials with desired properties and facilitate the exploration of their vast design space, generative inverse design has emerged as a promising approach. It aims to directly output materials with properties closely aligned with the desired ones using probabilistic generative models conditioned on desired properties, which can be more resource efficient than the traditional trial-and-error approach. However, due to the inherent stochasticity of probabilistic generative models, when element assignments are unconstrained, a large portion of generated materials may be charge unbalanced, and no existing methods can effectively mitigate this limitation. In this work, we propose AMGenC, a new generative inverse design method for amorphous materials that can guarantee the generation of charge balanced samples, with minimal additional computational overhead and without sacrificing inverse design accuracy. AMGenC achieves this through an element noise that gives the generation process a starting point centered around charge balance, and the combination of a per-step soft projection and a final discrete projection for steering the elements toward exact charge balance throughout the generation. We perform extensive experiments on two amorphous materials datasets. Experimental results provide evidence that AMGenC achieves its design goal.
