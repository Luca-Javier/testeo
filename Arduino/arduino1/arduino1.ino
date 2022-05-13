void setup(){ /*creo que 13 es el ping(de salida)*/
  pinMode (13, OUTPUT);
  /*tiene keysensitive y/por lo tanto camel case*/
  }

  void loop(){ /*enter y cierra la llave*/
    digitalWrite(13, HIGH);  /*prender led*/
    delay(1000); /* es pára esperar y se mide en ms*/
    digitalWrite(13, LOW);   /*apagar led*/
    delay(1000);
  }
