using NUnit.Framework;
using UnityEngine;
using System.Collections.Generic;
using System;

public class ButtonController : MonoBehaviour
{
    [SerializeField]
    private List<GameObject> Button;

    public void SetButton()
    {
        foreach (GameObject button in Button) { 
        
            button.SetActive(false);
        }

    }

}
