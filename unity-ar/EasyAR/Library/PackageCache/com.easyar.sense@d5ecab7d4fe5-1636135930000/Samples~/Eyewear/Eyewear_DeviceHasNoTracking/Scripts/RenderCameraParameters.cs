//================================================================================================================================
//
//  Copyright (c) 2015-2021 VisionStar Information Technology (Shanghai) Co., Ltd. All Rights Reserved.
//  EasyAR is the registered trademark or trademark of VisionStar Information Technology (Shanghai) Co., Ltd in China
//  and other countries for the augmented reality technology developed by VisionStar Information Technology (Shanghai) Co., Ltd.
//
//================================================================================================================================

using easyar;
using UnityEngine;

namespace Samples
{
    [CreateAssetMenu(menuName = "Samples/Render Camera Parameters")]
    public class RenderCameraParameters : ScriptableObject
    {
        /// <summary>
        /// <para xml:lang="en">Device model.</para>
        /// <para xml:lang="zh">设备型号。</para>
        /// </summary>
        public string DeviceModel;

        /// <summary>
        /// <para xml:lang="en">Position offset.</para>
        /// <para xml:lang="zh">位置偏移。</para>
        /// </summary>
        public Vector3 PositionOffset;
        /// <summary>
        /// <para xml:lang="en">Rotation offset.</para>
        /// <para xml:lang="zh">角度偏移。</para>
        /// </summary>
        public Vector3 RotationOffset;
        /// <summary>
        /// <para xml:lang="en">(Image) size.</para>
        /// <para xml:lang="zh">（图像）大小。</para>
        /// </summary>
        public Vector2 Size;

        /// <summary>
        /// <para xml:lang="en">Focal length.</para>
        /// <para xml:lang="zh">焦距。</para>
        /// </summary>
        public Vector2 FocalLength;
        /// <summary>
        /// <para xml:lang="en">Principal point.</para>
        /// <para xml:lang="zh">主点。</para>
        /// </summary>
        public Vector2 PrincipalPoint;

        private static Vector3 positionScale = new Vector3(1, -1, -1);

        public Matrix4x4 Projection(ARSession session, Camera camera)
        {
            var cameraParameters = session.FrameCameraParameters.Value;
            using (var parameters = new CameraParameters(new Vec2I((int)Size.x, (int)Size.y), new Vec2F(FocalLength.x, FocalLength.y), new Vec2F(PrincipalPoint.x, PrincipalPoint.y), cameraParameters.cameraDeviceType(), cameraParameters.cameraOrientation()))
            {
                return parameters.projection(camera.nearClipPlane, camera.farClipPlane, camera.aspect, session.Assembly.Display.Rotation, false, false).ToUnityMatrix()
                    * Matrix4x4.TRS(Vector3.Scale(PositionOffset, positionScale), Quaternion.Euler(RotationOffset), Vector3.one);
            }
        }
    }
}
