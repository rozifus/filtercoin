#!/bin/bash

TMPL_DIR='./templates'
OUT_DIR='./www'

for f in $(find $TMPL_DIR -name '*.tmpl'); do handlebars $f -f $OUT_DIR/${f}.js; done
