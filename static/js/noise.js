const noise = () => {
    let canvas, ctx;
    let wWidth, wHeight;
    let noiseData = [];
    let frame = 0;
    let loopTimeout;
    let resizeThrottle;

    // Create Noise
    const createNoise = () => {
        const idata = ctx.createImageData(wWidth, wHeight);
        const buffer32 = new Uint32Array(idata.data.buffer);
        const len = buffer32.length;
        for (let i = 0; i < len; i++) {
            if (Math.random() < 0.5) {
                buffer32[i] = 0xff000000;
            }
        }
        noiseData.push(idata);
    };

    // Paint Noise
    const paintNoise = () => {
        if (frame === 9) {
            frame = 0;
        } else {
            frame++;
        }
        ctx.putImageData(noiseData[frame], 0, 0);
    };

    // Loop
    const loop = () => {
        paintNoise(frame);
        loopTimeout = window.setTimeout(() => {
            window.requestAnimationFrame(loop);
        }, (1000 / 25));
    };

    // Setup
    const setup = () => {
        wWidth = window.innerWidth;
        wHeight = window.innerHeight;
        canvas.width = wWidth;
        canvas.height = wHeight;
        noiseData = []; // Clear existing noise data
        for (let i = 0; i < 10; i++) {
            createNoise();
        }
        loop();
    };

    // Reset on window resize
    const reset = () => {
        window.addEventListener('resize', () => {
            window.clearTimeout(resizeThrottle);
            resizeThrottle = window.setTimeout(() => {
                window.clearTimeout(loopTimeout);
                setup();
            }, 200);
        }, false);
    };

    // Initialize
    const init = () => {
        canvas = document.getElementById('noise');
        if (!canvas) return; // Safety check
        ctx = canvas.getContext('2d');
        setup();
        reset();
    };

    // Clean up function
    const cleanup = () => {
        window.clearTimeout(loopTimeout);
        window.clearTimeout(resizeThrottle);
    };

    return {
        init,
        cleanup
    };
};

// Start noise effect when page loads
window.addEventListener('load', () => {
    const noiseEffect = noise();
    noiseEffect.init();

    // Clean up when page unloads
    window.addEventListener('unload', noiseEffect.cleanup);
});