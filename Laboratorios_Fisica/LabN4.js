// Ulises Nahuel Choiman Zambrana

let x, y; 
let vx, vy; 
let tiempoInicio; 
let pausado = true; 
let alturaMaxima = 0; 
let rapidezMaxima = 0; 
let tiempoTranscurrido = 0; 
let tiempoPausa = 0;
let escala = 2;
let gravedad = 9.8; 
let origenX, origenY;
let trayectoria = []; // Array para almacenar puntos de la trayectoria

// Variables para los controles de interfaz
let velocidadSlider, anguloSlider;
let iniciarBtn, pausarBtn, reiniciarBtn;

let posXSpan, posYSpan, rapidezXSpan, rapidezYSpan, rapidezTotalSpan;
let acelXSpan, acelYSpan, alturaMaxSpan, rapidezMaxSpan, tiempoSpan;

function setup() {
  createCanvas(800, 800);
  
  origenX = 50;
  origenY = height - 20;
  
  crearControles();
  
  reiniciarSimulacion();
}

function draw() {
  background(240);
  
  stroke(0);
  strokeWeight(2);
  line(0, origenY, width, origenY);
  
  
  drawEjes();  
  dibujarTrayectoria();
  
  if (!pausado) {
    actualizarSimulacion();
  }
  
  
  fill(255, 0, 0);
  noStroke();
  let dibujoX = origenX + x * escala;
  let dibujoY = origenY - y * escala;
  ellipse(dibujoX, dibujoY, 15, 15);
  

  actualizarDatos();
}

function drawEjes() {
  // Eje Y 
  stroke(100);
  strokeWeight(1);
  line(origenX, origenY, origenX, 50);
  
  // Eje X 
  line(origenX, origenY, width - 50, origenY);
  
  
  for (let i = 0; i <= (width - origenX - 50) / escala; i += 25) {
    line(origenX + i * escala, origenY - 5, origenX + i * escala, origenY + 5);
    fill(0);
    noStroke();
    textAlign(CENTER);
    text(i + 'm', origenX + i * escala, origenY + 20);
  }
  
  for (let i = 0; i <= (origenY - 50) / escala; i += 25) {
    line(origenX - 5, origenY - i * escala, origenX + 5, origenY - i * escala);
    fill(0);
    noStroke();
    textAlign(RIGHT);
    text(i + 'm', origenX - 10, origenY - i * escala + 5);
  }
}

function dibujarTrayectoria() {
  if (trayectoria.length > 1) {
    stroke(0, 0, 255, 150);
    strokeWeight(2);
    noFill();
    beginShape();
    for (let punto of trayectoria) {
      vertex(origenX + punto.x * escala, origenY - punto.y * escala);
    }
    endShape();
  }
}

function actualizarSimulacion() {
  tiempoTranscurrido = (millis() - tiempoInicio - tiempoPausa) / 1000;
  
  x = vx * tiempoTranscurrido;
  y = vy * tiempoTranscurrido - 0.5 * gravedad * tiempoTranscurrido * tiempoTranscurrido;
  
  
  let velocidadY = vy - gravedad * tiempoTranscurrido;
  let velocidadTotal = sqrt(vx * vx + velocidadY * velocidadY);
  
  if (y > alturaMaxima) {
    alturaMaxima = y;
  }
  
  if (velocidadTotal > rapidezMaxima) {
    rapidezMaxima = velocidadTotal;
  }
  
  
  if (frameCount % 3 === 0) {
    trayectoria.push({x: x, y: y});
  }
  

  if (y < 0) {
    pausado = true;
    y = 0;
  }
}

function actualizarDatos() {
  
  let velocidadYActual = vy - gravedad * tiempoTranscurrido;
  let velocidadTotalActual = sqrt(vx * vx + velocidadYActual * velocidadYActual);
  
  // Actualizar los valores para el apartado de Datos de Simulacion
  posXSpan.html(x.toFixed(2) + ' m');
  posYSpan.html(y.toFixed(2) + ' m');
  rapidezXSpan.html(vx.toFixed(2) + ' m/s');
  rapidezYSpan.html(velocidadYActual.toFixed(2) + ' m/s');
  rapidezTotalSpan.html(velocidadTotalActual.toFixed(2) + ' m/s');
  acelXSpan.html('0.00 m/s²');
  acelYSpan.html((-gravedad).toFixed(2) + ' m/s²');
  alturaMaxSpan.html(alturaMaxima.toFixed(2) + ' m');
  rapidezMaxSpan.html(rapidezMaxima.toFixed(2) + ' m/s');
  tiempoSpan.html(tiempoTranscurrido.toFixed(2) + ' s');
}

function reiniciarSimulacion() {
  
  let velocidad = velocidadSlider.value();
  let angulo = anguloSlider.value();
  
  let anguloRadianes = radians(angulo);
  
  vx = velocidad * cos(anguloRadianes);
  vy = velocidad * sin(anguloRadianes);
  
  x = 0;
  y = 0;
  tiempoInicio = millis();
  tiempoPausa = 0;
  tiempoTranscurrido = 0;
  alturaMaxima = 0;
  rapidezMaxima = velocidad; // La rapidez inicial es la máxima si no hay resistencia del aire
  trayectoria = [];
  
  pausado = true;
}

function pausarReanudar() {
  if (pausado) {
    tiempoInicio = millis() - tiempoTranscurrido * 1000 - tiempoPausa;
    pausado = false;
  } else {
    // Si estaba ejecutándose, pausar
    tiempoPausa = millis() - tiempoInicio - tiempoTranscurrido * 1000;
    pausado = true;
  }
}

function crearControles() {
  
  createElement('h1', 'Simulación de Tiro Parabólico').position(140, -10);
  
  createElement('h3', 'Controles').position(60, 50);
  
  createElement('label', 'Velocidad inicial (m/s):').position(60, 100);
  velocidadSlider = createSlider(10, 100, 50);
  velocidadSlider.position(210, 100);
  velocidadSlider.size(150);
  
  createElement('label', 'Ángulo (grados):').position(60, 130);
  anguloSlider = createSlider(0, 90, 45);
  anguloSlider.position(210, 130);
  anguloSlider.size(150);
  
  iniciarBtn = createButton('Iniciar Simulación');
  iniciarBtn.position(60, 170);
  iniciarBtn.mousePressed(() => {
    reiniciarSimulacion();
    pausado = false;
  });
  
  pausarBtn = createButton('Pausar/Reanudar');
  pausarBtn.position(190, 170);
  pausarBtn.mousePressed(pausarReanudar);
  
  reiniciarBtn = createButton('Reiniciar');
  reiniciarBtn.position(320, 170);
  reiniciarBtn.mousePressed(() => {
    reiniciarSimulacion();
    pausado = true;
  });
  
  
  createElement('h3', 'Datos de la Simulación').position(450, 60);
  
  createElement('p', 'Posición horizontal (x):').position(450, 100);
  posXSpan = createSpan('0.00 m');
  posXSpan.position(650, 115);
  
  createElement('p', 'Posición vertical (y):').position(450, 140);
  posYSpan = createSpan('0.00 m');
  posYSpan.position(650, 155);
  
  createElement('p', 'Rapidez horizontal:').position(450, 180);
  rapidezXSpan = createSpan('0.00 m/s');
  rapidezXSpan.position(650, 190);
  
  createElement('p', 'Rapidez vertical:').position(450, 220);
  rapidezYSpan = createSpan('0.00 m/s');
  rapidezYSpan.position(650, 230);
  
  createElement('p', 'Rapidez total:').position(450, 260);
  rapidezTotalSpan = createSpan('0.00 m/s');
  rapidezTotalSpan.position(650, 270);
  
  createElement('p', 'Aceleración horizontal:').position(450, 300);
  acelXSpan = createSpan('0.00 m/s²');
  acelXSpan.position(650, 310);
  
  createElement('p', 'Aceleración vertical:').position(450, 340);
  acelYSpan = createSpan('0.00 m/s²');
  acelYSpan.position(650, 350);
  
  createElement('p', 'Altura máxima:').position(450, 380);
  alturaMaxSpan = createSpan('0.00 m');
  alturaMaxSpan.position(650, 390);
  
  createElement('p', 'Rapidez máxima:').position(450, 420);
  rapidezMaxSpan = createSpan('0.00 m/s');
  rapidezMaxSpan.position(650, 430);
  
  createElement('p', 'Tiempo transcurrido:').position(450, 460);
  tiempoSpan = createSpan('0.00 s');
  tiempoSpan.position(650, 470);
}