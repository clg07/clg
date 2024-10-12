using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI; // Required for using UI elements like RawImage

public class Scrolling : MonoBehaviour
{
    [SerializeField] RawImage img; // Corrected spelling and type
    public float x;
    public float y;

    // Update is called once per frame
    void Update()
    {
        // Corrected Time.deltaTime
        img.uvRect = new Rect(img.uvRect.position + new Vector2(x, y) * Time.deltaTime, img.uvRect.size);
    }
}
