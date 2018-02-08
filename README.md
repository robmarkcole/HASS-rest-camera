# HASS-rest-camera
Custom component for a camera which displays images served by a REST API.

For example, home-assistant serves the images captured by connected cameras [via its REST API](https://home-assistant.io/developers/rest_api/#get-apicamera_proxycameraltentity_id). This component allows you to display those images on a second home-assistant instance. Note that this can be achieved in a number of ways, for example [using the www folder](https://home-assistant.io/components/camera.generic/#local-image-with-hassio), but I felt that using the REST API required the least configuration effort. Furthermore this component should be extendible to work with other image APIs.

Place the custom_components folder [in your configuration directory](https://home-assistant.io/developers/platform_example_sensor/) (or add its contents to an existing custom_components folder). Add to your home-assistant config:

```yaml
camera:
  - platform: rest
    resource: http://192.168.0.28:8123/api/camera_proxy/camera.last_captured_motion
    name: bird-cam
  - platform: rest
    resource: http://192.168.0.28:8123/api/camera_proxy/camera.live_view

```

Configuration variables:

- **resource** (*Required*): The resource or endpoint that serves the image.
- **name** (*Optional*): The name to display.

<p align="center">
<img src="https://github.com/robmarkcole/HASS-rest-camera/blob/master/images/HA_view.png" width="500">
</p>

Here last_captured_motion is displaying the last image captured using the [motion hassio add-on](https://github.com/HerrHofrat/hassio-addons/tree/master/motion), whilst live_view is the live view from the camera. This is a project to count the number and species of bird visiting my bird-feeder. A longer write up is [here](https://github.com/robmarkcole/robins-hassio-config).
