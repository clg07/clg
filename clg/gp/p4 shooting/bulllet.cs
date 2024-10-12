using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bulllet : MonoBehaviour
{
    public Transform bullets;
    public float speed;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.Translate(Vector3.up * speed * Time.deltaTime);
    }

    public void OnTriggerEnter2D(Collider2D collision)
    {
        if(collision.tag == "enemy")
        {
            Destroy(gameObject);
        }
    }
}
