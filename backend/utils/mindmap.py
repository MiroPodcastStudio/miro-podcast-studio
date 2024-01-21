import logging
from bs4 import BeautifulSoup
from openai import OpenAI
from core.settings import settings

class MindMap:
    def __init__(self, mindmap):
        self.mindmap = mindmap
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

        self.prompts = {
            "en": "Use English rest of the text.I have a mind map, I want to create a podcast from the following mindmap.  Act as a podcast presenter called {presenter_name} from {podcast_name} and creat podcast transcript. I will use your output to create a podcast. Use friendly lang:. Don't include additional text only content to read. It should be less than 1 minute. Dont use too long transcript.",
            "tr": "Bu metnin tamamında türkçe kullan gerekirse çevir.Bir zihin haritam var, aşağıdaki zihin haritasından bir podcast oluşturmak istiyorum. {presenter_name} adlı bir podcast sunucusu olarak {podcast_name} ve podcast metni oluşturun. Çıktınızı bir podcast oluşturmak için kullanacağım. Kullanıcı dostu lang kullanın:. Okunacak ek metin içeriği eklemeyin. 1 dakikadan az olmalı. Çok uzun metin kullanmayın.",
            "fr": "Utilisez le reste du texte en french.J'ai une carte mentale, je veux créer un podcast à partir de la carte mentale suivante. Agissez en tant qu'animateur de podcast appelé {presenter_name} de {podcast_name} et créez une transcription de podcast. J'utiliserai votre sortie pour créer un podcast. Utilisez lang amical:. N'incluez pas de contenu texte supplémentaire à lire. Il doit être inférieur à 1 minute. N'utilisez pas de transcription trop longue.",
            "de": "Verwenden Sie den Rest des Textes in Deutsh.Ich habe eine Mindmap, ich möchte einen Podcast aus der folgenden Mindmap erstellen. Treten Sie als Podcast-Moderator namens {presenter_name} von {podcast_name} auf und erstellen Sie eine Podcast-Transkription. Ich werde Ihre Ausgabe verwenden, um einen Podcast zu erstellen. Verwenden Sie freundliche Sprache:. Fügen Sie keinen zusätzlichen Textinhalt zum Lesen hinzu. Es sollte weniger als 1 Minute dauern. Verwenden Sie keine zu lange Transkription.",
            "es": "Use el resto del texto en espanol.Tengo un mapa mental, quiero crear un podcast a partir del siguiente mapa mental. Actúe como presentador de podcast llamado {presenter_name} de {podcast_name} y cree una transcripción de podcast. Usaré su salida para crear un podcast. Use lang amigable:. No incluya contenido de texto adicional para leer. Debe ser inferior a 1 minuto. No use una transcripción demasiado larga.",
            "pt": "Use o restante do texto em portugues.Tenho um mapa mental, quero criar um podcast a partir do seguinte mapa mental. Atue como apresentador de podcast chamado {presenter_name} de {podcast_name} e crie uma transcrição de podcast. Usarei sua saída para criar um podcast. Use lang amigável:. Não inclua conteúdo de texto adicional para ler. Deve ser inferior a 1 minuto. Não use uma transcrição muito longa.",
            "it": "Usa il resto del testo in italiano.Ho una mappa mentale, voglio creare un podcast dalla seguente mappa mentale. Fai il moderatore del podcast chiamato {presenter_name} di {podcast_name} e crea una trascrizione del podcast. Utilizzerò la tua uscita per creare un podcast. Usa lang amichevole:. Non includere contenuti di testo aggiuntivi da leggere. Dovrebbe essere inferiore a 1 minuto. Non utilizzare una trascrizione troppo lunga."
        }

    def get_children(self, node_id):
        return [node for node in self.mindmap if node['parentId'] == node_id]

    def get_root_node(self):
        return [node for node in self.mindmap if node['parentId'] == None][0]

    def get_text(self, text):
        return BeautifulSoup(text, "html.parser").text

    def parents_of(self, node):
        if node['parentId'] == None:
            return []
        else:
            return [self.get_text(node["nodeView"]["content"])] + self.parents_of([parent for parent in self.mindmap if parent['id'] == node['parentId']][0])

    def export_to_str(self):
        terminal_nodes = ''

        for node in self.mindmap:
            if len(self.get_children(node['id'])) == 0:
                terminal_nodes += (",".join(list([self.get_text(self.get_root_node()[
                                   "nodeView"]["content"])]+list(reversed(self.parents_of(node))))))+'\n'

        return terminal_nodes

    def create_podcast_text(self, mindmap_csv, presenter_name, podcast_name, podcast_language="en"):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": self.prompts[podcast_language].format(presenter_name=presenter_name, podcast_name=podcast_name)},
                {"role": "user", "content": mindmap_csv}
            ],
            model="gpt-3.5-turbo",
        )
        return chat_completion.choices[0].message.content[:500]

    def create_podcast_title(self, podcast_text):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Create a title for the podcast. It should be less than 7 words. Only provide the title."},
                {"role": "user", "content": podcast_text}
            ],
            model="gpt-3.5-turbo",
        )
        return chat_completion.choices[0].message.content

