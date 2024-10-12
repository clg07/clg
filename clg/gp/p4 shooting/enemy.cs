using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class enemy : MonoBehaviour{
public float speed;
public Transform bullet;

    // Start is called before the first frame update
    void Start()
    {
      //  player = FindObjectOfType<playermove>().transform;
    }

    // Update is called once per frame
    void Update()
    {
      //  transform.position = Vector2.MoveTowards( transform.position, player.position, speed * Time.deltaTime);
    }

    void OnTriggerEnter2D(Collider2D collision)
    {
       if (collision.CompareTag("bullet"))  
        {
            Destroy(gameObject);
        }
    }
}

