using Unity.VisualScripting;
using UnityEngine;

public class RunningWalk : MonoBehaviour
{
    
    GameObject man;
    RaycastHit ray;
    bool gamestart;
    
    [SerializeField] float velocity;
    [SerializeField] float distance;
    [SerializeField] float jump_power;

    Rigidbody rb;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        rb = this.gameObject.GetComponent<Rigidbody>();
        gamestart = false;
        man = this.gameObject;
    }

    // Update is called once per frame
    void Update()
    {
        if(gamestart ){
            
            float x = 0;
            float y = 0;
            float z = 0.01f * velocity;

            if(Input.GetAxis("Horizontal") != 0){

                //Debug.Log(Input.GetAxis("Horizontal"));
                x = distance * Input.GetAxis("Horizontal") * Time.deltaTime;
                Debug.Log(x);

            }

            if( Physics.Raycast(transform.position, Vector3.down, out ray, 1.1f)){
                
                if(Input.GetKeyDown("space")){

                    //Debug.Log("jump");
                    rb.AddForce(Vector3.up *jump_power, ForceMode.Impulse);
                }
            }

            man.transform.position += new Vector3(x,y,z);
        
        } else {
            //Debug.Log(Physics.Raycast(transform.position, Vector3.down, out ray, 0.1f));

            if (Physics.Raycast(transform.position, Vector3.down, out ray, 1.1f)){
                gamestart = true;
                Debug.Log("Game Start");
            }
        }

    }
}
