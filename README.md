# HASS-rest-camera
Custom component for a camera which displays images served by a REST API

Config:
```yaml
camera:
  - platform: rest
    resource: http://192.168.0.28:8123/api/camera_proxy/camera.last_captured_motion
    name: bird-cam
```
