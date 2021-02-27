/*
Чеклин Павел  tscheklin@gmail.com
Проект команды Glina Mess 

Программа для управления двигателями nema 17 по usb через arduino nano


Взамодействие по интерфейсу uart будет производиться с помощью команд
x число шагов y число шагов
Подразумевается, что команда задана правильно (проверка не требуется)

1 ШАГ ДВИГАТЕЛЯ - ПОВОРОТ НА 1.8 градуса

ПРИМЕР
x 10 y 10
x -10 y -10
x 0 y 10
x 10 y 0
*/

// ********* ОБЬЯВЛЕНИЕ КОНСТАНТ

#define DRIVER_LOGIC 2 // питание логического уровня драйвера (отключаем во время простоя)
// отключаем во время простоя, чтобы избежать перегрева двигателей

#define X_STEP 5 // пин, отвечающий за шаг двигателя x
#define X_DIR 4 // пин, отвечающий за направление движения двигателя x

#define Y_STEP 7 // пин, отвечающий за шаг двигателя y
#define Y_DIR 6 // пин, отвечающий за направление движения двигателя y

#define MAGNET 8

#define MOVE_DELAY 1 // задержка для шага мотора (3 - самый используемый вариант)

// ********* ОБЪЯВЛЕНИЕ ГЛОБАЛЬНЫХ ПЕРЕМЕННЫХ

int move_x = 0, move_y = 0; // переменные для количества шагов мотора
String input; // переменная для чтения сообщений с порта
bool negative = false; // переменаня для проверки, является ли перемещение отрицательным
bool has_moved = true; // переменная для проверки, нужно ли перемещение
int magnet = 0; // переменая для проверки работы магнита (0 - ничего не делать, 1 - включить, 2 - выключить)
// ********* ОБЪЯВЛЕНИЕ ФУНКЦИЙ

// Функция для чтения команд, поступаемых с последовательного порта
// incoming_char - переменная для запоминания символа 
void read_serial();

// установка направления движения
void set_direction();

// функция для перемещения каретки (работа моторов)
void engine_move();

// функция для изменения состояния магнита
void magnet_actions();

// ********* ОСНОВНАЯ ПРОГРАММА

// Начальные настройки
void setup()
{
  // ******** Настройка пинов (все на вывод) 
  pinMode(DRIVER_LOGIC, OUTPUT);
  
  pinMode(X_STEP, OUTPUT);
  pinMode(X_DIR, OUTPUT);

  pinMode(Y_STEP, OUTPUT);
  pinMode(Y_DIR, OUTPUT);

  // ******** Начальное положение пинов
  digitalWrite(DRIVER_LOGIC, LOW);
  digitalWrite(X_DIR, LOW);
  digitalWrite(Y_DIR, LOW);
  digitalWrite(X_STEP, LOW);
  digitalWrite(Y_STEP, LOW);

  // ******** Открытие последовательного порта на скорость 9600 бит/с
  Serial.begin(9600); 


}


// Основной цикл
void loop()
{
  // счиываем команду 
  read_serial();
  
  if (magnet)
  {
    Serial.println("MAGNET");
    magnet_actions();

    magnet = 0;
  }
  if (!has_moved)
  {
    Serial.println("Let's move!");
    Serial.println(move_x);
    Serial.println(move_y);
    // включаем питание логического уровня драйвера
    digitalWrite(DRIVER_LOGIC, HIGH);
    // устанавливаем направление вращения
    set_direction();

    // перемещаем каретку
    engine_move();

    // отключаем питание логического уровня драйвера
    digitalWrite(DRIVER_LOGIC, LOW);

  }

}

// ********* ОПРЕДЕЛЕНИЕ ФУНКЦИЙ

// Функция для чтения команд, поступаемых с последовательного порта
// incoming_char - переменная для запоминания символа 
void read_serial()
{
  char incoming_char;
  while ((Serial.available()) && (incoming_char != '\n') && (incoming_char != EOF))
  {
    incoming_char = Serial.read();

    if (incoming_char == 'x')
    {
      input = "";
    }
    else if (incoming_char == 'y')
    {
      move_x = negative ? -1 * input.toInt() : input.toInt();
      input = "";
      negative = false;
    }
    else if (incoming_char == 'm')
    {
      magnet = 1;
    }
    else if (incoming_char == 'o')
    {
      magnet = 2;
    }
    else if (incoming_char == '\n')
    {
      if (!magnet)
      {
          move_y =  negative ? -1 * input.toInt() : input.toInt();
          Serial.println("Move x and move y");
          Serial.println(move_x);
          Serial.println(move_y);
          input = "";
          negative = false;
          incoming_char = '_';
          has_moved = false;
      }
    }
    else if (incoming_char == '-')
      negative = true;
    else if ((incoming_char >= '0') && (incoming_char <= '9'))
      input += incoming_char;
  }
}


// установка направления движения
void set_direction()
{
  if (move_x < 0)
  {
    digitalWrite(X_DIR, LOW);
    move_x *= -1;
  }
  else 
    digitalWrite(X_DIR, HIGH);

  if (move_y < 0) 
  {
    digitalWrite(Y_DIR, LOW);
    move_y *= -1;
  }
  else
    digitalWrite(Y_DIR, HIGH);
}


// функция для перемещения каретки (работа моторов)
void engine_move()
{
  while ((move_x > 0) || (move_y > 0))
  {
    if (move_x > 0)
      digitalWrite(X_STEP, HIGH);
    if (move_y > 0)
      digitalWrite(Y_STEP, HIGH);

    delay(MOVE_DELAY);

    digitalWrite(X_STEP, LOW);
    digitalWrite(Y_STEP, LOW);

    delay(MOVE_DELAY);

    move_x--;
    move_y--;
  }

  has_moved = true;
}

void magnet_actions()
{
  if (magnet == 1)
  {
    Serial.println("MAGNET_ON");
    digitalWrite(MAGNET, HIGH);
  }
  else if (magnet == 2)
  {
    Serial.println("MAGNET OFF");
    digitalWrite(MAGNET, LOW);
  }
}