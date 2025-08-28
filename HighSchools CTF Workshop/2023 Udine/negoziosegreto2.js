var messaggio = "=03ZulmclVmbpdmbl9VZzJXZ2Vmcf9GdhRnblZXak9VZf9GdzVWdxt3ZhxmZ";

function decodifica(msg) {
  msg = msg.split("").reverse().join("");
  msg = Buffer.from(msg, "base64").toString("utf-8"); 
  console.log(msg);
}

decodifica(messaggio);

// flag{questo_e_diventato_reverse_engineering}