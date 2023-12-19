var SNAKE_WIDTH = 40;
var SNAKE_HEIGHT = 40;
var SNAKE_COLOR = "green"; // Assuming the graphics library accepts string literals for color

var EAST = 0;
var SOUTH = 1;
var WEST = 2;
var NORTH = 3;
var snake; 
var direction;

function start() {
  snake = new Rectangle(SNAKE_WIDTH, SNAKE_HEIGHT);
  snake.setPosition(100, 100);
  snake.setColor(SNAKE_COLOR);
  
  keyDownMethod(changeDirection);
}

function changeDirection(e) {
  if (e.keyCode == Keyboard.LEFT) {
    direction = WEST;
  } else if (e.keyCode == Keyboard.RIGHT) {
    direction = EAST;
  } else if (e.keyCode == Keyboard.UP) {
    direction = NORTH;
  } else if (e.keyCode == Keyboard.DOWN) {
    direction = SOUTH;
  }
  
  moveSnake();
}

function moveSnake() {
  switch (direction) {
    case WEST:
      snake.move(-SNAKE_WIDTH, 0);
      break;
    case EAST:
      snake.move(SNAKE_WIDTH, 0);
      break;
    case NORTH:
      snake.move(0, -SNAKE_HEIGHT);
      break;
    case SOUTH:
      snake.move(0, SNAKE_HEIGHT);
      break;
  }
}
