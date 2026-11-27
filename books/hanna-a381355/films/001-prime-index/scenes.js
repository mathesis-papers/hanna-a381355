'use strict';

function hannaHeading(number, heading, opacity) {
  txt(number, W / 2, 150, {size: 32, fam: F.mono, c: C.cyan, a: opacity, align: 'center', ls: 6});
  txt(heading, W / 2, 255, {size: 68, fam: F.orb, w: 700, c: C.white, a: opacity, align: 'center'});
}

function hannaLine(message, y, opacity, colour, size = 49) {
  txt(message, W / 2, y, {size, fam: F.mono, c: colour, a: opacity, align: 'center'});
}

SCENES.open = S => {
  const ready = clamp(S.u / 0.6);
  hannaHeading('01  /  OEIS A381355', 'Choose one coefficient', ready);
  panel(310, 345, W - 620, 380, ready, C.cyan, 'FIRST NONTRIVIAL STEP');
  hannaLine('(1 + x + b x²)³', 465, ready, C.white, 66);
  hannaLine('degree 2:    3b + 3 = 0', 570, at(S, 1, 0.6), C.white);
  hannaLine('b = −1    →    next power: 5', 665, at(S, 2, 0.6), C.now, 43);
};

SCENES.transfer = S => {
  const ready = clamp(S.u / 0.6);
  hannaHeading('02  /  WHY IT WORKS', 'Differentiate and reduce', ready);
  panel(220, 345, W - 440, 400, ready, C.cyan, 'ONLY THE LOW DEGREES MATTER');
  hannaLine('Fᵖ acts like 1 modulo p', 458, at(S, 0, 0.6), C.white, 56);
  hannaLine('degree n  →  degree n − 1', 583, at(S, 1, 0.6), C.now, 55);
  hannaLine('selected coefficient of F′/F  ≡  0 (mod p)', 687, at(S, 2, 0.6), C.white, 43);
};

SCENES.close = S => {
  const ready = clamp(S.u / 0.6);
  hannaHeading('03  /  READ THE RIGHT COEFFICIENT', 'The index matters', ready);
  panel(310, 345, W - 620, 380, ready, C.cyan, 'FIRST TWO MULTIPLES');
  hannaLine('F′/F = 1 − 3x + 10x² + …', 470, ready, C.white, 62);
  hannaLine('−3 is a multiple of 3     10 is a multiple of 5', 580, ready, C.white, 35);
  hannaLine('Step n ≥ 2 reads degree n − 1', 676, at(S, 1, 0.6), C.now, 44);
};
