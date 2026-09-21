#!/usr/bin/env node
'use strict';
// Die aktuelle Nutzeranweisung erlaubt Ausgabe nur unter Lernen/bau.
// Der unveränderte feste Builder wird mit ausschließlich angepasstem Zielpfad ausgeführt.
const fs = require('fs');
const path = require('path');
const Module = require('module');
const original = path.join(__dirname, 'bauen.js');
const source = fs.readFileSync(original, 'utf8');
const expected = "const ziel = path.join(root, 'AP1_Lerndatei.html');";
if (source.split(expected).length !== 2) throw new Error('Erwartete Zieldefinition nicht eindeutig; keine Ausführung.');
const adjusted = source.replace(expected, "const ziel = path.join(root, 'bau', 'AP1_Lerndatei.html');");
const builder = new Module(original, module);
builder.filename = original;
builder.paths = Module._nodeModulePaths(__dirname);
builder._compile(adjusted, original);
