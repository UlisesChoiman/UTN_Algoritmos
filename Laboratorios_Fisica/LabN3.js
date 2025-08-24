//Ulises Nahuel Choiman Zambrana

// Declaramos las varibles

let x, y;
let velX, velY;
let tamano = 50;
let colorFigura;
let tipoMovimiento = 'Mixto';

// Elementos necesarios
let sliderTamano;
let inputVelX, inputVelY;
let selectMovimiento;
let botonReset;
let colorPicker;

function setup() {
  
  createCanvas(600, 500);
  
  resetear();
  
  crearInterfaz();
}

function draw() {
  
  background(220);
  
  actualizarPosicion();
  
  fill(colorFigura);
  ellipse(x, y, tamano, tamano);
  
  rebotarEnBordes();
}

function crearInterfaz() {
  
  let titulo = createP('CONTROLES DE LA FIGURA');
  titulo.position(20, 0);
  titulo.style('font-weight', 'bold');
  titulo.style('font-size', '20px');
  
  // Slider
  sliderTamano = createSlider(10, 100, 50);
  sliderTamano.position(20, 45);
  sliderTamano.input(() => {
    tamano = sliderTamano.value();
  });
  
  // Input del eje x
  inputVelX = createInput(velX);
  inputVelX.position(20, 70);
  inputVelX.input(() => {
    velX = parseFloat(inputVelX.value()) || 0;
  });
  
  // Imput del eje y
  inputVelY = createInput(velY);
  inputVelY.position(20, 100);
  inputVelY.input(() => {
    velY = parseFloat(inputVelY.value()) || 0;
  });
  
  // Seleccionar movimiento
  selectMovimiento = createSelect();
  selectMovimiento.position(20, 140);
  selectMovimiento.option('Horizontal');
  selectMovimiento.option('Vertical');
  selectMovimiento.option('Mixto');
  selectMovimiento.selected(tipoMovimiento);
  selectMovimiento.input(() => {
    tipoMovimiento = selectMovimiento.value();
  });
  
  // Reset
  botonReset = createButton('Reiniciar');
  botonReset.position(20, 180);
  botonReset.mousePressed(resetear);
  
  // Seleccion de color
  colorPicker = createColorPicker('#110101');
  colorPicker.position(20, 220);
  colorPicker.input(() => {
    colorFigura = colorPicker.color();
  });
  
  
}

function actualizarPosicion() {
  switch(tipoMovimiento) {
    case 'Horizontal':
      x += velX;
      break;
    case 'Vertical':
      y += velY;
      break;
    case 'Mixto':
      x += velX;
      y += velY;
      break;
  }
}

function rebotarEnBordes() {
  // En bordes horizontales
  if (x > width - tamano/2 || x < tamano/2) {
    velX *= -1;
  }
  
  // En bordes verticales 
  if (y > height - tamano/2 || y < tamano/2) {
    velY *= -1;
  }
}

function resetear() {

  //Esta funcion al cargarse, reinicia todo a su valor base en que esta programado
  
  x = width/2;
  y = height/2;
  
  velX = 0;
  velY = 0;
  
  tamano = 20;
  
  colorFigura = color(2, 0, 0);
  
  if (sliderTamano) {
    sliderTamano.value(tamano);
    inputVelX.value(velX);
    inputVelY.value(velY);
    selectMovimiento.selected(tipoMovimiento);
    colorPicker.color(colorFigura);
  }
}