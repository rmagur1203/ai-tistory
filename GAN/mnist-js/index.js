generate.addEventListener('click', async () => {
    document.getElementsByTagName('canvas').forEach(canvas => canvas.remove());
    const model = await tf.loadLayersModel('./generator/model.json');
    const noise = tf.randomNormal([1, 256]);
    const img = model.predict(noise);
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = 28;
    canvas.height = 28;
    canvas.style.width = '100%';
    canvas.style.maxWidth = '200px';
    ctx.imageSmoothingEnabled = false;
    const imageData = ctx.createImageData(28, 28);
    const data = await img.data();
    for (let i = 0; i < data.length; i++) {
        imageData.data[i * 4] = data[i] * 255;
        imageData.data[i * 4 + 1] = data[i] * 255;
        imageData.data[i * 4 + 2] = data[i] * 255;
        imageData.data[i * 4 + 3] = 255;
    }
    ctx.putImageData(imageData, 0, 0);
    document.body.appendChild(canvas);
});