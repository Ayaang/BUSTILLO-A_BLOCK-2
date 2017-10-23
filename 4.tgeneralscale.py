def generalScale(oldimage, widthscale, heighscale):
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()
    newim = EmptyImage(oldw*widthscaleoldh*heightscale)
    for row in range(newim.getHight()):
        for col in range(newim.getWidth()):
            originalCol = col//widthscale
            originalRow = row//heightscale
            oldpixel = oldimage.getPixel(originalCol, originalRow)

            newim.setPixel(col, row, oldpixel)
            
        return newim

            
