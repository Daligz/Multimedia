//================================================================================================================================
//
//  Copyright (c) 2015-2021 VisionStar Information Technology (Shanghai) Co., Ltd. All Rights Reserved.
//  EasyAR is the registered trademark or trademark of VisionStar Information Technology (Shanghai) Co., Ltd in China
//  and other countries for the augmented reality technology developed by VisionStar Information Technology (Shanghai) Co., Ltd.
//
//================================================================================================================================

using easyar;
#if EASYAR_ENABLE_NREAL
using NRKernal;
#endif
using System;
using System.Collections;
using UnityEngine;
using UnityEngine.UI;

namespace Sample
{
    public class Sample : MonoBehaviour
    {
#if EASYAR_ENABLE_NREAL
        public Text Status;
        public ARSession Session;

        private string deviceModel = string.Empty;
        private static Optional<DateTime> trialCounter;
        private bool inputBlocked;

#if UNITY_EDITOR
        [UnityEditor.InitializeOnLoadMethod]
        static void ImportSampleStreamingAssets()
        {
            FileUtil.ImportSampleStreamingAssets();
        }
#endif

        private void Awake()
        {
#if UNITY_ANDROID && !UNITY_EDITOR
            if (Application.platform == RuntimePlatform.Android)
            {
                try
                {
                    using (var buildClass = new AndroidJavaClass("android.os.Build"))
                    {
                        deviceModel = $"(Device = {buildClass.GetStatic<string>("DEVICE")}, Model = {buildClass.GetStatic<string>("MODEL")})";
                    }
                }
                catch (Exception e) { deviceModel = e.Message; }
            }
#endif

            Session.StateChanged += (state) =>
            {
                if (state == ARSession.SessionState.Ready)
                {
                    if (trialCounter.OnNone)
                    {
                        trialCounter = DateTime.Now;
                    }
                }
            };
        }

        private void Update()
        {
            Status.text = $"Device Model: {SystemInfo.deviceModel} {deviceModel}" + Environment.NewLine +
                "Nreal Session Status: " + NRFrame.SessionStatus + Environment.NewLine +
                "Frame Source: " + ((Session.Assembly != null && Session.Assembly.FrameSource) ? Session.Assembly.FrameSource.GetType().ToString().Replace("easyar.", "").Replace("FrameSource", "") : "-") + Environment.NewLine +
                "Tracking Status (Async): " + Session.TrackingStatus + Environment.NewLine;
            if (Session.State > ARSession.SessionState.Ready)
            {
                Status.text += Environment.NewLine +
                    "Motion Fusion is on, image must NOT move in real world." + Environment.NewLine +
                    "Push the device closer to the image if you cannot see cubes." + Environment.NewLine +
                    "    Image target scale must be set to physical image width." + Environment.NewLine +
                    "    Scale is preset to match long edge of A4 paper." + Environment.NewLine +
                    "    Suggest to print out images for test.";

                if (Session.Assembly.FrameSource is NrealFrameSource && trialCounter != DateTime.MinValue)
                {
                    var nrealFrameSource = (NrealFrameSource)Session.Assembly.FrameSource;
                    Status.text += Environment.NewLine +
                        Environment.NewLine +
                        $"EasyAR received frame count from Nreal: {nrealFrameSource.ReceivedFrameCount / 100 * 100}+";

                    StartCoroutine(CheckData(nrealFrameSource.ReceivedFrameCount, (c) => { inputBlocked = nrealFrameSource.ReceivedFrameCount == c; }));
                    if (inputBlocked)
                    {
                        Status.text += Environment.NewLine + "!! WARNING: RGB Camera input has been blocked for 1+ seconds, please check your device !!";
                    }
                }
            }

            // avoid misunderstanding when using personal edition, not necessary in your own projects
            if (!string.IsNullOrEmpty(Engine.errorMessage()))
            {
                trialCounter = DateTime.MinValue;
            }
            if (trialCounter.OnSome)
            {
                if (Session.State >= ARSession.SessionState.Ready && (Session.Assembly.FrameSource is ARFoundationFrameSource || Session.Assembly.FrameSource is HuaweiAREngineFrameSource || Session.Assembly.FrameSource is NrealFrameSource || trialCounter.Value == DateTime.MinValue))
                {
                    var time = Math.Max(0, (int)(trialCounter.Value - DateTime.Now).TotalSeconds + 100);
                    Status.text += $"\n\nEasyAR License for {Session.Assembly.FrameSource.GetType()} will timeout for current process within {time} seconds. (Personal Edition Only)";
                }
            }
        }

        private IEnumerator CheckData(int count, Action<int> callback)
        {
            yield return new WaitForSeconds(1);
            callback(count);
        }
#endif
    }
}
