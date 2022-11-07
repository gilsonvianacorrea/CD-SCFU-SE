## Micropython & ESP 32

Este repositório registra os códigos desenvolvidos pela turma de **Sistemas Embarcados (SE) e Sistemas Ciber Físicos e Ubíquos (SCFU)** do [MEEC](https://pos.ucpel.edu.br/ppgeec/) da UCPel.

  * **[ajusta-relogio.py](https://github.com/adenauery/micropython/blob/main/ajusta-relogio.py)**: ajusta o relógio da ESP32 utilizando o NTP (Network Time Protocol)
  * **[publica-sensores-sleep.py](https://github.com/adenauery/micropython/blob/main/publica-sensores-sleep.py)**: publica leituras feitas por sensores em JSON (DHT 22, no caso) utilizando o protocolo MQTT (biblioteca sem suporte a senha), com intervalo de publicação por sleep (sem agendamento). O programa tem impressões em vários pontos, as quais, quando em regime de produção, podem ser suprimidas.
  
Alguns dos materiais utilizados na concepção dos códigos:
  
  * [Sistema Embarcado com ESP32 e MicroPython - Prof. Marcos Carnevali](https://www.youtube.com/playlist?list=PLCcdteC1rwSFvJnUoe0DfORHv4p_1EFps)
  * [Secrets of MicroPython: MQTT on ESP32](https://bhave.sh/micropython-mqtt/)
  * [ESP32 MicroPython: Encoding JSON](https://techtutorialsx.com/2017/05/27/esp32-micropython-encoding-json/)
  
  
Cliente Web para Protocolo MQTT
  * http://www.hivemq.com/demos/websocket-client/
  * Tópico em uso: scfu/dados
  
