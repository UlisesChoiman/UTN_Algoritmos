/*
Laboratorio Nº6
Ulises Choiman
*/

// Variables de juego
let playerScore = 0;
let gameTime = 0;
let shieldActive = false;
let shieldCooldown = 0;
let shieldDuration = 0;

let playerCannon, enemyCannon;

let playerProjectiles = [];
let enemyProjectiles = [];

// Escudo
let shield = {
  angle: 0,
  radius: 60,
  angularSpeed: 0.1,
  position: { x: 0, y: 0 }
};

// Variables para imágenes
let playerImg, enemyImg, backgroundImg, projectileImg, shieldImg;
// Variables para precarga de imágenes
let imagesLoaded = false;

// Variables de movimiento del jugador
let playerVelocity = { x: 0, y: 0 };
let playerSpeed = 5;
let playerOnGround = false;


function setup() {
  createCanvas(650, 500);
  
  // Configurar cañones
  playerCannon = {
    x: 100, 
    y: height - 150,
    width: 60,
    height: 60,
    velocity: { x: 0, y: 0 },
    jumpForce: -12,
    onGround: false
  };
  
  enemyCannon = {
    x: width - 100, 
    y: height - 100,
    width: 60,
    height: 60,
    isStatic: true
  };
  
  
  
  setInterval(enemyShoot, 1500);
}

function draw() {
  
  if (imagesLoaded && backgroundImg) {
    image(backgroundImg, 0, 0, width, height);
  } else {
    background(135, 206, 235); 
    fill(139, 69, 19);
    noStroke();
    rect(0, height - 50, width, 50);
  }
  
  
  gameTime += deltaTime / 1000;
  updateCooldowns();
  
  
  updatePlayerPhysics();
  

  drawCannons();
  updateProjectiles();
  drawShield();
  drawUI();
  
  
  checkCollisions();
}


class Projectile {
  constructor(x, y, vx, vy, isPlayer) {
    this.x = x;
    this.y = y;
    this.vx = vx;
    this.vy = vy;
    this.radius = 12;
    this.mass = 1;
    this.isPlayer = isPlayer;
    this.active = true;
    this.rotation = 0;
  }
  
  update() {
    // Aplicar gravedad
    this.vy += 0.2;
    
    
    this.x += this.vx;
    this.y += this.vy;
    
    
    this.rotation += 0.1;
    
    // Verificar límites de pantalla
    if (this.x < 0 || this.x > width || this.y > height - 50) {
      this.active = false; // Choque plástico con bordes
    }
  }
  
  draw() {
    push();
    translate(this.x, this.y);
    rotate(this.rotation);
    
    if (imagesLoaded && projectileImg) {
      
      imageMode(CENTER);
      let size = this.radius * 2.5;
      tint(this.isPlayer ? color(0, 100, 255) : color(255, 100, 100));
      image(projectileImg, 0, 0, size, size);
      noTint();
    } else {
      
      fill(this.isPlayer ? 'blue' : 'red');
      noStroke();
      ellipse(0, 0, this.radius * 2);
    }
    
    pop();
  }
}

function updatePlayerPhysics() {
  // Aplicar gravedad
  playerCannon.velocity.y += 0.5;
  
  
  playerCannon.x += playerCannon.velocity.x;
  playerCannon.y += playerCannon.velocity.y;
  
  
  if (playerCannon.y > height - 50 - playerCannon.height/2) {
    playerCannon.y = height - 50 - playerCannon.height/2;
    playerCannon.velocity.y = 0;
    playerCannon.onGround = true;
  } else {
    playerCannon.onGround = false;
  }
  
  
  playerCannon.x = constrain(playerCannon.x, playerCannon.width/2, width - playerCannon.width/2);
  
  
  if (playerCannon.onGround) {
    playerCannon.velocity.x *= 0.9; // Fricción
  }
  
  
  playerCannon.velocity.x = constrain(playerCannon.velocity.x, -playerSpeed, playerSpeed);
}

// Controles del jugador
function keyPressed() {
  
  if (key === 'a' || key === 'A' || keyCode === LEFT_ARROW) {
    playerCannon.velocity.x = -playerSpeed;
  }
  if (key === 'd' || key === 'D' || keyCode === RIGHT_ARROW) {
    playerCannon.velocity.x = playerSpeed;
  }
  
  
  if ((key === 'w' || key === 'W' || keyCode === UP_ARROW || key === ' ') && playerCannon.onGround) {
    playerCannon.velocity.y = playerCannon.jumpForce;
  }
  
  
  if (keyCode === SHIFT && shieldCooldown <= 0) {
    shieldActive = true;
    shieldDuration = 3; // 3 segundos de duración
    shieldCooldown = 10; // 10 segundos de cooldown
  }
}

function keyReleased() {

  if (key === 'a' || key === 'A' || keyCode === LEFT_ARROW || 
      key === 'd' || key === 'D' || keyCode === RIGHT_ARROW) {
    playerCannon.velocity.x = 0;
  }
}

// Disparo del jugador con click del mouse
function mousePressed() {
  let angle = atan2(mouseY - playerCannon.y, mouseX - playerCannon.x);
  let speed = 12;
  let vx = cos(angle) * speed;
  let vy = sin(angle) * speed;
  
  playerProjectiles.push(new Projectile(
    playerCannon.x, 
    playerCannon.y, 
    vx, 
    vy, 
    true
  ));
}

// Disparo del enemigo controlado por IA
function enemyShoot() {
  
  let dx = playerCannon.x - enemyCannon.x;
  let dy = playerCannon.y - enemyCannon.y;
  let baseAngle = atan2(dy, dx);
  
  let angleVariation = random(-0.35, 0.35);
  let angle = baseAngle + angleVariation;
  
  let speed = random(10, 14);
  let vx = cos(angle) * speed;
  let vy = sin(angle) * speed;
  
  enemyProjectiles.push(new Projectile(
    enemyCannon.x, 
    enemyCannon.y, 
    vx, 
    vy, 
    false
  ));
}

// Sistema de detección de colisiones
function checkCollisions() {

  for (let i = playerProjectiles.length - 1; i >= 0; i--) {
    for (let j = enemyProjectiles.length - 1; j >= 0; j--) {
      let p1 = playerProjectiles[i];
      let p2 = enemyProjectiles[j];
      
      if (p1.active && p2.active && collisionProjectiles(p1, p2)) {
        handleProjectileCollision(p1, p2);
        playerScore += 10; // Puntos por intercepción
      }
    }
  }
  
  for (let i = enemyProjectiles.length - 1; i >= 0; i--) {
    let proj = enemyProjectiles[i];
    if (proj.active && collisionCannon(proj, playerCannon)) {
      if (!shieldActive) {
        enemyProjectiles.splice(i, 1);
        playerScore -= 20; // Penalización por golpe
      } else {
        // Si el escudo está activo, rebotar el proyectil
        proj.vx = -proj.vx * 0.5;
        proj.vy = -proj.vy * 0.5;
      }
    }
  }
  
  for (let i = playerProjectiles.length - 1; i >= 0; i--) {
    let proj = playerProjectiles[i];
    if (proj.active && collisionCannon(proj, enemyCannon)) {
      playerProjectiles.splice(i, 1);
      playerScore += 15; // Puntos por golpear al enemigo
    }
  }
}


function collisionProjectiles(p1, p2) {
  let dx = p1.x - p2.x;
  let dy = p1.y - p2.y;
  let distance = sqrt(dx * dx + dy * dy);
  return distance < (p1.radius + p2.radius);
}

function collisionCannon(projectile, cannon) {
  return projectile.x > cannon.x - cannon.width/2 &&
         projectile.x < cannon.x + cannon.width/2 &&
         projectile.y > cannon.y - cannon.height/2 &&
         projectile.y < cannon.y + cannon.height/2;
}

// Manejar colisión entre proyectiles
function handleProjectileCollision(p1, p2) {
  
  let restitution = 0.8;
  
  let dx = p2.x - p1.x;
  let dy = p2.y - p1.y;
  let distance = sqrt(dx * dx + dy * dy);
  
  if (distance === 0) return;
  
  let nx = dx / distance;
  let ny = dy / distance;
  
  // Velocidades relativas
  let dvx = p2.vx - p1.vx;
  let dvy = p2.vy - p1.vy;
  
  let dotProduct = dvx * nx + dvy * ny;
  
  if (dotProduct > 0) return; // Ya se están separando
  
  // Impulso
  let impulse = 2 * dotProduct / (p1.mass + p2.mass) * restitution;
  
  p1.vx += impulse * p2.mass * nx;
  p1.vy += impulse * p2.mass * ny;
  p2.vx -= impulse * p1.mass * nx;
  p2.vy -= impulse * p1.mass * ny;
  
  let overlap = (p1.radius + p2.radius) - distance;
  if (overlap > 0) {
    p1.x -= nx * overlap * 0.5;
    p1.y -= ny * overlap * 0.5;
    p2.x += nx * overlap * 0.5;
    p2.y += ny * overlap * 0.5;
  }
}


function updateCooldowns() {
  if (shieldActive) {
    shieldDuration -= deltaTime / 1000;
    if (shieldDuration <= 0) {
      shieldActive = false;
    }
  }
  
  if (shieldCooldown > 0) {
    shieldCooldown -= deltaTime / 1000;
  }
}

// Dibujar y actualizar el escudo
function drawShield() {
  if (!shieldActive) return;
  
  // Actualizar posición del escudo (Movimiento Circular Uniforme)
  shield.angle += shield.angularSpeed;
  shield.position.x = playerCannon.x + cos(shield.angle) * shield.radius;
  shield.position.y = playerCannon.y + sin(shield.angle) * shield.radius;
  
  // Dibujar órbita del escudo
  stroke(0, 100, 255, 100);
  strokeWeight(1);
  noFill();
  drawingContext.setLineDash([5, 5]);
  ellipse(playerCannon.x, playerCannon.y, shield.radius * 2);
  drawingContext.setLineDash([]);
  
  // Dibujar escudo
  if (imagesLoaded && shieldImg) {
    imageMode(CENTER);
    tint(0, 200, 255, 200);
    image(shieldImg, shield.position.x, shield.position.y, 30, 30);
    noTint();
  } else {
    fill(0, 255, 255, 150);
    stroke(0, 200, 255);
    strokeWeight(2);
    ellipse(shield.position.x, shield.position.y, 20);
  }
}

// Actualizar y dibujar todos los proyectiles
function updateProjectiles() {
  
  for (let i = playerProjectiles.length - 1; i >= 0; i--) {
    playerProjectiles[i].update();
    playerProjectiles[i].draw();
    
    if (!playerProjectiles[i].active) {
      playerProjectiles.splice(i, 1);
    }
  }
  
  
  for (let i = enemyProjectiles.length - 1; i >= 0; i--) {
    enemyProjectiles[i].update();
    enemyProjectiles[i].draw();
    
    if (!enemyProjectiles[i].active) {
      enemyProjectiles.splice(i, 1);
    }
  }
}

// Dibujar los cañones en pantalla
function drawCannons() {
  
  if (imagesLoaded && playerImg) {
    imageMode(CENTER);
    image(playerImg, playerCannon.x, playerCannon.y, playerCannon.width, playerCannon.height);
  } else {
    
    fill(0, 0, 255);
    noStroke();
    rectMode(CENTER);
    rect(playerCannon.x, playerCannon.y, playerCannon.width, playerCannon.height);
  }
  
  
  if (imagesLoaded && enemyImg) {
    imageMode(CENTER);
    image(enemyImg, enemyCannon.x, enemyCannon.y, enemyCannon.width, enemyCannon.height);
  } else {
    // Fallback a rectángulo rojo
    fill(255, 0, 0);
    rect(enemyCannon.x, enemyCannon.y, enemyCannon.width, enemyCannon.height);
  }
  
  rectMode(CORNER);
}

// Dibujar interfaz de usuario
function drawUI() {
  
  fill(0, 0, 0, 150);
  noStroke();
  rect(0, 0, 250, 80);
  
  
  fill(255);
  textSize(20);
  text(`Puntos: ${playerScore}`, 20, 30);
  

  textSize(16);
  if (shieldCooldown > 0) {
    fill(255, 100, 0);
    text(`Escudo: ${shieldCooldown.toFixed(1)}s`, 20, 60);
  } else {
    fill(0, 255, 0);
    text("Escudo: LISTO (SHIFT)", 20, 60);
  }
  
  if (shieldActive) {
    fill(0, 200, 255);
    textSize(18);
    text("ESCUDO ACTIVO", width - 180, 30);
  }
  
  
  fill(0);
  textSize(12);
  text("Controles:", 10, height - 80);
  text("A/D o ←/→: Moverse", 10, height - 65);
  text("W o ↑ o ESPACIO: Saltar", 10, height - 50);
  text("SHIFT: Activar escudo", 10, height - 35);
  text("CLICK: Disparar", 10, height - 20);
}