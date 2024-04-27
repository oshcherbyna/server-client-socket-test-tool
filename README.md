# server-client TCP-Socket test tool
A simple server-client tool for testing a TCP-Socket connection.

## [DE] Ein einfaches Server-Client-Tool zum Testen einer TCP-Socket-Verbindung.

1. Geben Sie die gewünschte _IP_ und _PORT_ in `server.py`
   ```server.py
       server_socket.bind(('localhost', 7777)) # ('192.168.1.10', 7777)
   ```
    und `client.py` an:
   ```client.py
       SERVER_ADDRESS = 'localhost' # '192.168.1.10'
       SERVER_PORT = 7777
   ```
3. Nach dem Start des Servers sollte die Firewall Ihnen mitteilen, dass die Anwendung den Port öffnen will => `erlauben`.
    - Falls dies nicht der Fall ist, müssen Sie die Erlaubnis für diesen Port manuell in den Firewall-Regeln hinzufügen:
      - 2.1. über GUI:
        > wf.msc => Inbounds Rules => New Rule => Port => 7777 => ...
      - 2.2. oder über die Kommandozeile:
        > netsh advfirewall firewall add rule name='7777' dir=in action=allow protocol=TCP localport=7777
        <img width="776" alt="05" src="https://github.com/oshcherbyna/server-client-socket-test-tool/assets/10991880/6dd1ff7e-7b60-4c68-8475-5e6eb36c08be">
      - 2.3. Nachdem eine neue Regel hinzugefügt wurde, wird der Status des angegebenen Ports im Status angezeigt:
        > netsh firewall show state
        <img width="776" alt="06" src="https://github.com/oshcherbyna/server-client-socket-test-tool/assets/10991880/ffbf314a-d4ed-4c2f-99c1-3984303a8b02">
      - 2.4. Der Status des offenen Ports kann auch in netstat überprüft werden:
        > netstat -a | find „7777“
        <img width="734" alt="04" src="https://github.com/oshcherbyna/server-client-socket-test-tool/assets/10991880/a41cd578-a925-4c61-bff5-2aa898e30d51">
      - 2.5. Außerdem ist zu beachten, dass die Firewall bei der automatischen Erstellung einer neuen Regel eine Regel für die Anwendung erstellt. Wenn Sie also manuell eine Regel für einen Server-Port erstellen und keine Verbindung zum Server besteht, sollten Sie auch eine Regel für die Anwendung hinzufügen.
        In unserem Fall handelt es sich um `python`, der den Server-Code ausführt.
4. Nachdem der Client gestartet wurde, stellt er eine Verbindung zum Server her. Wenn er erfolgreich ist, erhält der Client den Servernamen und beendet sich.

📌 Beim lokalen Test wird geprüft, ob der Port geöffnet wird, wenn der Server mit dem Lauschen beginnt.
<img width="408" alt="03" src="https://github.com/oshcherbyna/server-client-socket-test-tool/assets/10991880/371fab16-4769-494f-af8d-730a5c8e1db7">
<img width="408" alt="02" src="https://github.com/oshcherbyna/server-client-socket-test-tool/assets/10991880/0eb14068-8588-4469-ab60-fbf280ca3c3f">

📌 Beim Ferntest wird geprüft, ob die Netzwerkverbindung funktioniert, ob Pakete durch Router gehen oder ob die Firewall des Servers eingehende Verbindungen zum angegebenen Port zulässt.

<img width="321" alt="00" src="https://github.com/oshcherbyna/server-client-socket-test-tool/assets/10991880/b73de3ae-4784-410e-8755-345d440d3e4f">
<img width="523" alt="01" src="https://github.com/oshcherbyna/server-client-socket-test-tool/assets/10991880/d6243006-0c41-411e-a96d-e6f67b97aa41">

## [UA] Простий сервер-клієнт інструмент для тестування сокетного TCP зʼєднання.

1. Вказати потрібне _IP_ та _PORT_ в `server.py` та `client.py`
2. Після запуска сервера, firewall повинен повідомити, що застосунок хоче відкрити порт => `дозволяємо`.
    - Якщо цього не відбувається, потрібно власноруч додати дозвіл на цей порт в правилах firewall:
      - 2.1 через GUI: `wf.msc => Inbounds Rules => New Rule => Port => 7777 => ...`
      - 2.2 або з командної строки: `netsh advfirewall firewall add rule name='7777' dir=in action=allow protocol=TCP localport=7777`
      - 2.3 Після додавання нового правила, статус вказаного порта буде показано в статусі: `netsh firewall show state`
      - 2.4 Статус відкритого порта також можна перевірити в netstat: `netstat -a | find "7777"`
      - 2.5 Також варто зазначити, у випадку коли нове правло створюється firewall автоматично, він створює правило для застосунку. Тому коли після ручного створення правила для порту зʼєднання з сервером немає, варто додати правило для застосунку також.
        У нашому випадку це `python`, який виконує серверний код.
3. Після запуску клієнта, відбувається зʼєднання з сервером. Якщо воно вдале, клієнт отримує імʼя сервера і віключається.

📌 При локальному тесті ми перевіряємо, що порт відкривається коли сервер починає його слухати.

📌 При віддаленому тесті ми перевіряємо, чи відбувається мережеве зʼєднання, чи йдуть пакети через маршрутизатори, чи серверний фаєрвол дозволяє вхідні підключення на вказаний порт.


## [EN] A simple server-client tool for testing a TCP-Socket connection.

1. Specify the required _IP_ and _PORT_ in `server.py` and `client.py`
2. After starting the server, the firewall should inform you that the application wants to open the port => `allow`.
    - If this does not happen, you need to manually add permission for this port in the firewall rules:
      - 2.1 via GUI: `wf.msc => Inbounds Rules => New Rule => Port => 7777 => ...`
      - 2.2 or from the command line: `netsh advfirewall firewall add rule name='7777' dir=in action=allow protocol=TCP localport=7777`
      - 2.3 After adding a new rule, the status of the specified port will be shown in the status: `netsh firewall show state`
      - 2.4 The status of the open port can also be checked in netstat: `netstat -a | find “7777”`
      - 2.5 It is also worth noting that when a new rule is created automatically by the firewall, it creates a rule for the application. Therefore, when you manually create a rule for a server port and there is no connection to the server, you should add a rule for the application as well.
        In our case, it's `python` that executes the server code.
3. After the client starts, it connects to the server. If it is successful, the client receives the server name and shuts down.

📌 In the local test, we check that the port opens when the server starts listening.

📌 In the remote test, we check whether the network connection is working, whether packets are going through routers, or whether the server firewall allows incoming connections to the specified port.
