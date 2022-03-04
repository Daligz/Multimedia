using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class main : MonoBehaviour
{

    private AudioSource audio { get { return GetComponent<AudioSource>(); } }
    public AudioClip wuau;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {

    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.tag == "Pastel")
        {
            print("Chocaste con el pastel");
        } else if (other.gameObject.tag == "cheems")
        {
            print("Chocaste de nuevo");
            audio.PlayOneShot(wuau);
        }
    }
}
