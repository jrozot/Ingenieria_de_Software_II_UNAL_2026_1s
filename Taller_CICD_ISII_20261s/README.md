# Taller 1 CI/CD Ing. de Software II un
**Estudiante:** Juan Mateo Rozo Torres
Se ha desarrollado el taller de acuerdo al enunciado en /docs/taller_cicd.pdf

## Video demo:
![x](/docs/taller1_ingsoft2_vid.mp4)

---
## Capturas de pantalla:
- **Pipeline funcional:**
![x](/docs/img/pipeline.png)
- **Pruebas en Github Actions:**
![x](/docs/img/actions.png)
- **Despliegue en Github Pages:**
![x](/docs/img/ghpages.png)


## Solución del ejercicio endpoint GET:
- Se ha agregado el siguiente código a /src/app.js
```js
app.get('/version', (req, res) => {
  res.json({ version: '1.0.0' });
});
```
- Se ha agregado el siguiente test.
```js
test('GET /version should return version 1.0.0', async () => {
  const response = await request(app).get('/version');
  expect(response.status).toBe(200);
  expect(response.body.version).toBe('1.0.0');
});
```
- **Captura de pantalla:**
![x](/docs/img/GETpng.png)


