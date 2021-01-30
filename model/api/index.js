const tfjs =  require('@tensorflowjs/tfjs')
const tfjs =  require('@tensorflow/tfjs-automl')

async function run() {
    const model = await tf.automl.loadImageClassification('model.json');
    const image = document.getElementById('daisy');
    const predictions = await model.classify(image);
    console.log(predictions);
    // Show the resulting object on the page.
    const pre = document.createElement('pre');
    pre.textContent = JSON.stringify(predictions, null, 2);
    document.body.append(pre);
}

run();