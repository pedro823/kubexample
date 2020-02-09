import express from 'express'
import { getPeople } from './api/handlePeople'
import { getPlaces } from './api/handlePlaces'

const app = express()
{
  app.get('/people', getPeople)
  app.get('/places', getPlaces)
}

app.listen(5000)
