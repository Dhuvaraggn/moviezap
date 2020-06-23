<html itemscope="" itemtype="http://schema.org/WebPage" lang="en-IN">
 <body>
 
<center>
  <form id="f1" action='' method="POST">
    {% csrf_token %}
    <center>
        <h1>
        MovieZap Search Engine
        </h1>
      </center>
       
          
          <input  style="box-shadow:         3px 3px 5px 6px lightcoral;border-radius:20px;border:5px solid red; font-size:25px;width:450px;height:50px;border-left-width:900px;line-height:1px;border-width:5px" aria-autocomplete="both" aria-haspopup="false" aria-label="Search" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" class="gLFyf gsfi" data-ved="0ahUKEwiNy5fJ15LqAhUIzzgGHQkVC1IQ39UDCAQ" jsaction="paste:puy29d" maxlength="2048" name="search" onsearch="submitse()" placeholder="MovieZap Search" role="combobox" spellcheck="false" title="Search" type="search" value=""/>
          
          
          
        
  <div style="width:480px;height:50px;">  
      </center>
       <center><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>title</th>
      <th>language</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Apur Sansar</td>
      <td>Bengali, English</td>
      <td>1959</td>
    </tr>
    <tr>
      <td>Aparajito</td>
      <td>Bengali, English</td>
      <td>1956</td>
    </tr>
    <tr>
      <td>Ahí está el detalle</td>
      <td>Spanish</td>
      <td>1940</td>
    </tr>
    <tr>
      <td>All About Eve</td>
      <td>English, French</td>
      <td>1950</td>
    </tr>
    <tr>
      <td>A Face in the Crowd</td>
      <td>English</td>
      <td>1957</td>
    </tr>
  </tbody>
</table></center><div style="height:50px;">
</div>
      
    <center> 
      <input style="box-shadow:         3px 3px 5px 6px lightslategray;"class="gNO89b" aria-label="Google Search" name="btnK" type="submit" data-ved="0ahUKEwjbk4ul5orqAhX0xzgGHYlmAREQ4dUDCAo" value="MovieZap Search"> </input> 
    </center>
  </form> 
  <div style="width:480px;height:90px;">
  </div>

  <form action="/top/" class="tsf nj" data-submitfalse="q" id="tsf" method="POST" name="f" role="search" style="overflow:visible">
    {% csrf_token %}
    <div class="content" id="main">
    <span class="ctr-p" id="body">
      <center>
      <div data-responsive-height-resize="536" data-responsive-min-height="100" data-responsive-min-width="980" id="lga" jsaction="rcuQ6b:npT2md" jscontroller="cvn5cb" style="height: 100px;">
        <h1>
        MovieZap Top50
        </h1>
        <label  for="years">
        Choose a decade:
        </label>
          <select style="box-shadow:         3px 3px 5px 6px lightcoral;border-radius:20px;border:5px solid red;" id="year" name="year">
          <option value="2000">
            2000-present
          </option>
          <option value="1980">
            1980-2000
          </option>
          <option value="1960">
            1960-1980
          </option>
          <option value="1940">
            1940-1960
          </option>
          <option value="1900">
            1900-1940
          </option>
        </select>

        <label  for="genre">
        Choose a genre:
        </label>
        <select style="box-shadow:         3px 3px 5px 6px lightcoral;border-radius:20px;border:5px solid red;" id="genre" name="genre">
            <option value="Drama">
              Drama
            </option>
            <option value="Comedy">
                Comedy
              </option>
              <option value="Action">
                Action
              </option>
              <option value="Romance">
                Romance
              </option>
              <option value="Mystery">
                  Mystery
                </option>
            <option value="Horror">
                Horror
            </option>
            <option value="Animation">
                Animation
              </option>
            <option value="Fantasy">
              Fantasy
            </option>
            <option value="Sci-Fi">
              Sci-Fi
            </option>
            <option value="Thriller">
                Thriller
              </option>
            <option value="Crime">
                Crime
              </option>
              <option value="Film-Noir">
                  Film-Noir
                </option>
              <option value="Musical">
              Musical
                </option>
                <option value="Sport">
                    Sport
                  </option>
                <option value="Adventure">
                    Adventure
                  </option>
                  <option value="Biography">
                      Biography
                      </option>
                <option value="History">
                  History
                  </option>
                  <option value="War">
                      War
                    </option>
                  <option value="Western">
                    Western
                      </option>
                        
        </select>
        <label  for="lang">
        Choose a languague:
        </label>
        <select style="border-radius:20px;border:5px solid red;" id="lang" name="lang">
              <option value="English">
                English
              </option>
              <option value="Tamil">
                Tamil
              </option>
              <option value="Malayalam">
                Malayalam
              </option>
              <option value="Hindi">
                Hindi
              </option>
              <option value="Bengali">
                Bengali
              </option>
              <option value="Marathi">
                Marathi
              </option>
              <option value="Persian">
                Persian
              </option>
              <option value="French">
                French
              </option>
              <option value="Spanish">
                Spanish
              </option>
              <option value="Japanese">
                Japanese
              </option>
              <option value="Italian">
                Italian
              </option>
              <option value="Kurdish">
                Kurdish
              </option>
              <option value="German">
                  German
              </option>
              <option value="Russian">
                Russian
              </option>
              <option value="Arabic">
                Arabic
              </option>
              <option value="Urdu">
                Urdu
              </option>
        </select>
      </div>
        <center>
          <div style="width: 1000px;height: 100px;"></div>
        </center>
        <center>
       
          <center style="padding-left: 10px;">
          </center>
          <input style="box-shadow:         3px 3px 5px 6px lightslategray;"aria-label="Google Search" class="gNO89b" data-ved="0ahUKEwjbk4ul5orqAhX0xzgGHYlmAREQ4dUDCAo" name="btnK" type="submit" value="MovieZap Top50"/>
          <input style="box-shadow:         3px 3px 5px 6px lightslategray;;"aria-label="I'm Feeling Lucky" class="RNmpXc" data-ved="0ahUKEwjbk4ul5orqAhX0xzgGHYlmAREQ19QECAs" jsaction="sf.lck" name="btnI" type="submit" value="I'm Feeling Lucky"/>
          <div style="height:100px">
    
          </div>
        </center>
      </center>
    </span>
    </div>
  </form>

  <div style="width:480px;height:60px;">
  </div>

  <div style="margin-top:12px">
    <center>

      <center>
        MovieZap offered languages:
        <a>
        english
        </a>
        <a>
        हिन्दी
        </a>
        <a>
        বাংলা
        </a>
        <a>
        తెలుగు
        </a>
        <a>
        தமிழ்
        </a>
        <a>
        ಕನ್ನಡ
        </a>
        <a>
        മലയാളം
        </a>
        <a>
        ਪੰਜਾਬੀ
        </a>
      </center>
    </center>
  </div>

</form>
</body>
</html>