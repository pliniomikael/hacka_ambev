// Pino A3 do Arduino Uno recebe o input do sensor
float Sensor = A3;
// Variável para armazenar os valores lidos
float Dados = 0;
// Variável normalizada de 0 ~ 1024 [bits] (Analogica) para 0 ~ 5 [V] (Digital)
int NormalDados = 0;

// Chave para escolha de Variável ( 1- Normalizada ou 0 - Não Normalizada)
int Key = 1;

void setup() {
  // Porta serial configurada para receber informações a um taxa (Baud Rate) de 9600bps
  Serial.begin(9600);
}

void loop() {

  // Trabalhar com dados não normalizados (0~1024[bits])
  if (Key == 0){
    Dados = analogRead(Sensor);  
    Serial.println(Dados);  
  }
  // Trabalhar com dados normalizados (0~5[V])
  else if (Key == 1){
    Dados = analogRead(Sensor);  
    NormalDados = map(Dados, 0, 1023, 0, 5);
    Serial.println(NormalDados);  
  }
}
