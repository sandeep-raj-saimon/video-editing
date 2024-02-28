const Jimp = require('jimp')
const ffmpeg = require('fluent-ffmpeg')
const fs = require('fs')
const path = require('path')

const outputDir = './output'
const baseImagePath = 'Prod/Devotion/Images/0f96ef85dc103d9bfd35f0757c3b0a41.jpg' // Specify your base image path here
const totalFrames = 60 // Total number of frames for the animation
const videoOutputPath = path.join(outputDir, 'text_slide_video.mp4')

// Ensure the output directory exists
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true })
}

async function createFrame(frameIndex) {
  const image = await Jimp.read(baseImagePath)
  const font = await Jimp.loadFont(Jimp.FONT_SANS_32_BLACK)
  const text = 'शुभ मंगलवार' // Customize your text here
  const textWidth = Jimp.measureText(font, text)
  const textHeight = Jimp.measureTextHeight(font, text, textWidth)

  // Calculate the X position for the text to simulate sliding in
  const startX = -textWidth + (frameIndex * (image.bitmap.width + textWidth) / totalFrames)
  const startY = (image.bitmap.height - textHeight) / 2 // Center the text vertically

  image.print(font, startX, startY, text)

  await image.writeAsync(path.join(outputDir, `frame_${frameIndex}.jpg`))
}

async function createVideo() {
  // Create the frames
  for (let i = 0; i < totalFrames; i++) {
    await createFrame(i)
  }

  // Use ffmpeg to create a video from the frames
  ffmpeg()
    .input(path.join(outputDir, 'frame_%d.jpg'))
    .inputFPS(25)
    .output(videoOutputPath)
    .outputFPS(25)
    .on('end', () => console.log('Video creation completed.'))
    .run()
}

createVideo().catch(console.error)
