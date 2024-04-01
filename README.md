# HeadLight Sensor

This Python class simulates the behavior of headlights turning on and off based on the chance of nightfall and morning. It can be used to model the automatic switching of headlights in vehicles.

## Usage

1. Instantiate a `HeadLight` object:
    ```python
    head = HeadLight()
    ```

2. Use the `light_tuned_on` method to simulate turning on the headlights based on the chance of nightfall. It returns `True` if the headlights are turned on, otherwise `False`:
    ```python
    is_light_on = head.light_tuned_on(chance_to_night)
    ```

3. Use the `light_turned_off` method to simulate turning off the headlights based on the chance of morning. It returns `True` if the headlights are turned off, otherwise `False`:
    ```python
    is_light_off = head.light_turned_off(chance_to_morning)
    ```

## Example

```python
head = HeadLight()
night_chance = 0.4
morning_chance = 0.4

is_light_on = head.light_tuned_on(night_chance)
is_light_off = head.light_turned_off(morning_chance)

print("Headlights are on:", is_light_on)
print("Headlights are off:", is_light_off)
