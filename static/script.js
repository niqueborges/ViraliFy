
document.addEventListener("DOMContentLoaded", function () {
  const botao = document.querySelector("button");
  const resultado = document.querySelector("h2");

  botao.addEventListener("click", function () {
    botao.innerText = "⏳ Gerando...";
    botao.disabled = true;
  });

  // Se o resultado já existe na página, rola até ele
  if (resultado) {
    resultado.scrollIntoView({ behavior: "smooth" });
  }
});
