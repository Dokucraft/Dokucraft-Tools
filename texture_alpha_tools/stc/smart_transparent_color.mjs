import sharp from 'sharp'

const { data: inpx, info } = await sharp(process.argv[2]).ensureAlpha().raw().toBuffer({ resolveWithObject: true })

// Find the edge pixels in the input image
const scpx = Buffer.alloc(info.width*info.height*5)
let scpxCount = 0
for (let i = 0; i < inpx.length; i += 4) {
  const x = (i / 4) % info.width
  const y = Math.floor(i / 4 / info.width)
  if (inpx[i+3] > 127 && ((x < info.width - 1 && inpx[i+4+3] <= 127) || (x > 0 && inpx[i-4+3] <= 127) || (y < info.height - 1 && inpx[i+info.width*4+3] <= 127) || (y > 0 && inpx[i-info.width*4+3] <= 127))) {
    const si = scpxCount * 5
    scpx[si] = x
    scpx[si+1] = y
    inpx.copy(scpx, si+2, i, i+3)
    scpxCount++
  }
}

// Create a new buffer to store the pixels of the output
const btpx = Buffer.alloc(inpx.length)

// Calculate the color for each pixel in the output
for (let x = 0; x < info.width; x++) for (let y = 0; y < info.height; y++) {
  const i = x + y * info.width

  // If this pixel is not transparent in the input image, just use that color
  if (inpx[i*4+3] > 127) {
    inpx.copy(btpx, i*4, i*4, i*4+4)
    continue
  }

  // The color is based on the inverse squared distance to all of the colored pixels from the input image
  let ratioSum = 0,
      rs = 0,
      gs = 0,
      bs = 0
  for (let j = 0; j < scpxCount * 5; j += 5) {
    const r = 1 / Math.max(1, Math.pow(Math.sqrt((x - scpx[j]) * (x - scpx[j]) + (y - scpx[j+1]) * (y - scpx[j+1])), 2))
    ratioSum += r
    rs += scpx[j+2] * r
    gs += scpx[j+3] * r
    bs += scpx[j+4] * r
  }
  btpx[i*4]   = rs / ratioSum
  btpx[i*4+1] = gs / ratioSum
  btpx[i*4+2] = bs / ratioSum
  btpx[i*4+3] = inpx[i*4+3]
}

await sharp(btpx, {
  raw: {
    width: info.width,
    height: info.height,
    channels: 4
  }
}).png().toFile(process.argv[2])