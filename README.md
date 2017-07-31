# opsdroid skill lab location

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to record and request lab member locations. For use with the [lab-location-service](https://github.com/met-office-lab/lab-location-service).

## Requirements

An instance of the [lab-location-service](https://github.com/met-office-lab/lab-location-service).

## Configuration

```yaml
- name: location
  # Required
  auth-token: aabbcc112233  # Auth token set for the lab-location-service
  # Optional
  url: http://localhost:5000  # Url of the lab-location-service server
```

## Usage

#### `I am working from home.`

Sets your location to 'home' in the [lab-location-service](https://github.com/met-office-lab/lab-location-service).

> user: I am working from home.
>
> opsdroid: Ah thanks! I've updated your location to 'Home'.

#### `Where is Bob?`

Tell you where Bob is, if Bob has told opsdroid.

> user: Where is Bob?
>
> opsdroid: Bob is at home.

## License

GNU General Public License Version 3 (GPLv3)
