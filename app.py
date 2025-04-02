import streamlit as st
import random

# --- Configuração da Página ---
st.set_page_config(page_title="Desafio Linfático!", page_icon="💧", layout="wide")

# --- Conteúdo Anatômico (Preciso) ---
def mostrar_conteudo_anatomico():
    st.header("🔬 Revisão Rápida: Anatomia do Sistema Linfático")
    st.markdown("""
    O sistema linfático é uma rede complexa de vasos, tecidos e órgãos que desempenham um papel crucial no **equilíbrio de fluidos** e na **defesa imunológica** do corpo.

    **Componentes Principais:**

    *   **Linfa:** Fluido claro, semelhante ao plasma sanguíneo, mas com menos proteínas. É o líquido intersticial que entra nos capilares linfáticos. Transporta células de defesa (linfócitos), gorduras absorvidas e resíduos celulares.
    *   **Vasos Linfáticos:**
        *   **Capilares Linfáticos:** Vasos microscópicos de fundo cego que coletam a linfa do espaço intersticial. Possuem alta permeabilidade.
        *   **Vasos Coletores:** Formados pela união dos capilares, possuem válvulas para garantir o fluxo unidirecional da linfa. Seguem trajetos semelhantes aos das veias.
        *   **Troncos Linfáticos:** Formados pela união de vasos coletores maiores. Drenam grandes regiões do corpo (ex: Tronco Lombar, Tronco Intestinal, Tronco Subclávio).
        *   **Ductos Linfáticos:** Os maiores vasos linfáticos. Existem dois principais:
            *   **Ducto Torácico (ou Esquerdo):** O maior. Coleta linfa da maior parte do corpo (membros inferiores, abdômen, lado esquerdo do tórax, cabeça, pescoço e membro superior esquerdo). Desemboca na junção da veia subclávia esquerda com a veia jugular interna esquerda.
            *   **Ducto Linfático Direito:** Menor. Coleta linfa do lado direito da cabeça, pescoço, tórax e membro superior direito. Desemboca na junção da veia subclávia direita com a veia jugular interna direita.
    *   **Órgãos Linfóides:**
        *   **Primários (onde linfócitos se desenvolvem e maturam):**
            *   **Medula Óssea Vermelha:** Local de origem de todas as células sanguíneas, incluindo linfócitos B e T. Local de maturação dos linfócitos B.
            *   **Timo:** Localizado no mediastino superior. Essencial para a maturação dos linfócitos T (T de Timo). Atrofia com a idade.
        *   **Secundários (onde ocorrem as respostas imunes):**
            *   **Linfonodos (Gânglios Linfáticos):** Pequenos órgãos em forma de feijão, distribuídos ao longo dos vasos linfáticos. Filtram a linfa, removendo patógenos e detritos. Local de ativação de linfócitos.
            *   **Baço:** O maior órgão linfóide. Filtra o sangue (não a linfa), removendo células sanguíneas velhas e patógenos. Importante na resposta imune contra antígenos sanguíneos.
            *   **Tonsilas (Amígdalas):** Aglomerados de tecido linfóide na entrada da faringe (palatinas, faríngea/adenóide, linguais). Formam um anel de proteção contra patógenos inalados ou ingeridos.
            *   **MALT (Tecido Linfóide Associado à Mucosa):** Agregados difusos de tecido linfóide em mucosas (trato gastrointestinal - Placas de Peyer, respiratório, urinário).

    **Funções Principais:**
    1.  **Drenagem do Excesso de Líquido Intersticial:** Retorna o excesso de fluido e proteínas que extravasam dos capilares sanguíneos de volta para a corrente sanguínea, mantendo o equilíbrio hídrico.
    2.  **Transporte de Gorduras:** Absorve lipídios e vitaminas lipossolúveis do intestino delgado (através dos vasos lactíferos) e os transporta para o sangue.
    3.  **Resposta Imune:** Transporta antígenos para os linfonodos, onde os linfócitos são ativados para iniciar a defesa do corpo.

    Lembre-se: O fluxo da linfa é lento e depende de fatores como contração muscular esquelética, pulsação arterial próxima, movimentos respiratórios e contração da musculatura lisa nas paredes dos vasos linfáticos maiores. **Não há uma bomba central como o coração no sistema circulatório!**
    """)
    # Sugestão: Adicionar uma imagem local
    # st.image("diagrama_linfatico.png", caption="Diagrama simplificado do Sistema Linfático")
    # Para isso, você precisaria ter um arquivo de imagem na mesma pasta do script.

# --- Banco de Perguntas do Quiz ---
perguntas_quiz = [
    {
        "pergunta": "Qual destes é considerado um órgão linfóide primário, principal local de maturação dos linfócitos T?",
        "opcoes": ["Baço", "Linfonodo", "Timo", "Tonsila Palatina"],
        "correta": "Timo",
        "feedback": "Correto! O Timo é essencial para a maturação dos linfócitos T. O Baço, Linfonodos e Tonsilas são órgãos secundários."
    },
    {
        "pergunta": "A maior parte da linfa do corpo é drenada para a circulação venosa através de qual estrutura?",
        "opcoes": ["Ducto Linfático Direito", "Veia Cava Superior", "Cisterna do Quilo", "Ducto Torácico"],
        "correta": "Ducto Torácico",
        "feedback": "Exato! O Ducto Torácico é o maior ducto linfático e drena a linfa da maior parte do corpo para a junção venosa subclávia/jugular interna esquerda."
    },
    {
        "pergunta": "Qual a principal função dos Linfonodos (gânglios linfáticos)?",
        "opcoes": ["Produzir linfa", "Filtrar o sangue", "Filtrar a linfa e ativar linfócitos", "Absorver gorduras do intestino"],
        "correta": "Filtrar a linfa e ativar linfócitos",
        "feedback": "Perfeito! Os linfonodos atuam como filtros para a linfa, removendo patógenos e detritos, e são sítios importantes para o início da resposta imune."
    },
    {
        "pergunta": "O que é a 'Linfa'?",
        "opcoes": ["O mesmo que sangue, mas sem hemácias", "Líquido intersticial que entrou nos capilares linfáticos", "Fluido produzido pelo baço", "Secreção das tonsilas"],
        "correta": "Líquido intersticial que entrou nos capilares linfáticos",
        "feedback": "Isso mesmo! A linfa é essencialmente o fluido que banha as células (líquido intersticial) após ser coletado pelos capilares linfáticos."
    },
    {
        "pergunta": "Qual destes órgãos linfóides secundários é especializado em filtrar o SANGUE, e não a linfa?",
        "opcoes": ["Linfonodo Mesentérico", "Tonsila Faríngea (Adenóide)", "Baço", "Placa de Peyer"],
        "correta": "Baço",
        "feedback": "Correto! O Baço é o grande filtro do sangue no sistema linfático, removendo células velhas e combatendo infecções sanguíneas."
    },
    {
        "pergunta": "O fluxo da linfa nos vasos linfáticos depende principalmente de:",
        "opcoes": ["Batimentos cardíacos", "Contração muscular esquelética e válvulas", "Pressão arterial elevada", "Atividade do timo"],
        "correta": "Contração muscular esquelética e válvulas",
        "feedback": "Exato! Diferente do sangue, a linfa não tem uma bomba central. Seu movimento depende da 'bomba' muscular, respiração e válvulas unidirecionais."
    },
     {
        "pergunta": "As estruturas linfáticas especializadas na absorção de gorduras no intestino delgado são chamadas de:",
        "opcoes": ["Capilares Sanguíneos", "Vasos Lactíferos", "Criptas de Lieberkühn", "Vilosidades Intestinais (em geral)"],
        "correta": "Vasos Lactíferos",
        "feedback": "Muito bem! Os vasos lactíferos são capilares linfáticos especializados presentes nas vilosidades intestinais, responsáveis pela absorção de gorduras (formando o quilo)."
    },
    {
        "pergunta": "Onde se originam os linfócitos B e T antes de sua maturação?",
        "opcoes": ["No Timo", "Nos Linfonodos", "Na Medula Óssea Vermelha", "No Baço"],
        "correta": "Na Medula Óssea Vermelha",
        "feedback": "Correto! Todas as células sanguíneas, incluindo os precursores dos linfócitos B e T, se originam na medula óssea vermelha."
    },
    {
        "pergunta": "Qual o nome do conjunto de tecido linfóide associado às mucosas, como as Placas de Peyer no intestino?",
        "opcoes": ["SALT (Skin-Associated Lymphoid Tissue)", "BALT (Bronchus-Associated Lymphoid Tissue)", "GALT (Gut-Associated Lymphoid Tissue)", "MALT (Mucosa-Associated Lymphoid Tissue)"],
        "correta": "MALT (Mucosa-Associated Lymphoid Tissue)",
        "feedback": "Perfeito! MALT é o termo geral. GALT (intestino), BALT (brônquios), etc., são subtipos de MALT."
    },
    {
        "pergunta": "O Ducto Linfático Direito drena a linfa de qual(is) região(ões) do corpo?",
        "opcoes": ["Todo o lado direito do corpo", "Apenas o membro inferior direito", "Lado direito da cabeça, pescoço, tórax e membro superior direito", "Todo o corpo exceto o membro superior direito"],
        "correta": "Lado direito da cabeça, pescoço, tórax e membro superior direito",
        "feedback": "Exato! O Ducto Linfático Direito é responsável por uma área bem menor que o Ducto Torácico, coletando linfa dessas regiões específicas."
    }
]

# --- Inicialização do Estado do Jogo ---
def inicializar_estado():
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'pergunta_atual_index' not in st.session_state:
        st.session_state.pergunta_atual_index = 0
    if 'quiz_iniciado' not in st.session_state:
        st.session_state.quiz_iniciado = False
    if 'quiz_concluido' not in st.session_state:
        st.session_state.quiz_concluido = False
    if 'resposta_selecionada' not in st.session_state:
        st.session_state.resposta_selecionada = None
    if 'feedback_dado' not in st.session_state:
        st.session_state.feedback_dado = False
    if 'nome_jogador' not in st.session_state:
        st.session_state.nome_jogador = ""
    # Embaralhar as perguntas apenas uma vez no início
    if 'perguntas_embaralhadas' not in st.session_state:
         perguntas_shuffled = random.sample(perguntas_quiz, len(perguntas_quiz))
         st.session_state.perguntas_embaralhadas = perguntas_shuffled

inicializar_estado()

# --- Interface do Usuário ---

st.title("💧 Desafio Linfático: Teste seus Conhecimentos! 💧")
st.markdown("*" "Um quiz interativo para revisar a anatomia do Sistema Linfático." " *")

# --- Seção de Revisão (Expansível) ---
with st.expander("🤓 Quer revisar antes de jogar? Clique aqui!"):
    mostrar_conteudo_anatomico()
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Lymphatic_system_diagram_pt.svg/1024px-Lymphatic_system_diagram_pt.svg.png", caption="Diagrama geral do Sistema Linfático (Fonte: Wikimedia Commons, Autor: Tvanbr)")
    # Nota: Usando imagem da Wikimedia Commons para evitar problemas de direitos autorais.
    # Se tiver uma imagem local melhor/mais detalhada, use st.image("seu_arquivo.png")

st.divider() # Linha divisória

# --- Lógica do Quiz ---

# Botão para iniciar o quiz
if not st.session_state.quiz_iniciado and not st.session_state.quiz_concluido:
    if st.button("🚀 Começar o Quiz!", type="primary"):
        st.session_state.quiz_iniciado = True
        st.rerun() # Reinicia o script para refletir a mudança de estado

# Exibição da pergunta atual
elif st.session_state.quiz_iniciado and not st.session_state.quiz_concluido:
    index_atual = st.session_state.pergunta_atual_index
    total_perguntas = len(st.session_state.perguntas_embaralhadas)
    pergunta_obj = st.session_state.perguntas_embaralhadas[index_atual]

    st.subheader(f"Pergunta {index_atual + 1} de {total_perguntas}")
    st.progress((index_atual + 1) / total_perguntas) # Barra de progresso
    st.markdown(f"**{pergunta_obj['pergunta']}**")

    # Opções de resposta
    # Usamos um 'key' único para o radio baseado no índice da pergunta para evitar conflitos
    opcao_escolhida = st.radio(
        "Escolha sua resposta:",
        options=pergunta_obj['opcoes'],
        index=None, # Nenhuma opção pré-selecionada
        key=f"q_{index_atual}" # Chave única para este widget
    )

    # Botão de confirmação de resposta
    if st.button("Confirmar Resposta", key=f"submit_{index_atual}"):
        if opcao_escolhida:
            st.session_state.resposta_selecionada = opcao_escolhida
            st.session_state.feedback_dado = True
            # Verificar se a resposta está correta
            if opcao_escolhida == pergunta_obj['correta']:
                st.session_state.score += 1
                st.success(f"✅ Correto! {pergunta_obj['feedback']}")
            else:
                st.error(f"❌ Incorreto. A resposta correta é: **{pergunta_obj['correta']}**. {pergunta_obj['feedback']}")

            # Preparar para a próxima pergunta ou finalizar
            if index_atual + 1 < total_perguntas:
                 st.session_state.pergunta_atual_index += 1
            else:
                 st.session_state.quiz_concluido = True

            # Botão para avançar (aparece após confirmar)
            if st.session_state.quiz_concluido:
                st.button("Ver Resultado Final", key="ver_resultado") # A ação real acontece no rerun abaixo
            else:
                st.button("Próxima Pergunta", key="proxima") # A ação real acontece no rerun abaixo

            st.rerun() # Atualiza a interface para mostrar feedback e botão de avançar

        else:
            st.warning("🤔 Por favor, selecione uma resposta antes de confirmar.")


# --- Tela de Resultados Finais ---
elif st.session_state.quiz_concluido:
    st.balloons()
    st.header("🎉 Quiz Concluído! 🎉")
    pontuacao = st.session_state.score
    total_perguntas = len(st.session_state.perguntas_embaralhadas)
    percentual = (pontuacao / total_perguntas) * 100

    st.metric("Sua Pontuação Final:", f"{pontuacao} / {total_perguntas}", f"{percentual:.1f}% de acerto")

    if percentual == 100:
        st.markdown(" Baita Futuro Anatomista! Você gabaritou! Mandou muito bem! 💪")
    elif percentual >= 70:
        st.markdown(" Ótimo trabalho! Você conhece bem o sistema linfático! 👍")
    elif percentual >= 50:
        st.markdown(" Bom esforço! Continue revisando alguns pontos e você chegará lá! 😉")
    else:
        st.markdown(" Parece que precisamos revisar um pouco mais. Use a seção de revisão e tente novamente! 😊")

    st.divider()

    # --- "Competição" Simples (Registro de Nome) ---
    st.subheader("Registre seu Desempenho:")
    nome = st.text_input("Digite seu nome para registrar sua pontuação:", key="nome_jogador_input")

    if nome:
        st.session_state.nome_jogador = nome
        st.success(f"Pontuação de **{st.session_state.nome_jogador}** registrada: **{pontuacao}/{total_perguntas}** pontos.")
        st.info("Professor, peça aos alunos para tirarem um print desta tela ou anotarem o nome e a pontuação!")

    # Botão para reiniciar
    if st.button("Jogar Novamente"):
        # Resetar o estado para um novo jogo
        st.session_state.score = 0
        st.session_state.pergunta_atual_index = 0
        st.session_state.quiz_iniciado = False
        st.session_state.quiz_concluido = False
        st.session_state.resposta_selecionada = None
        st.session_state.feedback_dado = False
        st.session_state.nome_jogador = ""
        # Reembaralhar perguntas para a nova tentativa
        perguntas_shuffled = random.sample(perguntas_quiz, len(perguntas_quiz))
        st.session_state.perguntas_embaralhadas = perguntas_shuffled
        st.rerun()

# --- Rodapé ---
st.divider()
st.caption("Desenvolvido com 🧠 e ❤️ para os futuros experts em anatomia!")