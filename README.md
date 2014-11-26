This project is dead, but I kept the empty repository around to preserve some history of how things evolved here. While rewriting some parts of this to use a messaging queue, and fully decouple its communication components from another project ([Holly](https://github.com/projectweekend/Holly)), I realized things needed to be broken down even further. Instead of having multiple services here in one place, it made more sense to separate items. Keeping each one small and focused made them more flexible and reusable.

--------------------------------------------------------------------------------------------

## Background

This is a Raspberry Pi project that works directly with one of my Arduino projects: [Ar-Starbug](https://github.com/projectweekend/Ar-Starbug). These two projects combine to replace two older ones: [Pi-Starbug](https://github.com/projectweekend/Pi-Starbug) and [Pi-Nova-5](https://github.com/projectweekend/Pi-Nova-5). The sensor logic for each older project has been moved off of a Raspberry Pi and onto an Arduino. This new structure:

* Let's the Arduino do what it does best: run a small, fast loop and read data from various sensors. It can communicate with the Raspberry Pi using both digital GPIO pins and serial when needed.
* Frees up one of my Raspberry Pis. Instead of using two, now I only need one. Also since this project is designed to collect and report data for another [project](https://github.com/projectweekend/Holly), the Pi is a perfect fit. Connecting an Arduino to the internet and sending/receiving data is misreably tedious in my opinion. The Pi does a much better job.
