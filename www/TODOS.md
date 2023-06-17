TODOs:

-~~ Menü für Trust Boundaries erstellen~~

- Import Funktion schreiben, also in der this.addAction("import...", function () {
  ~~ DataDiagram importieren anschließend Assets importieren und edges~~
- Defaultwerte setzen bei ersten erstellen
- Tagify listener programmmieren, damit die Werte gesetzt werden.
- Christian Schneider Styles vielleicht einbauen
  - z.B. Birectional
  - Legende einbauen
-
- Threat Analysis Tab erstellen in den Technology Assets und dort RAA, sowie Threats berechnen
  wenn darauf geklickt wird und erlauben das man dort Sachen mitigiert und so weiter
- Export Funktion schreiben, also über die ganzen Daten iterieren, anschließend über die Cellen und Edges, sowie wie die Threats die mitigiert wurden

- Boundary Tab muss man einstellen können was für eine Art von Trust Boundary das ist
  ~~- ID soll im Objekt stehen, also listener hinzufügen, wenn id sich ändert, dann setze es im Objekt~~
- Mach Git Projekt public
- Die jetzigen TODOS, lagere sie als Issues aus
- Lösche deutsche Kommentare im Code

~~- Bevor man importieren mit dem program testen ob der Graph korrekt ist~~

- Fehlerhandling, fehler zeigen beim import

- exportieren... umschreiben für threagile oder yaml

Anschließend Table mit den Initalwerten und einen haken daneben den man mit doppelklick hinzufügen der löschen kann - Ein Initalwert für die Id wird der derzeitige Zeitpunkt sein.

- Noch eine Table mit den ausgwählten Daten und nicht allen

- Erst Initialisierung, erstelle Default werte für ID etc.

  ~~- Data einbauen mit einer Liste und + und mit und einem WIndow wo die Eingabefelder sind~~
  ~~- In den Assets die Datas angebbar machen~~

- --Die Verbindung nicht mehr erlauben das die frei schweben können mit mxgrpah--
  Verbindugen:
- Wenn man auf den Pfeil klingt, steht da nicht Asset sondern die Verbindung, also z.B. html usw.
  - Da steht tatsächlich eine ganze Menge siehe Communication Link und da muss man dann die Daten referenzieren
- In den Assets die Verbindung sehen können
- Alle Assets auf Kategorien sortieren und die restlichen einfügen
- Rechteck um die Assets, sieht besser aus
- New rausnehmen bei den Assets
  Trust Boundaries:
- Trust Boundaries Kategorie erstellen mit den 4 verschiedenen Kategorien
- Die TrustBoundaries hat auch eine Custom Tab mit Beschreibung, technicals Assets inside und trustboundaries nested, sowie Type und ID
- Jetzt geht es los mit rekursion und überprüfen ob es Assets in den TrustBoundaries gibt oder nicht
  Import:
- Zeit sich den GoCode und Webassembly anzutun. Und zwar muss bei dem Import das ganze geparsed werden, dafür webassembly mit go, anschließend
  muss man mit vis.js gucken wie das ganze aussehen würde und dann die verschiedenen Assets mit Model etc. erstellen.
  Export:
  - Einmal über die ganzen Elemente iterieren
    ExtraInfos:
- Bei dem Diagramm noch Autor etc als Feld hinzufügen.
- Bug, man kann kante ziehen und dann hat sie keine Verbindung mehr.
- Export Funktion einbauen die alle Dateien generiert
- Einbauen das man bei den Threats schreiben können ob man Threats mtigiert hat wie in der Excel
- Slack auf einen anderne Computer setzen https://slack.com/help/articles/207262907-Change-your-email-address
- Vor der Veröffentlichungen eine Woche testen.
- Merke dir den hide zustand in den DataAssets
- Baue noch tags ein in allen Sachen wo das fehlt
- ToolTIps
  Das in die JSON einbauen und dann geht das super einfacher
  descriptionButton.title = "Dies ist ein Tooltip für den X-Button";
- Code Refactoren
- Bug error
- Es gibt ein Model, da sollten wir Sachen speichern, damit man exportieren kann.
- Shared Runtimes fehlen noch

- ~~General wird zu Technologies~~ Das ist nicht Done, sondenr falsch, General wird nicht zu technologies
- Die anderen müssen invisible gemacht werden, also Misc usw. in dem Menü oder Sidebar, was auch immer das ist.
- "Format Panel" wird unbennant
  -~~ Es muss ein neues Tab geben, wie nenne ich das? - Sowie User Object" wäre am besten, also als xml speichern~~
- ~~Die ganzen technologies, als XML oder Image auswählbar machen:- Falls man auf Pfeil klingt, dann zeigt er einige Formen, dass sollten am besten andere werden, die!~~
- Import Funktion programmieren, also dass man eine threagile.yaml angeben kann
- Export Funktion programmieren
- Es gibt nicht nur Technologies sondern auch Verbindungen
  - Verbindungen dürfen nicht hängen, als müssen immer ausgeführt werden
  - Wenn man eine verbindung erstellt muss man in Rechts aussuchen können, was das für eine Verbindung ist
- ~~Es muss Trust Boundaries geben~~
- ~~Es muss auch in den Technologies ein Tab mit den Data Assets geben, also zwei Tabs~~
- ~~Trusted Boundaries wird etwas komplizierter, weil man nachschauen muss ob die nested sind, dass ist schon etwas schwieriger. Siehe CodeBeispiel unten: ~~
  Technologies:

- "unknown-technology",
- "client-system"
- "browser",
- "desktop",
- "mobile-app",
- "devops-client",
- "web-server",
- "web-application",
- "application-server",
- "database",
- "file-server",
- "local-file-system",
- "erp",
- "cms",
- "web-service-rest",
- "web-service-soap",
- "ejb",
  "service-registry",
- "reverse-proxy",
- "load-balancer",
- "build-pipeline",
- "sourcecode-repository",
- "artifact-registry",
- "code-inspection-platform",
- "monitoring",
- "ldap-server",
- "container-platform",
- "batch-processing",
- "event-listener",
- "identity-provider",
- "identity-store-ldap",
- "identity-store-database",
- "tool",
- "cli",
- "task",
- "function",
- "gateway",
- "iot-device",
- "message-queue",
- "stream-processing",
- "service-mesh",
- "data-lake",
- "report-engine",
- "ai",
- "mail-server",
- "vault",
- "hsm",
- "waf",
- "ids",
- "ips",
- "scheduler",
- "mainframe",
- "block-storage",
- "library"

Sortiert:
Unknown Technology:
"unknown-technology" x

Client System:
"client-system" x
"desktop" x
"mobile-app" x
"devops-client" x

Web-related:
"browser" x
"web-server" x
"web-application" x
"reverse-proxy" x nginx, haproxy, traefik, envoy
"load-balancer" x

Development-related:
"build-pipeline" x hier bitte mehr! Argo,Jenkins, Azure Pipelines, Tekton
"sourcecode-repository" X Gitlab, Github, Bitbucket
"artifact-registry" X
"code-inspection-platform" Sonarqube, Crucible, CodeClimate, Eslint, PMD Source code analyzer X

Infrastructure-related:
"file-server"X
"local-file-system"X
"database" X
"ldap-server"X
"container-platform"X
"mainframe"X
"block-storage"X

Web Services:
"web-service-rest"X
"web-service-soap"X

Content Management:
"cms"X

Enterprise-related:
"erp"X

Security-related:
"identity-provider"X
"identity-store-ldap"X
"identity-store-database"X
"vault"X
"hsm"X
"waf"X
"ids"X
"ips"X

Tools and Utilities:
"tool"X
"cli"X

Task and Function:
"task"X
"function"X

Messaging and Processing:
"message-queue"X
"stream-processing"X
"batch-processing"X
"event-listener"X

Networking:
"gateway"X

Data-related:

    "data-lake"X

Reporting and Analytics:

    "report-engine"X
    "ai"X

Monitoring:
"monitoring"X

Search related:
search-index",X
"search-engine",X

Other:

    "service-registry"X
    "scheduler"X
    "library"Xj
    "iot-device"X
    "service-mesh"Xjk
    "mail-server"

CodeBeispiel Nested\*\*:
function isObjectNested(graph, cell) {
var parent = graph.getModel().getParent(cell);

// Überprüfen, ob das übergeordnete Element vorhanden ist und eine Zelle ist
if (parent != null && graph.getModel().isVertex(parent)) {
// Überprüfen, ob das übergeordnete Element wiederum ein übergeordnetes Element hat
var grandparent = graph.getModel().getParent(parent);
if (grandparent != null && graph.getModel().isVertex(grandparent)) {
return isObjectNested(graph, parent); // Rekursiver Aufruf
}
}

return false;
}

// Beispielanwendung
var graph = new mxGraph(container);

// Erstellen Sie Zellen und fügen Sie sie dem Graphen hinzu
var cell1 = graph.insertVertex(parent, null, 'Cell 1', 20, 20, 80, 30);
var cell2 = graph.insertVertex(parent, null, 'Cell 2', 150, 20, 80, 30);
var cell3 = graph.insertVertex(parent, null, 'Cell 3', 280, 20, 80, 30);

// Fügen Sie cell1 als Kind zu cell2 hinzu
graph.addEdge(null, parent, null, cell1, cell2);

// Fügen Sie cell2 als Kind zu cell3 hinzu
graph.addEdge(null, parent, null, cell2, cell3);

// Überprüfen, ob cell1 in einem anderen Objekt verschachtelt ist
console.log(isObjectNested(graph, cell1)); // true
console.log(isObjectNested(graph, cell2)); // true
console.log(isObjectNested(graph, cell3)); // false

Kategorie: Allgemein

    Description

Category: General

    Description

Category: Properties

    Type
    Size
    Machine
    Internet
    Owner
    Encryption

    Confidentiality
    Integrity
    Availability
    Justification of the rating

Category: Usage

    Usage
    Used as client by human
    Multi tenant
    Redundant
    Custom developed parts
    Out of scope
    Justification of out of scope

Category: Data

    Data assets processed
    Data assets stored
    Data formats accepted

Category: Diagram Tweaking

    Diagram tweak order

Category: Communication Links

    Communication links

Category: Tags

    Tags

TODO:

Assets:

- ~~Asset fertig machen mit Styling~~
- ~~Assets speicherbar machen via model~~
- ~~Diagram noch ein TAB mit data~~

  - ~~Das eine tab speicherbar machen~~
  - ~~Die Datenstruktur muss sich ändern, weil wir zur Zeit die daten mit einem Array speichern also [Data1, Data2] und wenn jetzt eins gelöscht wird, dann sind die Indexe Falsch.~~
  - ~~Muss noch ändern, dass anstatt eines clones~~

- ~~Data auswählbar machen~~

~~- Clip zu Trust Boundaries umbennen~~
~~- 4 Rects einfügen mit Namen, siehe Treagile Trust Boundaries~~

~~- Programmieren, falls man die 4 Rects auswählt, dass dann ein bestimmtes Tab aufgeht~~
~~- Programmieren, das er die Elemente in dem Rect als table hat,~~
~~- Nested trust boundaries programmieren~~

- Import Function, yes
  ~~- WebAssembly mit Go, und anfangen eine Methode zu schreiben, die den graphen zurück gibt~~
  ~~- Viz.js benutzen um Koordinaten zu kriegen, indem ein svg~~
  - Die Daten importieren, jetzt wird es Zeit,
  - Neues Tab mit Threats
  - Alle Daten in Objekte schreiben

~~ - Mach alle Koordinaten positiv, damit man fit machen kann~~

~~- Bau waypoints ein~~

~~- Bau farben ein von threagile~~

~~- Bau animation ein, also Fluß~~
~~- Mach die TrustBoundaries dicker,die Linien~~

~~- Schreibe README mit schönen KI generierten Bild~~
~~- Verändere Ordnerstruktur~~

Info:

- Wenn veröffentlichen dann sowas schreiben wie: "Hi CoP-Security, hier ein kleines Urlaubsprojekt von mir, dass Threagile für einige etwas benutzerfreundlich machen soll. <GIF> in der README ein cooles Video
- In der ReadME schreiben, dass keine daten verschickt werden siehe Requests Tab
  "data_assets": {
  "description": "Data assets",
  "type": "object",
  "uniqueItems": true,
  "additionalProperties": {
  "type": "object",
  "properties": {
  "id": {
  "description": "ID",
  "type": "string"
  },
  "description": {
  "description": "Description",
  "type": [
  "string",
  "null"
  ]
  },
  "usage": {
  "description": "Usage",
  "type": "string",
  "enum": [
  "business",
  "devops"
  ]
  },
  "tags": {
  "description": "Tags",
  "type": [
  "array",
  "null"
  ],
  "uniqueItems": true,
  "items": {
  "type": "string"
  }
  },
  "origin": {
  "description": "Origin",
  "type": [
  "string",
  "null"
  ]
  },
  "owner": {
  "description": "Owner",
  "type": [
  "string",
  "null"
  ]
  },
  "quantity": {
  "description": "Quantity",
  "type": "string",
  "enum": [
  "very-few",
  "few",
  "many",
  "very-many"
  ]
  },
  "confidentiality": {
  "description": "Confidentiality",
  "type": "string",
  "enum": [
  "public",
  "internal",
  "restricted",
  "confidential",
  "strictly-confidential"
  ]
  },
  "integrity": {
  "description": "Integrity",
  "type": "string",
  "enum": [
  "archive",
  "operational",
  "important",
  "critical",
  "mission-critical"
  ]
  },
  "availability": {
  "description": "Availability",
  "type": "string",
  "enum": [
  "archive",
  "operational",
  "important",
  "critical",
  "mission-critical"
  ]
  },
  "justification_cia_rating": {
  "description": "Justification of the rating",
  "type": [
  "string",
  "null"
  ]
  }
  },
  "required": [
  "id",
  "description",
  "usage",
  "quantity",
  "confidentiality",
  "integrity",
  "availability"
  ]
  }
  },
