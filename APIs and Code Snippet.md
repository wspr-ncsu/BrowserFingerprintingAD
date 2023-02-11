# Seed Fingerprinting API List

| API Name    |
| ----------- |
| AudioParam.setValueAtTime |
| CanvasRenderingContext2D.arc |
| CanvasRenderingContext2D.fill |
| CanvasRenderingContext2D.fillText |
| DynamicsCompressorNode.connect |
| Geolocation.getCurrentPosition |
| Geolocation.watchPosition |
| Navigator.appCodeName |
| Navigator.appName |
| Navigator.cookieEnabled |
| Navigator.doNotTrack |
| Navigator.getBattery |
| Navigator.hardwareConcurrency |
| Navigator.javaEnabled |
| Navigator.language |
| Navigator.languages |
| Navigator.mimeTypes |
| Navigator.platform |
| Navigator.plugins |
| Navigator.productSub |
| Navigator.vendor |
| Navigator.vendorSub |
| OfflineAudioContext.createDynamicsCompressor |
| OfflineAudioContext.createOscillator |
| OscillatorNode.frequency |
| Screen.colorDepth |
| Screen.height |
| Screen.orientation |
| Screen.pixelDepth |
| Screen.width |
| WebGL2RenderingContext.canvas |
| WebGL2RenderingContext.getExtension |
| WebGL2RenderingContext.getParameter |
| WebGLRenderingContext.canvas |
| Window.devicePixelRatio |


# Sink API List

| API Name    |
| ----------- |
| Client.postMessage |
| DedicatedWorkerGlobalScope.postMessage |
| Document.cookie |
| IDBObjectStore.add |
| IDBObjectStore.put |
| MessagePort.postMessage |
| Navigator.sendBeacon |
| RTCDataChannel.send |
| ServiceWorker.postMessage |
| WebSocket.send |
| Window.indexedDB |
| Window.localStorage |
| Window.openDatabase |
| Window.postMessage |
| Window.sessionStorage |
| Worker.postMessage |
| XMLHttpRequest.send |


# FP_APIs

| API Name    |Documentation  |  Proof | Deployed(T/F) |
| ----------- | ----------- | ----------- | ----------- |
| AudioBuffer.getChannelData   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/AudioBuffer/getChannelData)   |[1](https://audiofingerprint.openwpm.com/)   |  T    |
| BatteryManager.charging   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/BatteryManager/charging)   |[1](https://browserleaks.com/javascript)   |  T    |
| BatteryManager.chargingTime   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/BatteryManager/chargingTime)   |[1](https://browserleaks.com/javascript)   |  T    |
| BatteryManager.dischargingTime   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/BatteryManager/dischargingTime)   |[1](https://browserleaks.com/javascript)   |  T    |
| BatteryManager.level   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/BatteryManager/level)   |[1](https://browserleaks.com/javascript), [2](https://privacycheck.sec.lrz.de/active/fp_css/fp_css.html)   |  T    |
| CSSRuleList.length   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CSSRuleList)   |[1](https://csstracking.dev/), [2](https://privacycheck.sec.lrz.de/active/fp_css/fp_css.html)   |  F    |
| CSSStyleDeclaration.cssText   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration/cssText)   |[1](https://csstracking.dev/), [2](https://privacycheck.sec.lrz.de/active/fp_css/fp_css.html)   |  F    |
| CSSStyleDeclaration.getPropertyValue   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration/getPropertyValue)   |[1](https://csstracking.dev/), [2](https://privacycheck.sec.lrz.de/active/fp_css/fp_css.html)   |  F    |
| CSSStyleDeclaration.setProperty   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration/setProperty)   |[1](https://csstracking.dev/), [2](https://privacycheck.sec.lrz.de/active/fp_css/fp_css.html)   |  F    |
| CSSStyleSheet.cssRules   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleSheet/cssRules)   |[1](https://csstracking.dev/), [2](https://privacycheck.sec.lrz.de/active/fp_css/fp_css.html)   |  F    |
| CSSStyleSheet.insertRule   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleSheet/insertRule)   |[1](https://csstracking.dev/), [2](https://privacycheck.sec.lrz.de/active/fp_css/fp_css.html)   |  F    |
| CanvasGradient.addColorStop   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasGradient/addColorStop)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.beginPath   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/beginPath)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.bezierCurveTo   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/bezierCurveTo)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.canvas   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/canvas)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.clearRect   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/clearRect)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.clip   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/clip)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.closePath   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/closePath)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.createLinearGradient   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/createLinearGradient)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.createRadialGradient   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/createRadialGradient)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.ellipse   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/ellipse)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.fillRect   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/fillRect)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.getImageData   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/getImageData)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.isPointInPath   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/isPointInPath)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.lineTo   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/lineTo)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.measureText   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/measureText)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.moveTo   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/moveTo)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.quadraticCurveTo   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/quadraticCurveTo)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.rect   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/rect)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.restore   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/restore)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.rotate   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/rotate)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.save   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/save)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.stroke   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/stroke)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.strokeText   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/strokeText)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| CanvasRenderingContext2D.translate   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/translate)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| Crypto.getRandomValues   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Crypto.subtle   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/subtle)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| DOMRect.width   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/width)   |[1](https://privacycheck.sec.lrz.de/active/fp_gcr/fp_getclientrects.html)   |  F    |
| DOMRect.y   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/y)   |[1](https://privacycheck.sec.lrz.de/active/fp_gcr/fp_getclientrects.html)   |  F    |
| DeviceMotionEvent.rotationRate   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEvent/rotationRate)   |[1](https://dl.acm.org/doi/pdf/10.1145/3243734.3243860), [2](https://bl.ocks.org/bellbind/raw/c885f85a0dd0e4681ee5/?raw=true)   |  T    |
| DeviceMotionEventRotationRate.beta   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEventRotationRate/beta)   |[1](https://dl.acm.org/doi/pdf/10.1145/3243734.3243860), [2](https://bl.ocks.org/bellbind/raw/c885f85a0dd0e4681ee5/?raw=true)   |  T    |
| DeviceMotionEventRotationRate.gamma   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEventRotationRate/gamma)   |[1](https://dl.acm.org/doi/pdf/10.1145/3243734.3243860), [2](https://bl.ocks.org/bellbind/raw/c885f85a0dd0e4681ee5/?raw=true)   |  T    |
| DeviceOrientationEvent.alpha   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/DeviceOrientationEvent/alpha)   |[1](https://dl.acm.org/doi/pdf/10.1145/3243734.3243860), [2](https://bl.ocks.org/bellbind/raw/c885f85a0dd0e4681ee5/?raw=true)   |  T    |
| DeviceOrientationEvent.beta   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/DeviceOrientationEvent/beta)   |[1](https://dl.acm.org/doi/pdf/10.1145/3243734.3243860), [2](https://bl.ocks.org/bellbind/raw/c885f85a0dd0e4681ee5/?raw=true)   |  T    |
| DeviceOrientationEvent.gamma   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/DeviceOrientationEvent/gamma)   |[1](https://dl.acm.org/doi/pdf/10.1145/3243734.3243860), [2](https://bl.ocks.org/bellbind/raw/c885f85a0dd0e4681ee5/?raw=true)   |  T    |
| DynamicsCompressorNode.attack   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/DynamicsCompressorNode/attack)   |[1](https://audiofingerprint.openwpm.com/)   |  T    |
| DynamicsCompressorNode.knee   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/DynamicsCompressorNode/knee)   |[1](https://audiofingerprint.openwpm.com/)   |  T    |
| DynamicsCompressorNode.ratio   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/DynamicsCompressorNode/ratio)   |[1](https://audiofingerprint.openwpm.com/)   |  T    |
| DynamicsCompressorNode.reduction   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/DynamicsCompressorNode/reduction)   |[1](https://audiofingerprint.openwpm.com/)   |  T    |
| DynamicsCompressorNode.release   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/DynamicsCompressorNode/release)   |[1](https://audiofingerprint.openwpm.com/)   |  T    |
| DynamicsCompressorNode.threshold   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/DynamicsCompressorNode/threshold)   |[1](https://audiofingerprint.openwpm.com/)   |  T    |
| GainNode.gain   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/GainNode/gain)   |[1](https://audiofingerprint.openwpm.com/)   |  T    |
| Geolocation.clearWatch   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/clearWatch)   |[1](https://browserleaks.com/geo)   |  T    |
| HTMLCanvasElement.getContext   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html)   |  T    |
| HTMLCanvasElement.height   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/height)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html)   |  T    |
| HTMLCanvasElement.toDataURL   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html)   |  T    |
| HTMLCanvasElement.width   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/width)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html)   |  T    |
| History.length   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/History/length)   |N/A   |  T    |
| IdleDeadline.timeRemaining   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/IdleDeadline/timeRemaining)   |[1](https://webresource.c-ctrip.com/resaresonline/risk/ubtrms/d.min.d7a9ee87.js)   |  F    |
| ImageData.data   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/ImageData/data)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| IntersectionObserver.disconnect   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/disconnect)   |[1](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API), [2](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API/Timing_element_visibility)   |  F    |
| IntersectionObserver.observe   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/observe)   |[1](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API), [2](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API/Timing_element_visibility)   |  F    |
| IntersectionObserver.unobserve   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/unobserve)   |[1](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API), [2](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API/Timing_element_visibility)   |  F    |
| IntersectionObserverEntry.intersectionRatio   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/intersectionRatio)   |[1](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API), [2](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API/Timing_element_visibility)   |  F    |
| IntersectionObserverEntry.isIntersecting   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/isIntersecting)   |[1](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API), [2](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API/Timing_element_visibility)   |  F    |
| IntersectionObserverEntry.target   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserverEntry/target)   |[1](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API), [2](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API/Timing_element_visibility)   |  F    |
| MediaDevices.enumerateDevices   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/enumerateDevices)   |[1](https://browserleaks.com/webrtc)   |  T    |
| MediaDevices.getDisplayMedia   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getDisplayMedia)   |[1](https://browserleaks.com/webrtc)   |  T    |
| MediaQueryList.addListener   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryList/addListener)   |[1](https://mdn.github.io/dom-examples/mediaquerylist/index.html)   |  T    |
| MediaQueryList.matches   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryList/matches)   |[1](https://mdn.github.io/dom-examples/mediaquerylist/index.html)   |  T    |
| MediaSource.readyState   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/MediaSource/readyState)   |[1](https://f.vimeocdn.com/p/3.45.4/js/player.js)   |  F    |
| MemoryInfo.jsHeapSizeLimit   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Performance/memory)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| MemoryInfo.totalJSHeapSize   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Performance/memory)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| MemoryInfo.usedJSHeapSize   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Performance/memory)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| MimeTypeArray.item   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/MimeTypeArray)   |[1](https://browserleaks.com/javascript)   |  T    |
| MimeTypeArray.length   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/MimeTypeArray)   |[1](https://browserleaks.com/javascript)   |  T    |
| MimeTypeArray.namedItem   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/MimeTypeArray)   |[1](https://browserleaks.com/javascript)   |  T    |
| MutationObserver.observe   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver/observe)   |[1](https://hal.inria.fr/hal-02441653/document)   |  F    |
| MutationRecord.addedNodes   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord)   |[1](https://hal.inria.fr/hal-02441653/document)   |  F    |
| MutationRecord.attributeName   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord)   |[1](https://hal.inria.fr/hal-02441653/document)   |  F    |
| MutationRecord.target   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord)   |[1](https://hal.inria.fr/hal-02441653/document)   |  F    |
| Navigator.appVersion   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/appVersion)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.connection   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/connection)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)  |  T    |
| Navigator.credentials   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/credentials)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.geolocation   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/geolocation)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.getGamepads   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/getGamepads)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.getUserMedia   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/getUserMedia)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.keyboard   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/keyboard)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.locks   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/locks)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.maxTouchPoints   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/maxTouchPoints)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.mediaCapabilities   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/mediaCapabilities)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.mediaDevices   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/mediaDevices)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.onLine   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/onLine)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.permissions   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/permissions)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.product   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/product)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.serviceWorker   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/serviceWorker)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.unregisterProtocolHandler   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/unregisterProtocolHandler)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.userAgent   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/userAgent)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.userAgentData   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/userAgentData)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.vibrate   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/vibrate)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.webdriver   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/webdriver)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.webkitGetUserMedia   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/webkitGetUserMedia)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.webkitPersistentStorage   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/webkitPersistentStorage)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.webkitTemporaryStorage   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/webkitTemporaryStorage)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Navigator.xr   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/xr)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| NetworkInformation.downlink   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation/downlink)   |[1](https://browserleaks.com/javascript)   |  T    |
| NetworkInformation.effectiveType   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation/effectiveType)   |[1](https://browserleaks.com/javascript)   |  T    |
| NetworkInformation.rtt   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation/rtt)   |[1](https://browserleaks.com/javascript)   |  T    |
| NetworkInformation.saveData   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation/saveData)   |[1](https://browserleaks.com/javascript)   |  T    |
| NetworkInformation.type   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation/type)   |[1](https://browserleaks.com/javascript)   |  T    |
| OfflineAudioCompletionEvent.renderedBuffer   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/OfflineAudioCompletionEvent/renderedBuffer)   |[1](https://audiofingerprint.openwpm.com/)   |  T    |
| OfflineAudioContext.startRendering   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/OfflineAudioContext/startRendering)   |[1](https://audiofingerprint.openwpm.com/)   |  T    |
| Performance.measure   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Performance/measure)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  F    |
| Performance.memory   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Performance/memory)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Performance.now   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Performance/now)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://www.darkwavetech.com/index.php/device-fingerprint-blog/device-clock-speed-virtual-machine), [3](https://arxiv.org/pdf/2112.01662.pdf)   |  F    |
| Performance.timeOrigin   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Performance/timeOrigin)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Performance.timing   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Performance/timing)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| PerformanceObserverEntryList.getEntries   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserverEntryList/getEntries)   |[1](https://f.vimeocdn.com/p/3.45.4/js/player.js)   |  F    |
| PerformanceResourceTiming.connectStart   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming/connectStart)   |[1](https://www.darkwavetech.com/index.php/device-fingerprint-blog/latency-fingerprinting)   |  T    |
| PerformanceResourceTiming.fetchStart   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming/fetchStart)   |N/A   |  T    |
| PerformanceResourceTiming.responseEnd   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming/responseEnd)   |N/A   |  T    |
| PerformanceResourceTiming.responseStart   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming/responseStart)   |N/A   |  T    |
| PerformanceResourceTiming.toJSON   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming/toJSON)   |N/A   |  T    |
| PerformanceTiming.connectEnd   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming/connectEnd)   |[1]([1](https://www.darkwavetech.com/index.php/device-fingerprint-blog/latency-fingerprinting))   |  T    |
| PerformanceTiming.domainLookupEnd   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming/domainLookupEnd)   |[1](https://arxiv.org/pdf/2112.01662.pdf)   |  T    |
| PerformanceTiming.fetchStart   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming/fetchStart)   |N/A   |  T    |
| PerformanceTiming.loadEventStart   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming/loadEventStart)   |N/A   |  T    |
| PerformanceTiming.navigationStart   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming/navigationStart)   |N/A   |  T    |
| PerformanceTiming.responseStart   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceTiming/responseStart)   |N/A   |  T    |
| PermissionStatus.state   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PermissionStatus/state)   |[1](https://browserleaks.com/geo)   |  F    |
| PluginArray.item   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PluginArray)   |[1](https://browserleaks.com/javascript)   |  T    |
| PluginArray.length   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PluginArray)   |[1](https://browserleaks.com/javascript)   |  T    |
| PluginArray.namedItem   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PluginArray)   |[1](https://browserleaks.com/javascript)   |  T    |
| PluginArray.refresh   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PluginArray)   |[1](https://browserleaks.com/javascript)   |  T    |
| PresentationRequest.getAvailability   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PresentationRequest/getAvailability)   |[1](https://w3c.github.io/presentation-api/), [2](https://github.com/uiowa-irl/FP-Inspector/blob/master/Data/potential_fingerprinting_APIs.md)   |  F    |
| ProgressEvent.loaded   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/ProgressEvent/loaded)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  F    |
| ProgressEvent.total   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/ProgressEvent/total)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  F    |
| RTCSessionDescription.sdp   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/RTCSessionDescription/sdp)   |[1](https://privacycheck.sec.lrz.de/active/fp_wrtc/fp_webrtc.html)   |  F    |
| Screen.availHeight   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Screen/availHeight)   |[1](https://browserleaks.com/javascript)   |  T    |
| Screen.availLeft   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Screen/availLeft)   |[1](https://browserleaks.com/javascript)   |  T    |
| Screen.availTop   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Screen/availTop)   |[1](https://browserleaks.com/javascript)   |  T    |
| Screen.availWidth   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Screen/avaiavailWidthlHeight)   |[1](https://browserleaks.com/javascript)   |  T    |
| Screen.left   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Screen/left)   |[1](https://browserleaks.com/javascript)   |  T    |
| ScreenOrientation.angle   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/ScreenOrientation/angle)   |[1](https://browserleaks.com/javascript), [2](https://whatwebcando.today/screen-orientation.html)   |  T    |
| ScreenOrientation.lock   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/ScreenOrientation/lock)   |[1](https://whatwebcando.today/screen-orientation.html)   |  T    |
| ScreenOrientation.type   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/ScreenOrientation/type)   |[1](https://browserleaks.com/javascript), [2](https://whatwebcando.today/screen-orientation.html)   |  T    |
| ScreenOrientation.unlock   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/ScreenOrientation/unlock)   |[1](https://whatwebcando.today/screen-orientation.html)   |  T    |
| ServiceWorkerContainer.controller   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerContainer/controller)   |[1](https://www.cs.uic.edu/~skarami/files/sw21/sw21.pdf)   |  F    |
| SourceBuffer.appendBuffer   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/SourceBuffer/appendBuffer)   |[1](https://privacycheck.sec.lrz.de/active/fp_cpt/fp_can_play_type.html), [2](https://player.vimeo.com/api/demo)   |  F    |
| SourceBuffer.buffered   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/SourceBuffer/buffered)   |[1](https://privacycheck.sec.lrz.de/active/fp_cpt/fp_can_play_type.html), [2](https://player.vimeo.com/api/demo)   |  F    |
| SourceBuffer.updating   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/SourceBuffer/updating)   |[1](https://privacycheck.sec.lrz.de/active/fp_cpt/fp_can_play_type.html), [2](https://player.vimeo.com/api/demo)   |  F    |
| TextMetrics.fontBoundingBoxAscent   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/TextMetrics/fontBoundingBoxAscent)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| TextMetrics.width   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/TextMetrics/width)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html), [2](https://browserleaks.com/canvas)   |  T    |
| TimeRanges.end   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/TimeRanges/end)   |[1](https://f.vimeocdn.com/p/3.45.3/js/player.js)   |  F    |
| TimeRanges.length   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/TimeRanges/length)   |[1](https://f.vimeocdn.com/p/3.45.3/js/player.js)   |  F    |
| TimeRanges.start   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/TimeRanges/start)   |[1](https://f.vimeocdn.com/p/3.45.3/js/player.js)   |  F    |
| WebGL2RenderingContext.attachShader   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/attachShader)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.bindBuffer   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/bindBuffer)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.bindTexture   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/bindTexture)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.bufferData   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/bufferData)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.compileShader   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/compileShader)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.createBuffer   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/createBuffer)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.createProgram   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/createProgram)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.createShader   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/createShader)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.createTexture   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/createTexture)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.deleteProgram   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/deleteProgram)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.drawArrays   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/drawArrays)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.getContextAttributes   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/getContextAttributes)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.getShaderPrecisionFormat   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/getShaderPrecisionFormat)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.getSupportedExtensions   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/getSupportedExtensions)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.isContextLost   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/isContextLost)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.isEnabled   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/isEnabled)   |[1](https://browserleaks.com/webgl) , [2](https://webglreport.com/?v=2)  |  T    |
| WebGL2RenderingContext.shaderSource   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/shaderSource)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.texImage2D   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/texImage2D)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGL2RenderingContext.texParameteri   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/texParameteri)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=2)   |  T    |
| WebGLLoseContext.loseContext   |[W3](https://docs.w3cub.com/dom/webgl_lose_context)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=1)  |  T    |
| WebGLRenderingContext.createBuffer   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/createBuffer)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=1)   |  T    |
| WebGLRenderingContext.drawArrays   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/drawArrays)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=1)   |  T    |
| WebGLRenderingContext.getExtension   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/getExtension)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=1)   |  T    |
| WebGLRenderingContext.getParameter   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/getParameter)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=1)   |  T    |
| WebGLRenderingContext.getShaderPrecisionFormat   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/getShaderPrecisionFormat)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=1)   |  T    |
| WebGLShaderPrecisionFormat.precision   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLShaderPrecisionFormat/precision)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=1)  |  T    |
| WebGLShaderPrecisionFormat.rangeMax   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLShaderPrecisionFormat/rangeMax)   |[1](https://browserleaks.com/webgl), [2](https://webglreport.com/?v=1)   |  T    |
| Window.applicationCache   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/applicationCache)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.clearTimeout   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/clearTimeout)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.clientInformation   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.closed   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/closed)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.crypto   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/crypto)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.defaultstatus   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/defaultstatus)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.document   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/document)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.event   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/event)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.external   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/external)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.fetch   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.frames   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/frames)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.getComputedStyle   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.history   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/history)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.innerHeight   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/innerHeight)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Window.innerWidth   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/innerWidth)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Window.length   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/length)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.location   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/location)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.locationbar   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/locationbar)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.matchMedia   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.name   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/name)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.navigator   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/navigator)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.onerror   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/onerror)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.ontouchstart   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/ontouchstart)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.open   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/open)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.opener   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.orientation   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/orientation)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.outerHeight   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/outerHeight)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Window.outerWidth   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/outerWidth)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html), [2](https://browserleaks.com/javascript)   |  T    |
| Window.pageXOffset   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/pageXOffset)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.pageYOffset   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/pageYOffset)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.parent   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/parent)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.performance   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/performance)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.requestAnimationFrame   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.requestIdleCallback   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestIdleCallback)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.screen   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/screen)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.screenLeft   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/screenLeft)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.screenTop   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/screenTop)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.screenX   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/screenX)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.screenY   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/screenY)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.self   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/self)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.setInterval   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/setInterval)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.setTimeout   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.speechSynthesis   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/speechSynthesis)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.top   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/top)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.visualViewport   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/visualViewport)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.webkitRequestFileSystem   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/webkitRequestFileSystem)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| Window.window   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/window)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |


# (De)Obfuscation APIs
| API Name    | Documentation | Crawled Script |
| ----------- | ----------- | ----------- |
| TextDecoder.decode   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder/decode)   |[Obfuscation](https://newassets.hcaptcha.com/c/cdb91b45/hsw.js)   | 
| TextEncoder.encode   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder/encode)   |[Obfuscation](https://newassets.hcaptcha.com/c/cdb91b45/hsw.js)   |
| Window.atob   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/atob)   |[Obfuscation](https://www.skyscanner.com/rf8vapwA/init.js)   | 
| Window.btoa   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/btoa)   |[Obfuscation](https://www.skyscanner.com/rf8vapwA/init.js)   | 

# New Fingerprinting APIs Found in Second Crawling
| API Name    |Documentation  |  Proof | Deployed(T/F) |
| ----------- | ----------- | ----------- | ----------- |
| BarProp.visible  |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/BarProp/visible)   |N/A   |  F    |
| CanvasRenderingContext2D.font   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/font)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html)   |  T    |
| CanvasRenderingContext2D.scale   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/scale)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html)   |  T    |
| CanvasRenderingContext2D.setLineDash   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/setLineDash)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html)   |  T    |
| DOMRect.height  |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/height)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html)   |  T    |
| MutationRecord.type   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/MutationRecord)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  F    |
| Navigator.bluetooth   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  T    |
| NetworkInformation.onchange   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation/onchange)   |[1](https://browserleaks.com/javascript)   |  T    |
| OffscreenCanvas.getContext   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/OffscreenCanvas/getContext)   |[1](https://privacycheck.sec.lrz.de/active/fp_c/fp_canvas.html)   |  T    |
| PageTransitionEvent.persisted   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PageTransitionEvent/persisted)   |N/A   |  F    |
| Performance.mark   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Performance/mark)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  F    |
| PerformanceResourceTiming.initiatorType   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming/initiatorType)   |[1](https://privacycheck.sec.lrz.de/active/fp_je/fp_js_echo.html)   |  F    |
| Permissions.query  |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Permissions/query)   |N/A   |  F    |
| SpeechSynthesis.getVoices   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis/getVoices)   |[1](https://browserleaks.com/javascript)   |  F    |
| VisualViewport.width   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/VisualViewport/width)   |N/A   |  F    |
| WebGLRenderingContext.getContextAttribute   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/getContextAttribute)   |[1](https://browserleaks.com/webgl)   |  T    |
| WebGLShaderPrecisionFormat.rangeMin   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGLShaderPrecisionFormat/rangeMin)   |[1](https://browserleaks.com/webgl)   |  T    |
| Window.statusbar   |[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/statusbar)   |N/A   |  F    |


# Sinks + URl-related APIs
| API Name    |
| ----------- | 
|    DeprecatedStorageQuota.requestQuota    |
|    HTMLAnchorElement.hash    |
|    HTMLAnchorElement.host    |
|    HTMLAnchorElement.hostname    |
|    HTMLAnchorElement.href    |
|    HTMLAnchorElement.origin    |
|    HTMLAnchorElement.password    |
|    HTMLAnchorElement.pathname    |
|    HTMLAnchorElement.port    |
|    HTMLAnchorElement.protocol    |
|    HTMLAnchorElement.search    |
|    HTMLAnchorElement.text    |
|    HTMLIFrameElement.contentDocument    |
|    HTMLIFrameElement.contentWindow    |
|    HTMLIFrameElement.name    |
|    HTMLIFrameElement.src    |
|    HTMLScriptElement.src    |
|    IDBDatabase.createObjectStore    |
|    IDBFactory.open    |
|    Location.ancestorOrigins    |
|    Location.hash    |
|    Location.host    |
|    Location.hostname    |
|    Location.href    |
|    Location.origin    |
|    Location.pathname    |
|    Location.port    |
|    Location.protocol    |
|    Location.reload    |
|    Location.search    |
|    Location.toString    |
|    Location.valueOf    |
|    MessageEvent.data    |
|    MessageEvent.origin    |
|    RTCPeerConnection.createDataChannel    |
|    RTCPeerConnection.createOffer    |
|    RTCPeerConnection.localDescription    |
|    RTCPeerConnection.setLocalDescription    |
|    Response.json    |
|    Storage.clear    |
|    Storage.getItem    |
|    Storage.length    |
|    Storage.removeItem    |
|    Storage.setItem    |
|    URL.host    |
|    URL.href    |
|    URL.pathname    |
|    URL.searchParams    |
|    URLSearchParams.get    |
|    Window.clearInterval    |
|    XMLHttpRequest.abort    |
|    XMLHttpRequest.getResponseHeader    |
|    XMLHttpRequest.open    |
|    XMLHttpRequest.readyState    |
|    XMLHttpRequest.response    |
|    XMLHttpRequest.responseText    |
|    XMLHttpRequest.responseURL    |
|    XMLHttpRequest.setRequestHeader    |
|    XMLHttpRequest.status    |
|    XMLHttpRequest.statusText    |
|    XMLHttpRequest.timeout    |
|    XMLHttpRequest.withCredentials    |


# False Positives
| API Name    |
| ----------- | 
|    AbortController.abort    |
|    AbortController.signal    |
|    Attr.name    |
|    Attr.value    |
|    CustomEvent.detail    |
|    DOMException.message    |
|    DOMStringList.length    |
|    DOMTokenList.add    |
|    DOMTokenList.contains    |
|    DOMTokenList.remove    |
|    Document.evaluate    |
|    Element.matches    |
|    Event.stopImmediatePropagation    |
|    Event.target    |
|    FormData.append    |
|    HTMLCollection.length    |
|    HTMLImageElement.decode    |
|    HTMLInputElement.defaultValue    |
|    HTMLInputElement.files    |
|    HTMLInputElement.value    |
|    HTMLMetaElement.content    |
|    HTMLMetaElement.name    |
|    Node.appendChild    |
|    NodeList.item    |
|    NodeList.length    |
|    UnderlyingSourceBase.type    |

# Fingerprinting Code Snippets 
## PermissionStatus.state and Permissions.query
```
        t.prototype.getPermissionsMetadata = function () {
            return __awaiter(this, void 0, void 0, function () {
                var t, n, i, r, o, a;
                return __generator(this, function (s) {
                    switch (s.label) {
                        case 0:
                            if (t = {}, n = ["accelerometer", "accessibility-events", "ambient-light-sensor", "background-sync", "camera", "clipboard-read", "clipboard-write", "geolocation", "gyroscope", "magnetometer", "microphone", "midi", "notifications", "payment-handler", "persistent-storage", "push"], i = [], navigator.permissions)
                                for (o in r = function (e) {
                                        var r = n[e];
                                        i.push(navigator.permissions.query({
                                            name: r
                                        }).then(function (e) {
                                            t[r] = e.state
                                        }).catch(function (e) {}))
                                    }, n) r(o);
                            s.label = 1;
                        case 1:
                            return s.trys.push([1, 3, , 4]), [4, Promise.all(i)];
                        case 2:
                            return s.sent(), [3, 4];
                        case 3:
                            return a = s.sent(), e.STLogger.warn(a), [3, 4];
                        case 4:
                            return [2, t]
                    }
                })
            })
        }
```
## PageTransitionEvent.persisted
```
            function () {
                var t = !1;
                if ("localStorage" in window) try {
                    window.localStorage.setItem("\_tmptest", "tmpval"), t = !0, window.localStorage.removeItem("\_tmptest")
                } catch (t) {}
                if (t) try {
                    window.localStorage && (_ = window.localStorage, b = "localStorage", j = \_.jStorage_update)
                } catch (t) {} else if ("globalStorage" in window) try {
                    window.globalStorage && (_ = "localhost" == window.location.hostname ? window.globalStorage["localhost.localdomain"] : window.globalStorage[window.location.hostname], b = "globalStorage", j = \_.jStorage_update)
                } catch (t) {} else {
                    if (w = document.createElement("link"), !w.addBehavior) return void(w = null);
                    w.style.behavior = "url(#default#userData)", document.getElementsByTagName("head")[0].appendChild(w);
                    try {
                        w.load("jStorage")
                    } catch (t) {
                        w.setAttribute("jStorage", "{}"), w.save("jStorage"), w.load("jStorage")
                    }
                    var n = "{}";
                    try {
                        n = w.getAttribute("jStorage")
                    } catch (t) {}
                    try {
                        j = w.getAttribute("jStorage_update")
                    } catch (t) {}
                    \_.jStorage = n, b = "userDataBehavior"
                }
                s(), h(), e(), u(), "addEventListener" in window && window.addEventListener("pageshow", function (t) {
                    t.persisted && i()
                }, !1)
            }()
```

## ServiceWorkerContainer.controller
```
            t.prototype.ht = function () {
            var t = this;
            this.u.X = this.tt("longtask", (function (e) {
                t.ft({
                    W: e
                })
            }))
        }, t.prototype.v = function () {
            return s && !!s.getEntriesByType && !!s.now && !!s.mark
        }, t.prototype.l = function () {
            return "PerformanceObserver" in o
        }, t.prototype.ct = function (t) {
            var e = s.getEntriesByName(t),
                i = e[e.length - 1];
            return i && "measure" === i.entryType ? i.duration : -1
        }, t.prototype.L = function () {
            return a ? {
                deviceMemory: a.deviceMemory ? a.deviceMemory : 0,
                hardwareConcurrency: a.hardwareConcurrency ? a.hardwareConcurrency : 0,
                serviceWorkerStatus: "serviceWorker" in a ? a.serviceWorker.controller ? "controlled" : "supported" : "unsupported"
            } : {}
        }, t.prototype._ = function () {
            if (!this.v()) return {};
            var t = performance.getEntriesByType("navigation")[0];
            if (!t) return {};
            var e = t.responseStart,
                i = t.responseEnd;
            return {
                fetchTime: i - t.fetchStart,
                workerTime: t.workerStart > 0 ? i - t.workerStart : 0,
                totalTime: i - t.requestStart,
                downloadTime: i - e,
                timeToFirstByte: e - t.requestStart,
                headerSize: t.transferSize - t.encodedBodySize || 0,
                dnsLookupTime: t.domainLookupEnd - t.domainLookupStart
            }
        }, t.prototype.I = function () {
            if ("connection" in a) {
                var t = a.connection;
                return "object" != typeof t ? {} : (f = t.effectiveType, d = !!t.saveData, {
                    downlink: t.downlink,
                    effectiveType: t.effectiveType,
                    rtt: t.rtt,
                    saveData: !!t.saveData
                })
            }
            return {}
        }
```
## History.length
```
        var ke = X("guid", "ON"),
            le = !d.google_conversion_domain && "GooglemKTybQhCsO" in v &&
            "function" == typeof v.GooglemKTybQhCsO ? X("resp", "GooglemKTybQhCsO") : "",
            me = X("disvt", d.google_disable_viewthrough),
            ne = X("eid", Nb().join());
        var ha = d.google_conversion_date;
        var x = [];
        if (a) {
            var H = a.screen;
            H && (x.push(X("u_h", H.height)), x.push(X("u_w", H.width)), x.push(X("u_ah", H.availHeight)), x.push(X("u_aw", H.availWidth)), x.push(X("u_cd", H.colorDepth)));
            a.history && x.push(X("u_his", a.history.length))
        }
        ha && "function" == typeof ha.getTimezoneOffset && x.push(X("u_tz", -ha.getTimezoneOffset()));
        b && ("function" == typeof b.javaEnabled &&
            x.push(X("u_java", b.javaEnabled())), b.plugins && x.push(X("u_nplug", b.plugins.length)), b.mimeTypes && x.push(X("u_nmime", b.mimeTypes.length)));
        ha = x.join("");
        x = X("gtm", d.google_gtm);
        b = b && b.sendBeacon ? X("sendb", "1") : "";
```
## Window.statusbar and BarProp.visible
```
        function g() {
            var e = [];
            return document.querySelectorAll("script[src*=extension]").forEach(function(t) {
                var r = t.getAttribute("src");
                r && e.push(r)
            }), JSON.stringify(e)
        }

        function m() {
            for (var e = ["innerHeight", "innerWidth", "outerWidth", "outerHeight", "devicePixelRatio"], t = {}, r = 0; r < e.length; r++) {
                var n = e[r];
                t[n] = window[n]
            }
            return window.statusbar && (t.statusbar_visible = window.statusbar.visible), t.length = window.length, t.modified = Object.getOwnPropertyNames(window.screen), JSON.stringify(t)
        }

        function w(e) {
            var r = {};
            for (var n in e)
                if ("enabledPlugin" !== n && "function" != typeof e[n])
                    if ("object" === (0, t.default)(e[n])) {
                        var o = w(e[n]);
                        Object.keys(o) && (r[n] = o)
                    } else r[n] = e[n];
            return r
        }
```
## MediaQueryList.matches
```
      isHighDensity: (a = window.matchMedia && (window.matchMedia("only screen and (min-resolution: 124dpi), only screen and (min-resolution: 1.3dppx), only screen and (min-resolution: 48.8dpcm)").matches || window.matchMedia("only screen and (-webkit-min-device-pixel-ratio: 1.3), only screen and (-o-min-device-pixel-ratio: 2.6/2), only screen and (min--moz-device-pixel-ratio: 1.3), only screen and (min-device-pixel-ratio: 1.3)").matches) || window.devicePixelRatio && window.devicePixelRatio > 1.3, function () {
        return a
      }),
      isSmartPhone: (s = window.matchMedia && window.matchMedia(" only screen and (min-device-width : 320px) and (max-device-width : 480px)").matches || /(iPhone|iPod)/g.test(navigator.userAgent), function () {
        return s
      }),
      isTablet: (n = window.matchMedia && window.matchMedia(" only screen and (min-device-width : 768px) and (max-device-width : 1024px)").matches || /(iPhone|iPod)/g.test(navigator.userAgent), function () {
        return n
      }),
      isDesktop: function () {
        return !(this.isTablet() || this.isSmartPhone())
      },
      getOuterWidth: function (e) {
        var t, r, i;
        return e.getBoundingClientRect().width + parseFloat(getComputedStyle(e).marginLeft) + parseFloat(getComputedStyle(e).marginRight)
      },
      isHtmlContent: function (e) {
        return /(?:%3C|[<>&])/.test(e)
      },
      setContentToElement: function (e, t) {
        TRC.dom.isHtmlContent(t) ? e.innerHTML = t : e.innerText = t
      }
```
