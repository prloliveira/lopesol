<script>
    // You can add your Svelte script logic here
  </script>
  
  <style>
    /* You can add custom styles here if needed */
  </style>
  
  <main class="bg-gray-100 text-gray-900 min-h-screen flex flex-col items-center justify-center">
    <header class="bg-white shadow-md w-full py-4">
      <div class="container mx-auto flex justify-between items-center">
        <h1 class="text-2xl font-bold text-gray-800">Limpeza Setúbal</h1>
        <nav>
          <a href="#sobre" class="text-gray-600 hover:text-gray-800 mx-2">Sobre</a>
          <a href="#serviços" class="text-gray-600 hover:text-gray-800 mx-2">Serviços</a>
          <a href="#contato" class="text-gray-600 hover:text-gray-800 mx-2">Contato</a>
        </nav>
      </div>
    </header>
  
    <section class="text-center py-16 px-4" id="sobre">
      <h2 class="text-3xl font-semibold mb-4">Bem-vindo à Lopesol</h2>
      <p class="text-lg mb-8">Somos uma empresa de limpeza dedicada a manter o ambiente de trabalho das empresas na cidade de Setúbal impecável. Oferecemos serviços de alta qualidade para garantir a satisfação dos nossos clientes.</p>
      <a href="#contato" class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600">Solicite um Orçamento</a>
    </section>
  
    <section class="bg-gray-200 py-16 px-4" id="serviços">
      <div class="container mx-auto text-center">
        <h2 class="text-3xl font-semibold mb-8">Nossos Serviços</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div class="bg-white p-6 rounded-lg shadow-md">
            <h3 class="text-xl font-bold mb-4">Limpeza de Escritórios</h3>
            <p>Serviço completo de limpeza para manter seu escritório sempre limpo e organizado.</p>
          </div>
          <div class="bg-white p-6 rounded-lg shadow-md">
            <h3 class="text-xl font-bold mb-4">Limpeza Pós-Obra</h3>
            <p>Remoção de resíduos e sujeira após a realização de obras para deixar o espaço pronto para uso.</p>
          </div>
          <div class="bg-white p-6 rounded-lg shadow-md">
            <h3 class="text-xl font-bold mb-4">Limpeza de Áreas Comuns</h3>
            <p>Manutenção e limpeza regular das áreas comuns de prédios e empresas.</p>
          </div>
        </div>
      </div>
    </section>
  
    <section class="text-center py-16 px-4" id="contato">
      <h2 class="text-3xl font-semibold mb-4">Entre em Contato</h2>
      <p class="text-lg mb-8">Para mais informações ou para solicitar um orçamento, entre em contato conosco.</p>
      <a href="mailto:angelicacosta008@gmail.com" class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600">Enviar Email</a>
    </section>
  
    <footer class="bg-gray-800 text-white py-4 w-full text-center">
      <p>&copy; 2024 Lopesol. Todos os direitos reservados.</p>
    </footer>
  </main>
  