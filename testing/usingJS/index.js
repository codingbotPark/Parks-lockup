import * as poseDetection from '@tensorflow-models/pose-detection';

// 기본적인 Lightning
const detector = await poseDetection.createDetector(poseDetection.SupportedModels.MoveNet);

const video = document.getElementById('video')
const poses = await detector.estimatePoses(video)
console.log(poses[0].keypoints);