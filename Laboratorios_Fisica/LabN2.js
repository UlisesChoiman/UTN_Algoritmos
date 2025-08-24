//Ulises Choiman

//Triangulo que rebota en todas las paredes

let x, y; 
let speedX, speedY; // Velocidad del triángulo
let triangleSize = 50; //Tamaño de triangulo

function setup() {
  createCanvas(600, 500); //Crea el tablero de 600 x 500
  
  x = random(triangleSize, width - triangleSize); //Posicion en x
  y = random(triangleSize, height - triangleSize); //Posicion en y
  
  speedX = random(2,3); //Velocidad de X
  speedY = random(2,3); //Velocidad de Y
}

function draw() {
  background(90); // Color Tablero
  
  // Dibujar el triángulo
  fill("red");
  triangle(
    x, y - triangleSize/2, 
    x - triangleSize/2, y + triangleSize/2, 
    x + triangleSize/2, y + triangleSize/2
  );
  
  // Mover el triángulo
  x += speedX;
  y += speedY;
  
  // Rebotar en los bordes
  if (x > width - triangleSize/2 || x < triangleSize/2) {
    speedX *= -1;
  }
  if (y > height - triangleSize/2 || y < triangleSize/2) {
    speedY *= -1;
  }
}