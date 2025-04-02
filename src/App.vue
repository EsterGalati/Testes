<template>
  <div class="container">
    <img src="@/assets/logo.png" alt="Logo" class="logo" />
    <h1>Busca de Operadoras</h1>

    <div class="search-container">
      <input type="text" v-model="query" placeholder="Digite o nome da operadora" @keyup.enter="buscarOperadoras"
        class="search-input" />
      <button @click="buscarOperadoras" class="search-button">
        Pesquisar
      </button>
    </div>

    <div v-if="loading" class="loading">Carregando...</div>
    <div v-if="error" class="error">{{ error }}</div>

    <div class="results" v-if="resultados.length">
      <div class="card" v-for="operadora in resultados" :key="operadora.CNPJ">
        <h3>{{ operadora.Nome_Fantasia || "Nome não disponível" }}</h3>
        <p><strong>Razão Social:</strong> {{ operadora.Razao_Social }}</p>
        <p><strong>Cidade:</strong> {{ operadora.Cidade }} - {{ operadora.UF }}</p>
        <p><strong>Telefone:</strong> {{ operadora.Telefone || "Não informado" }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      query: "",
      resultados: [],
      loading: false,
      error: null
    };
  },
  methods: {
    async buscarOperadoras() {
      if (!this.query) {
        this.error = "Por favor, digite um termo de busca.";
        return;
      }

      this.loading = true;
      this.error = null;

      try {
        const response = await axios.get(`http://localhost:5000/buscar?q=${this.query}`);
        this.resultados = response.data;
      } catch (err) {
        this.error = "Erro ao buscar dados. Verifique se o servidor está rodando.";
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style>
.container {
  max-width: 600px;
  margin: auto;
  text-align: center;
  font-family: Arial, sans-serif;
}

.logo {
  width: 150px;
  display: block;
  margin: 0 auto 20px;
}

.search-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  margin-bottom: 15px;
}

.search-input {
  width: 75%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 20px;
  outline: none;
  font-size: 16px;
  text-indent: 10px;
  transition: 0.3s;
  background-color: #f9f9f9;
}

.search-input:focus {
  border-color: #666;
  box-shadow: 0 0 5px rgba(102, 102, 102, 0.5);
}

.search-button {
  padding: 10px 15px;
  background-color: #5c85d6;
  color: white;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  font-size: 16px;
  transition: 0.3s;
}

.search-button:hover {
  background-color: #4a74c3;
}

.error {
  color: red;
  font-weight: bold;
  margin-bottom: 10px;
}

.results {
  margin-top: 20px;
}

.card {
  background: #ffffff;
  margin: 10px 0;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  text-align: left;
  border-left: 5px solid #5c85d6;
}

.card h3 {
  color: #5c85d6;
  margin-bottom: 5px;
}
</style>
