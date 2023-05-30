// Datenstruktur für den Knoten
var nodeData = {
  id: 'customer-client',
  description: 'Customer Web Client',
  type: 'external-entity',
  usage: 'business',
  used_as_client_by_human: true,
  out_of_scope: true,
  justification_out_of_scope: 'Owned and managed by enduser customer',
  size: 'component',
  technology: 'browser',
  // ...
  // Weitere Eigenschaften des Knotens
};

// SVG-Container erstellen
var svg = d3.select('#svg-container')
  .attr('width', 400)
  .attr('height', 400);

// Knoten erstellen
var node = svg.append('circle')
  .attr('cx', 100)
  .attr('cy', 100)
  .attr('r', 50)
  .attr('fill', 'blue')
  .on('click', function() {
    // Knoteninformationen anzeigen und bearbeiten
    showNodeInformation(nodeData);
  });

// Funktion zum Anzeigen und Bearbeiten der Knoteninformationen
function showNodeInformation(data) {
  // Hier können Sie eine benutzerdefinierte Modaldialog-Box, eine Seitenleiste oder eine andere Art der Anzeige erstellen

  // Beispiel: Ein Modaldialog-Box mit einem Formular
  var modal = d3.select('body')
    .append('div')
    .attr('class', 'modal');

  modal.append('h2')
    .text('Knoteninformationen');

  var form = modal.append('form');

  // ID
  form.append('label')
    .text('ID:');
  form.append('input')
    .attr('type', 'text')
    .attr('value', data.id);

  // Beschreibung
  form.append('label')
    .text('Beschreibung:');
  form.append('textarea')
    .text(data.description);

  // Weitere Eigenschaften des Knotens

  // Typ
  form.append('label')
    .text('Typ:');
  form.append('input')
    .attr('type', 'text')
    .attr('value', data.type);

  // Nutzung
  form.append('label')
    .text('Nutzung:');
  form.append('input')
    .attr('type', 'text')
    .attr('value', data.usage);

  // Verwendet von Menschen
  form.append('label')
    .text('Verwendet von Menschen:');
  form.append('input')
    .attr('type', 'checkbox')
    .property('checked', data.used_as_client_by_human);

  // Außerhalb des Scopes
  form.append('label')
    .text('Außerhalb des Scopes:');
  form.append('input')
    .attr('type', 'checkbox')
    .property('checked', data.out_of_scope);

  // Begründung für außerhalb des Scopes
  form.append('label')
    .text('Begründung für außerhalb des Scopes:');
  form.append('textarea')
    .text(data.justification_out_of_scope);

  // Größe
  form.append('label')
    .text('Größe:');
  form.append('input')
    .attr('type', 'text')
    .attr('value', data.size);

  // Technologie
  form.append('label')
    .text('Technologie:');
  form.append('input')
    .attr('type', 'text')
    .attr('value', data.technology);

  // Weitere Eigenschaften des Knotens

  // Speichern-Button
  form.append('button')
    .attr('type', 'submit')
    .text('Speichern')
    .on('click', function() {
      // Funktion zum Speichern der bearbeiteten Informationen aufrufen
      saveNodeInformation();
    });

  // Schließen-Button
  form.append('button')
    .attr('type', 'button')
    .text('Schließen')
    .on('click', function() {
      // Modaldialog-Box schließen
      modal.remove();
    });
}

// Funktion zum Speichern der bearbeiteten Knoteninformationen
function saveNodeInformation() {
  // Hier können Sie den Code hinzufügen, um die bearbeiteten Informationen zu speichern
  // und den Knoten entsprechend zu aktualisieren

  // Beispiel:
  var modal = d3.select('.modal');
  var id = modal.select('input[type="text"]').node().value;
  var description = modal.select('textarea').node().value;

  // Aktualisierte Informationen auf den Knoten anwenden
  nodeData.id = id;
  nodeData.description = description;

  // Knoten aktualisieren
  node.attr('fill', 'red');

  // Modaldialog-Box schließen
  modal.remove();
}
