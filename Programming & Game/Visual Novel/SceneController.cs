using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.UI;

public class SceneController : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    
    [SerializeField] private ButtonController buttonController;
    [SerializeField] private Text Name_Text;
    [SerializeField] private Text Panel_text;
    [SerializeField] private GameObject Panel;
    [SerializeField] private ButtonController btn;

    private string Next;

    
    [Header("Background initial")]
    [Space(10)]
    [SerializeField] private Image BG_Parent;
    [SerializeField] private List<ItemData> Background;
    
    [Header("Char & Ekspression initial")]
    [Space(10)]
    [SerializeField] private List<ItemData> Character;
    
    [Header("Char Container")]
    [Space(10)]
    [SerializeField] private List<CharPosition> Character_Position;
    
    [Header("Plot Game")]
    [Space(10)]
    [SerializeField] TextAsset Game_Plot;
    
    
    private Database Data;
    private bool click;
    private string Dialog;

    private void Awake()
    {
        Data = JsonUtility.FromJson<Database>(Game_Plot.text);
        Next = "000";
        click = false;
    }

    void Start()
    {
        Scene_Manager();
    }

    private void Update()
    {

        if (Input.GetKeyUp(KeyCode.Space))
        {
            Debug.Log("Tombol spasi dilepas!");
            Scene_Manager();    
        }

    }

    private void Scene_Manager()
    {
        StopAllCoroutines();

        if (!click)
        {

            Change_Dialog(Next, click);
        }
        else 
        { 
            Panel_text.text = Dialog;
        }

        click = !click;
    }

    private void Change_Dialog(string key, bool click)
    {
        var entry = Data.Plot.Find(e => e.Key == key);

        foreach (var plot in entry.Entries)
        {
            if (plot.Type == "Teks")
            {

                Name_Text.text = plot.Content.PlayerName;
                    // Panel_text.text = plot.Content.Dialog;
                StartCoroutine(TypeText(Panel_text, plot.Content.Dialog));
                Change_Background(plot.Content.Background);
                Change_Character(plot.Content.Mid, plot.Content.Duo_Right, plot.Content.Duo_Left, plot.Content.Trio_Right, plot.Content.Trio_Left);
                btn.SetButton();

                this.Next = plot.Content.Next;
                this.Dialog = plot.Content.Dialog;
             }
         }

    }

    private void Change_Background( string itemName )
    {
        foreach (var item in Background) 
        {
            if (item.itemName == itemName) {

                BG_Parent.sprite = item.Background;

            }
        }
    }

    private void Change_Character( string char1, string char2, string char3, string char4, string char5)
    {

        List<string> list = new List<string>();
        list.Add(char1);
        list.Add(char2);
        list.Add(char3);
        list.Add(char4);
        list.Add(char5);

        int i = 0;

        foreach (var item in list) {

            if (item != null)
            {
            
                Character_Position[i].image.gameObject.SetActive(true);
                Character_Position[i].image.sprite = Character[0].Background;
                //blur(Character_Position[i].image);       
                StartCoroutine(Shake(Character_Position[i].image.gameObject.GetComponent<RectTransform>()));

            }
            else {

                Character_Position[i].image.gameObject.SetActive(false);
                
            }
            
            i++;
        }

    }

    IEnumerator TypeText( Text uiText, string FullText)
    {

        uiText.text = ""; // Kosongkan teks awalnya
        foreach (char letter in FullText)
        {
            uiText.text += letter; // Tambah huruf satu per satu
            yield return new WaitForSeconds(0.1f); // Tunggu sebelum menambah huruf berikutnya
        }

        click = false;
    }

    private void blur( Image image )
    {
        image.color = new Color(0.3f, 0.3f, 0.3f, 1f);  // Warna hitam penuh (RGBA)
    }

    IEnumerator Shake(RectTransform imageRect)
    {
          // Drag Image ke sini di Inspector
        float duration = 0.5f;     // Durasi getaran
        float magnitude = 10f;
        
        Vector3 originalPos = imageRect.anchoredPosition;
        float elapsedTime = 0f;

        while (elapsedTime < duration)
        {
            float offsetX = Random.Range(-magnitude, magnitude);
            //float offsetY = Random.Range(-magnitude, magnitude);

            imageRect.anchoredPosition = new Vector3(originalPos.x + offsetX, originalPos.y, originalPos.z);

            elapsedTime += Time.deltaTime;
            yield return null;
        }

        // Kembalikan ke posisi semula setelah selesai
        imageRect.anchoredPosition = originalPos;
    }

}



[System.Serializable]
public class Database
{
    public List<PlotEntryWrapper> Plot;
}

[System.Serializable]
public class PlotEntryWrapper
{
    public string Key;
    public List<PlotEntry> Entries;
}


[System.Serializable]
public class PlotData
{
    public Dictionary<string, List<PlotEntry>> Entries;
}

[System.Serializable]
public class PlotEntry
{
    public string Type;
    public PlotContent Content;
}

[System.Serializable]
public class PlotContent
{
    public string PlayerName; // Untuk teks
    public string Dialog;     // Untuk teks
    public string Next;       // Untuk navigasi

    public string Dialog1;    // Untuk button
    public string Dialog2;
    public string Dialog3;
    public string Link1;
    public string Link2;
    public string Link3;

    public string Mid;
    public string Duo_Right;
    public string Duo_Left;
    public string Trio_Right;
    public string Trio_Left;

    public string Background;

}



[System.Serializable]
public class ItemData
{
    public string itemName;
    public Sprite Background;
}

[System.Serializable]
public class CharPosition
{
    public string itemName;
    public Image image;
}

