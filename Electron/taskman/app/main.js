const {
  app,
  BrowserWindow
} = require('electron')

let win

function createWindow() {
  win = new BrowserWindow({
    width: 1020,
    height: 800,
    frame: false
  })

  win.loadURL(`file://${__dirname}/view/index.html`)
  //win.webContents.openDevTools()

  win.on('closed', () => {
    win = null
  })
}

app.on('ready', createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (win === null) {
    createWindow()
  }
})