## Background

This is a Raspberry Pi project that works directly with one of my Arduino projects: [Ar-Starbug](https://github.com/projectweekend/Ar-Starbug). These two projects combine to replace two older ones: [Pi-Starbug](https://github.com/projectweekend/Pi-Starbug) and [Pi-Nova-5](https://github.com/projectweekend/Pi-Nova-5). The sensor logic for each older project has been moved off of a Raspberry Pi and onto an Arduino. This new structure:

* Let's the Arduino do what it does best: run a small, fast loop and read data from various sensors. It can communicate with the Raspberry Pi using both digital GPIO pins and serial when needed.
* Frees up one of my Raspberry Pis. Instead of using two, now I only need one. Also since this project is designed to report the data it collects back to another [project](https://github.com/projectweekend/Holly), the Pi is a perfect fit. Connecting an Arduino to the internet and sending/receiving data is misreably tedious in my opinion. The Pi does a much better job.

## Project Info

This project is in the process of being reorganized/rewritten to use a messaging queue to fully decouple its communication components from another project: [Holly](https://github.com/projectweekend/Holly). Once everything has settled, I'll refresh this section to include some more meaningful information.

