using UnityEngine;

public class FactoryManager
{
    private CarFactory carFactory;
    private PersonFactory personFactory;
    private static FactoryManager _instance;
    public static FactoryManager Instance
    {
        get
        {
            if (_instance == null)
            {
                _instance = new FactoryManager();
            }
            return _instance;
        }
    }

    public FactoryManager()
    {
        carFactory = new CarFactory();
        personFactory = new PersonFactory();
    }

    public GameObject CreateCar(string carId, Vector3 position, Quaternion rotation)
    {
        return carFactory.CreateObject(carId, position, rotation);
    }

    public GameObject CreatePerson(string personId, Vector3 position, Quaternion rotation)
    {
        return personFactory.CreateObject(personId, position, rotation);
    }
}
