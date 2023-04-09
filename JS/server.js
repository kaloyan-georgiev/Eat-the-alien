const express = require('express')
const app = express()
const port = 3000
const path = require('path')
const pug = require('pug')
const fs = require('fs')
app.use(express.static(path.join(__dirname, 'public')))
const scoresTemplate = pug.compileFile(path.join(__dirname, "scores_template.pug"))


app.get('/', (req, res) => {
  res.send('')
})


app.get('/scores', (req, res) => {
  let rawdata = fs.readFileSync("scores.json")
  let scores = JSON.parse(rawdata)
  res.send(scoresTemplate(scores))
})


app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})