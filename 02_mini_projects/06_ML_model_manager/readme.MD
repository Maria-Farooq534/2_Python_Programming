# ML Model Manager

A small Python OOP practice project that models a simple machine learning model hierarchy.

## Overview

This project demonstrates how object-oriented programming concepts can be applied to represent different types of machine learning models.

### Model Hierarchy

```text
Model
├── Classification
│   ├── DecisionTree
│   └── NeuralNetwork
│
└── Regression
    └── LinearRegression
```

## Concepts Practiced

* Classes and objects
* Instance and class attributes
* Constructors (`__init__`)
* Inheritance
* Multi-level inheritance
* `super()`
* Method overriding
* Polymorphism
* Properties and setters
* Attribute validation
* `__str__()`
* `isinstance()` and `issubclass()`

## Example

Different model objects can be handled uniformly using polymorphism:

```python
models = [tree, neural, linear]

for model in models:
    model.describe()
```

Each model provides its own implementation of `describe()`.

## Purpose

This project was created as hands-on Python practice, with examples designed around machine learning concepts to strengthen Python and OOP skills for ML development.
