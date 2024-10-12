using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class gunrotate : MonoBehaviour
{
    public Transform guntip;
    public float offset;
    public Transform gun;
    public GameObject bullet;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        Vector3 displacement = gun.position - Camera.main.ScreenToWorldPoint(Input.mousePosition);
        float angle = Mathf.Atan2(displacement.y, displacement.x) * Mathf.Rad2Deg;
        gun.rotation = Quaternion.Euler(0f , 0f , angle + offset);
        if(Input.GetMouseButtonDown(0)){
            Instantiate(bullet , guntip.position, guntip.rotation);
        }
    }
}
