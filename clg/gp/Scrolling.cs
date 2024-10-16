using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class scrolling : MonoBehaviour
{
    [SerializeField] RawImage img;
    public float x;
    public float y;
     
    void Start()
    {
        
    }
    void Update()
    {
        Vector2 A = img.uvRect.position;
        Vector2 B = new Vector2(x,y) * Time.deltaTime;
        Vector2 C = img.uvRect.size;

        img.uvRect = new Rect(A + B,C);
    }
}
