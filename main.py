from utils.myreadseq import readseq
from utils.myinfo_on_video import info
from extract import OpticalFlowAnalyzer

import matplotlib.pyplot as plt
import cv2
import os

# Define the directory where the videos are stored
video_directory = 'videos'
video_files = [os.path.join(video_directory, f) for f in os.listdir(video_directory) if f.endswith('.y4m')]

window_sizes = range(5, 31, 5)

# This dictionary will store the average PSNRs for each video
video_average_psnrs = {winsize: [] for winsize in window_sizes}

# This loop goes through each video file
for video_file in video_files:
    cap = cv2.VideoCapture(video_file)
    ret, frame1 = cap.read()
    if not ret:
        print(f"Error: Unable to read video file {video_file}")
        cap.release()
        continue

    for winsize in window_sizes:
        analyzer = OpticalFlowAnalyzer(winsize=winsize)
        psnrs = []
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  

        while True:
            ret, frame2 = cap.read()
            if not ret:
                break

            metrics = analyzer.compute_metrics(frame1, frame2)
            psnr_value = metrics['psnr']
            psnrs.append(psnr_value)

            frame1 = frame2

        average_psnr = sum(psnrs) / len(psnrs)
        video_average_psnrs[winsize].append(average_psnr)
        print(f"Video {video_file} - Window Size {winsize}: Average PSNR={average_psnr}")

    cap.release()

# Now we calculate the overall average PSNR for each window size
overall_average_psnrs = {winsize: sum(psnrs) / len(psnrs) for winsize, psnrs in video_average_psnrs.items()}

# Plotting the average PSNR for each video
plt.figure()

for winsize in window_sizes:
    plt.plot([winsize] * len(video_files), video_average_psnrs[winsize], marker='o', linestyle='', label=f"WinSize {winsize}")

plt.xlabel('Window Size')
plt.ylabel('Average PSNR per Video')
plt.title('Average PSNR per Video for Different Window Sizes')
plt.legend()
plt.grid(True)
plt.show()

# Plotting the overall average PSNR for all videos
plt.figure()
plt.plot(window_sizes, [overall_average_psnrs[winsize] for winsize in window_sizes], marker='o', linestyle='-')
plt.xlabel('Window Size')
plt.ylabel('Overall Average PSNR')
plt.title('Overall Average PSNR for All Videos')
plt.grid(True)
plt.show()



