using System;
using UnityEngine;
using UnityEngine.AI;

public class NPCCarNavigation : MonoBehaviour
{
    [HideInInspector]
    public NavMeshAgent agent;
    [HideInInspector]
    public bool isArrive;
    public Action Arrive;

    void Awake()
    {
        agent = this.GetComponent<NavMeshAgent>();
    }

    public void SetDestination(Transform pos)
    {
        agent.destination = pos.position;//自动导航
    }

    void Update()
    {
        if (!agent.pathPending && agent.remainingDistance < 0.5f && !isArrive)
        {
            isArrive = true;
            Arrive?.Invoke();
        }
    }

    /// <summary>
    /// TODO 对象池
    /// </summary>
    public void Pool()
    {
        Destroy(gameObject);
    }
}
