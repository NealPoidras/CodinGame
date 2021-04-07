using System;

public abstract  class Mammal
{
	private int _numberOfLegs = 0;
	private string _specie = string.Empty;

    public Mammal(){
		_specie = "Unknown";
	}
    
	public Mammal(string specie, int numberOfLegs)
	{
		this._numberOfLegs = numberOfLegs;
		this._specie = specie;
	}

	public int NumberOfLegsS
	{
		get {return _numberOfLegs;}
		set {_numberOfLegs=value;}	
	}

	public string Specie
	{
		get {return _specie;}
		set {_specie=value;}
		
	}
	public abstract void MakeSound();
}

public class Dog : Mammal
{
	public Dog() : base("Dogs", 4)
	{
	}
	public override void MakeSound()
	{
		Console.WriteLine("wuf wuf!!");
	}
}

public class Human : Mammal
{
	private string _name = string.Empty;
	public Human(string name) : base("Humans", 2)
	{
		this._name=name;
	}
	public string Name{
		get {return _name;}
		set {_name=value;}
	}
	public override void MakeSound()
	{
		Console.WriteLine("Hey! My name is "+_name+" and i'm a Human!");
	}
}

class ExecuteInheritance {
	static void Main(string[] args) {
		var d = new Dog();
		var h = new Human("Neal");
		Console.WriteLine("it's a "+d.Specie+" and has "+ d.NumberOfLegs+" legs.");
		Console.WriteLine("it's a "+h.Specie+" and has "+ h.NumberOfLegs+" legs.");		
		d.MakeSound();
		h.MakeSound();
		h.Name = "Clémence";
		h.MakeSound();
		Console.ReadLine();
   }
}

