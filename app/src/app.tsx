import { useState, useEffect, FC } from "react";
import { createRoot } from "react-dom/client";
import './assets/style.css';
import AudioPlayer from "react-h5-audio-player";
import 'react-h5-audio-player/lib/styles.css';

interface podcast {
  url: string;
  presenter: string;
  title: string;
  language: string;
}

const App: FC = () => {

  const [isMindMapSelected, setIsMindMapSelected] = useState(false);
  const [iswaiting, setIswaiting] = useState(false);
  const [mindmap, setMindmap] = useState([]);
  const [isPodcastCreated, setIsPodcastCreated] = useState(false);
  const [podcastList, addPodcastList] = useState<podcast[]>([]);
  const [podcast, setPodcast] = useState<podcast>();
  const [selectedVoice, setSelectedVoice] = useState("sarah");
  const [selectedLanguage, setSelectedLanguage] = useState("en");

  useEffect(() => {

    miro.board.ui.on("selection:update", async (event) => {

      if (podcast != null) {
        addPodcastList([...podcastList, podcast]);
      }
      setIsPodcastCreated(false);
      const items = await miro.board.experimental.getSelection();
      setMindmap(items);
      if (items.length === 0) {
        setIsMindMapSelected(false);
      } else {
        setIsMindMapSelected(true);
      }
    }
    );
  }
    , []);



  const handlePodcast = async () => {

    setIswaiting(true);



    await fetch("https://podcast-generator-2.fly.dev/podcast",
      {
        method: "POST",
        body: JSON.stringify({
          mindmap: mindmap,
          presenter_name: selectedVoice,
          podcast_language: selectedLanguage,
          podcast_name: "Techy Talks"
        }),
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then(res => res.json())
      .then((response) => {
        setPodcast(response);
        addPodcastList([response, ...podcastList]);
        setIswaiting(false);
        setIsPodcastCreated(true);
      });


  };



  return (
    <>
      <h1 className="h1 ">Miro Podcast Studio</h1>
      <div
        style={{
          height: "200px",
          width: "100%",
          margin: "0px",
          padding: "0px",
        }}
      >


        {!isPodcastCreated ?
          <>
            <p className="p-large">Select a mind map to create podcast</p>


            <div className="form-group" style={{
              display: "flex",
              flexDirection: "row",
              justifyContent: "center",


            }}>


              <div style={
                {
                  display: "flex",
                  flexDirection: "row",
                  alignItems: "center",
                  justifyContent: "center",
                  height: "100%",
                  width: "100%",
                }

              }>
                <div class="form-group"
                  style={{ padding: "10px" }}
                >
                  <label for="select-1"></label>
                  <select onChange={(e) => setSelectedVoice(e.target.value)} class="select" id="select-1">
                    <option value="sarah">Sarah</option>
                    <option value="ryan">Ryan</option>

                  </select>
                </div>

                <div class="form-group" style={{ padding: "10px" }}>
                  <label for="select-1"></label>
                  <select onChange={(e) => setSelectedLanguage(e.target.value)} class="select" id="select-1">
                    <option value="en">🇺🇸</option>
                    <option value="tr">🇹🇷</option>
                    <option value="de">🇩🇪</option>
                    <option value="fr">🇫🇷</option>
                    <option value="es">🇪🇸</option>
                    <option value="it">🇮🇹</option>
                    <option value="pt">🇵🇹</option>
                  </select>
                </div>
              </div>


            </div>
            <div style={
              {
                display: "flex",
                flexDirection: "column",
                // alignItems: "center",   
                height: "100%",
                width: "100%",
                margin: "0px",
                padding: "0px",
              }
            }>

              {iswaiting ?
                <button className="button button-primary button-loading" style={{ justifyContent: "center", alignItems: "center" }} type="button"></button>
                :
                <button className="button button-primary"
                  style={{ justifyContent: "center", alignItems: "center" }}
                  onClick={handlePodcast}
                  disabled={!isMindMapSelected}
                ><span className="icon-mic-on"></span>
                  Create Podcast</button>
              }
            </div>
          </>
          :

          <div className="app-card" style={{ padding: "5px", margin: '0px' }}>
            <h1 className="app-card--description p-medium">{podcast?.title}</h1>
            <AudioPlayer
              src={podcast?.url}
              onPlay={e => console.log("onPlay")}
            />

          </div>


        }


      </div>

      <div>
        <h2> Previous Podcasts</h2>
        {podcastList.map((podcast) => (
          <div className="app-card" style={{ padding: "5px" }}>
            <h1 class="app-card--description p-medium">{podcast.title}</h1>
            <AudioPlayer
              src={podcast.url}
              onPlay={e => console.log("onPlay")}
            />
          </div>
        ))}



      </div>
    </>

  );
};

const container = document.getElementById("root");
const root = createRoot(container!);
root.render(<App />);