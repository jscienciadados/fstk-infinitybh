// Solicita o primeiro número ao usuário
let num1String = prompt("Digite o primeiro número:");

// Verifica se o usuário cancelou a entrada ou digitou algo vazio
if (num1String === null || num1String.trim() === "") {
  console.log("Nenhum primeiro número foi digitado.");
} else {
  // Converte a entrada para um número
  let num1 = parseFloat(num1String);

  // Verifica se a conversão foi bem-sucedida
  if (isNaN(num1)) {
    console.log("O primeiro valor digitado não é um número válido.");
  } else {
    // Solicita o segundo número ao usuário
    let num2String = prompt("Digite o segundo número:");

    // Verifica se o usuário cancelou a entrada ou digitou algo vazio
    if (num2String === null || num2String.trim() === "") {
      console.log("Nenhum segundo número foi digitado.");
    } else {
      // Converte a entrada para um número
      let num2 = parseFloat(num2String);

      // Verifica se a conversão foi bem-sucedida
      if (isNaN(num2)) {
        console.log("O segundo valor digitado não é um número válido.");
      } else {
        // Realiza as operações e exibe os resultados no console

        let resultado = num1; // Inicializa 'resultado' com o primeiro número

        console.log(`Primeiro número: ${num1}`);
        console.log(`Segundo número: ${num2}`);
        console.log("--- Operações ---");

        // Adição
        resultado += num2;
        console.log(`Adição: ${num1} + ${num2} = ${resultado}`);

        // Subtração (redefine 'resultado' para o primeiro número novamente)
        resultado = num1;
        resultado -= num2;
        console.log(`Subtração: ${num1} - ${num2} = ${resultado}`);

        // Multiplicação (redefine 'resultado')
        resultado = num1;
        resultado *= num2;
        console.log(`Multiplicação: ${num1} * ${num2} = ${resultado}`);

        // Divisão (redefine 'resultado')
        resultado = num1;
        if (num2 !== 0) {
          resultado /= num2;
          console.log(`Divisão: ${num1} / ${num2} = ${resultado}`);
        } else {
          console.log("Divisão por zero não é permitida.");
        }

        // Resto da divisão (redefine 'resultado')
        resultado = num1;
        resultado %= num2;
        console.log(`Resto da divisão: ${num1} % ${num2} = ${resultado}`);
      }
    }
  }
}