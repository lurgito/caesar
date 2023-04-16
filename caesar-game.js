function encryptMessage() {
  const shift = parseInt(document.getElementById('shift-input').value);
  const message = document.getElementById('message-input').value;
  const encryptedMessage = caesarCipher(message, shift);
  document.getElementById('game-message').innerHTML = encryptedMessage;
}

function decryptMessage() {
  const shift = parseInt(document.getElementById('shift-input').value);
  const message = document.getElementById('message-input').value;
  const decryptedMessage = caesarCipher(message, -shift);
  document.getElementById('game-message').innerHTML = decryptedMessage;
}

function caesarCipher(str, shift) {
  return str
      .split('')
      .map(char => shiftChar(char, shift))
      .join('');
}

function shiftChar(char, shift) {
  const code = char.charCodeAt();
  if (code >= 65 && code <= 90) {
      return String.fromCharCode(((code - 65 + shift) % 26) + 65);
  }
  if (code >= 97 && code <= 122) {
      return String.fromCharCode(((code - 97 + shift) % 26) + 97);
  }
  return char;
}
