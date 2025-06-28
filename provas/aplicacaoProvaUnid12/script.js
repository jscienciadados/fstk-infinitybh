// Constantes para referenciar elementos HTML
const noteTitleInput = document.getElementById('noteTitle');
const addNoteButton = document.getElementById('addNoteButton');
const notesList = document.getElementById('notesList');
const noNotesMessage = document.getElementById('noNotesMessage');

// Chave para armazenar as notas no localStorage
const LOCAL_STORAGE_KEY = 'notes_app_notes';

// Função para gerar um ID único (simples) para cada nota
function generateUniqueId() {
    return '_' + Math.random().toString(36).substr(2, 9);
}

// Função para salvar as notas no Local Storage
function saveNotes(notes) {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(notes));
}

// Função para carregar as notas do Local Storage
function getNotes() {
    const notesJSON = localStorage.getItem(LOCAL_STORAGE_KEY);
    // Retorna um array vazio se não houver notas salvas
    return notesJSON ? JSON.parse(notesJSON) : [];
}

// Função para exibir as notas na interface
function displayNotes() {
    const notes = getNotes(); // Carrega as notas
    notesList.innerHTML = ''; // Limpa a lista atual

    if (notes.length === 0) {
        noNotesMessage.style.display = 'block'; // Mostra mensagem se não houver notas
    } else {
        noNotesMessage.style.display = 'none'; // Esconde a mensagem
        notes.forEach(note => {
            const listItem = document.createElement('li');
            listItem.setAttribute('data-id', note.id); // Adiciona o ID como atributo de dado

            // Cria o span para o título da nota
            const noteTitleSpan = document.createElement('span');
            noteTitleSpan.textContent = note.title;

            // Cria o botão de remover
            const removeButton = document.createElement('button');
            removeButton.textContent = 'Remover';
            removeButton.addEventListener('click', () => removeNote(note.id)); // Passa o ID para a função de remoção

            listItem.appendChild(noteTitleSpan);
            listItem.appendChild(removeButton);
            notesList.appendChild(listItem);
        });
    }
}

// Função para adicionar uma nova nota
function addNote() {
    const title = noteTitleInput.value.trim();

    if (title) {
        const notes = getNotes(); // Carrega as notas existentes
        
        // Verifica se já existe uma nota com o mesmo título (para garantir unicidade)
        const isDuplicate = notes.some(note => note.title.toLowerCase() === title.toLowerCase());
        if (isDuplicate) {
            alert('Já existe uma nota com este título. Por favor, escolha um título diferente.');
            return; // Sai da função
        }

        const newNote = {
            id: generateUniqueId(), // Gera um ID único
            title: title
        };

        notes.push(newNote); // Adiciona a nova nota ao array
        saveNotes(notes);    // Salva o array atualizado
        noteTitleInput.value = ''; // Limpa o campo de entrada
        displayNotes();      // Atualiza a exibição
    } else {
        alert('Por favor, digite um título para a nota.');
    }
}

// Função para remover uma nota
function removeNote(idToRemove) {
    let notes = getNotes(); // Carrega as notas existentes
    // Filtra o array, mantendo apenas as notas cujo ID não corresponde ao ID a ser removido
    notes = notes.filter(note => note.id !== idToRemove);
    saveNotes(notes);       // Salva o array atualizado
    displayNotes();         // Atualiza a exibição
}

// Event Listeners
addNoteButton.addEventListener('click', addNote);

// Permite adicionar nota pressionando Enter no campo de texto
noteTitleInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        addNote();
    }
});

// Carrega as notas ao carregar a página
document.addEventListener('DOMContentLoaded', displayNotes);