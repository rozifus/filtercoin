#!/bin/bash

TMPL_DIR='./templates'
PART_DIR='./partials'
OUT_DIR='../www'

for f in $(find $TMPL_DIR -name '*.handlebars'); do handlebars $f -f $OUT_DIR/${f}.js; done
for f in $(find $PART_DIR -name '*.handlebars'); do handlebars $f -p -f $OUT_DIR/${f}.js; done
