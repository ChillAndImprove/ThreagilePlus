AssetFormatPanel.prototype.addThreagileMenu = function (container) {
  let self = this;

  let main = document.createElement("div");
  var typeProperties = {
    description: {
      description: "Description",
      type: "button",
      section: "General",
      tooltip: "Provide a brief description of the technology asset. ",
      defaultValue:
        "<This technology asset is responsible for managing the secure transmission of data between client applications and the server infrastructure.>",
    },
    id: {
      description: "Id",
      type: "button",
      section: "General",
      tooltip: "All id attribute values must be unique ",
      defaultValue: "<Your ID>",
    },
    type: {
      description: "Type",
      defaultValue: 0,
      type: "select",
      options: [
        {
          group: "Category 1",
          options: ["external-entity", "process", "datastore"],
          defaultValue: "external-entity",
        },
      ],
      section: "Properties",
      tooltip:
        "",
    },
	  ....
   },
    justification_out_of_scope: {
      description: "Justification out of Scope",
      type: "button",
      section: "Utilization",
      defaultValue:
        "",
      tooltip:
        "Provide justification if the resource is marked as out of scope.",
    },
  };
  let customListener = {
    install: function (apply) {
      this.listener = function () {};
    },
    destroy: function () {},
  };

  {
    let cell = self.editorUi.editor.graph.getSelectionCell();
    for (let property in typeProperties) {
      if (typeProperties.hasOwnProperty(property)) {
        let propertyValue = typeProperties[property];

        if (
          !cell.technicalAsset ||
          cell.technicalAsset[property] === undefined
        ) {
          if (propertyValue.hasOwnProperty("defaultValue")) {
            cell.technicalAsset[property] = propertyValue.defaultValue;
          }
        }
      }
    }
  }
  sections = {};
  for (let property in typeProperties) {
    let sectionName = typeProperties[property].section;
    if (!sections[sectionName]) {
      sections[sectionName] = createSection(sectionName);
    }
    let typeItem = document.createElement("li");
    typeItem.style.display = "flex";
    typeItem.style.alignItems = "baseline";
    typeItem.style.marginBottom = "8px";

    let propertyName = document.createElement("span");
    propertyName.innerHTML = property;
    propertyName.style.width = "100px";
    propertyName.style.marginRight = "10px";

    let propertyType = typeProperties[property].type;

    if (propertyType === "select") {
      const propertySelect = property;
      typeItem.appendChild(propertyName);
      let selectContainer = document.createElement("div");
      selectContainer.style.display = "flex";
      selectContainer.style.alignItems = "center";
      selectContainer.style.marginLeft = "auto";
      let selectDropdown = document.createElement("select");
      selectDropdown.style.width = "100px";
      selectDropdown.title = typeProperties[property].tooltip;
      selectContainer.appendChild(selectDropdown);

      let optionGroups = typeProperties[property].options;
      for (var i = 0; i < optionGroups.length; i++) {
        let optgroup = document.createElement("optgroup");
        optgroup.label = optionGroups[i].group;
        let options = optionGroups[i].options;
        for (let j = 0; j < options.length; j++) {
          let option = document.createElement("option");
          option.value = options[j];
          option.text = options[j];
          optgroup.appendChild(option);
        }
        selectDropdown.appendChild(optgroup);
      }
      let cell = self.editorUi.editor.graph.getSelectionCell();
      if (cell && cell.technicalAsset && cell.technicalAsset[propertySelect]) {
        selectDropdown.selectedIndex = cell.technicalAsset[propertySelect];
      }
      let createChangeListener = function (selectDropdown, propertySelect) {
        return function (evt) {
          var vals = selectDropdown.value;

          if (vals != null) {
            var cells = self.editorUi.editor.graph.getSelectionCells();
            if (cells != null && cells.length > 0) {
              var cell = self.editorUi.editor.graph.getSelectionCell();
              if (!cell.technicalAsset) {
                cell.technicalAsset = {
                  [propertySelect]: selectDropdown.selectedIndex,
                };
              } else {
                cell.technicalAsset[propertySelect] =
                  selectDropdown.selectedIndex;
              }
            }
          }
          mxEvent.consume(evt);
        };
      };
      mxEvent.addListener(
        selectDropdown,
        "change",
        createChangeListener(selectDropdown, propertySelect)
      );
      typeItem.appendChild(selectContainer);
      sections[sectionName].appendChild(typeItem);
    } else if (propertyType === "checkbox") {
      let optionElement = this.createOption(
        property,
        createCustomOption(self, property),
        setCustomOption(self, property),
        customListener
      );
      optionElement.querySelector('input[type="checkbox"]').title =
        typeProperties[property].tooltip;

      sections[sectionName].appendChild(optionElement);
    } else if (propertyType === "button") {
      let button = mxUtils.button(
        property,
        mxUtils.bind(this, function (evt) {
          let cells = self.editorUi.editor.graph.getSelectionCells();
          let cell = cells && cells.length > 0 ? cells[0] : null;
          let dataValue =
            cell && cell.technicalAsset && cell.technicalAsset[property]
              ? cell.technicalAsset[property]
              : typeProperties[property].defaultValue;

          var dlg = new TextareaDialog(
            this.editorUi,
            property + ":",
            dataValue,
            function (newValue) {
              if (newValue != null) {
                if (cell) {
                  if (property === "id") {
                    var adjustedValue = newValue
                      .replace(/</g, "&lt;")
                      .replace(/>/g, "&gt;");
                    let model = self.editorUi.editor.graph.model;
                    model.beginUpdate();
                    try {
                      model.setValue(cell, adjustedValue);

                      self.editorUi.editor.graph.refresh(cell);

                      self.editorUi.editor.graph.refresh();
                    } finally {
                      model.endUpdate();
                    }
                  }
                  if (!cell.technicalAsset) {
                    cell.technicalAsset = {
                      [property]: newValue,
                    };
                  } else {
                    cell.technicalAsset[property] = newValue;
                  }
                }
              }
            },
            null,
            null,
            400,
            220
          );
          this.editorUi.showDialog(dlg.container, 420, 300, true, true);
          dlg.init();
        })
      );
      button.title = typeProperties[property].tooltip;
      button.style.width = "200px";
      typeItem.appendChild(button);
      sections[sectionName].appendChild(typeItem);
    }
  }
  let selects = sections.CIA.querySelectorAll("select");
  selects.forEach(function (select) {
    switch (select.value) {
      case "public":
      case "archive":
        select.style.backgroundColor = "#CCFFCC";
        break;
      case "internal":
      case "operational":
        select.style.backgroundColor = "#99FF99";
        break;
      case "restricted":
      case "important":
        select.style.backgroundColor = "#FFCCCC";
        break;
      case "confidential":
      case "critical":
        select.style.backgroundColor = "#FF9999";
        break;
      case "strictly-confidential":
      case "mission-critical":
        select.style.backgroundColor = "#FF6666";
        break;
      default:
        select.style.backgroundColor = "";
    }

    select.addEventListener("change", function () {
      switch (this.value) {
        case "public":
        case "archive":
          this.style.backgroundColor = "#CCFFCC";
          break;
        case "internal":
        case "operational":
          this.style.backgroundColor = "#99FF99";
          break;
        case "restricted":
        case "important":
          this.style.backgroundColor = "#FFCCCC";
          break;
        case "confidential":
        case "critical":
          this.style.backgroundColor = "#FF9999";
          break;
        case "strictly-confidential":
        case "mission-critical":
          this.style.backgroundColor = "#FF6666";
          break;
        default:
          this.style.backgroundColor = "";
      }
    });
    let options = select.querySelectorAll("option");
    options.forEach(function (option) {
      switch (option.value) {
        case "public":
        case "archive":
          option.style.backgroundColor = "#CCFFCC";
          break;
        case "internal":
        case "operational":
          option.style.backgroundColor = "#99FF99";
          break;
        case "restricted":
        case "important":
          option.style.backgroundColor = "#FFCCCC";
          break;
        case "confidential":
        case "critical":
          option.style.backgroundColor = "#FF9999";
          break;
        case "strictly-confidential":
        case "mission-critical":
          option.style.backgroundColor = "#FF6666";
          break;
      }
    });
  });
  for (let sectionName in sections) {
    main.appendChild(sections[sectionName]);
  }
  // Add Cell Value
  {
    let cells = self.editorUi.editor.graph.getSelectionCells();
    let cell = cells && cells.length > 0 ? cells[0] : null;
    if (!cell.getValue()) {
      let model = self.editorUi.editor.graph.model;
      model.beginUpdate();
      try {
        let newStyle = cell.getStyle() + "verticalAlign=top";
        cell.setStyle(newStyle);
        model.setValue(cell, typeProperties["id"].defaultValue);
        self.editorUi.editor.graph.refresh(cell);
        self.editorUi.editor.graph.refresh();
      } finally {
        model.endUpdate();
      }
    }
  }

  idsData = [];
  // Iterate over the Map and create table rows
  let diagramData = this.editorUi.editor.graph.model.diagramData;
  if (diagramData && diagramData.data_assets) {
    diagramData.data_assets.forEach(function (value, property) {
      idsData.push(value.id);
    });
  }

  let inputElement = document.createElement("input");
  inputElement.placeholder = "Data Processed";
  let cells = self.editorUi.editor.graph.getSelectionCells();
  let cell = cells && cells.length > 0 ? cells[0] : null;

  let sentSection = createSection("Data Processed:");

  sentSection.appendChild(document.createElement("br"));
  if (cell && cell.technicalAsset) {
    inputElement.value = cell.technicalAsset.data_assets_stored;
  } // Append it to body (or any other container)
  sentSection.appendChild(inputElement);
  let tinput = document.querySelector('input[name="input-custom-dropdown"]'),
    // init Tagify script on the above inputs
    tagify = new Tagify(inputElement, {
      whitelist: idsData,
      dropdown: {
        maxItems: 20, // <- mixumum allowed rendered suggestions
        classname: "tags-look", // <- custom classname for this dropdown, so it could be targeted
        enabled: 0, // <- show suggestions on focus
        closeOnSelect: false, // <- do not hide the suggestions dropdown once an item has been selected
      },
    });
  main.appendChild(sentSection);
  let inputElement2 = document.createElement("input");

  let receivedSecion = createSection("Data Stored:");

  receivedSecion.appendChild(document.createElement("br"));
  if (cell && cell.technicalAsset) {
    inputElement2.value = cell.technicalAsset.data_assets_processed;
  } // Append it to body (or any other container)
  receivedSecion.appendChild(inputElement2);
  let tinput2 = document.querySelector('input[name="input-custom-dropdown"]'),
    // init Tagify script on the above inputs
    tagify2 = new Tagify(inputElement2, {
      whitelist: idsData,
      dropdown: {
        maxItems: 20, // <- mixumum allowed rendered suggestions
        classname: "tags-look", // <- custom classname for this dropdown, so it could be targeted
        enabled: 0, // <- show suggestions on focus
        closeOnSelect: false, // <- do not hide the suggestions dropdown once an item has been selected
      },
    });
  main.appendChild(receivedSecion);
  container.appendChild(main);

  return container;
};

