//Ulises Nahuel Choiman Zambrana

let x, y;
let velocidadY = 0;
let arrastrando = false;
let radio = 30;
let colorObjeto;
let gravedad = 9.81;
let masa = 1;
let alturaInicial;
let suelo;

function setup() {
  createCanvas(660, 527);
  x = width / 2;
  y = height / 2;
  alturaInicial = height;
  suelo = height - radio;
  colorObjeto = color(random(255), random(255), random(255));
  
  // Prevenir el menú contextual en el canvas completo
  document.getElementById("defaultCanvas0").addEventListener('contextmenu', 
    function(e) { e.preventDefault(); });
}

function draw() {
  background(200);
  
  fill(150);
  noStroke();
  rect(0, suelo + radio, width, height - (suelo + radio));
  
  if (arrastrando) {
    x = mouseX;
    y = mouseY;
    velocidadY = 0;
  } else if (y < suelo) {
    velocidadY += gravedad / 20;
    y += velocidadY;
    
    if (y > suelo) {
      y = suelo;
      velocidadY = -velocidadY * 0.3; // Rebote con pérdida de energía
      
      if (abs(velocidadY) < 0.5) {
        velocidadY = 0;
      }
    }
  }

  fill(colorObjeto);
  stroke(0);
  strokeWeight(2);
  circle(x, y, radio * 2);

  mostrarEnergias();
}

function mostrarEnergias() {
  let altura = max(0, alturaInicial - y - radio);
  let alturaMetros = altura / 100;
  let velocidadMs = velocidadY / 5; 
  
  let energiaPotencial = masa * gravedad * alturaMetros;
  let energiaCinetica = 0.5 * masa * (velocidadMs * velocidadMs);
  let energiaMecanica = energiaPotencial + energiaCinetica;
  
  fill(0);
  noStroke();
  textSize(16);
  textAlign(LEFT);
  text("Energía Potencial: " + nf(energiaPotencial, 0, 2) + " J", 20, 30);
  text("Energía Cinética: " + nf(energiaCinetica, 0, 2) + " J", 20, 60);
  text("Energía Mecánica: " + nf(energiaMecanica, 0, 2) + " J", 20, 90);
  text("Instrucciones: Arrastrar con click izquierdo. Click derecho para cambiar color.", 20, height - 20);
}

function mousePressed() {
  if (dist(mouseX, mouseY, x, y) < radio) {
    if (mouseButton === LEFT) {
      arrastrando = true;
    } else if (mouseButton === RIGHT) {
      // Cambiar color al hacer clic derecho
      colorObjeto = color(random(255), random(255), random(255));
    }
  }
  
  if (mouseButton === RIGHT) {
    return false;
  }
}

function mouseReleased() {
  if (mouseButton === LEFT) {
    arrastrando = false;
  }
}

function mouseDragged() {
  if (mouseButton === LEFT && dist(mouseX, mouseY, x, y) < radio) {
    arrastrando = true;
  }
}