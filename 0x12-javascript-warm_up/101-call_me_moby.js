#!/usr/bin/node
function callMeMoby (x, theFunction) {
  for (i = 0; i < x; i++) {
    theFunction();
  }
}
exports.callMeMoby = callMeMoby;
